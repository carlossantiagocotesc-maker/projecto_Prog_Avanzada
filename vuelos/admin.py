from django.contrib import admin
from .models import Vuelo, VueloXPasajeros

class VueloXPasajerosInline(admin.TabularInline):
    model = VueloXPasajeros
    extra = 1

@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    list_display = ('vuel_origen', 'vuel_destino', 'vuel_fecha', 'avio', 'num_pasajeros')
    search_fields = ('vuel_origen', 'vuel_destino')
    list_filter = ('vuel_origen', 'vuel_destino')
    inlines = [VueloXPasajerosInline]

    def num_pasajeros(self, obj):
        # ✅ Ahora usamos el related_name definido en models.py
        return obj.vuelxpasajeros.count()
    num_pasajeros.short_description = 'Pasajeros'

@admin.register(VueloXPasajeros)
class VueloXPasajerosAdmin(admin.ModelAdmin):
    list_display = ('pasa', 'vuel')