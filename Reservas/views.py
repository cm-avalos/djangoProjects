from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import  AsignacionesForm,AgendaForm,ExamenForm,ExaminadorForm, CustomUserCreationForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Q
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
           messages.success(request, 'La reserva se ha solicitado exitosamente.')
           return home(request)
    data={'form':agenda_form}
    return render(request,'Reservas/ui1.html',data)
@login_required 
def ui2(request):    
    asignaciones_form=AsignacionesForm()
    if request.method == 'POST':
        asignaciones_form = AsignacionesForm(request.POST)           #funcion donde permite crear un nuevo empleado ygenerar los cambios
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
    examinador_l= Examinador.objects.all()

    busqueda=request.GET.get("buscar")


    if request.method == 'POST':
        examinador_form = ExaminadorForm(request.POST)           #funcion donde permite crear un nuevo empleado ygenerar los cambios
        if examinador_form.is_valid():
            examinador_form.save()   
            return home(request)
    data={'form':examinador_form}
    data2= {'examinador': examinador_l}
    # data = {'form' : form} opcional

    if busqueda:
        examinador_l=Examinador.objects.filter(
            Q(nombre__icontains = busqueda) 
            
        ).distinct()

    
    return render(request,'Reservas/ui4.html',{**data, **data2})

def loginn(request):
    return render(request,'/Reservas/login.html')


def exit(request):
    logout(request)
    return redirect('login')

def listar_reservados(request):

    busqueda=request.GET.get("buscar")

    reservadoss= Asignaciones.objects.all()

    if busqueda:
        reservadoss=Asignaciones.objects.filter(
            Q(Examinador__nombre__icontains = busqueda) |
            Q(Horario__dia__icontains = busqueda) 
        ).distinct()


    data = {'reservados': reservadoss}
    return render(request, 'Reservas/ui5.html', data)



def listar_agenda(request):

    busqueda=request.GET.get("buscar")

    agendas_l= Agenda.objects.all()

    if busqueda:
        agendas_l=Agenda.objects.filter(
            Q(Examinador__nombre__icontains = busqueda) |
            Q(Horario__dia__icontains = busqueda) 
        ).distinct()


    data = {'agendas': agendas_l}
    return render(request, 'Reservas/lista_agenda.html', data)


def listar_examen(request):

    busqueda=request.GET.get("buscar")

    examen_l= Examen.objects.all()

    if busqueda:
        examen_l=Examen.objects.filter(
            Q(Examinador__nombre__icontains = busqueda) |
            Q(Horario__dia__icontains = busqueda) 
        ).distinct()


    data = {'examen': examen_l}
    return render(request, 'Reservas/lista_examen.html', data)


def listar_examinador(request):

    busqueda=request.GET.get("buscar")

    examinador_l= Examinador.objects.all()

    if busqueda:
        examen_l=Examen.objects.filter(
            Q(Examinador__nombre__icontains = busqueda) |
            Q(Horario__dia__icontains = busqueda) 
        ).distinct()


    data = {'examinador': examinador_l}
    return render(request, 'Reservas/lista_examinador.html', data)

def register(request):
    data={'form':CustomUserCreationForm()}
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)

            return redirect('Home')
    return render(request,'registration/register.html',data)


def AsocData(request,id):
    
    asignaciones=get_object_or_404(Asignaciones,pk=id)
    data={'e':asignaciones}
    return render(request,'Reservas/ui6.html',data)

def eliminarAsoc(request, id):
    empleado = Asignaciones.objects.get(id = id)      #funcion donde permite eliminar un nuevo empleado ygenerar los cambios
    empleado.delete()
    return redirect('Ui5',)


def actualizarAsoc(request, id):
    asoc = Asignaciones.objects.get(id = id)
    form = AsignacionesForm(instance=asoc)
    if request.method == 'POST':                            #funcion donde permite eliminar un nuevo empleado ygenerar los cambios
        form = AsignacionesForm(request.POST, instance=asoc)
        if form.is_valid():
            form.save()
        return listar_reservados(request)
    data = {'form' : form}
    return render(request, 'Reservas/ui2.html', data)
