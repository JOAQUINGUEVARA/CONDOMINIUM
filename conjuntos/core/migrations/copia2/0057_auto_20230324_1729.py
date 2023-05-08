# Generated by Django 3.1.13 on 2023-03-24 22:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_auto_20230324_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asamblea',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(17, 29, 12, 201713), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='asamblea',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(17, 29, 12, 200714), verbose_name='Hora Inicio'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(17, 29, 12, 194712), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(17, 29, 12, 194712), verbose_name='Hora Inicio'),
        ),
    ]