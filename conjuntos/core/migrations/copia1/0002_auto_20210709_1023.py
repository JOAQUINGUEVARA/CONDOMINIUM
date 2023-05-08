# Generated by Django 3.2.5 on 2021-07-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartamento',
            name='coeficiente',
            field=models.FloatField(default=0, verbose_name='coeficiente'),
        ),
        migrations.AddField(
            model_name='parqueadero',
            name='coeficiente',
            field=models.FloatField(default=0, verbose_name='coeficiente'),
        ),
        migrations.AlterField(
            model_name='ingreso_peatonal',
            name='foto',
            field=models.ImageField(blank=True, default='/static/img/no-avatar.jpg', null=True, upload_to='static/'),
        ),
    ]