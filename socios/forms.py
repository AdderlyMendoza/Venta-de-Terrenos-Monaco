from django import forms
from .models import *
class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['estado', 'documento', 'nombre', 'ap_paterno', 'ap_Materno', 'celular']
        widgets = {
            'estado': forms.Select(choices=((True, 'Activo'), (False, 'No Activo'))),
        }



class InversionForm(forms.ModelForm):
    class Meta:
        model = Inversion
        fields = ['tipo', 'socio', 'proyectos', 'cantidad_invertida', 'porcentaje_ganancia']
