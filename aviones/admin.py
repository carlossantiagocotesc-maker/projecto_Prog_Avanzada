from django.contrib import admin
from .models import Avion

@admin.register(Avion)
class AvionAdmin(admin.ModelAdmin):
    list_display = ('avio_codigo', 'avio_capacidad')  # ← nombres correctos
    search_fields = ('avio_codigo',)
