from django.conf.urls import url
from .views import HomeContaView, ListContasView, DetailContasView

urlpatterns = [

    url(r'^$', HomeContaView.as_view(), name='index'),
    url(r'^contas/', ListContasView.as_view(), name='contas'),
    url(r'^(?P<pk>\d+)/contas/$', DetailContasView.as_view(), name='detail')

]
