# Generated by Django 2.2.4 on 2019-08-11 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190810_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='fecha_recibo',
            field=models.DateField(null=True),
        ),
    ]
