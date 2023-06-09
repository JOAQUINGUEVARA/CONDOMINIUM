# Generated by Django 3.1.13 on 2023-02-07 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20230207_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='correspondencia',
            name='fechahora_notifica',
        ),
        migrations.AddField(
            model_name='correspondencia',
            name='fechahora_entrega',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Fecha Hora Notifica'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(17, 54, 6, 213426), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(17, 54, 6, 213426), verbose_name='Hora Inicio'),
        ),
    ]
