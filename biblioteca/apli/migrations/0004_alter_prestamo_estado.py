# Generated by Django 5.1.3 on 2024-12-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apli', '0003_remove_usuario_telefono_usuario_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='estado',
            field=models.CharField(choices=[('entregado', 'Entregado'), ('atrasado', 'Atrasado'), ('en_prestamo', 'En Préstamo')], default='en_prestamo', max_length=20),
        ),
    ]