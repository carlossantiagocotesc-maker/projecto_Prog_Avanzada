from django.contrib import admin
from .models import Pasajero

@admin.register(Pasajero)
class PasajeroAdmin(admin.ModelAdmin):
    list_display = ('pasa_nombre', 'pasa_email', 'pasa_telefono')
    search_fields = ('pasa_nombre',)
