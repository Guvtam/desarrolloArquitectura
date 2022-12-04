from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    anno = models.IntegerField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.marca 



class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True)
    valor = models.IntegerField(blank=True,editable=True)

    def __str__(self):
        return self.nombre 

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    reserva = models.DateField(auto_now_add=False, auto_now=False)
    hora = models.TimeField(null=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.descripcion
    
    
     
    
