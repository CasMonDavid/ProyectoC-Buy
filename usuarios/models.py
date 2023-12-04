from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class modeloImagenes(models.Model):
    imagenes = models.ImageField(upload_to="productos", null=True)
