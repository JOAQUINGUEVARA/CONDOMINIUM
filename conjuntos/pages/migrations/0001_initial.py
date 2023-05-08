# Generated by Django 3.1.13 on 2023-03-27 14:29

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', ckeditor.fields.RichTextField(blank=True, default='', null=True, verbose_name='Contenido')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='pages', verbose_name='Foto Comunicado')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='upload/anexos')),
                ('dias_publicacion', models.SmallIntegerField(default=0, verbose_name='Dias Comunicación')),
                ('publicar', models.BooleanField(default=False, verbose_name='Publicar en Web')),
                ('comunidad', models.BooleanField(default=False, verbose_name='Publicar sólo a Cominidad')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Comunicado',
                'verbose_name_plural': 'Comunicado',
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Legislacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', ckeditor.fields.RichTextField(blank=True, default='', null=True, verbose_name='Contenido')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'legislacion',
                'verbose_name_plural': 'legislacion',
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Normatividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Normatividad Interna',
                'verbose_name_plural': 'Normatividad Interna',
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'página',
                'verbose_name_plural': 'páginas',
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'panel',
                'verbose_name_plural': 'panel',
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Pqr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('remitente', models.CharField(blank=True, default='', max_length=60, verbose_name='Remitente')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='pages', verbose_name='Foto Pqr')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('recibida', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Fecha de recibida')),
                ('fecha_respuesta', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Fecha de Respuesta')),
                ('pendiente', models.BooleanField(blank=True, default=False, null=True)),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.apartamento', verbose_name='Apartamento')),
                ('interior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.interior', verbose_name='Interior')),
            ],
            options={
                'verbose_name': 'Pqr',
                'verbose_name_plural': 'Pqr',
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='TipoPqr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo Pqr',
                'verbose_name_plural': 'Tipos Pqr',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='RespuestaPqr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('pqr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.pqr', verbose_name='Pqr')),
            ],
            options={
                'verbose_name': 'Respuesta Pqr',
                'verbose_name_plural': 'Respuestas Pqr',
                'ordering': ['content'],
            },
        ),
        migrations.AddField(
            model_name='pqr',
            name='tipo_pqr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.tipopqr'),
        ),
        migrations.AddField(
            model_name='pqr',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.CreateModel(
            name='Clasificado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='pages', verbose_name='Foto Clasificado')),
                ('informes', models.CharField(default='', max_length=100, verbose_name='Informes')),
                ('vigente', models.BooleanField(default=True, verbose_name='Venta vigente')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Residente')),
            ],
            options={
                'verbose_name': 'Clasificado',
                'verbose_name_plural': 'Clasificados',
                'ordering': ['order', 'title'],
            },
        ),
    ]