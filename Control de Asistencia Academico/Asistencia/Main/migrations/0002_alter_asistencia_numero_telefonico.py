# Generated by Django 4.2.1 on 2023-11-01 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='numero_telefonico',
            field=models.CharField(max_length=10, verbose_name='Número Telefónico'),
        ),
    ]