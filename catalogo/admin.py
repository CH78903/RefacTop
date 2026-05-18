from django.contrib import admin
from .models import Auto, Marca, Vendedor, Sucursal, Cliente, Venta

admin.site.register(Auto)
admin.site.register(Marca)
admin.site.register(Vendedor)
admin.site.register(Sucursal)
admin.site.register(Cliente)
admin.site.register(Venta)