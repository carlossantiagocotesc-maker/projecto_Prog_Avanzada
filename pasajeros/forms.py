from django import forms
from .models import Pasajero

class PasajeroForm(forms.ModelForm):
    class Meta:
        model = Pasajero
        fields = ['pasa_nombre', 'pasa_email', 'pasa_telefono']