from django.contrib import admin

# Register your models here.
from .models import *
# Register your FROMmodels here.
admin.site.register(Proyectos)
admin.site.register(Sub_Proyecto)
admin.site.register(Imagen)