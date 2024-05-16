from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Socio)
admin.site.register(Inversion)
admin.site.register(Pagos)
