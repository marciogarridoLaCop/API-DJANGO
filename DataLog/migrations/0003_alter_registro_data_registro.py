# Generated by Django 4.0.5 on 2022-06-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataLog', '0002_registro_data_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='data_registro',
            field=models.DateTimeField(auto_now=True, verbose_name='Data do registro'),
        ),
    ]
