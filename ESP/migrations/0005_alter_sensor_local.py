# Generated by Django 4.0.5 on 2022-06-19 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESP', '0004_sensor_local'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='local',
            field=models.CharField(max_length=11, verbose_name='Local de Instalação'),
        ),
    ]
