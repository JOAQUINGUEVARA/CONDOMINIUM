# Generated by Django 3.1.13 on 2023-05-03 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20230503_1229'),
        ('upload', '0003_anexopagoreserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anexoinformerevisor',
            name='informe_revisor',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anexo_informe_revisor', to='core.informerevisor', verbose_name='Anexo Informe Revisor'),
        ),
    ]
