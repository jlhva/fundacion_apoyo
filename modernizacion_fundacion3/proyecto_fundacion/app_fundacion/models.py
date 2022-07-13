from django.db import models
from unittest.util import _MAX_LENGTH
# Create your models here.
nacionalidad_choice=(
    (1,'Chileno'),
    (2,'Venenzolano'),
    (3,'Haitiano'),
    (4,'Colombiano'),
    (5,'Otros'),
)

estado_choice=(
    (1,'Viudo/a'),
    (2,'Casado/a'),
    (3,'Soltero/a'),
    (4,'Divorciado/a'),
)
nacionalidad_aportador_choice=(
    (1,'Chileno'),
    (2,'Venenzolano'),
    (3,'Haitiano'),
    (4,'Colombiano'),
    (5,'Otros'),
)
class Paciente(models.Model):
    nombre_completo=models.CharField(max_length=30)
    rut=models.CharField(max_length=30)
    correo=models.CharField(max_length=30)
    hijos=models.CharField(max_length=30)
    nacionalidad=models.IntegerField(choices=nacionalidad_choice)
    cuidados_especiales=models.CharField(max_length=30)
    telefono=models.CharField(max_length=30)
    estado_civil=models.IntegerField(choices=estado_choice)

class Insumos(models.Model):
    medicamento=models.CharField(max_length=30)
    laboratorio=models.CharField(max_length=50)
    stock=models.CharField(max_length=4)
class Aportadores(models.Model):
    nombreAportador=models.CharField(max_length=50)
    rutAportador=models.CharField(max_length=12)
    correoAportador=models.CharField(max_length=320)
    peticion=models.CharField(max_length=150)
    pais=models.IntegerField(choices=nacionalidad_aportador_choice)
    monto=models.CharField(max_length=20)

