from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from .models import Proveedor

# Create your views here.


class ProveedorDetailView(generic.DetailView):
    model = Proveedor
    template_name = "proveedores/proveedores_detail.html"


class ProveedorListView(generic.ListView):
    model = Proveedor
    context_object_name = 'proveedores_list'
    template_name = "proveedores/proveedores_list.html"

def proveedor_productos(request,id):
    proveedor = get_object_or_404(Proveedor,id = id)
    #revisar
    productos = proveedor.producto_set.all()
    return render(request,'productos/productos_list.html',{'productos_list': productos})


class ProveedorCreateView(CreateView):
    model = Proveedor
    fields = ["nombre", "apellido", "dni"]
    template_name = "proveedores/proveedores_edit.html"
    success_url = "http://localhost:8000/proveedores/"


class ProveedorUpdateView(UpdateView):
    model = Proveedor
    fields = ["nombre", "apellido", "dni"]
    template_name = "proveedores/proveedores_edit.html"
    success_url = "http://localhost:8000/proveedores/"
