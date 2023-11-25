from django.contrib import admin
from .models import *

# Register your models here.

# admin.py

from .models import Examinador, Examen


admin.site.register(Examen)
admin.site.register(Asignaciones)
admin.site.register(Agenda)



class ExaminadorAdmin(admin.ModelAdmin):
    # Lista de campos a mostrar en la vista de lista
    list_display = ('nombre','apellido','correos','rut','fono')

    # Agregar la opción de eliminar
    actions = ['eliminar_registros']

    def eliminar_registros(self, request, queryset):
        # Lógica para eliminar los registros seleccionados
        queryset.delete()
    eliminar_registros.short_description = "Eliminar registros seleccionados"

admin.site.register(Examinador, ExaminadorAdmin)

