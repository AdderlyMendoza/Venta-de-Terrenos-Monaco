from django.db import models

class Web( models.Model ):
    dni = models.IntegerField()
    nombres = models.CharField(max_length=50, verbose_name='Nombres')
    apellidos = models.CharField(max_length=50, verbose_name='Apellidos')
    telefono = models.IntegerField()  
    email = models.CharField(max_length=50, verbose_name='Email')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    terrenos = models.CharField(max_length=500, verbose_name='Terrenos')
        
    class Meta:
        verbose_name = ("Web")
        verbose_name_plural = ("Webs")

    def __str__(self):
        return self.nombres
