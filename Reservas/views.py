from django.shortcuts import render,HttpResponse,redirect
from .forms import  AsignacionesForm,AgendaForm,ExamenForm,ExaminadorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

@login_required
def home(request):
    return render(request,'Reservas/home.html')
@login_required 
def ui1(request):
    agenda_form=AgendaForm()
    if request.method == 'POST':
       agenda_form = AgendaForm(request.POST)           #funcion donde permite crear un nuevo empleado ygenerar los cambios
       if agenda_form.is_valid():
           agenda_form.save()   
           return home(request)
    data={'form':agenda_form}
    return render(request,'Reservas/ui1.html',data)
@login_required 
def ui2(request):    
    asignaciones_form=AsignacionesForm()
    if request.method == 'POST':
        asignacion_form = AsignacionesForm(request.POST)           #funcion donde permite crear un nuevo empleado ygenerar los cambios
        if asignaciones_form.is_valid():
            asignaciones_form.save()   
            return home(request)
    data={'form':asignaciones_form}
    
    return render(request,'Reservas/ui2.html',data)
@login_required 
def ui3(request):
    examen_form= ExamenForm()

    if request.method == 'POST':
       examen_form = ExamenForm(request.POST)           #funcion donde permite crear un nuevo empleado ygenerar los cambios
       if examen_form.is_valid():
           examen_form.save()   
           return home(request)
    data={'form':examen_form}
    
    return render(request,'Reservas/ui3.html',data)
@login_required 
def ui4(request):    
    examinador_form=ExaminadorForm()

    if request.method == 'POST':
        examinador_form = ExaminadorForm(request.POST)           #funcion donde permite crear un nuevo empleado ygenerar los cambios
        if examinador_form.is_valid():
            examinador_form.save()   
            return home(request)
    data={'form':examinador_form}
    # data = {'form' : form} opcional

    
    return render(request,'Reservas/ui4.html',data)

def login(request):
    return render(request,'/Reservas/login.html')


def exit(request):
    logout(request)
    return redirect('login')
    

