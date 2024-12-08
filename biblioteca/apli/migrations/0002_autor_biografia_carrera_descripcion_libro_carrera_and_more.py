# Generated by Django 5.1.3 on 2024-12-06 05:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apli', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='biografia',
            field=models.TextField(default='Sin Biografía'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='descripcion',
            field=models.TextField(default='Sin Descripción'),
        ),
        migrations.AddField(
            model_name='libro',
            name='carrera',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apli.carrera'),
        ),
        migrations.AddField(
            model_name='libro',
            name='isbn',
            field=models.CharField(default='0000000000000', max_length=13),
        ),
        migrations.AddField(
            model_name='libro',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='portadas/'),
        ),
        migrations.AddField(
            model_name='multa',
            name='fecha',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='libro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apli.libro'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(default='Sin Apellido', max_length=100),
        ),
        migrations.AlterField(
            model_name='autor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(default='Sin Nombre', max_length=100),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='nombre',
            field=models.CharField(default='Sin Nombre', max_length=100),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(default='Sin Nombre', max_length=100),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='direccion',
            field=models.CharField(default='Sin Dirección', max_length=255),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='nombre',
            field=models.CharField(default='Sin Nombre', max_length=100),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='telefono',
            field=models.CharField(default='0000000000', max_length=20),
        ),
        migrations.AlterField(
            model_name='estadolibro',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='estadolibro',
            name='nombre',
            field=models.CharField(default='Sin Estado', max_length=50),
        ),
        migrations.AlterField(
            model_name='estadomulta',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='estadomulta',
            name='nombre',
            field=models.CharField(default='Sin Nombre', max_length=50),
        ),
        migrations.AlterField(
            model_name='estadoprestamo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='estadoprestamo',
            name='nombre',
            field=models.CharField(default='Sin Nombre', max_length=50),
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apli.autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apli.categoria'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='descripcion',
            field=models.TextField(default='Sin Descripción'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='editorial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apli.editorial'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apli.estadolibro'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='fecha_publicacion',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(default='Sin Título', max_length=200),
        ),
        migrations.AlterField(
            model_name='multa',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apli.estadomulta'),
        ),
        migrations.AlterField(
            model_name='multa',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='multa',
            name='monto',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='multa',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apli.usuario'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apli.estadoprestamo'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion',
            field=models.DateField(default='2000-01-02'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apli.usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='carrera',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apli.carrera'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(default='sin@correo.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default='Sin Nombre', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='puesto',
            field=models.CharField(default='Sin Puesto', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(default='0000000000', max_length=20),
        ),
    ]
