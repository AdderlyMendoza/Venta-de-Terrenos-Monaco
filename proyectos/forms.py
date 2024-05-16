from django import forms
from .models import Proyectos ,Sub_Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = '__all__'  

    def __init__(self, *args, **kwargs):
        super(ProyectoForm, self).__init__(*args, **kwargs)

        self.fields['estado'].label = 'Estado'
        self.fields['nombre'].label = 'Nombre del Proyecto'
        self.fields['lugar'].label = 'Ubicación'
        self.fields['direccion'].label = 'Dirección'
        self.fields['google_maps'].label = 'Google Maps'
        self.fields['tipo'].label = 'Tipo'
        self.fields['precio_compra'].label = 'Precio de Compra'
        self.fields['precio_venta'].label = 'Precio de Venta'
        self.fields['observacion'].label = 'Observaciones'
     
        self.fields['estado'].widget.attrs['placeholder'] = 'Estado'
        self.fields['nombre'].widget.attrs['placeholder'] = 'Ingrese el nombre del proyecto'
        self.fields['direccion'].widget.attrs['placeholder'] = 'Ingrese la dirección del proyecto'
        self.fields['precio_compra'].widget.attrs['placeholder'] = 'Ingrese el precio de compra'
        self.fields['precio_venta'].widget.attrs['placeholder'] = 'Ingrese el precio de venta'
        
        self.fields['estado'].widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['direccion'].widget.attrs['class'] = 'form-control'
        self.fields['tipo'].widget.attrs['class'] = 'form-control'
        self.fields['precio_compra'].widget.attrs['class'] = 'form-control'
        self.fields['precio_venta'].widget.attrs['class'] = 'form-control'
        self.fields['observacion'].widget.attrs['class'] = 'form-control'
        
    
    def clean(self):
        cleaned_data = super().clean()
        precio_compra = cleaned_data.get('precio_compra')
        precio_venta = cleaned_data.get('precio_venta')
        
        if precio_compra and precio_venta:
            if precio_venta <= precio_compra:
                raise forms.ValidationError("El precio de venta debe ser mayor que el precio de compra.")
        return cleaned_data
    
    


class SubProyectoForm(forms.ModelForm):
    proyecto = forms.ModelChoiceField(queryset=Proyectos.objects.all(), empty_label="Seleccione un proyecto")
    
    class Meta:
        model = Sub_Proyecto
        fields = ['estado','proyecto','nombre', 'm2', 'precio_venta', 'plano', 'observacion']
        widgets = {
            'plano': forms.FileInput(attrs={'accept': 'application/pdf,image/*'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(SubProyectoForm, self).__init__(*args, **kwargs)
        
        self.fields['estado'].label = 'Estado'
        self.fields['nombre'].label = 'Nombre'
        
        self.fields['m2'].label = 'M2'
        self.fields['precio_venta'].label = 'Precio Venta'
        self.fields['plano'].label = 'Plano'
        self.fields['observacion'].label = 'Observacion'
        
        
        self.fields['estado'].widget.attrs['placeholder'] = 'Estado'
        self.fields['nombre'].widget.attrs['placeholder'] = 'Nombre'
       
        self.fields['m2'].widget.attrs['placeholder'] = 'M2'
        self.fields['precio_venta'].widget.attrs['placeholder'] = 'Precio Venta'
        self.fields['plano'].widget.attrs['placeholder'] = 'Plano'
        self.fields['observacion'].widget.attrs['placeholder'] = 'Observacion'
        
        self.fields['estado'].widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        
        self.fields['m2'].widget.attrs['class'] = 'form-control'
        self.fields['precio_venta'].widget.attrs['class'] = 'form-control'
        self.fields['plano'].widget.attrs['class'] = 'form-control'
        self.fields['observacion'].widget.attrs['class'] = 'form-control'
