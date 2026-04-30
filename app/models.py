from django.db import models
from datetime import date, time

class Task(models.Model):
    Product = models.CharField(max_length=200, )
    
    descripcion = models.TextField()

    ESTADOS = [
        ('Sin previo', 'Sin previo'),
        ('Grabando', 'Para Grabar'),
        ('Entregar', 'Para Entregar'),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='Sin previo'
    )

    nombre = models.CharField(max_length=200)

    fecha = models.DateField(default=date.today)

    hora = models.TimeField(default='12:00')

    numero_telefono = models.CharField(max_length=20,)

    tipografia = models.CharField(max_length=200, )

    total = models.DecimalField(max_digits=10, decimal_places=2, )

    anticipo = models.DecimalField(max_digits=10, decimal_places=2, )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.Product