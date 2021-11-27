from django.db import models
from django.db.models.fields import CharField, DateField
from django.contrib.auth.models import User

# Create your models here.

class Estado (models.Model):
    nome = models.CharField (max_length=50)
    sigla = models.CharField(max_length=2)
    
    def __str__(self):
        return '{}/{}'.format(self.nome, self.sigla)

class Cidade(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Cidade')
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
 
    def __str__(self):
        return '{}/{}'.format(self.nome, self.estado.sigla)
    
class Fornecedor (models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do fornecedor')
    cnpj = models.CharField(max_length=18)
    endereço = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT )

    def __str__(self):
        return '{} ({})'.format(self.nome, self.email)

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome Completo", help_text="Insira seu nome completo")
    nascimento = models.DateField(verbose_name='Data de nascimento')
    email = models.EmailField(max_length=100)
    cep = models.CharField(max_length=10)
    cpf= models.CharField(max_length=14)
    telefone= models.CharField(max_length=15)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.nome, self.nascimento)

class Categoria(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Categoria do produto", help_text="Insira a categoria do produto")
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return '{}: \n {}'.format(self.nome, self.descricao)
    
class Produto(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do produto", help_text="Insira o nome do produto")
    codigo = models.IntegerField(verbose_name="Código")
    preco = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço")
    descricao = models.CharField(max_length=20, verbose_name="Descrição")
    qtd_estoque = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({}) - {}\n {}'.format(self.nome, self.codigo, self.categoria, self.preco)

class Venda (models.Model):
    total_produtos= models.IntegerField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    desconto=models.DecimalField(max_digits=8, decimal_places=2)
    data_compra= models.DateTimeField(auto_now_add=True)
    tipoPagamento= models.CharField(max_length=50)
    frete= models.DecimalField(max_digits=8, decimal_places=2)
    tipo_entrega= models.CharField(max_length=50)
    previsao_entrega= DateField()
    cep_entrega= CharField(max_length=10)
    logradouro= models.CharField(max_length=100, blank=True, null=True)
    numero= models.CharField(max_length=20)
    bairro= models.CharField(max_length=50)
    complemento= models.CharField(max_length=50, blank=True, null=True)
    cidade= models.ForeignKey(Cidade, on_delete=models.PROTECT)
    comprador= models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return 'Data da compra: {}\n Valor: {}\n Frete: {}\n Desconto: {}\n Total: {}\n Forma de pagamento: {}\n Previsão de entrega: {}'.format(self.data_compra, self.total_produtos, self.frete, self.desconto, self.valor, self.tipoPagamento, self.previsao_entrega)

class Itens_Venda (models.Model):
    preco_unitario=models.DecimalField(max_digits=8, decimal_places=2)
    quantidade=models.IntegerField()
    venda=models.ForeignKey(Venda, on_delete=models.PROTECT, null=True)
    produto=models.ForeignKey(Produto, on_delete=models.PROTECT)
    carrinho=models.BooleanField(default=True)

    def __str__(self):
        return 'Venda:{} Preço/unidade: {} Quantidade: {}'.format(self.venda.pk, self.preco_unitario, self.quantidade)

