from django.contrib import admin

from .models import *

admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Cuotas)
admin.site.register(Cobro)
admin.site.register(Contrato)

