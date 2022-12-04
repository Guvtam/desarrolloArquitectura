from django import forms
from django.forms import DateField, DateInput, ModelForm, NumberInput, Select, Textarea
from .models import Servicio, Reserva, Vehiculo

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre','descripcion']



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
                'class': 'form-control'})
        }
        

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca','modelo','anno']
        
