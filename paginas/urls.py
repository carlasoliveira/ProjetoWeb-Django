from django.urls import path
from .views import PaginaInicial, PaginaSobre

urlpatterns = [
    #path ('endereço/', MinhaView.as.viiew(), name= 'referência/apelido'),
    path('inicio/', PaginaInicial.as_view(), name='index'),
    path('sobre/', PaginaSobre.as_view(), name='sobre'),
]