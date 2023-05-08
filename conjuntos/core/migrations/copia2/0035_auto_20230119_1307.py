# Generated by Django 3.1.13 on 2023-01-19 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20230119_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamoactivofijo',
            name='dias',
            field=models.TimeField(default=0, verbose_name='Dias'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(13, 7, 33, 234487), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(13, 7, 33, 234487), verbose_name='Hora Inicio'),
        ),
    ]