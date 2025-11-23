# aviones/forms.py
from django import forms
from .models import Avion

class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['avion_codigo', 'avion_capacidad']