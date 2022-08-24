from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nacimiento = models.DateField()
    lugar_origen = models.CharField(max_length=40)

