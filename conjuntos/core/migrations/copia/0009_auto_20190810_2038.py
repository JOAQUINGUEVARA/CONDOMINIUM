# Generated by Django 2.2.4 on 2019-08-11 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190810_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='correspondencia',
            old_name='Detalle',
            new_name='detalle',
        ),
    ]
