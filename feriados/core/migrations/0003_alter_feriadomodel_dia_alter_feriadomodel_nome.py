# Generated by Django 4.1.1 on 2023-04-12 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_feriadomodel_modificado_em'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feriadomodel',
            name='dia',
            field=models.IntegerField(verbose_name='Dia'),
        ),
        migrations.AlterField(
            model_name='feriadomodel',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Feriado'),
        ),
    ]
