# Generated by Django 4.2.3 on 2023-11-26 22:41

import Reservas.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reservas', '0004_alter_agenda_horario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='examinadorA',
        ),
        migrations.RemoveField(
            model_name='examen',
            name='examinadorE',
        ),
        migrations.AddField(
            model_name='agenda',
            name='Tipo_reserva',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Reservas.examen', verbose_name='Examen'),
        ),
        migrations.AddField(
            model_name='examen',
            name='examinador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Reservas.examinador', verbose_name='examinador'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='dia',
            field=models.DateField(validators=[Reservas.models.validar_dia]),
        ),
    ]
