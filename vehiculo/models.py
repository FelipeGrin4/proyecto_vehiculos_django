from django.db import models


# Create your models here.

class Vehiculo(models.Model):
    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]
    
    CATEGORIA_VEHICULO = [
        ('Particular', 'Vehículo Particular'),
        ('Transporte', 'Vehículo de Transporte'),
        ('Carga', 'Vehículo de Carga'),
    ]
    
    marca= models.CharField(max_length=20, blank=False, null=False, choices=MARCAS, default='Ford')
    modelo= models.CharField(max_length=100, blank=False, null=False)
    serial_carroceria= models.CharField(max_length=50, blank=False, null=False)
    serial_motor= models.CharField(max_length=50, blank=False, null=False)
    categoria= models.CharField(max_length=20, blank=False, null=False, choices=CATEGORIA_VEHICULO, default='Particular')
    precio = models.IntegerField(null=False, blank=False)
    fecha_creacion = models.DateField(auto_now_add=True)   #función auspiciada por Hugo
    fecha_modificacion = models.DateField(auto_now=True)   #función auspiciada por Hugo
    
    def filtrar_por_precios(self):
        if self.precio <= 10000:
            return 'Bajo'
        elif 10000 < self.precio <= 30000:
            return 'Medio'
        else:
            return 'Alto'
    
    class Meta:
        permissions = [
            ("visualizar_catalogo", "Puede ver el catálogo de vehículos"),
            ("add_vehiculomodel", "Puede Agregar Nuevos Vehiculos"),
        ]
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"