
from rest_framework import serializers
from .models import Conta, Caixa


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id', 'nome', 'saldo']


class CaixaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caixa
        fields = ['cedula', 'quantidade']
