from django.db import models


class Habitacion (models.Model):

     # Opciones de Tipo de Habitaciones
    TIPO_CHOICES= [
        ('SIM', 'Simple'),
        ('DOB', 'Doble'),
        ('SUI', 'Suite'),
        ('FAM', 'Familiar'),
    ]

    numero= models.CharField(max_length=10 , unique=True)
    tipo= models.CharField(max_length=3, choices=TIPO_CHOICES, default='DOB')
    precio_noche= models.DecimalField(max_digits=8 , decimal_places=2)
    max_huespedes= models.IntegerField(default=2)
    disponible= models.BooleanField(default=True) 
  

def __str__(self):
    return f"Habitacion {self.numero} ({self.get_tipo_display()})"