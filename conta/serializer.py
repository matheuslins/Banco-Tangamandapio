
from rest_framework import serializers
from .models import Conta, Caixa, Saque


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id', 'nome', 'saldo']


class CaixaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caixa
        fields = ['cedula', 'quantidade']


class SaqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saque
        fields = ['conta', 'valor']
