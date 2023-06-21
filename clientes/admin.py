from django.contrib import admin

# Register your models here.

from .models import Clientes, Carro

admin.site.register(Clientes)
admin.site.register(Carro)