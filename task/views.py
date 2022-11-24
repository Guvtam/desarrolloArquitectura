from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import ServicioForm , ReservaForm, VehiculoForm
from . models import Servicio, Reserva, Vehiculo
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')

def contacto(request):
    return render(request,'contacto.html')

def registrarse(request):

    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # registrar usuario
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return render(request,'contacto.html')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'La contraseña no coincide'
        })

@login_required
def reservar(request):
    if request.method == 'GET':
        return render(request,'reservar.html',{
            'form' : ReservaForm
            
        })
    else:
        try:
            form = ReservaForm(request.POST)
            new_reserva= form.save(commit=False)
            new_reserva.user = request.user
            new_reserva.save()
            return render(request,'contacto.html')
        except:
            return render(request,'reservar.html',{
            'form' : ReservaForm,
            'error': 'Ingresa un valor válido'
        })


def iniciarSesion(request):
    if request.method == 'GET':
        return render(request,'login.html',{
            'form' : AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'login.html',{
                'form' : AuthenticationForm,
                'error' : 'Usuario o Constraseña Incorrectos'
            })
        else:
            login(request, user)
            return render(request,'contacto.html')

@login_required    
def cerrarSesion(request):
    logout(request)
    return render(request,'home.html')


@login_required
def crearServicio(request):
    if request.method == 'GET':
        return render(request,'crear_servicio.html',{
            'form': ServicioForm
        })
    else:
        try:
            form = ServicioForm(request.POST)
            new_servicio= form.save(commit=False)
            new_servicio.save()
            return render(request,'home.html')
        except:
            return render(request,'crear_servicio.html',{
            'form' : ServicioForm,
            'error': 'Ingresa un valor válido'
        })

@login_required
def listReservas(request):
    reservas = Reserva.objects.all()#Reserva.objects.filter(user=request.user)
    return render(request, 'list_reservas.html',{
        'reservas': reservas
    })

@login_required
def vehiculo(request):
    if request.method == 'GET':
        return render(request,'vehiculo.html',{
            'form' : VehiculoForm
        })
    else:
        try:
            form = VehiculoForm(request.POST)
            new_vehiculo= form.save(commit=False)
            new_vehiculo.user = request.user
            new_vehiculo.save()
            return render(request,'reservar.html')
        except:
            return render(request,'vehiculo.html',{
            'form' : VehiculoForm,
            'error': 'Ingresa un valor válido'
        })
