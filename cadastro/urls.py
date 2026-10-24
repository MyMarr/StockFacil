from django.urls import path
from cadastro.views import ProdutoListar


app_name = 'cadastro'
urlpatterns = [
    path("listar/", ProdutoListar.as_view(), name = "listar_produto")
 ]