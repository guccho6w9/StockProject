# Generated by Django 5.0.1 on 2024-02-21 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlStock', '0002_alter_producto_cod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='rub',
        ),
        migrations.AddField(
            model_name='producto',
            name='aju',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='ofe',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]