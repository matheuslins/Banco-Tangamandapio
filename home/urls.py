from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^$', auth_views.login,
        {'template_name': 'home/login.html'},
        name='login'),
    url(r'^sair/$', auth_views.logout,
        {'next_page': 'home:login'}, name='logout'),

]
