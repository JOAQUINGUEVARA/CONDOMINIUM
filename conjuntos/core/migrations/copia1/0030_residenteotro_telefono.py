# Generated by Django 3.2.5 on 2021-08-30 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_rename_residenteotros_residenteotro'),
    ]

    operations = [
        migrations.AddField(
            model_name='residenteotro',
            name='telefono',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Teléfono'),
        ),
    ]
