# Generated by Django 3.2.5 on 2021-07-09 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210709_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingreso_peatonal',
            name='hora_ingreso',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ingreso_peatonal',
            name='hora_salida',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Hora de Salida'),
        ),
    ]
