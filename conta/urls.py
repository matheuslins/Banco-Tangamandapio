from django.conf.urls import url
from .views import (HomeContaView, ListContasView, DetailContasView,
                    ListCaixaView, DetailCaixaView, CreateSaqueView)

urlpatterns = [

    url(r'^$', HomeContaView.as_view(), name='index'),
    # Urls contas
    url(r'^contas/',
        ListContasView.as_view(),
        name='list_contas'),
    url(r'^(?P<pk>\d+)/contas/$',
        DetailContasView.as_view(),
        name='detail_contas'),
    # Urls caixa
    url(r'^caixa/',
        ListCaixaView.as_view(),
        name='list_caixa'),
    url(r'^(?P<pk>\d+)/caixa/$',
        DetailCaixaView.as_view(),
        name='detail_caixa'),
    # Urls saque
    url(r'^(?P<pk>\d+)/conta/saque/$',
        CreateSaqueView.as_view(),
        name='query_saque'),

]
