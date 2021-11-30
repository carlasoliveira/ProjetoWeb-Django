from django.shortcuts import render
from .models import Estado, Cidade, Pessoa, Fornecedor, Produto, Categoria, Venda, ItensVenda
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

#CreateView
class EstadoCreate(CreateView):
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')
 
class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome', 'cpf', 'nascimento', 'email', 'telefone', 'cep', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')

class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'endereco', 'cidade', 'email', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome', 'categoria', 'codigo', 'preco', 'descricao', 'qtd_estoque']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')
     
class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

class VendaCreate(CreateView):
    model = Venda
    fields = ['tipoPagamento', 'cep_entrega', 'tipo_entrega', 'cep_entrega', 'logradouro', 'cidade', 'bairro', 'numero', 'complemento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-venda')

class ItensVendaCreate(CreateView):
    model = ItensVenda
    fields = ['preco_unitario', 'quantidade', 'venda', 'produto', 'carrinho']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-itens-venda')
     
#UpdateView
class EstadoUpdate(UpdateView):
    model = Estado
    fields = ['sigla','nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = ['nome', 'endereco', 'cidade', 'email', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')

class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['email', 'telefone', 'cep', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['nome', 'categoria', 'codigo', 'preco', 'descricao', 'qtd_estoque']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

class ItensVendaUpdate(UpdateView):
    model = ItensVenda
    fields = ['carrinho']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-venda')   

#DeleteView
class EstadoDelete(DeleteView):
	model = Estado
	template_name = 'cadastros/form-excluir.html'
	success_url = reverse_lazy('listar-estado')

class CidadeDelete(DeleteView):
	model = Cidade
	template_name = 'cadastros/form-excluir.html'
	success_url = reverse_lazy('listar-cidade')

class FornecedorDelete(DeleteView):
	model = Fornecedor
	template_name = 'cadastros/form-excluir.html'
	success_url = reverse_lazy('listar-fornecedor')

class PessoaDelete(DeleteView):
	model = Pessoa
	template_name = 'cadastros/form-excluir.html'
	success_url = reverse_lazy('listar-pessoa')

class CategoriaDelete(DeleteView):
	model = Categoria
	template_name = 'cadastros/form-excluir.html'
	success_url = reverse_lazy('listar-categoria')

class ProdutoDelete(DeleteView):
	model = Produto
	template_name = 'cadastros/form-excluir.html'
	success_url = reverse_lazy('listar-produto')

class VendaDelete(DeleteView):
	model = Venda
	template_name = 'cadastros/form-excluir.html'
	success_url = reverse_lazy('listar-venda')

class ItensVendaDelete(DeleteView):
    model = ItensVenda
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-venda')

#ListView
class EstadoList(ListView):
	model = Estado
	template_name = 'cadastros/listas/estado.html'

class CidadeList(ListView):
	model = Cidade
	template_name = 'cadastros/listas/cidade.html'

class PessoaList(ListView):
	model = Pessoa
	template_name = 'cadastros/listas/pessoa.html'

class FornecedorList(ListView):
	model = Fornecedor
	template_name = 'cadastros/listas/fornecedor.html'

class ProdutoList(ListView):
	model = Produto
	template_name = 'cadastros/listas/produto.html'

class CategoriaList(ListView):
	model = Categoria
	template_name = 'cadastros/listas/categoria.html'

class VendaList(ListView):
	model = Venda
	template_name = 'cadastros/listas/venda.html'
