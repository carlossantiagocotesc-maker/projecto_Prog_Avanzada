from django.contrib import admin
from .models import Avion

class AvionAdmin(admin.ModelAdmin):
    list_display = ('avion_codigo', 'avion_capacidad')

admin.site.register(Avion, AvionAdmin)

