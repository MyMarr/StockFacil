#Lógica das páginas, recebe a requisição e devolve a resposta.
# Create your views here.

from django.shortcuts import render
from  cadastro.models import Produto, Quantidade, Preco
from django.views.generic import ListView


class ProdutoListar(ListView):
    model = Produto
    template_name = "cadastro/produto_list.html"
    context_object_name = "produtos"
    paginate_by = 5