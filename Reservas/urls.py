from django.contrib import admin
from django.urls import path
from Reservas import views



urlpatterns = [
    path('',views.home, name='Home1'),
    path('home/',views.home, name='Home'),
    path('ui1/',views.ui1, name='Ui1'),
    path('ui2/',views.ui2, name='Ui2'),
    path('ui3/',views.ui3, name='Ui3'),
    path('ui4/',views.ui4, name='Ui4'),
    path('ui5/',views.listar_reservados, name='Ui5'),
    path('listas_agendas/',views.listar_agenda, name='Agenda_u'),
    path('listas_Examen/',views.listar_examen, name='Examen_u'),
    path('listas_Examinador/',views.listar_examinador, name='Examinador_u'),
    path('logout/',views.exit, name='exit'),
    path('register/',views.register, name='register'),
    path('verasociacion/<int:id>', views.AsocData,name='ver_asociacion'),
    path('eliminarAsoc/<int:id>', views.eliminarAsoc, name='eliminar_asoc'),
    path('actualizarAsoc/<int:id>', views.actualizarAsoc, name='actualizar_asoc'),

]
