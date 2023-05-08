# Generated by Django 3.1.13 on 2023-03-31 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20230331_1244'),
        ('upload', '0002_auto_20230328_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnexoPagoReserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default='', max_length=50)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='upload/anexos')),
                ('publicar', models.BooleanField(default=False, verbose_name='Publicar Anexo ')),
                ('reserva', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anexo_baja_activo_fijo', to='core.reservas', verbose_name='Anexo BajaActivoFijo')),
            ],
        ),
    ]