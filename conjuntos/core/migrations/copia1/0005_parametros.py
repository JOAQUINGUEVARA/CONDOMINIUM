# Generated by Django 3.2.5 on 2021-07-13 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210709_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_parametro_uno', models.IntegerField(blank=True, default=0, null=True)),
                ('valor_parametro_dos', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.IntegerField(verbose_name='Usuario')),
            ],
        ),
    ]