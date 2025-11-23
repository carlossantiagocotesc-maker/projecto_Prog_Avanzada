from django.db import models

class Avion(models.Model):
    avion_codigo = models.CharField(max_length=30, unique=True)
    avion_capacidad = models.CharField(max_length=30)

    def __str__(self):
        return self.avion_codigo