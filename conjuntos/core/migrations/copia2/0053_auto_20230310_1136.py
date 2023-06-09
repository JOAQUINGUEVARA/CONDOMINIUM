# Generated by Django 3.1.13 on 2023-03-10 16:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_auto_20230309_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAsamblea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo Asamblea',
                'verbose_name_plural': 'Tipos Asamblea',
                'ordering': ['descripcion'],
            },
        ),
        migrations.AlterField(
            model_name='asamblea',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(11, 35, 49, 740285), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='asamblea',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(11, 35, 49, 740285), verbose_name='Hora Inicio'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_final',
            field=models.TimeField(blank=True, default=datetime.time(11, 35, 49, 732286), verbose_name='Hora Final'),
        ),
        migrations.AlterField(
            model_name='reunionconsejo',
            name='hora_inicio',
            field=models.TimeField(blank=True, default=datetime.time(11, 35, 49, 732286), verbose_name='Hora Inicio'),
        ),
        migrations.AddField(
            model_name='asamblea',
            name='tipo_asamblea',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tipo_asamblea', to='core.tipoasamblea'),
            preserve_default=False,
        ),
    ]
