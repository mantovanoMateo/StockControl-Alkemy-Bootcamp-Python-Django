from django.urls import path
from .views import ProveedorCreateView, ProveedorDetailView, ProveedorListView, ProveedorUpdateView,proveedor_productos

app_name='proveedores'

urlpatterns = [
    path("", ProveedorListView.as_view(), name='proveedores_list'),
    path("<int:pk>", ProveedorDetailView.as_view(), name='proveedores_detail'),
    path('crear/',ProveedorCreateView.as_view(),name='proveedor_crear'),
    path("editar/<int:pk>", ProveedorUpdateView.as_view(), name='proveedores_edit'),
    path("productos/<int:id>/",proveedor_productos, name="proveedor_productos")
]

