# Generated by Django 5.0.1 on 2024-03-21 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlStock', '0038_facturaproducto_subtotal_calculado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='pre',
            field=models.FloatField(default=0),
        ),
    ]