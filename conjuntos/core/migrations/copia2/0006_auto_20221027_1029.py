# Generated by Django 3.1.13 on 2022-10-27 15:29

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20221026_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='correspondencia',
            name='observacion',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Observaciones'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='calificacion',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Calificación'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(10, 29, 30, 463301), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(10, 29, 30, 463301), verbose_name='Hora Inicio'),
        ),
        migrations.CreateModel(
            name='Proponente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_nit', models.CharField(default='', max_length=20, verbose_name='Identificaciòn')),
                ('nombre', models.CharField(default='', max_length=50, verbose_name='Nombre/Razón Social')),
                ('telefono', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Teléfono')),
                ('celular', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Celular')),
                ('direccion', models.CharField(blank=True, default='', max_length=80, null=True, verbose_name='Dirección')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('persona_contacto', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Persona Contacto')),
                ('telefono_contacto', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Teléfono Contacto')),
                ('celular_contacto', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Celular Contacto')),
                ('email_contacto', models.EmailField(blank=True, default='', max_length=200, null=True, verbose_name='Email Contacto')),
                ('calificacion', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Calificación')),
                ('servicio_provee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.servicioproveedor', verbose_name='Servicio Proveedor')),
                ('tipo_identificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoidentificacion', verbose_name='Tipo de Identificación')),
            ],
            options={
                'verbose_name': 'Proponentes',
                'verbose_name_plural': 'Proponentes',
                'ordering': ['nombre'],
            },
        ),
    ]
