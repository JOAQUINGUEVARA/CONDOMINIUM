# Generated by Django 3.2.5 on 2021-07-27 17:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_reservazonascomunes_hora_incial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservazonascomunes',
            name='hora_incial',
        ),
        migrations.AddField(
            model_name='reservazonascomunes',
            name='hora_inicial',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(24)], verbose_name='Hora Inicial'),
        ),
    ]