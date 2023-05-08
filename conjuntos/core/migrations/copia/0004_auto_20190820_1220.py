# Generated by Django 2.2.4 on 2019-08-20 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190819_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso_peatonal',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
        migrations.AddField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='conjuntos', verbose_name='Foto Mascota'),
        ),
        migrations.AlterField(
            model_name='autorizado',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='correspondencia',
            name='fecha_recibo',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='correspondencia',
            name='fechahora_notifica',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='correspondencia',
            name='vigilante',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Vigilante'),
        ),
        migrations.AlterField(
            model_name='ingreso_peatonal',
            name='hora_ingreso',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='ingreso_peatonal',
            name='hora_salida',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Hora de Salida'),
        ),
        migrations.AlterField(
            model_name='ingreso_peatonal',
            name='vigilante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Vigilante'),
        ),
        migrations.AlterField(
            model_name='ingreso_vehiculo',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='ingreso_vehiculo',
            name='hora_ingreso',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='ingreso_vehiculo',
            name='hora_salida',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]