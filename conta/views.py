# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django.views.generic.list import ListView


@method_decorator(login_required, name='dispatch')
class HomeContaView(TemplateView):
    template_name = "conta/index.html"


# @login_required
# class ListContasView(ListView):
#     pass
