# Generated by Django 3.1.13 on 2023-04-28 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20230425_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='residente',
            name='envio_token',
            field=models.BooleanField(default=False, verbose_name='Envío Token'),
        ),
        migrations.AlterField(
            model_name='asamblea',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(12, 8, 32, 672650), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='asamblea',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(12, 8, 32, 672650), verbose_name='Hora Inicio'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(12, 8, 32, 664650), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(12, 8, 32, 664650), verbose_name='Hora Inicio'),
        ),
    ]