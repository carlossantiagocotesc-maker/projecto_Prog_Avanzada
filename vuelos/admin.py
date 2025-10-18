from django.contrib import admin
from .models import Vuelo, VueloXPasajeros

class VueloXPasajerosInline(admin.TabularInline):
    model = VueloXPasajeros
    extra = 1

@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    list_display = ('vuel_origen', 'vuel_destino', 'vuel_fecha', 'avio')
    search_fields = ('vuel_origen', 'vuel_destino')
    list_filter = ('vuel_origen', 'vuel_destino')
    inlines = [VueloXPasajerosInline]

@admin.register(VueloXPasajeros)
class VueloXPasajerosAdmin(admin.ModelAdmin):
    list_display = ('pasa', 'vuel')
