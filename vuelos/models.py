from django.db import models
from aviones.models import Avion
from pasajeros.models import Pasajero

class Vuelo(models.Model):
    vuel_origen = models.CharField(max_length=30)
    vuel_destino = models.CharField(max_length=30)
    vuel_fecha = models.DateField()
    avio = models.ForeignKey(Avion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vuel_origen} → {self.vuel_destino} ({self.vuel_fecha})"

class VueloXPasajeros(models.Model):
    pasa = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    # ✅ Se agrega related_name para acceso inverso desde Vuelo
    vuel = models.ForeignKey(Vuelo, on_delete=models.CASCADE, related_name="vuelxpasajeros")

    def __str__(self):
        return f"{self.pasa} en {self.vuel}"

    class Meta:
        verbose_name = "Vuelo x Pasajeros"
        verbose_name_plural = "Vuelos x Pasajeros"
