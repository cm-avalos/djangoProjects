from django import forms 
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import User

class ExaminadorForm(forms.ModelForm):
        class Meta:
                model=Examinador
                fields=['nombre','apellido','correos','rut','fono']
    
        
        
class ExamenForm(forms.ModelForm):
        class Meta:
               model=Examen
               fields=['Tipo_examen','descripcion_examen','tipo_vehiculo']


class AgendaForm(forms.ModelForm):

       
        class Meta:
               model=Agenda
               fields=['dia','horario','tipo_evaluacion','rut']
               widgets = {'dia': forms.DateInput(attrs={'type': 'date'}),}

class AsignacionesForm(forms.ModelForm):
        class Meta:
                model=Asignaciones
                fields=['Examinador', 'Horario']


class CustomUserCreationForm(UserCreationForm):
       
         class Meta:
                 model= User
                 fields = ['username','first_name','last_name','email','password1','password2']


