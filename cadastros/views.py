from django.shortcuts import render
from .models import Estado, Cidade, Pessoa, Fornecedor, Produto, Categoria, Venda
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class EstadoCreate(CreateView):
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')

class EstadoUpdate(CreateView):
    model = Estado
    fields = ['nome']
    template_name = '.cadastros/formulario.html'
    success_url = reverse_lazy('index')
 
 
class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')

class CidadeUpdate(CreateView):
    model = Cidade
    fields = [ 'nome']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')

class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome', 'nascimento', 'email', 'telefone', 'cpf', 'cep', 'cidade']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')

class PessoaUpdate(CreateView):
    model = Pessoa
    fields = ['nome', 'nascimento', 'email', 'telefone', 'cep', 'cidade']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')

class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = ['nome', 'nascimento', 'email', 'telefone', 'cep', 'cidade', 'cnpj']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')
     
class FornecedorUpdate(CreateView):
    model = Fornecedor
    fields = ['nome', 'nascimento', 'email', 'telefone', 'cep', 'cidade']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome', 'categoria', 'codigo', 'preco', 'descricao', 'qtd_estoque']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')

class ProdutoUpdate(CreateView):
    model = Produto
    fields = ['nome', 'categoria', 'codigo', 'preco', 'descricao', 'qtd_estoque']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')


     
class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome', 'descricao']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')

    
class CategoriaUpdate(CreateView):
    model = Categoria
    fields = ['nome', 'descricao']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')

class VendaCreate(CreateView):
    model = Venda
    fields = ['tipoPagamento', 'frete', 'tipo_entrega', 'cep_entrega', 'logradouro', 'cidade', 'bairro', 'numero', 'complementos']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')

class VendaUpdate(CreateView):
    model = Venda
    fields = ['tipoPagamento', 'frete', 'tipo_entrega', 'cep_entrega', 'logradouro', 'cidade', 'bairro', 'numero', 'complementos']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')
          
     
# Create your views here.
