# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework import generics

from .models import Conta, Caixa, Saque
from .serializer import ContaSerializer, CaixaSerializer, SaqueSerializer


@method_decorator(login_required, name='dispatch')
class HomeContaView(TemplateView):
    template_name = "conta/index.html"


@method_decorator(login_required, name='dispatch')
class ListContasView(generics.ListCreateAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer


@method_decorator(login_required, name='dispatch')
class DetailContasView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer


@method_decorator(login_required, name='dispatch')
class ListCaixaView(generics.ListCreateAPIView):
    queryset = Caixa.objects.all()
    serializer_class = CaixaSerializer


@method_decorator(login_required, name='dispatch')
class DetailCaixaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Caixa.objects.all()
    serializer_class = CaixaSerializer


@method_decorator(login_required, name='dispatch')
class CreateSaqueView(generics.CreateAPIView):
    queryset = Saque.objects.all()
    serializer_class = SaqueSerializer
