# Generated by Django 4.2.3 on 2023-11-20 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('correos', models.EmailField(max_length=100, verbose_name='Correos Electronico')),
                ('rut', models.CharField(max_length=100, verbose_name='Rut identificador')),
                ('fono', models.CharField(max_length=100, verbose_name='Telefono')),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_examen', models.CharField(max_length=100, verbose_name='Evaluacion')),
                ('examinadorE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservas.examinador', verbose_name='Examinador')),
            ],
        ),
    ]
