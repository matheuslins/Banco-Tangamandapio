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
