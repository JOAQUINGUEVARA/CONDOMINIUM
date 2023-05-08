# Generated by Django 3.1.13 on 2022-10-25 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20221025_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(16, 8, 14, 917751), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(16, 8, 14, 916755), verbose_name='Hora Inicio'),
        ),
    ]