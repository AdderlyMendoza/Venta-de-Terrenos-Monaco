from django.urls import path
from . import views
from .views import *


app_name="clientes"

urlpatterns = [
   
    # Your URL patterns here
    path('clientes_panel/', views.app_clientes, name='clientes_panel'),
    path('clientes/', views.clientes, name='clientes'),
    
    path('crear/', views.crear_cliente, name='crear_cliente'),
    path('ver/<int:pk>/', views.ver_cliente, name='ver_cliente'),
    
    path('editar_cliente/<str:pk>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar/<str:pk>/', views.eliminar_cliente, name='eliminar_cliente'),

    #SEPARAR LOTES
    path('ventas/', views.listar_ventas, name='listar_ventas'),
    path('ventas/crear/', views.crear_venta, name='crear_venta'),
    path('ventas/<int:venta_id>/', views.ver_venta, name='ver_venta'),
    path('ventas/<int:venta_id>/actualizar/', views.actualizar_venta, name='actualizar_venta'),
    path('ventas/<int:venta_id>/eliminar/', views.eliminar_venta, name='eliminar_venta'),

    #cuotas
 
    


    
]

