from django.db import models
from django.db.models.fields import CharField, DateField

# Create your models here.

class Estado (models.Model):
    nome = models.CharField (max_length= 50)
    sigla = models.CharField(max_length= 2)
    def __str__(self):
        return self.sigla + "-" + self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=50, verbose_name='nome da cidade')
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
 
    def __str__(self):
        return self.nome + "-" + self.estado
    
class Fornecedor (models.Model):
    nome = models.CharField(max_length=100, verbose_name='nome do fornecedor')
    cnpj = models.IntegerField()
    endereço = models.CharField(max_length=100)
    telefone = int ()
    email = CharField (max_length=100)
    cidade = models.ForeignKey(Cidade,  on_delete=models.PROTECT )

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Qual seu nome?", help_text="Digite seu nome completo")
    nascimento = models.DateField(verbose_name='data de nascimento')
    email = models.CharField(max_length=100)
    cep = models.IntegerField ()
    cpf= models.IntegerField()
    telefone= models.IntegerField()
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
 
    def __str__(self):
        return '{} ({})'.format(self.nome, self.nascimento)

class Categoria(models.Model):
     nome = models.CharField(max_length=50, verbose_name="categoria do produto", help_text="Digite a categoria do produto")
     descricao = models.CharField(max_length=100)
    
class Produto(models.Model):
     nome = models.CharField(max_length=50, verbose_name="nome do produto", help_text="Digite o nome do produto")
     codigo = models.IntegerField()
     preco = models.FloatField()
     descricao = models.CharField(max_length=10)
     qtd_estoque = models.IntegerField()
     categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

     def __str__(self):
        return '{} ({})'.format(self.nome, self.codigo, self.categoria)

class Venda (models.Model):
    total_produtos= models.IntegerField()
    total_vendas= models.IntegerField()
    desconto= models.FloatField()
    data_compra= models.DateTimeField(auto_now=True)
    tipoPagamento= models.CharField(max_length=50)
    frete= models.FloatField()
    tipo_entrega= models.CharField(max_length=50)
    previsao_entrega= DateField()
    cep_entrega= models.IntegerField()
    logradouro= models.CharField(max_length=100)
    numero= models.IntegerField()
    bairro= models.CharField(max_length=50)
    complemento= models.CharField(max_length=50)
    cidade= models.ForeignKey(Cidade, on_delete=models.PROTECT)
    produto= models.ForeignKey(Produto, on_delete=models.PROTECT)
    comprador= models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return '{} \n {} \n {} \n {}'.format(self.comprador, self.produto, self.tipoPagamento, self.data_compra)

class Itens_Venda (models.Model):
    preco_unitario=models.FloatField()
    quantidade=models.IntegerField()
    venda=models.ForeignKey(Venda, on_delete=models.PROTECT)
    produto=models.ForeignKey(Produto, on_delete=models.PROTECT)

    def __str__(self):
        return 'Preço/unidade: {} Quantidade: {}'.format(self.preco_unitario, self.quantidade)
# Create your models here.
