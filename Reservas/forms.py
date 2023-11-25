from django import forms 
from .models import *

class ExaminadorForm(forms.ModelForm):
        class Meta:
                model=Examinador
                fields=['nombre','apellido','correos','rut','fono']
    
        
        
class ExamenForm(forms.ModelForm):
        class Meta:
               model=Examen
               fields=['Tipo_examen','examinadorE']


class AgendaForm(forms.ModelForm):
        class Meta:
               model=Agenda
               fields=['dia','horario','examinadorA']
               widgets = {'dia': forms.DateInput(attrs={'type': 'date'}),}

class AsignacionesForm(forms.ModelForm):
        class Meta:
                model=Asignaciones
                fields=['Examinador', 'Horario']
