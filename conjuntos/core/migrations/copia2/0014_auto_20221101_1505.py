# Generated by Django 3.1.13 on 2022-11-01 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20221031_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proponenteproyecto',
            name='fecha_aprobacion',
        ),
        migrations.AddField(
            model_name='proponenteproyecto',
            name='fecha_seleccion',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Fecha Selección'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(15, 5, 27, 165680), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(15, 5, 27, 165680), verbose_name='Hora Inicio'),
        ),
    ]