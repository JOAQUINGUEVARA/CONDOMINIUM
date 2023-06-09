# Generated by Django 3.2.5 on 2021-08-12 21:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_reservazonascomunes_hora_final'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filtros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime.today, verbose_name='Fecha')),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.apartamento', verbose_name='Apartamento')),
                ('interior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.interior', verbose_name='Interior')),
            ],
        ),
    ]
