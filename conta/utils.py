from .constants import CEDULAS_R


def sacar(response, conta, lista_cedulas):
    valor = response.data['valor']
    if not valor > conta.saldo:
        response.data['cedulas'], response.data['caixa'] = retirar_caixa(valor, lista_cedulas, conta)  # noqa
        if 'Atencao!' in response.data['cedulas']:
            response.data['message'] = response.data['cedulas']
            return response.data['message']
    else:
        response.data['message'] = ('Atencao! Conta nao possui saldo '
                                    'suficiente para o saque')
        return response.data['message']


def remove_key(lista, chave):
    dicionario = dict(lista)
    del dicionario[chave]
    return dicionario


def retirar_caixa(valor, lista_cedulas, conta):
    u""" Medotdo que faz a retirada de cedulas do caixa eletronico.

        - Passo 1: Salva-se a quantidade de cedulas do caixa e as ordenas
            de forma decrescente.

        - Passo 2: Na iteracao de cedulas, o caixa precisa ter
            pelo menos uma cedula para o saque acontecer
    """
    # Passo 1
    qtd_cedulas = dict(lista_cedulas).values()
    cedulas = sorted(dict(lista_cedulas).keys(), key=int, reverse=True)
    total_caixa = sum(list(reduce(lambda x, y: x*y, cedula) for cedula in lista_cedulas))  # noqa
    # Passo 2
    if valor <= total_caixa:
        for idx, cedula in enumerate(cedulas):
            if idx == 0:
                qtd_retirar = valor/cedula
                qtd_tem = dict(lista_cedulas)[cedula]
                resto = valor % cedula
                # Se o valor sacado for abaixo de 100 eh preciso
                # setar o caixa_final para a proxima chamada
                caixa_final = dict(lista_cedulas)
                while qtd_retirar > 0:
                    qtd_retirar -= 1
                    if qtd_tem > 0:
                        novo_valor = qtd_tem - 1
                        conta.saldo = conta.saldo - cedula
                        caixa_final = remove_key(lista_cedulas, cedula)
                        caixa_final.update({cedula: novo_valor})
                        qtd_tem -= 1
                        CEDULAS_R[cedula] += 1
                        resto = valor % cedula
            else:
                qtd_retirar = resto/cedula
                qtd_tem = caixa_final[cedula]
                while qtd_retirar > 0:
                    qtd_retirar -= 1
                    if qtd_tem > 0:
                        novo_valor = qtd_tem - 1
                        conta.saldo = conta.saldo - cedula
                        caixa_final = remove_key(
                            zip(caixa_final.keys(),
                                caixa_final.values()),
                            cedula
                        )
                        caixa_final.update({cedula: novo_valor})
                        qtd_tem -= 1
                        CEDULAS_R[cedula] += 1
                        resto = resto % cedula
        conta.save()
        return CEDULAS_R, caixa_final
    else:
        return 'Atencao! Numero de cedulas insuficiente para saque', ''
