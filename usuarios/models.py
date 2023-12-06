from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
class modeloImagenes(models.Model):
    imagenes = models.ImageField(upload_to="productos", null=True)

class customUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=1000)
    numero_celular = models.CharField(max_length=20)

    def di_atributos(self):
        #user = User.objects.last()
        #persUsuario = customUsuario.objects.create(user=user, direccion='Sin direccion', numero_celular='6120000000')
        return "Hola, mi nombre es {}".format(self.user.first_name)