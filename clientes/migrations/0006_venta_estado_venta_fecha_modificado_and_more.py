# Generated by Django 5.0.4 on 2024-05-28 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_cuotas_fecha_pago_cuotas_fecha_vencimiento_and_more'),
        ('proyectos', '0002_manzana'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='estado',
            field=models.CharField(choices=[('pagado', 'pagado'), ('pendiente', 'pendiente')], default='pendiente', max_length=20),
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha_modificado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha_separacion',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='manzana',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='proyectos.manzana'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='adelanto',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='precio_venta',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='venta',
            name='proyecto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='proyectos.proyectos'),
            preserve_default=False,
        ),
    ]
