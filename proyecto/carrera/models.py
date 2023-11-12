# models.py
from django.db import models

# Definir el modelo de registro
class Registro(models.Model):
    # Definir los campos del modelo
    numero_identificacion = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.PositiveSmallIntegerField()
    correo_electronico = models.EmailField()
    genero = models.CharField(max_length=10, choices=[('MASCULINO', 'Masculino'), ('FEMENINO', 'Femenino')])
    distancia = models.CharField(max_length=10, choices=[('5K', '5K'), ('10K', '10K')])
    categoria = models.CharField(max_length=10, choices=[('ELITE', 'Elite'), ('RECREATIVO', 'Recreativo')])

    # Definir la representación del modelo
    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
    

    class Meta:
        app_label = 'carrera'
