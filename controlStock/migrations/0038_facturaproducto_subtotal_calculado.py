# Generated by Django 5.0.1 on 2024-03-19 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlStock', '0037_alter_facturaproducto_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaproducto',
            name='subtotal_calculado',
            field=models.FloatField(default=0),
        ),
    ]
