# Generated by Django 3.1.13 on 2023-03-08 23:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20230306_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asamblea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, default=None, null=True, verbose_name='Fecha')),
                ('contenido', models.TextField(blank=True, default='', null=True, verbose_name='Contenido')),
            ],
            options={
                'verbose_name': 'Asamblea',
                'verbose_name_plural': 'Asambleas',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(18, 1, 1, 51627), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(18, 1, 1, 51627), verbose_name='Hora Inicio'),
        ),
    ]
