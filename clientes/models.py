from django.db import models
from datetime import timedelta
from django.db.models.signals import pre_save, post_save
from proyectos.models import *
from web.models import *
from django.dispatch import receiver
from django.utils import timezone
from datetime import date


class Cliente(models.Model):

    nombres = models.CharField(max_length=100)
    ap_paterno  = models.CharField(max_length=100)
    ap_materno = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    documento = models.IntegerField()
    celular = models.IntegerField()
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificado =models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("Cliente")
        verbose_name_plural = ("Clientes")

    def __str__(self):
        return self.nombres


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE, related_name='ventas', blank=True, null=True)
    subproyecto = models.ForeignKey(Sub_Proyecto, on_delete=models.CASCADE, related_name='ventas')
    precio_venta = models.FloatField()
    adelanto = models.FloatField(default=0)  # Campo para precio de adelanto
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.subproyecto.estado = 'SEPARADO'
        self.subproyecto.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = ("Venta")
        verbose_name_plural = ("Ventas")

    def __str__(self):
        return f"Venta de {self.subproyecto.nombre} del proyecto {self.proyecto.nombre} a {self.cliente.nombres}"


    def obtener_nombre_cliente(self):
        return self.cliente.nombres

    def obtener_precio_subproyecto(self):
        return self.subproyecto.precio_venta



@receiver(pre_save, sender=Venta)
def actualizar_precio_venta(sender, instance, **kwargs):
    instance.precio_venta = instance.subproyecto.precio_venta
    instance.proyecto = instance.subproyecto.proyecto

@receiver(pre_save, sender=Venta)
def verificar_subproyecto(sender, instance, **kwargs):
    if instance.subproyecto.ventas.exists():
        raise ValueError('Este subproyecto ya está asociado a una venta')
    


class Contrato(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    contenido = models.TextField()
    pdf_contrato = models.FileField(upload_to='contratos/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def guardar_pdf_contrato(self, pdf):
        self.pdf_contrato.save(f'contrato_{self.id}.pdf', pdf)



class Cuotas(models.Model):
    FORMA_PAGO_CHOICES = (
        ('contado', 'Contado'),
        ('cuotas', 'Cuotas')
    )

    ESTADO_CHOICES = (
        ('pagado', 'Pagado'),
        ('no_pagado', 'No pagado'),
        ('cancelado', 'Cancelado')
    )
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='no_pagado')
    forma_pago = models.CharField(max_length=20, choices=FORMA_PAGO_CHOICES)
    venta = models.ForeignKey('Venta', on_delete=models.CASCADE)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cuota_inicial = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cuota_numero = models.IntegerField(default=1)
    min_cuota = models.IntegerField(default=500)
    cuotas_pendientes = models.IntegerField(default=0)
    montos_de_cuotas = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    porcentaje_inicial = models.DecimalField(max_digits=5, decimal_places=2, default=0.3)
    saldo_pendiente = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_pago = models.DateField(null=True, blank=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    fechas_de_pagos = models.TextField(null=True, blank=True)
    pagada = models.BooleanField(default=False)

    @classmethod


    def __str__(self):
        return f"Cuota {self.cuota.id} - Fecha de vencimiento: {self.fecha_vencimiento}"


class Cobro(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    

    def __str__(self):
        return f"Cobro de {self.monto} para la venta {self.venta}"
    
