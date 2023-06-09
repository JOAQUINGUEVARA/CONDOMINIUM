# Generated by Django 3.1.13 on 2023-04-25 15:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20230331_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='residente',
            name='envio_email',
            field=models.BooleanField(default=False, verbose_name='Envío Mail'),
        ),
        migrations.AlterField(
            model_name='asamblea',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(10, 41, 34, 743035), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='asamblea',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(10, 41, 34, 743035), verbose_name='Hora Inicio'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(10, 41, 34, 736034), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(10, 41, 34, 736034), verbose_name='Hora Inicio'),
        ),
    ]
