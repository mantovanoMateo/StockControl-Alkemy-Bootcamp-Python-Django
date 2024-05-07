from django.urls import path
from .views import ProductoCreateView, ProductosList, ProductoUpdateView, comprar, vender, productos_buscar

app_name = 'productos'

urlpatterns = [
    path('crear/',ProductoCreateView.as_view(),name='productos_crear'),
    path('',ProductosList.as_view(),name='productos_list'),
    path('editar/<int:pk>/',ProductoUpdateView.as_view(), name='productos_editar'),
    path('comprar/<int:id>',comprar,name="producto_comprar"),
    path('vender/<int:id>',vender,name="producto_vender"),
    path('buscar/', productos_buscar, name='buscar'),
]
