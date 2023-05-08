# Generated by Django 3.1.13 on 2022-10-31 23:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20221031_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(18, 42, 59, 345640), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(18, 42, 59, 345640), verbose_name='Hora Inicio'),
        ),
    ]