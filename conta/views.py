# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics
from rest_framework import permissions

from .models import Conta
from .serializer import ContaSerializer


@method_decorator(login_required, name='dispatch')
class HomeContaView(TemplateView):
    template_name = "conta/index.html"


@method_decorator(csrf_exempt, name='dispatch')
class ListContasView(generics.ListCreateAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer


@method_decorator(csrf_exempt, name='dispatch')
class DetailContasView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    permission_classes = (permissions.IsAdminUser,)
