from django import forms 
from .models import Web

    
class formularioWeb( forms.ModelForm ):
    class Meta:
        model = Web
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(formularioWeb, self).__init__(*args, **kwargs)
        
        self.fields['dni'].label = "DNI"
        self.fields['nombres'].label = "NOMBRES"
        self.fields['apellidos'].label = "APELLIDOS"
        self.fields['telefono'].label = "TELEFONO"
        self.fields['email'].label = "EMAIL"
        self.fields['direccion'].label = "DIRECCION"
        self.fields['terrenos'].label = "TERRENOS"

        self.fields['dni'].widget.attrs['class'] = "form-control"
        self.fields['nombres'].widget.attrs['class'] = "form-control"
        self.fields['apellidos'].widget.attrs['class'] = "form-control"
        self.fields['telefono'].widget.attrs['class'] = "form-control"
        self.fields['email'].widget.attrs['class'] = "form-control"
        self.fields['direccion'].widget.attrs['class'] = "form-control"
        self.fields['terrenos'].widget.attrs['class'] = "form-control"
