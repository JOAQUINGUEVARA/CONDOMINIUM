# Generated by Django 3.1.13 on 2022-12-15 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20221212_1827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reparacion',
            options={'ordering': ['id'], 'verbose_name': 'Reparacion', 'verbose_name_plural': 'Reparaciones'},
        ),
        migrations.AddField(
            model_name='obra',
            name='valor_pagado',
            field=models.FloatField(default=0, verbose_name='Valor Pagado'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(11, 31, 15, 248242), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(11, 31, 15, 248242), verbose_name='Hora Inicio'),
        ),
    ]