from django.urls import path
from . import views
from .views import *


app_name="proyectos"

urlpatterns = [
   
    path('proyectos/', views.app_proyectos, name = 'proyectos'),

    path('listar/', views.listar_proyectos, name='listar_proyectos'),
    path('crear/', views.crear_proyecto, name='crear_proyecto'),
    path('ver/<int:pk>/', views.ver_proyecto, name='ver_proyecto'),
    
    path('editar_empleado/<str:pk>/', views.editar_proyecto, name='editar_proyecto'),
    path('eliminar/<str:pk>/', views.eliminar_proyecto, name='eliminar_proyecto'),
    
    # Subproyectos
    path('subproyectos', views.proyectos_y_subproyectos, name='subproyectos'),    
    path('subproyectos/crear/', views.crear_subproyecto, name='crear_subproyecto'),
    path('subproyectos/<str:pk>/', views.actualizar_subproyecto, name='actualizar_subproyecto'),
    path('subproyectos/<str:pk>/eliminar', views.eliminar_subproyecto, name='eliminar_subproyecto'),

    # path('subproyectos/disponibles/', views.lista_subproyectos_disponibles, name='subproyectos_disponibles'),
    # path('subproyectos/vendidos/', views.lista_subproyectos_vendidos, name='subproyectos_vendidos'),
    

 

    
]

