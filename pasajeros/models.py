from django.db import models

class Pasajero(models.Model):
    pasa_nombre = models.CharField(max_length=30)
    pasa_email = models.CharField(max_length=50, blank=True, null=True)
    pasa_telefono = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.pasa_nombre
