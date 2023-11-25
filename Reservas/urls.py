from django.contrib import admin
from django.urls import path
from Reservas import views



urlpatterns = [
    
    path('',views.home, name='Home'),
    path('ui1/',views.ui1, name='Ui1'),
    path('ui2/',views.ui2, name='Ui2'),
    path('ui3/',views.ui3, name='Ui3'),
    path('ui4/',views.ui4, name='Ui4'),
    path('logout/',views.exit, name='exit')

]
