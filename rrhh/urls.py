from django.urls import path
from . import views
from .views import *

app_name="rrhh"

urlpatterns = [
   
    path('rrhh/', views.app_rrhh, name='rrhh_panel'),
    path('empleados/', views.listar_empleados, name='listar_empleados'),
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('empleados/<str:pk>/actualizar/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/<str:pk>/eliminar/', views.eliminar_empleado, name='eliminar_empleado'),
]