from django.db import models

class Avion(models.Model):
    avio_codigo = models.CharField(max_length=30, unique=True)
    avio_capacidad = models.CharField(max_length=30)

    def __str__(self):
        return self.avio_codigo
