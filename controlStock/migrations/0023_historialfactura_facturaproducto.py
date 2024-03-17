# Generated by Django 5.0.1 on 2024-03-17 20:37

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlStock', '0022_remove_historialfactura_producto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('domicilio', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('condicion_venta', models.CharField(default='efectivo', max_length=100)),
                ('condicion_fiscal', models.CharField(default='Arg.Consumidor Final', max_length=100)),
                ('cuit_dni', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FacturaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlStock.producto')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='controlStock.historialfactura')),
            ],
        ),
    ]