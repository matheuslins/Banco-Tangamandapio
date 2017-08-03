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
        return self.nome + ' -> ' + 'R$' + str(self.saldo)

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'


class Caixa(models.Model):
    CELUDAS = (
        ('1', 'P$1'),
        ('2', 'P$2'),
        ('5', 'P$5'),
        ('10', 'P$10'),
        ('20', 'P$20'),
        ('50', 'P$50'),
        ('100', 'P$100'),
    )
    cedula = models.CharField(
        max_length=3, choices=CELUDAS, default='1',
        verbose_name='cedula', primary_key=True)
    quantidade = models.IntegerField()

    def __str__(self):
        return 'P$' + self.cedula + ' -> ' + str(self.quantidade)

    class Meta:
        verbose_name = 'Caixa'
        verbose_name_plural = 'Caixas'
