# Generated by Django 5.0.1 on 2024-03-17 21:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlStock', '0023_historialfactura_facturaproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaproducto',
            name='factura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlStock.historialfactura'),
        ),
    ]
