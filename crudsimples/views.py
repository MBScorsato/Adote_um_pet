from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from crudsimples.models import Produto


class ProdutoNovo(generic.CreateView):
    model = Produto
    fields = '__all__'


class ProdutoLista(generic.ListView):
    model = Produto
    queryset = Produto.objects.all()


class ProdutoAtualizar(generic.UpdateView):
    model = Produto
    fields = '__all__'
    template_name_suffix = '_update_form'


class ProdutoDetalhe(generic.DetailView):
    model = Produto


class ProdutoApagar(generic.DeleteView):
    model = Produto
    success_url = reverse_lazy('produto-lista')

