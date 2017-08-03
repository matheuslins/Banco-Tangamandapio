# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Conta, Caixa, Saque

admin.site.register(Conta)
admin.site.register(Caixa)
admin.site.register(Saque)
