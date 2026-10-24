#Registra os models para aparecerem no painel /admin.
# Register your models here.

#Campos usados na barra de busca = search_fields
#Colunas exibidas na listagem= list_display
#Filtros na lateral da listagem = list_filter

from django.contrib import admin
from .models import Produto, Quantidade, Preco

class ProdutoAdmin(admin.ModelAdmin): 
    list_display = ("nome_produto",)
    search_fields = ("nome_produto",)

class QuantidadeAdmin(admin.ModelAdmin):
    list_display = ("quantidade_produto",)
    search_fields = ("quantidade_produto",)

class PrecoAdmin(admin.ModelAdmin):
    list_display = ("preco_produto",)
    search_fields = ("preco_produto",)

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Quantidade, QuantidadeAdmin)
admin.site.register(Preco, PrecoAdmin)