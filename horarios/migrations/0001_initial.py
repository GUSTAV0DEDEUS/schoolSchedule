# Generated by Django 5.0.2 on 2024-09-23 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField()),
                ('periodo', models.IntegerField(choices=[(1, 'Matutino'), (2, 'Vespertino'), (3, 'Noturno')])),
            ],
        ),
    ]
