from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import Estado, Cidade, Pessoa, Fornecedor, Produto, Categoria, Venda, ItensVenda
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

import datetime

#CreateView
class EstadoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')
    group_required = u"Administrador"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de estado"
        context['botao'] = "Cadastrar"

        return context
 
class CidadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de cidade"
        context['botao'] = "Cadastrar"

        return context
class PessoaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Pessoa
    fields = ['nome', 'cpf', 'nascimento', 'email', 'telefone', 'cep', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')

class FornecedorCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Fornecedor
    fields = ['nome', 'cnpj', 'endereco', 'cidade', 'email', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de fornecedor"
        context['botao'] = "Cadastrar"

        return context

class ProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Produto
    fields = ['nome', 'categoria', 'codigo', 'preco', 'descricao', 'qtd_estoque']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de produto"
        context['botao'] = "Cadastrar"

        return context
     
class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Categoria
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de categoria"
        context['botao'] = "Cadastrar"

        return context

class VendaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Venda
    fields = ['tipoPagamento', 'cep_entrega', 'tipo_entrega', 'cep_entrega', 'logradouro', 'cidade', 'bairro', 'numero', 'complemento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-venda')

    def form_valid(self, form):
        iv=ItensVenda.objects.filter(usuario=self.request.user, carrinho=True)
        if(not iv):
            form.add_error(None, 'Seu carrinho está vazio')
            return self.form_invalid(form)

        form.instance.total_produtos=0
        form.instance.valor=0
        form.instance.desconto=0
        form.instance.frete=10
        form.instance.previsao_entrega= datetime.date.today() + datetime.timedelta(10)
        form.instance.comprador=self.request.user
        url = super().form_valid(form)
        
        valor=0
        for item in iv:
            valor+=item.produto.preco
            item.venda=self.object
            item.carrinho=False
            item.save()

        self.object.valor=valor
        self.object.save()
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Carrinho"
        context['botao'] = "Finalizar"

        return context
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
class EstadoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Estado
    fields = ['sigla','nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar estado"
        context['botao'] = "Atualizar"

        return context

class CidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar cidade"
        context['botao'] = "Atualizar"

        return context

class FornecedorUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Fornecedor
    fields = ['nome', 'endereco', 'cidade', 'email', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar fornecedor"
        context['botao'] = "Atualizar"

        return context

class PessoaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Pessoa
    fields = ['email', 'telefone', 'cep', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')

class CategoriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Categoria
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar categoria"
        context['botao'] = "Atualizar"

        return context

class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Produto
    fields = ['nome', 'categoria', 'codigo', 'preco', 'descricao', 'qtd_estoque']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar produto"
        context['botao'] = "Atualizar"

        return context

class ItensVendaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = ItensVenda
    fields = ['quantidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-carrinho')   
    #self.object.produto

#DeleteView
class EstadoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Estado
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-estado')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir estado"
        context['botao'] = "Excluir"

        return context

class CidadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url=reverse_lazy('login')
    group_required = u"Administrador"
    model=Cidade
    template_name='cadastros/form-excluir.html'
    success_url=reverse_lazy('listar-cidade')

def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir cidade"
        context['botao'] = "Excluir"

        return context

class FornecedorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url=reverse_lazy('login')
    group_required = u"Administrador"
    model=Fornecedor
    template_name='cadastros/form-excluir.html'
    success_url=reverse_lazy('listar-fornecedor')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir fornecedor"
        context['botao'] = "Excluir"

        return context

class PessoaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Pessoa
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pessoa')

class CategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categoria')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir categoria"
        context['botao'] = "Excluir"

        return context

class ProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir produto"
        context['botao'] = "Excluir"

        return context

class VendaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Venda
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-venda')

class ItensVendaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = ItensVenda
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-carrinho')

#ListView
class EstadoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Estado
    template_name = 'cadastros/listas/estado.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Estados cadastrados"

        return context

class CidadeList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Cidade
    template_name = 'cadastros/listas/cidade.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cidades cadastradas"

        return context

class PessoaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Pessoa
    template_name = 'cadastros/listas/pessoa.html'

class FornecedorList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Fornecedor
    template_name = 'cadastros/listas/fornecedor.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Fornecedores cadastrados"

        return context

class ProdutoList(ListView):
    model = Produto
    template_name = 'cadastros/listas/produto.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Produtos cadastrados"

        return context

class CategoriaList(ListView):
	model = Categoria
	template_name = 'cadastros/listas/categoria.html'

class VendaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Venda
    template_name = 'cadastros/listas/venda.html'

    def get_queryset(self):
        self.object_list=Venda.objects.filter(comprador=self.request.user)
        return self.object_list

class ItensVendaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = ItensVenda
    template_name = 'cadastros/listas/carrinho.html'

    def get_queryset(self):
        self.object_list=ItensVenda.objects.filter(usuario=self.request.user, carrinho=True)
        return self.object_list