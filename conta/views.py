# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView
from rest_framework import generics

from .models import Conta
from .serializer import ContaSerializer


class HomeContaView(TemplateView):
    template_name = "conta/index.html"


class ListContasView(generics.ListCreateAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer


class DetailContasView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
