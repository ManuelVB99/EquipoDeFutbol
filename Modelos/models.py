from django.db import models

# Create your models here.

class Jugadores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=20)
    pieHabil = models.CharField(max_length=20)

class Equipo_Tecnico(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    funcion = models.CharField(max_length=20)

class Fechas(models.Model):
    equipoContrario = models.CharField(max_length=40)
    fecha = models.DateField()
    lugar = models.CharField(max_length=15)