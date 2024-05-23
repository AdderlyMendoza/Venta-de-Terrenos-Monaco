# Generated by Django 5.0.4 on 2024-05-23 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('ap_paterno', models.CharField(max_length=100)),
                ('ap_materno', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('documento', models.IntegerField()),
                ('celular', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('pagado', 'pagado'), ('pendiente', 'pendiente')], default='pendiente', max_length=20)),
                ('precio_venta', models.FloatField(default=0.0)),
                ('adelanto', models.FloatField(blank=True, default=0.0, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_separacion', models.IntegerField()),
                ('fecha_modificado', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='clientes.cliente')),
                ('manzana', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='proyectos.manzana')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='proyectos.proyectos')),
                ('subproyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='proyectos.sub_proyecto')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.CreateModel(
            name='Cuotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('pagado', 'Pagado'), ('no_pagado', 'No pagado'), ('cancelado', 'Cancelado')], default='no_pagado', max_length=20)),
                ('forma_pago', models.CharField(choices=[('contado', 'Contado'), ('cuotas', 'Cuotas')], max_length=20)),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cuota_inicial', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cuota_numero', models.IntegerField(default=1)),
                ('min_cuota', models.IntegerField(default=500)),
                ('cuotas_pendientes', models.IntegerField(default=0)),
                ('montos_de_cuotas', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('porcentaje_inicial', models.DecimalField(decimal_places=2, default=0.3, max_digits=5)),
                ('saldo_pendiente', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fecha_pago', models.DateField(blank=True, null=True)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('fechas_de_pagos', models.TextField(blank=True, null=True)),
                ('pagada', models.BooleanField(default=False)),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('pdf_contrato', models.FileField(blank=True, null=True, upload_to='contratos/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Cobro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField()),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.venta')),
            ],
        ),
    ]
