# Generated by Django 3.2.7 on 2021-09-22 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Productos', '0002_auto_20210916_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('dcto', models.FloatField(default=0)),
                ('cantMinima', models.IntegerField(default=0)),
                ('pagado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InfoEnvio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('departamento', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout_80159226.carritocompras')),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout_80159226.carritocompras')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Productos.producto')),
            ],
        ),
    ]
