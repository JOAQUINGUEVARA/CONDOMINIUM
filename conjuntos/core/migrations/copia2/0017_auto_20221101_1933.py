# Generated by Django 3.1.13 on 2022-11-02 00:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20221101_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(19, 33, 21, 112116), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(19, 33, 21, 112116), verbose_name='Hora Inicio'),
        ),
    ]
