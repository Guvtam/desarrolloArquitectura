from django import forms
from django.forms import DateField, DateInput, ModelForm, NumberInput, Select, TextInput, Textarea
from .models import Servicio, Reserva, Vehiculo, Proveedor, Producto, Boleta

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre','descripcion', 'valor']
        widgets = {
            'nombre' : TextInput(attrs={'class': 'form-control'}),           
            'descripcion' : Textarea(attrs={'class': 'form-control'}),
            'valor' : NumberInput(attrs={'class': 'form-control'})
            
        }



class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['servicio','vehiculo','reserva','hora','descripcion']
        widgets = {
            'servicio' : Select(attrs={'class': 'form-control'}),
            'vehiculo' : Select(attrs={'class': 'form-control'}),
            #'user' : Select(attrs={'class': 'form-control'}),
            'reserva' : forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'}),
            'descripcion' : Textarea(attrs={'class': 'form-control'}),
            
            'hora' : forms.DateInput( attrs={
                'type': 'time',
                'class': 'form-control'}),
            
        }

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre','rubro','direccion','telefono']
        widgets = {
            'nombre' : TextInput(attrs={'class': 'form-control'}),           
            'rubro' : TextInput(attrs={'class': 'form-control'}),
            'direccion' : TextInput(attrs={'class': 'form-control'}), 
            'telefono' : NumberInput(attrs={'class': 'form-control'})
            
        }

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','proveedor','cantidad']
        widgets = {
            'nombre' : TextInput(attrs={'class': 'form-control'}),           
            'descripcion' : Textarea(attrs={'class': 'form-control'}),
            'proveedor' : Select(attrs={'class': 'form-control'}), 
            'cantidad' : NumberInput(attrs={'class': 'form-control'})
            
        }
        

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca','modelo','anno']
        widgets = {
            'marca' : TextInput(attrs={'class': 'form-control'}),           
            'modelo' : TextInput(attrs={'class': 'form-control'}), 
            'anno' : NumberInput(attrs={'class': 'form-control'})
            
        }

class BoletaForm(ModelForm):
    class Meta:
        model = Boleta
        fields = ['fecha','descripcion','total']
        widgets = {
            'fecha' : forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'}),
            'descripcion' : Textarea(attrs={'class': 'form-control'}),
            'total' : NumberInput(attrs={'class': 'form-control'})
            
            
        }

        
