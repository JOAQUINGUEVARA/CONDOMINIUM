# Generated by Django 3.1.13 on 2023-05-03 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20230503_1229'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecomendacionAuditor',
            new_name='RecomendacionRevisor',
        ),
        migrations.AlterField(
            model_name='asamblea',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(12, 45, 27, 780848), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='asamblea',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(12, 45, 27, 780848), verbose_name='Hora Inicio'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(12, 45, 27, 775847), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(12, 45, 27, 775847), verbose_name='Hora Inicio'),
        ),
    ]
