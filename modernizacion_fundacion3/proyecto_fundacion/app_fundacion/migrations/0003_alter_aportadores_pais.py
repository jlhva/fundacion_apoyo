# Generated by Django 4.0.6 on 2022-07-13 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_fundacion', '0002_aportadores_delete_pacientes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aportadores',
            name='pais',
            field=models.IntegerField(choices=[(1, 'Chileno'), (2, 'Venenzolano'), (3, 'Haitiano'), (4, 'Colombiano'), (5, 'Otros')]),
        ),
    ]
