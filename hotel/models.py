from django.db import models

class Huesped(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    dni= models.CharField(max_length=20 , unique=True)
    email= models.EmailField(max_length=150 , unique=True)
    telefono= models.CharField(max_length=20 , blank=True , null=True)
    fecha_de_nacimiento= models.DateField(null=True)

def __str__(self):
    return f"{self.apellido} , {self.nombre}"


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
    disponible= models.BooleanField(default=True) # Indica si esta libre en ese momento

def __str__(self):
    return f"Habitacion {self.numero} ({self.get_tipo_display()})"


class Reserva(models.Model):

    #Claves Foraneas(FOREIGNKEY)
    #Una reserva pertenece al huesped y la habitacion
    Huesped= models.ForeignKey(Huesped, on_delete=models.CASCADE)
    Habitacion= models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    fecha_entrada= models.DateField()
    fecha_salida=models.DateField()

    ESTADO_CHOICES= [
        ('CONF', 'Confirmada'),
        ('CHIN', 'Check-in'),
        ('CHOU', 'Check-out'),
        ('CANC', 'Cancelada'),
    ]

    estado= models.CharField(max_length=4 ,choices=ESTADO_CHOICES, default='CONF')
    costo_total= models.DecimalField(max_digits=10 , decimal_places=2 , blank=True , null=True)

def __str__(self):
    return f"Reserva {self.id} | H: {self.husped.apellido} | Hab: {self.habitacion}"

def dias_estadia(self):
        #Calcula el numero de las noches reservadas
        if self.fecha_salida and self.fecha_entrada:
            return (self.fecha_salida - self.fecha_entrada).days
        return 0