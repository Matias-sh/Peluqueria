from django import forms
from .models import Cliente, Tratamiento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email']

class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = ['cliente', 'servicio', 'fecha']
