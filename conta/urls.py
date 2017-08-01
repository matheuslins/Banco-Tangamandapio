from django.conf.urls import url
from .views import HomeContaView

urlpatterns = [

    url(r'^$', HomeContaView.as_view(), name='index'),
    # url(r'^contas/$', ListContasView.as_view(), name='contas'),

]
