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
    manzana = forms.ModelChoiceField(queryset=Manzana.objects.all(), empty_label=None, label="Manzana")
    subproyecto = forms.ModelChoiceField(queryset=Sub_Proyecto.objects.all(), empty_label=None, label='Subproyecto')

    class Meta:
        model = Venta
        # fields = [  'cliente', 'proyecto', 'manzana', 'subproyecto',  'fecha_separacion']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Obtener el proyecto y la manzana seleccionados
        proyecto_id = self.data.get('proyecto')
        manzana_id = self.data.get('manzana')

        if proyecto_id and manzana_id:
            # Filtrar los subproyectos que pertenecen al proyecto y a la manzana seleccionados
            self.fields['subproyecto'].queryset = Sub_Proyecto.objects.filter(
                proyecto_id=proyecto_id,
                manzana_id=manzana_id,
                estado="DISPONIBLE"
            )
        else:
            # Si no se seleccionó ningún proyecto o manzana, mostrar todos los subproyectos disponibles
            self.fields['subproyecto'].queryset = Sub_Proyecto.objects.filter(estado="DISPONIBLE")

        

class CuotaForm(forms.ModelForm):
    class Meta:
        model = Cuotas
        fields = '__all__'  
    
