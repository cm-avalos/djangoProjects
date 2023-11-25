from django.db import models
from datetime import datetime, date 
# Create your models here.

class Examinador(models.Model):
    nombre=models.CharField(max_length=100, verbose_name='Nombre')
    apellido=models.CharField(max_length=100, verbose_name='Apellido')
    correos=models.EmailField(max_length=100, verbose_name='Correos Electronico')    
    rut=models.CharField(max_length=100, verbose_name='Rut identificador')
    fono =models.CharField(max_length=100, verbose_name='Telefono')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Examen(models.Model):
    Tipo_examen=models.CharField(max_length=100, verbose_name='Evaluacion')    
    examinadorE = models.ForeignKey(Examinador, on_delete=models.CASCADE, verbose_name='Examinador')
    
    def __str__(self):
        return f"{self.Tipo_examen}"
    

class Agenda(models.Model):
    opciones=[
        ['0','8:30-9:00'],
        ['1','9:00-9:30'],
        ['2','9:30-10:00'],
        ['3','10:00-10:30'],
        ['4','10:30-11:00'],
        ['5','11:00-11:30'],
        ['6','11:30-12:00'],]

    dia=models.DateField()
    horario=models.CharField(choices=opciones,max_length=100)
    examinadorA = models.ForeignKey(Examinador, on_delete=models.CASCADE, verbose_name='Examinador')
    
    def __str__(self):
        return f"dia: {self.dia} examinador:  {self.examinadorA} horario:{self.horario} "
    
class Asignaciones(models.Model):
    Examinador = models.ForeignKey(Examinador, on_delete=models.CASCADE, verbose_name='Examinador')
    Horario = models.ForeignKey(Agenda, on_delete=models.CASCADE, verbose_name='Horario')
