from django.utils import timezone
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import ServicioForm , ReservaForm, VehiculoForm, ProductoForm, ProveedorForm , BoletaForm
from . models import Servicio, Reserva, Vehiculo , Proveedor, Producto, Boleta
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')

@login_required
def proveedor(request):
    return render(request,'proveedor.html')

@login_required
def crearProveedor(request):
    if request.method == 'GET':
        return render(request,'crearProveedor.html',{
            'form' : ProveedorForm
            
        })
    else:
        try:
            form = ProveedorForm(request.POST)
            new_proveedor= form.save(commit=False)
            new_proveedor.save()
            return render(request,'proveedor.html')
        except:
            return render(request,'crearProveedor.html',{
            'form' : ProveedorForm,
            'error': 'Ingresa un valor válido'
        })

@login_required
def crearProducto(request):
    if request.method == 'GET':
        return render(request,'crearProducto.html',{
            'form' : ProductoForm
            
        })
    else:
        try:
            form = ProductoForm(request.POST)
            new_producto= form.save(commit=False)
            new_producto.save()
            return redirect('listProductos')
        except:
            return render(request,'crearProducto.html',{
            'form' : ProductoForm,
            'error': 'Ingresa un valor válido'
        })

@login_required
def crearBoleta(request):
    if request.method == 'GET':
        return render(request,'crearBoleta.html',{
            'form' : BoletaForm
            
        })
    else:
        try:
            form = BoletaForm(request.POST)
            new_boleta= form.save(commit=False)
            new_boleta.save()
            return render(request,'boletas.html')
        except:
            return render(request,'crearBoleta.html',{
            'form' : BoletaForm,
            'error': 'Ingresa un valor válido'
        })
    

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
def crearReservar(request):
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

@login_required    
def cerrarSesion(request):
    logout(request)
    return render(request,'home.html')


@login_required
def crearServicio(request):
    if request.method == 'GET':
        return render(request,'crearServicio.html',{
            'form': ServicioForm
        })
    else:
        try:
            form = ServicioForm(request.POST)
            new_servicio= form.save(commit=False)
            new_servicio.save()
            return render(request,'servicios.html')
        except:
            return render(request,'crearServicio.html',{
            'form' : ServicioForm,
            'error': 'Ingresa un valor válido'
        })

@login_required
def listReservas(request):
    reservas = Reserva.objects.all()#Reserva.objects.filter(user=request.user)
    return render(request, 'reservas.html',{
        'reservas': reservas
    })

@login_required
def listProductos(request):
    productos = Producto.objects.all()#Reserva.objects.filter(user=request.user)
    return render(request, 'productos.html',{
        'productos': productos
    })

@login_required
def listProveedores(request):
    proveedor = Proveedor.objects.all()#Reserva.objects.filter(user=request.user)
    return render(request, 'proveedor.html',{
        'proveedor': proveedor
    })

@login_required
def listBoletas(request):
    boleta = Boleta.objects.all()#Reserva.objects.filter(user=request.user)
    return render(request, 'boletas.html',{
        'boleta': boleta
    })

@login_required
def listServicios(request):
    servicio = Servicio.objects.all()#Reserva.objects.filter(user=request.user)
    return render(request, 'servicios.html',{
        'servicio': servicio
    })
    
@login_required
def listVehiculo(request):
    vehiculo = Vehiculo.objects.all()#Reserva.objects.filter(user=request.user)
    return render(request, 'vehiculos.html',{
        'vehiculo': vehiculo
    })


@login_required
def crearVehiculo(request):
    if request.method == 'GET':
        return render(request,'crearVehiculo.html',{
            'form' : VehiculoForm
        })
    else:
        try:
            form = VehiculoForm(request.POST)
            new_vehiculo= form.save(commit=False)
            new_vehiculo.user = request.user
            new_vehiculo.save()
            return render(request,'vehiculos.html')
        except:
            return render(request,'crearVehiculo.html',{
            'form' : VehiculoForm,
            'error': 'Ingresa un valor válido'
        })


@login_required
def detalleReserva(request, id):
    if request.method == 'GET':
        reserva = get_object_or_404(Reserva, pk=id)
        form = ReservaForm(instance=reserva)
        return render(request,'detalleReserva.html',{
            'reserva' : reserva, 'form': form
        })
    else:
        try:
            reserva = get_object_or_404(Reserva, pk=id)
            form = ReservaForm(request.POST, instance=reserva)
            form.save()
            return redirect('reservas')
        except ValueError:
            return render(request,'detalleReserva.html',{
            'reserva' : reserva, 
            'form': form,
            'error' : "Error al actualizar reserva"
        })



@login_required
def detalleBoleta(request, id):
    if request.method == 'GET':
        boleta = get_object_or_404(Boleta, pk=id)
        form = BoletaForm(instance=boleta)
        return render(request,'detalleBoleta.html',{
            'boleta' : boleta, 'form': form
        })
    else:
        try:
            boleta = get_object_or_404(Boleta, pk=id)
            form = BoletaForm(request.POST, instance=boleta)
            form.save()
            return redirect('listBoletas')
        except ValueError:
            return render(request,'boletas.html',{
            'boleta' : boleta, 
            'form': form,
            'error' : "Error al actualizar boleta"
        })


@login_required
def detalleProveedor(request, id):
    if request.method == 'GET':
        proveedor = get_object_or_404(Proveedor, pk=id)
        form = ProveedorForm(instance=proveedor)
        return render(request,'detalleProveedor.html',{
            'proveedor' : proveedor, 'form': form
        })
    else:
        try:
            proveedor = get_object_or_404(Proveedor, pk=id)
            form = ProveedorForm(request.POST, instance=proveedor)
            form.save()
            return redirect('listProveedor')
        except ValueError:
            return render(request,'proveedor.html',{
            'proveedor' : proveedor, 
            'form': form,
            'error' : "Error al actualizar proveedor"
        })


@login_required
def detalleServicio(request, id):
    if request.method == 'GET':
        servicio = get_object_or_404(Servicio, pk=id)
        form = ServicioForm(instance=servicio)
        return render(request,'detalleServicio.html',{
            'servicio' : servicio, 'form': form
        })
    else:
        try:
            servicio = get_object_or_404(Proveedor, pk=id)
            form = ServicioForm(request.POST, instance=servicio)
            form.save()
            return redirect('listServicios')
        except ValueError:
            return render(request,'servicios.html',{
            'servicio' : servicio, 
            'form': form,
            'error' : "Error al actualizar servicio"
        })


@login_required
def reservaCompletada(request, id):
    reserva = get_object_or_404(Reserva, pk= id)
    if request.method == 'POST':
        reserva.atendido = timezone.now()
        reserva.save()
        return redirect('reservas')

@login_required
def eliminarProveedor(request, id):
    proveedor = get_object_or_404(Proveedor, pk= id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('listproveedores')

@login_required
def eliminarServicio(request, id):
    servicio = get_object_or_404(Servicio, pk= id)
    if request.method == 'POST':
        servicio.delete()
        return redirect('listServicios')


@login_required
def reservasRealizadas(request):
    reservas = Reserva.objects.filter(atendido__isnull=False)
    return render(request, 'reservas.html',{
        'reservas' : reservas
    })

@login_required
def reservasPorRealizar(request):
    reservas = Reserva.objects.filter(atendido__isnull=True)
    return render(request, 'reservas.html',{
        'reservas' : reservas
    })

