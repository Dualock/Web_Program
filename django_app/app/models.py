from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Estadio(models.Model):
    nombre = models.CharField(max_length=200)
    descripción = models.TextField(default="")
    def __str__(self):
        return "%d %s" % (self.id, self.nombre)

class ImagenEstadio(models.Model):
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    altText = models.CharField(max_length=200, default="Imagen de Estadio")

class ImagenUsuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    altText = models.CharField(max_length=200, default="Imagen de Usuario")

class Partido(models.Model):
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()

class ImagenPartido(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    altText = models.CharField(max_length=200, default="Imagen de Usuario")

class TipoAsiento(models.Model):
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    costo = models.FloatField()
    capacidad = models.IntegerField()
    descripcion = models.TextField()
    def __str__(self):
        return "%s. Precio: %.2f. Capacidad %d." % (self.nombre, self.costo, self.capacidad)

class Reserva(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipoAsiento = models.ForeignKey(TipoAsiento, on_delete=models.CASCADE)
    cantidad_espacios_reservados = models.IntegerField()
