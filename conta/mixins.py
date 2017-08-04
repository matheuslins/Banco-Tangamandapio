from .models import Conta, Caixa
from .utils import sacar


class SaqueSuccessMixin(object):
    def dispatch(self, request, *args, **kwargs):
        response = super(SaqueSuccessMixin, self).dispatch(request, *args, **kwargs)  # noqa
        if response.status_code == 201:
            conta = Conta.objects.get(pk=response.data['conta'])
            lista_cedulas = [(caixa.cedula, caixa.quantidade) for caixa in Caixa.objects.all()]  # noqa
            sacar(response, conta, lista_cedulas)  # noqa
        return response
