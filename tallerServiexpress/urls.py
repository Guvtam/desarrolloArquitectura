"""tallerServiexpress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('registrarse/',views.registrarse,name='registrarse'),
    path('reservar/crear/',views.crearReservar,name='crearReserva'),
    path('iniciarSesion/',views.iniciarSesion,name='iniciarSesion'),
    path('logout/', views.cerrarSesion,name='cerrarSesion'),
    path('servicio/crear/', views.crearServicio,name='crearServicio'),
    path('servicios/', views.listServicios,name='listServicios'),
    path('servicios/<int:id>/', views.detalleServicio,name='detalleServicio'),
    path('servicios/<int:id>/eliminar/', views.eliminarServicio,name='eliminarServicio'),
    path('reservas/', views.listReservas,name='reservas'),
    path('reservas_realizadas/', views.reservasRealizadas,name='reservasRealizadas'),
    path('reservas_porRealizar/', views.reservasPorRealizar,name='reservasPorRealizar'),
    path('reservas/<int:id>/', views.detalleReserva,name='detalleReserva'),
    path('reservas/<int:id>/atendido/', views.reservaCompletada,name='reservaCompletada'),
    path('vehiculo/crear/', views.crearVehiculo,name='crearVehiculo'),
    path('vehiculos/', views.listVehiculo,name='listVehiculo'),
    path('proveedor/crear/', views.crearProveedor,name='crearProveedor'),
    path('proveedor/', views.listProveedores,name='listProveedor'),
    path('proveedor/<int:id>/', views.detalleProveedor,name='detalleProveedor'),
    path('proveedor/<int:id>/eliminar/', views.eliminarProveedor,name='eliminarProveedor'),
    path('boleta/crear/', views.crearBoleta,name='crearBoleta'),
    path('boletas/<int:id>/', views.detalleBoleta,name='detalleBoleta'),
    path('boletas/', views.listBoletas,name='listBoletas'),
    path('producto/crear/', views.crearProducto,name='crearProducto'),
    path('productos/', views.listProductos,name='listProductos'),
    path('contacto/', views.contacto,name='contacto'),
    
    
]
