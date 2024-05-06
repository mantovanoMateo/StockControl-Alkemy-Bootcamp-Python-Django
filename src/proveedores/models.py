from django.db import models

# Create your models here.
class Proveedor(models.Model):
    '''Clase que representa a los proveedores de productos'''
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()

    def __str__ (self):   
        return F'{self.nombre} - {self.apellido} - {self.dni}'