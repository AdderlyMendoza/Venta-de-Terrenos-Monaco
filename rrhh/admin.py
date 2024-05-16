from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Cargo)
admin.site.register(Empleado)
admin.site.register(Asistencia)