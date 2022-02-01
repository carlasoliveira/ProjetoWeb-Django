from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from cadastros.models import Pessoa
from django.urls import reverse_lazy
from .forms import UsuarioForm
from django.shortcuts import get_object_or_404

# Create your views here.

class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('login')
    form_class =UsuarioForm

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="cliente")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Pessoa.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registre-se"
        context['botao'] = "Finalizar cadastro"

        return context

class PessoaUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    model = Pessoa
    fields = ['nome', 'nascimento', 'email', 'cep', 'cidade', 'cpf', 'telefone']
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Pessoa, usuario=self.request.user)
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Meus dados"
        context['botao'] = "Atualizar"

        return context