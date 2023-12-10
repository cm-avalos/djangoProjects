# Generated by Django 4.2.3 on 2023-11-27 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservas', '0010_alter_agenda_horario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examen',
            name='tipo_vehiculo',
        ),
        migrations.AddField(
            model_name='agenda',
            name='tipo_vehiculo',
            field=models.CharField(blank=True, choices=[['0', '8:30-9:00'], ['1', '9:00-9:30'], ['2', '9:30-10:00'], ['3', '10:00-10:30'], ['4', '10:30-11:00'], ['5', '11:00-11:30'], ['6', '11:30-12:00']], max_length=100, null=True),
        ),
    ]
