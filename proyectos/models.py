from django.db import models
from ubigeo.models import Distrito

class Proyectos(models.Model):
    class estado(models.TextChoices):

            ACTIVO = "ACTIVO"
            VENDIDO= "VENDIDO"
            PENDIENTE = "PENDIENTE"

    estado = models.CharField(choices=estado.choices, default="ACTIVO", max_length=30, )
    nombre = models.CharField(max_length=50, verbose_name='Nombre del proyecto')
    lugar = models.ForeignKey(Distrito,  on_delete=models.CASCADE, verbose_name='Ubicacion')
    direccion = models.CharField(max_length=50,  verbose_name='Direccion')
    google_maps = models.CharField(max_length=400, verbose_name='Google Maps', blank=True, null=True)
    tipo = models.CharField(max_length=50)
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()
    observacion = models.CharField(max_length=50,blank=True, null=True)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificado =models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("Proyecto")
        verbose_name_plural = ("Proyectos")

    def __str__(self):
        return self.nombre

class Manzana(models.Model):

    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Manzana")
        verbose_name_plural = ("Manzanas")

    def __str__(self):
        return self.nombre


class Sub_Proyecto(models.Model):

    class estados(models.TextChoices):

            VENDIDO = "VENDIDO"
            CUOTAS = "CUOTAS"
            DISPONIBLE = "DISPONIBLE"
            SEPARADO = "SEPARADO"

    estado = models.CharField(choices=estados.choices, default="DISPONIBLE", max_length=20, verbose_name="Estado")
    proyecto = models.ForeignKey(Proyectos,  on_delete=models.CASCADE)
    manzana = models.ForeignKey(Manzana, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    m2 = models.IntegerField()
    precio_venta = models.IntegerField()
    plano = models.FileField(upload_to='plano/', verbose_name="Plano", blank=True, null=True)
    observacion = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificado =models.DateTimeField(auto_now_add=True)
    id_personalizado = models.CharField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = ("Sub_Proyecto")
        verbose_name_plural = ("Sub_Proyectos")
  
    def __str__(self):
        return self.id_personalizado
    
    def save(self, *args, **kwargs):
        super(Sub_Proyecto, self).save(*args, **kwargs)

class Imagen(models.Model):
    sub_proyecto = models.ForeignKey(Sub_Proyecto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(verbose_name="Imagen", blank=True, null=True)

    class Meta:
        verbose_name = ("Imagen")
        verbose_name_plural = ("Imágenes")

    def __str__(self):
        return f"Imagen de {self.sub_proyecto.nombre}"
