from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from .models import Producto

# Create your views here.

class ProductosList(generic.ListView):
    queryset = Producto.objects.all()
    context_object_name = 'productos_list'
    template_name = "productos/productos_list.html"


class ProductoCreateView(CreateView):
    model = Producto
    fields = ["nombre", "precio", "stock_actual", "proveedor"]
    template_name = "productos/productos_edit.html"
    success_url = "http://localhost:8000/productos/"


class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ["nombre", "precio", "stock_actual", "proveedor"]
    template_name = "productos/productos_edit.html"
    success_url = "http://localhost:8000/productos/"

def comprar(request,id):
    producto = get_object_or_404(Producto, id=id)
    producto.stock_actual = producto.stock_actual+1
    producto.save()
    return redirect('productos:productos_list')

def vender(request,id):
    producto = get_object_or_404(Producto, id=id)
    producto.stock_actual = producto.stock_actual-1
    producto.save()
    return redirect('productos:productos_list')
