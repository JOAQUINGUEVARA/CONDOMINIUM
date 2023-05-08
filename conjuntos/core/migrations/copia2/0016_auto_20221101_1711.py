# Generated by Django 3.1.13 on 2022-11-01 22:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20221101_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(17, 11, 7, 581860), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(17, 11, 7, 581860), verbose_name='Hora Inicio'),
        ),
    ]