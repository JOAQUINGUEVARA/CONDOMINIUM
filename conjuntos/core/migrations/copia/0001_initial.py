# Generated by Django 2.1.7 on 2019-05-10 16:26

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartamento',
            fields=[
                ('numero', models.IntegerField(default='', primary_key=True, serialize=False, verbose_name='Número')),
            ],
            options={
                'verbose_name': 'Apartamento',
                'verbose_name_plural': 'Apartamentos',
                'ordering': ['numero'],
            },
        ),
        migrations.CreateModel(
            name='Autorizado',
            fields=[
                ('identificacion', models.CharField(default='', max_length=20, primary_key=True, serialize=False, verbose_name='Identificaciòn')),
                ('nombre', models.CharField(default='', max_length=50, verbose_name='Nombre')),
                ('foto', models.FileField(upload_to='static/')),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Apartamento')),
            ],
            options={
                'verbose_name': 'Autorizado',
                'verbose_name_plural': 'Autorizados',
                'ordering': ['identificacion'],
            },
        ),
        migrations.CreateModel(
            name='Correspondencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remitente', models.CharField(default='', max_length=100, verbose_name='Remitente')),
                ('destinatario', models.CharField(default='', max_length=100, verbose_name='Destinatario')),
                ('tipo_correspondencia', models.CharField(choices=[('normal', 'Normal'), ('urgente', 'Urgente')], max_length=10, verbose_name='Tipo de Correspondencia')),
                ('fecha_recibo', models.DateField()),
                ('fechahora_notifica', models.DateTimeField(auto_now_add=True)),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Apartamento')),
            ],
            options={
                'verbose_name': 'Correspondencia',
                'verbose_name_plural': 'Correspondencias',
                'ordering': ['fecha_recibo'],
            },
        ),
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('numero', models.IntegerField(default='', primary_key=True, serialize=False, verbose_name='Número')),
                ('valor_arriendo', models.FloatField(default=0, verbose_name='Valor Arriendo')),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Apartamento')),
            ],
            options={
                'verbose_name': 'Depósito',
                'verbose_name_plural': 'Depósitos',
                'ordering': ['numero'],
            },
        ),
        migrations.CreateModel(
            name='Ingreso_peatonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_ingreso', models.DateTimeField(auto_now_add=True)),
                ('hora_salida', models.DateTimeField(auto_now=True)),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Apartamento')),
            ],
            options={
                'verbose_name': 'Ingreso',
                'verbose_name_plural': 'Ingresos',
                'ordering': ['hora_ingreso'],
            },
        ),
        migrations.CreateModel(
            name='Ingreso_vehiculo',
            fields=[
                ('placa', models.CharField(default='', max_length=10, primary_key=True, serialize=False, verbose_name='placa')),
                ('tipo_ingreso', models.CharField(choices=[('visitante', 'Visitante'), ('residente', 'Residente')], max_length=15, verbose_name='Visitante/Residente')),
                ('foto', models.FileField(upload_to='static/')),
                ('hora_ingreso', models.DateTimeField(auto_now_add=True)),
                ('hora_salida', models.DateTimeField(auto_now=True)),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Apartamento')),
            ],
            options={
                'verbose_name': 'Ingreso Vehículo',
                'verbose_name_plural': 'Ingreso Vehículos',
                'ordering': ['hora_ingreso'],
            },
        ),
        migrations.CreateModel(
            name='Inmobiliaria',
            fields=[
                ('código', models.IntegerField(default='', primary_key=True, serialize=False, verbose_name='Código')),
                ('nit', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Nit')),
                ('razon_social', models.CharField(max_length=100, verbose_name='Razón Social')),
                ('nombre_contacto', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Nombre Contacto')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('pagina_web', models.URLField(blank=True, default='', null=True, verbose_name='Link Página Web')),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Apartamento')),
            ],
            options={
                'verbose_name': 'Inmobiliaria',
                'verbose_name_plural': 'Inmobiliarias',
                'ordering': ['razon_social'],
            },
        ),
        migrations.CreateModel(
            name='Interior',
            fields=[
                ('numero', models.IntegerField(default='', primary_key=True, serialize=False, verbose_name='Número')),
            ],
            options={
                'verbose_name': 'Interior',
                'verbose_name_plural': 'Interiores',
                'ordering': ['numero'],
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=20, verbose_name='Nombre')),
                ('tipo_mascota', models.CharField(choices=[('perro', 'Perro'), ('gato', 'Gato'), ('otro', 'Otro')], max_length=10, verbose_name='Tipo de Mascota')),
                ('raza', models.CharField(default='', max_length=20, verbose_name='Raza')),
                ('edad', models.IntegerField(blank=True, default=0, null=True, verbose_name='Edad')),
                ('vacuna', models.CharField(choices=[('si', 'Si'), ('no', 'No')], max_length=5, verbose_name='Vacuna')),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Apartamento')),
                ('interior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Interior')),
            ],
            options={
                'verbose_name': 'Mascota',
                'verbose_name_plural': 'Mascotas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Parqueadero',
            fields=[
                ('numero', models.IntegerField(default='', primary_key=True, serialize=False, verbose_name='Número')),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Apartamento')),
                ('interior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Interior')),
            ],
            options={
                'verbose_name': 'Parqueadero',
                'verbose_name_plural': 'Parqueaderos',
                'ordering': ['numero'],
            },
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('identificacion', models.CharField(default='', max_length=20, primary_key=True, serialize=False, verbose_name='Identificaciòn')),
                ('nombre', models.CharField(default='', max_length=50, verbose_name='Nombre')),
                ('telefono', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Teléfono')),
                ('celular', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Celular')),
                ('direccion', models.CharField(blank=True, default='', max_length=80, null=True, verbose_name='Dirección')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Apartamento')),
                ('interior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Interior')),
            ],
            options={
                'verbose_name': 'Propietario',
                'verbose_name_plural': 'Propietarios',
                'ordering': ['identificacion'],
            },
        ),
        migrations.CreateModel(
            name='Residente',
            fields=[
                ('identificacion', models.CharField(default='', max_length=20, primary_key=True, serialize=False, verbose_name='Identificaciòn')),
                ('nombre', models.CharField(default='', max_length=50, verbose_name='Nombre')),
                ('tipo_residente', models.CharField(choices=[('propietario', 'Propietario'), ('arrendatario', 'Arrendatario')], max_length=20, verbose_name='Propietario/Residente')),
                ('telefono', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Teléfono')),
                ('celular', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Celular')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('edad', models.IntegerField(blank=True, default=0, null=True, verbose_name='Edad')),
                ('persona_discapacitada', models.CharField(choices=[('no', 'No'), ('si', 'Si')], max_length=5, verbose_name='Persona con Discapacidad')),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Apartamento')),
                ('interior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Interior')),
            ],
            options={
                'verbose_name': 'Residente',
                'verbose_name_plural': 'Residentes',
                'ordering': ['identificacion'],
            },
        ),
        migrations.CreateModel(
            name='TipoIngreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'TipoIngreso',
                'verbose_name_plural': 'TipoIngresos',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('placa', models.CharField(default='', max_length=10, primary_key=True, serialize=False, verbose_name='placa')),
                ('tipo_vehiculo', models.CharField(choices=[('automovil', 'Automóvil'), ('camioneta', 'Camioneta')], max_length=15, verbose_name='Tipo de vehículo')),
                ('uso', models.CharField(choices=[('particular', 'Particular'), ('publico', 'Público')], max_length=15, verbose_name='Tipo de Uso')),
                ('marca', models.CharField(default='', max_length=20, verbose_name='Marca')),
                ('modelo', models.IntegerField(blank=True, default=0, null=True, verbose_name='Modelo')),
                ('color', models.CharField(default='', max_length=30, verbose_name='Color')),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Apartamento')),
                ('interior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Interior')),
                ('parqueadero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Parqueadero')),
            ],
            options={
                'verbose_name': 'vehículo',
                'verbose_name_plural': 'Vehículos',
                'ordering': ['placa'],
            },
        ),
        migrations.CreateModel(
            name='Vigilante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Vigilante',
                'verbose_name_plural': 'Vigilantes',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('identificacion', models.CharField(default='', max_length=20, primary_key=True, serialize=False, verbose_name='Identificaciòn')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('foto', models.FileField(upload_to='static/')),
            ],
            options={
                'verbose_name': 'Visitante',
                'verbose_name_plural': 'Visitante',
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='inmobiliaria',
            name='interior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Interior'),
        ),
        migrations.AddField(
            model_name='ingreso_vehiculo',
            name='interior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Interior'),
        ),
        migrations.AddField(
            model_name='ingreso_vehiculo',
            name='vigilante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Vigilante'),
        ),
        migrations.AddField(
            model_name='ingreso_peatonal',
            name='foto',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='identificacion', chained_model_field='identificacion', on_delete=django.db.models.deletion.CASCADE, related_name='visitante_foto', to='core.Visitante', verbose_name='Foto'),
        ),
        migrations.AddField(
            model_name='ingreso_peatonal',
            name='identificacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Visitante', verbose_name='Identificación'),
        ),
        migrations.AddField(
            model_name='ingreso_peatonal',
            name='interior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Interior'),
        ),
        migrations.AddField(
            model_name='ingreso_peatonal',
            name='tipoingreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TipoIngreso'),
        ),
        migrations.AddField(
            model_name='ingreso_peatonal',
            name='vigilante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Vigilante'),
        ),
        migrations.AddField(
            model_name='deposito',
            name='interior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Interior'),
        ),
        migrations.AddField(
            model_name='correspondencia',
            name='interior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Interior'),
        ),
        migrations.AddField(
            model_name='correspondencia',
            name='vigilante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Vigilante'),
        ),
        migrations.AddField(
            model_name='autorizado',
            name='interior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Interior'),
        ),
        migrations.AddField(
            model_name='autorizado',
            name='tipoingreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TipoIngreso'),
        ),
    ]
