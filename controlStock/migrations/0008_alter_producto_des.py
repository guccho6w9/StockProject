# Generated by Django 5.0.1 on 2024-02-22 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlStock', '0007_historialproducto_cod_anterior'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='des',
            field=models.CharField(max_length=75),
        ),
    ]
