from django.contrib import admin

from .models import Estado, Cidade, Pessoa, Produto, Categoria, Fornecedor, Venda
 
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Pessoa)
admin.site.register(Produto)
admin.site.register(Fornecedor)
admin.site.register(Categoria)
admin.site.register(Venda)

# Register your models here.
