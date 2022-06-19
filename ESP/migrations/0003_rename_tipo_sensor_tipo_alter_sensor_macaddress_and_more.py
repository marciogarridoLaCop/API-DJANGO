# Generated by Django 4.0.5 on 2022-06-19 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESP', '0002_alter_tipo_sensor_nome'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tipo_sensor',
            new_name='Tipo',
        ),
        migrations.AlterField(
            model_name='sensor',
            name='macaddress',
            field=models.CharField(max_length=11, verbose_name='Endereço MAC'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor',
            field=models.CharField(max_length=30, verbose_name='Nome do sensor'),
        ),
    ]
