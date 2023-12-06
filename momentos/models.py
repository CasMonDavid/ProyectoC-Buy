from django.utils import timezone
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User



# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nomProducto = models.CharField(max_length=300, verbose_name="nombre_producto")
    costo = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="costo_producto")
    precio = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="precio_producto")
    descripcion = models.CharField(max_length=1000, verbose_name="descripcion_producto")
    cantidad = models.IntegerField(verbose_name="cantidad_producto")
    imagen_direccion = models.ImageField(upload_to='carritoImagenes/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], null=True)

class carrito_usuario(models.Model):
    id_compra = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    total = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    esta_completado = models.BooleanField(default=False)

class carrito_producto(models.Model):
    id_compra_producto = models.AutoField(primary_key=True)
    id_compra = models.ForeignKey(carrito_usuario, on_delete=models.DO_NOTHING)
    id_producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    cantidad_pro = models.IntegerField(default=1)
    total_precio = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    esta_completado = models.BooleanField(default=False)

class historial_usuario(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    id_compra = models.ForeignKey(carrito_usuario, on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField(default=timezone.now)