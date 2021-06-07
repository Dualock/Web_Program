from django.db import models

# Create your models here.
class Estadio(models.Model):
    nombre = models.CharField(max_length=200)
    capacidad = models.IntegerField(default=0)
