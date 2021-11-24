
from django.contrib import admin
from django.urls import path, include

from cadastros.apps import CadastrosConfig
from paginas.views import PaginaInicial     
from .views import EstadoCreate, CidadeCreate, PessoaCreate, ProdutoCreate, VendaCreate, CategoriaCreate, FornecedorCreate

urlpatterns = [
   path('', PaginaInicial.as_view(), name="index"),
   path('cadastros/estado/', EstadoCreate.as_view(), name="cadastrar-estado"),
   path('cadastros/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
   path('cadastros/pessoa/', EstadoCreate.as_view(), name="cadastrar-pessoa"),
   path('cadastros/produto/', CidadeCreate.as_view(), name="cadastrar-produto"),
   path('cadastros/venda/', EstadoCreate.as_view(), name="cadastrar-venda"),
   path('cadastros/fornecedor/', CidadeCreate.as_view(), name="cadastrar-fornecedor"),
]
