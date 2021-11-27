from django.views.generic import TemplateView


class PaginaInicial (TemplateView):
    template_name = 'paginas/modelo.html'

class PaginaSobre (TemplateView):
    template_name = 'paginas/sobre.html'
