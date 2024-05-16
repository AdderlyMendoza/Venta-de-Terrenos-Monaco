from django.db import models

# Create your models here.
class Departamento(models.Model):
    codigo = models.CharField(max_length=6, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=6, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Distrito(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=6, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre