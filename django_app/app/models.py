from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
Clase estadio: se utiliza para crear un objeto estadio y almacenar
los datos en la base de datos de sql
'''
class Estadio(models.Model):
    nombre = models.CharField(max_length=200)
    descripción = models.TextField(default="")
    def __str__(self):
        return "%d %s" % (self.id, self.nombre)

'''
Clase ImagenEstadio: hecha para mostrar la imagen del estadio
'''
class ImagenEstadio(models.Model):
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    altText = models.CharField(max_length=200, default="Imagen de Estadio")

'''
Clase ImagenUsuario: hecha para mostrar la imagen del estadio
'''
class ImagenUsuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    altText = models.CharField(max_length=200, default="Imagen de Usuario")

'''
Clase Partido: se utiliza para crear el objeto Partido y almacenar
los datos en la base de datos de sql
'''
class Partido(models.Model):
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()

'''
Clase ImagenPartido: hecha para mostrar la imagen del los equipos
'''
class ImagenPartido(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    altText = models.CharField(max_length=200, default="Imagen de Partido")

'''
Clase TipoAsiento: se utiliza para crear objetos tipo asiento y almacenar
sus datos en la base de datos de sql
'''
class TipoAsiento(models.Model):
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    costo = models.FloatField()
    capacidad = models.IntegerField()
    descripcion = models.TextField()
    def __str__(self):
        return "%s. Precio: %.2f. Capacidad %d." % (self.nombre, self.costo, self.capacidad)

'''
Clase Reserva: se utiliza para crear objetos tipo reserva y almacenar
sus datos en la base de datos de sql
'''
class Reserva(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipoAsiento = models.ForeignKey(TipoAsiento, on_delete=models.CASCADE)
