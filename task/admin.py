from django.contrib import admin
from .models import Servicio, Reserva, Vehiculo, Producto, Proveedor, Boleta



# Register your models here.
admin.site.register(Servicio)
admin.site.register(Reserva)
admin.site.register(Vehiculo)
admin.site.register(Boleta)
admin.site.register(Proveedor)
admin.site.register(Producto)

