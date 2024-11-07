from django.contrib import admin
from .models import Vehiculo
# Register your models here.

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    search_fields= ['marca', 'modelo', 'precio', 'categoria', 'fecha_creacion', 'fecha_modificacion']
    list_display= ['marca', 'modelo', 'precio', 'categoria', 'fecha_creacion', 'fecha_modificacion']