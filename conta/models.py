# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Conta(models.Model):

    nome = models.CharField(max_length=100,
                            verbose_name='Nome')
    saldo = models.DecimalField(max_digits=8,
                                decimal_places=2,
                                verbose_name='Saldo')

    def __str__(self):
        return self.nome + ' -> ' + 'P$' + str(self.saldo)

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'


class Caixa(models.Model):
    cedula = models.IntegerField(primary_key=True)
    quantidade = models.IntegerField()

    def __str__(self):
        return 'P$' + str(self.cedula) + ' -> ' + str(self.quantidade)

    class Meta:
        verbose_name = 'Caixa'
        verbose_name_plural = 'Caixas'


class Saque(models.Model):
    conta = models.ForeignKey(
        Conta,
        on_delete=models.CASCADE,
        related_name="conta_saque",
        verbose_name='id_conta'
    )
    valor = models.IntegerField()

    def __str__(self):
        return str(self.conta.nome) + ' sacou R$' + str(self.valor)

    class Meta:
        verbose_name = 'Saque'
        verbose_name_plural = 'Saques'
