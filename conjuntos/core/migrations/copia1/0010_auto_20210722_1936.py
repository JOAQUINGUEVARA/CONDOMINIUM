# Generated by Django 3.2.5 on 2021-07-23 00:36

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210719_1953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservazonascomunes',
            options={'ordering': ['hora_inicial'], 'verbose_name': 'Reserva Zona Común', 'verbose_name_plural': 'Reserva Zonas Comunes'},
        ),
        migrations.RemoveField(
            model_name='reservazonascomunes',
            name='fechahora_final',
        ),
        migrations.RemoveField(
            model_name='reservazonascomunes',
            name='fechahora_inicial',
        ),
        migrations.RemoveField(
            model_name='reservazonascomunes',
            name='minutos',
        ),
        migrations.AddField(
            model_name='reservazonascomunes',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Fecha'),
        ),
        migrations.AddField(
            model_name='reservazonascomunes',
            name='hora_final',
            field=models.TimeField(default=datetime.datetime.today, verbose_name='Hora Final'),
        ),
        migrations.AddField(
            model_name='reservazonascomunes',
            name='hora_inicial',
            field=models.TimeField(default=datetime.datetime.today, verbose_name='Hora Inicial'),
        ),
        migrations.AlterField(
            model_name='reservazonascomunes',
            name='horas',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(24)]),
        ),
    ]
