from django.db import models

# Create your models here.

class Project(models.Model):
    nombre_producto = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()

    