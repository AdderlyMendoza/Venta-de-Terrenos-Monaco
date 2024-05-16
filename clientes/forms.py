from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)

        self.fields['nombres'].label = 'Nombres'
        self.fields['ap_paterno'].label = 'Apellido Paterno'
        self.fields['ap_materno'].label = 'Apellido Materno'
        self.fields['direccion'].label = 'Dirección'
        self.fields['documento'].label = 'Documento'
        self.fields['celular'].label = 'Celular'
       
       
       
        self.fields['nombres'].widget.attrs['placeholder'] = 'Nombres'
        self.fields['ap_paterno'].widget.attrs['placeholder'] = 'Apellido Paterno'
        self.fields['ap_materno'].widget.attrs['placeholder'] = 'Apellido Materno'
        self.fields['direccion'].widget.attrs['placeholder'] = 'Dirección'
        self.fields['documento'].widget.attrs['placeholder'] = 'Documento'
        self.fields['celular'].widget.attrs['placeholder'] = 'Celular'


        self.fields['nombres'].widget.attrs['class'] = 'form-control'
        self.fields['ap_paterno'].widget.attrs['class'] = 'form-control'
        self.fields['ap_materno'].widget.attrs['class'] = 'form-control'
        self.fields['direccion'].widget.attrs['class'] = 'form-control'
        self.fields['documento'].widget.attrs['class'] = 'form-control'
        self.fields['celular'].widget.attrs['class'] = 'form-control'
     



class VentaForm(forms.ModelForm):
    proyecto = forms.ModelChoiceField(queryset=Proyectos.objects.all(), empty_label=None, label='Proyecto')
    subproyecto = forms.ModelChoiceField(queryset=Sub_Proyecto.objects.none(), empty_label=None, label='Subproyecto')

    class Meta:
        model = Venta
        fields = ['cliente', 'proyecto', 'subproyecto', 'adelanto' ]
        widgets = {
            'precio_venta': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs and kwargs['instance'] is not None:
            self.fields['precio_venta'].initial = kwargs['instance'].subproyecto.precio_venta

        if 'proyecto' in self.data:
            proyecto_id = int(self.data.get('proyecto'))
            self.fields['subproyecto'].queryset = Sub_Proyecto.objects.filter(proyecto_id=proyecto_id)
        elif self.instance.pk:
            self.fields['subproyecto'].queryset = self.instance.proyecto.subproyecto_set

        

class CuotaForm(forms.ModelForm):
    class Meta:
        model = Cuotas
        fields = '__all__'  
    
