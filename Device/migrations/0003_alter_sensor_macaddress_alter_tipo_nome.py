# Generated by Django 4.0.5 on 2022-06-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0002_alter_sensor_options_alter_tipo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='macaddress',
            field=models.CharField(max_length=11, unique=True, verbose_name='Endereço MAC'),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='nome',
            field=models.CharField(max_length=30, unique=True, verbose_name='Tipo do sensor'),
        ),
    ]