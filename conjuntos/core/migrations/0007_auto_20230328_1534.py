# Generated by Django 3.1.13 on 2023-03-28 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230328_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asamblea',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(15, 34, 16, 761808), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='asamblea',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(15, 34, 16, 761808), verbose_name='Hora Inicio'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(15, 34, 16, 755813), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(15, 34, 16, 755813), verbose_name='Hora Inicio'),
        ),
    ]
