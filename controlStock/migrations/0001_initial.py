# Generated by Django 4.2.7 on 2024-01-12 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_pd', models.AutoField(primary_key=True, serialize=False)),
                ('cod', models.CharField(max_length=10)),
                ('des', models.CharField(max_length=45)),
                ('rub', models.CharField(max_length=20)),
                ('pre', models.FloatField()),
            ],
        ),
    ]
