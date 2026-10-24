#Tabelas do banco de dados, escritas como classes Python.
# Create your models here.
#Cada model é uma classe Python que vira uma tabela no banco. Cada atributo vira uma coluna.


# verificcado, mas ainda não tem migração 

from django.db import models

#criando a classe para a tabela de produtos, com o nome do produto como atributo.
class Produto(models.Model):
    nome_produto = models.CharField(max_length=80)

    #Configurações do model, não viram coluna.
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["nome_produto"]

    #Texto exibido no admin no lugar de Person object(1)
    def __str__(self):
        return f"{self.nome_produto}"

#Criando

class Quantidade(models.Model): 
    quantidade_produto = models.PositiveIntegerField(
        verbose_name="Quantidade produto(s)", 
        default=0)   

    produto = models.ForeignKey(
        Produto, 
        on_delete=models.CASCADE, 
        verbose_name="Produto")

    class Meta:
        verbose_name = "Quantidade"
        verbose_name_plural = "Quantidades"
        ordering = ["produto"]

    def __str__(self):
        return f"{self.quantidade_produto}X"

class Preco(models.Model):
    
    preco_produto = models.DecimalField(max_digits=5, decimal_places = 2, verbose_name="Preço produto(s)")

    produto = models.ForeignKey( 
    Produto, 
    on_delete = models.CASCADE,
    verbose_name = "Valor(Un)")

    class Meta:
        verbose_name = "Valor(Un)"
        verbose_name_plural = "Valores(Un)"
        ordering = ["produto"]
   



