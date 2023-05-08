# Generated by Django 3.2.5 on 2021-07-16 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_parametros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='clase_correspondencia',
            field=models.CharField(choices=[('Sobre', 'Sobre'), ('Paquete', 'Paquete'), ('', 'No Determinado')], default='', max_length=10, verbose_name='Clase de Correspondencia'),
        ),
        migrations.AlterField(
            model_name='correspondencia',
            name='tipo_correspondencia',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Urgente', 'Urgente'), ('', 'No Determinado')], default='', max_length=10, verbose_name='Tipo de Correspondencia'),
        ),
        migrations.AlterField(
            model_name='ingresopeatonal',
            name='identificacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.visitante', verbose_name='Identificación'),
        ),
        migrations.AlterField(
            model_name='ingresovehiculo',
            name='tipo_ingreso',
            field=models.CharField(choices=[('Visitante', 'Visitante'), ('Residente', 'Residente'), ('', 'No Determinado')], max_length=10, verbose_name='Visitante/Residente'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='tipo_mascota',
            field=models.CharField(choices=[('Perro', 'Perro'), ('Gato', 'Gato'), ('Otro', 'Otro'), ('', 'No Determinado')], max_length=10, verbose_name='Tipo de Mascota'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='vacuna',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No'), ('', 'No Determinado')], max_length=5, verbose_name='Vacuna'),
        ),
        migrations.AlterField(
            model_name='residente',
            name='persona_discapacitada',
            field=models.CharField(choices=[('No', 'No'), ('Si', 'Si'), ('', 'No Determinado')], max_length=5, verbose_name='Persona con Discapacidad'),
        ),
        migrations.AlterField(
            model_name='residente',
            name='tipo_residente',
            field=models.CharField(choices=[('Propietario', 'Propietario'), ('Arrendatario', 'Arrendatario'), ('', 'No Determinado')], max_length=15, verbose_name='Propietario/Residente'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='tipo_vehiculo',
            field=models.CharField(choices=[('Automóvil', 'Automóvil'), ('Camioneta', 'Camioneta'), ('', 'No Determinado')], max_length=15, verbose_name='Tipo de vehículo'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='uso',
            field=models.CharField(choices=[('Particular', 'Particular'), ('Público', 'Público'), ('', 'No Determinado')], max_length=15, verbose_name='Tipo de Uso'),
        ),
    ]
