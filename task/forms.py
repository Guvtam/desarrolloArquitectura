from django.forms import ModelForm
from .models import Servicio, Reserva, Vehiculo

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre','descripcion']



class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['servicio','vehiculo','reserva','hora']
        

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca','modelo','anno']
