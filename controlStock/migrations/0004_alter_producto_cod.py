# Generated by Django 5.0.1 on 2024-02-21 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlStock', '0003_remove_producto_rub_producto_aju_producto_ofe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cod',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
