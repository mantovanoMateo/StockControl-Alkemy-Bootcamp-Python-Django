from django.db import models
from proveedores.models import Proveedor

# Create your models here.
class Producto(models.Model):
    '''Clase que representa los productos que seran cargados a la plataforma'''
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    
    def __str__ (self):   
        return F'{self.nombre.upper()} - {self.precio} - {self.stock_actual}'