# Generated by Django 5.0.6 on 2024-10-22 20:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('materias', models.ManyToManyField(blank=True, to='materias.materia')),
            ],
        ),
    ]
