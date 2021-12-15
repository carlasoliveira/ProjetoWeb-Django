from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Estado, Cidade, Pessoa, Fornecedor, Produto, Categoria, Venda, ItensVenda
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

#CreateView
class EstadoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')
 
class CidadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

class PessoaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Pessoa
    fields = ['nome', 'cpf', 'nascimento', 'email', 'telefone', 'cep', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')

class FornecedorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    fields = ['nome', 'cnpj', 'endereco', 'cidade', 'email', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')

class ProdutoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome', 'categoria', 'codigo', 'preco', 'descricao', 'qtd_estoque']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')
     
class CategoriaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

class VendaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Venda
    fields = ['tipoPagamento', 'cep_entrega', 'tipo_entrega', 'cep_entrega', 'logradouro', 'cidade', 'bairro', 'numero', 'complemento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-venda')

class ItensVendaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = ItensVenda
    fields = ['quantidade', 'produto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-carrinho')

    def form_valid(self, form):
        form.instance.preco_unitario=form.instance.produto.preco
        form.instance.usuario=self.request.user
        url = super().form_valid(form)
        return url
     
#UpdateView
class EstadoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Estado
    fields = ['sigla','nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

class CidadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

class FornecedorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    fields = ['nome', 'endereco', 'cidade', 'email', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')

class PessoaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Pessoa
    fields = ['email', 'telefone', 'cep', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome', 'categoria', 'codigo', 'preco', 'descricao', 'qtd_estoque']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

class ItensVendaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = ItensVenda
    fields = ['quantidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-carrinho')   
    #self.object.produto

#DeleteView
class EstadoDelete(LoginRequiredMixin, DeleteView):
	model = Estado
	template_name = 'cadastros/form-excluir.html'
	success_url = reverse_lazy('listar-estado')

class CidadeDelete(LoginRequiredMixin, DeleteView):
	model = Cidade
	template_name = 'cadastros/form-excluir.html'
	success_url = reverse_lazy('listar-cidade')

class FornecedorDelete(LoginRequiredMixin, DeleteView):
	model = Fornecedor
	template_name = 'cadastros/form-excluir.html'
	success_url = reverse_lazy('listar-fornecedor')

class PessoaDelete(LoginRequiredMixin, DeleteView):
	model = Pessoa
	template_name = 'cadastros/form-excluir.html'
	success_url = reverse_lazy('listar-pessoa')

class CategoriaDelete(LoginRequiredMixin, DeleteView):
	model = Categoria
	template_name = 'cadastros/form-excluir.html'
	success_url = reverse_lazy('listar-categoria')

class ProdutoDelete(LoginRequiredMixin, DeleteView):
	model = Produto
	template_name = 'cadastros/form-excluir.html'
	success_url = reverse_lazy('listar-produto')

class VendaDelete(LoginRequiredMixin, DeleteView):
	model = Venda
	template_name = 'cadastros/form-excluir.html'
	success_url = reverse_lazy('listar-venda')

class ItensVendaDelete(LoginRequiredMixin, DeleteView):
    model = ItensVenda
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-carrinho')

#ListView
class EstadoList(LoginRequiredMixin, ListView):
	model = Estado
	template_name = 'cadastros/listas/estado.html'

class CidadeList(LoginRequiredMixin, ListView):
	model = Cidade
	template_name = 'cadastros/listas/cidade.html'

class PessoaList(LoginRequiredMixin, ListView):
	model = Pessoa
	template_name = 'cadastros/listas/pessoa.html'

class FornecedorList(LoginRequiredMixin, ListView):
	model = Fornecedor
	template_name = 'cadastros/listas/fornecedor.html'

class ProdutoList(ListView):
	model = Produto
	template_name = 'cadastros/listas/produto.html'

class CategoriaList(ListView):
	model = Categoria
	template_name = 'cadastros/listas/categoria.html'

class VendaList(LoginRequiredMixin, ListView):
	model = Venda
	template_name = 'cadastros/listas/venda.html'

class ItensVendaList(LoginRequiredMixin, ListView):
    model = ItensVenda
    template_name = 'cadastros/listas/carrinho.html'

    def get_queryset(self):
        self.object_list=ItensVenda.objects.filter(usuario=self.request.user, carrinho=True)