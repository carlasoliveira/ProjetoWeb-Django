
from django.contrib import admin
from django.urls import path, include

from cadastros.apps import CadastrosConfig
from paginas.views import PaginaInicial     
from .views import EstadoCreate, CidadeCreate, PessoaCreate, ProdutoCreate, VendaCreate, CategoriaCreate, FornecedorCreate, ItensVendaCreate 
from .views import EstadoUpdate, CidadeUpdate, FornecedorUpdate, PessoaUpdate, CategoriaUpdate, ProdutoUpdate, ItensVendaUpdate
from .views import EstadoDelete, CidadeDelete, FornecedorDelete, PessoaDelete, CategoriaDelete, ProdutoDelete, VendaDelete, ItensVendaDelete
from .views import EstadoList, CidadeList, FornecedorList, PessoaList, CategoriaList, ProdutoList, VendaList

urlpatterns = [
   path('', PaginaInicial.as_view(), name="index"),

   #URLS - CreateView
   path('cadastrar/estado/', EstadoCreate.as_view(), name="cadastrar-estado"),
   path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
   path('cadastrar/pessoa/', PessoaCreate.as_view(), name="cadastrar-pessoa"),
   path('cadastrar/fornecedor/', FornecedorCreate.as_view(), name="cadastrar-fornecedor"),
   path('cadastrar/produto/', ProdutoCreate.as_view(), name="cadastrar-produto"),
   path('cadastrar/categoria/', CategoriaCreate.as_view(), name="cadastrar-categoria"),
   path('cadastrar/venda/', VendaCreate.as_view(), name="cadastrar-venda"),
   path('cadastrar/itens-venda/', ItensVendaCreate.as_view(), name="cadastrar-itens-venda"),

   #URLS - UpdateView
   path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
   path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
   path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name="editar-pessoa"),
   path('editar/fornecedor/<int:pk>/', FornecedorUpdate.as_view(), name="editar-fornecedor"),
   path('editar/produto/<int:pk>/', ProdutoUpdate.as_view(), name="editar-produto"),
   path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name="editar-categoria"),
   path('editar/itens-venda/<int:pk>/', ItensVendaUpdate.as_view(), name="editar-itens-venda"),

   #URLS - DeleteView
   path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name="deletar-estado"),
   path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name="deletar-cidade"),
   path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name="deletar-pessoa"),
   path('excluir/fornecedor/<int:pk>/', FornecedorDelete.as_view(), name="deletar-fornecedor"),
   path('excluir/produto/<int:pk>/', ProdutoDelete.as_view(), name="deletar-produto"),
   path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(), name="deletar-categoria"),
   path('excluir/venda/<int:pk>/', VendaDelete.as_view(), name="deletar-venda"),
   path('excluir/itens-venda/<int:pk>/', ItensVendaDelete.as_view(), name="deletar-itens-venda"),

   #URLS - ListView
   path('listar/estado/', EstadoList.as_view(), name="listar-estado"),
   path('listar/cidade/', CidadeList.as_view(), name="listar-cidade"),
   path('listar/pessoa/', PessoaList.as_view(), name="pessoa-pessoa"),
   path('listar/fornecedor/', FornecedorList.as_view(), name="listar-fornecedor"),
   path('listar/produto/', ProdutoList.as_view(), name="listar-produto"),
   path('listar/categoria/', CategoriaList.as_view(), name="listar-categoria"),
   path('listar/venda/', VendaList.as_view(), name="listar-venda"),
]
