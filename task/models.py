from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    rubro = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    telefono = models.IntegerField(blank=False)

    def __str__(self):
        return self.nombre 

class Producto(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    cantidad = models.IntegerField(blank=False)

    def __str__(self):
        return self.nombre 

class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    anno = models.IntegerField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.marca + ' - ' + self.modelo



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
    atendido = models.DateTimeField(null=True)

    def __str__(self):
        return self.descripcion 
    

class Boleta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=False, auto_now=False)
    descripcion = models.TextField(blank=True)
    total = models.IntegerField(blank=True,editable=True)
    fechaRealizado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion