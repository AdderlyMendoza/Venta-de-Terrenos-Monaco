from django import forms
from .models import *

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'  

    def __init__(self, *args, **kwargs):
        super(EmpleadoForm, self).__init__(*args, **kwargs)

        self.fields['estado'].label = 'estado'
        self.fields['cargo'].label = 'cargo'
        self.fields['nombres'].label = 'nombres'
        self.fields['ap_paterno'].label = 'ap_paterno'
        self.fields['ap_materno'].label = 'ap_materno'
        self.fields['documento'].label = 'Documento'
        self.fields['celular'].label = 'Celular'

        self.fields['estado'].widget.attrs['placeholder'] = 'Estado'
        self.fields['cargo'].widget.attrs['placeholder'] = 'Cargo'
        self.fields['nombres'].widget.attrs['placeholder'] = 'Nombres'
        self.fields['ap_paterno'].widget.attrs['placeholder'] = 'Apellido Paterno'
        self.fields['ap_materno'].widget.attrs['placeholder'] = 'Apellido Materno'
        self.fields['documento'].widget.attrs['placeholder'] = 'Documento'
        self.fields['celular'].widget.attrs['placeholder'] = 'Celular'

        self.fields['estado'].widget.attrs['class'] = 'form-control'
        self.fields['cargo'].widget.attrs['class'] = 'form-control'
        self.fields['nombres'].widget.attrs['class'] = 'form-control'
        self.fields['ap_paterno'].widget.attrs['class'] = 'form-control'
        self.fields['ap_materno'].widget.attrs['class'] = 'form-control'
        self.fields['documento'].widget.attrs['class'] = 'form-control'
        self.fields['celular'].widget.attrs['class'] = 'form-control'
     