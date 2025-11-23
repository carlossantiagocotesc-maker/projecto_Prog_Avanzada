from django import forms
from .models import Vuelo

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['vuel_origen', 'vuel_destino', 'vuel_fecha', 'avio']