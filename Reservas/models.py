from django.db import models
from datetime import datetime, date 
# Create your models here.
from django.core.exceptions import ValidationError

class Examinador(models.Model):
     nombre=models.CharField(max_length=100, verbose_name='Nombre')
     apellido=models.CharField(max_length=100, verbose_name='Apellido')
     correos=models.EmailField(max_length=100, verbose_name='Correos Electronico')    
     rut=models.CharField(max_length=100, verbose_name='Rut identificador')
     fono =models.CharField(max_length=100, verbose_name='Telefono')
    

     def __str__(self):
         return f"{self.nombre} {self.apellido}"

class Examen(models.Model):
    opciones1=[
            ['0','auto'],
            ['1','motocicleta'],
            ['2','camion '],
            ['3','maquinaria pesada '],
            ['4','transporte escolar '],
            ['5','otro '],
        ]
    Tipo_examen=models.CharField(max_length=100, verbose_name='Evaluacion')    
    #examinadorE = models.ForeignKey(Examinador, on_delete=models.CASCADE, verbose_name='Examinador' ,default=1
    descripcion_examen=models.CharField(max_length=300, verbose_name='Describe Algo Del Examen',null=True,blank=True)
    tipo_vehiculo=models.CharField(choices=opciones1,max_length=100,null=True,blank=True)
    def __str__(self):
        return f"{self.Tipo_examen}"
    


def validar_dia(value):
     today = date.today()
     weekday = date.fromisoformat(f'{value}').weekday()

     if value < today:
         raise ValidationError('Esa fecha ya no esta disponible..')
     if (weekday == 5) or (weekday == 6):
         raise ValidationError('Elija un día de la semana.')

class Agenda(models.Model):
     opciones=[
         ['0','8:30-9:00'],
         ['1','9:00-9:30'],
         ['2','9:30-10:00'],
         ['3','10:00-10:30'],
         ['4','10:30-11:00'],
         ['5','11:00-11:30'],
         ['6','11:30-12:00'],]
     
     

     dia=models.DateField( validators=[validar_dia])
     horario=models.CharField(choices=opciones,max_length=100)
    #  examinadorA = models.ForeignKey(Examinador, on_delete=models.CASCADE, verbose_name='Examinador' ,default=1)
     rut=models.CharField(max_length=100,null=False,blank=False)
     tipo_evaluacion = models.ForeignKey(Examen, on_delete= models.CASCADE, verbose_name='Tipo de reserva',null=True,blank=True)
     
    
     def __str__(self):
         return f"Reserva el dia: {self.dia} | Bloque: {self.horario} | EVALUADO: {self.rut}"
    
class Asignaciones(models.Model):
        Examinador = models.ForeignKey(Examinador, on_delete=models.CASCADE, verbose_name='Examinador')
        Horario = models.ForeignKey(Agenda, on_delete=models.CASCADE, verbose_name='Horario')


        def __str__(self):
         return f"EXAMINADOR: {self.Examinador} | HORARIO: {self.Horario} "