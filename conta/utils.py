
def sacar(response, conta):
    valor = response.data['valor']
    if not valor > conta.saldo:
        conta.saldo = conta.saldo - valor
    else:
        response.data['message'] = ('Atencao! Conta nao possui saldo '
                                    'suficiente para o saque')
        return response.data['message']
    return conta.save()
