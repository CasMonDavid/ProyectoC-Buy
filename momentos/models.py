from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nomProducto = models.CharField(max_length=300, verbose_name="nombre_producto")
    costo = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="costo_producto")
    precio = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="precio_producto")
    descripcion = models.CharField(max_length=1000, verbose_name="descripcion_producto")
    cantidad = models.IntegerField(verbose_name="cantidad_producto")