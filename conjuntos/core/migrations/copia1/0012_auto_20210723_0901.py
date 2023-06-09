# Generated by Django 3.2.5 on 2021-07-23 14:01

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_reservazonascomunes_fecha'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservazonascomunes',
            options={'ordering': ['fecha_hora_inicial'], 'verbose_name': 'Reserva Zona Común', 'verbose_name_plural': 'Reserva Zonas Comunes'},
        ),
        migrations.RemoveField(
            model_name='reservazonascomunes',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='reservazonascomunes',
            name='hora_final',
        ),
        migrations.RemoveField(
            model_name='reservazonascomunes',
            name='hora_inicial',
        ),
        migrations.AddField(
            model_name='reservazonascomunes',
            name='fecha_hora_final',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='Fecha Hora Final'),
        ),
        migrations.AddField(
            model_name='reservazonascomunes',
            name='fecha_hora_inicial',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='Fecha Hora Inicial'),
        ),
        migrations.AlterField(
            model_name='reservazonascomunes',
            name='horas',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(24)], verbose_name='Horas'),
        ),
    ]
