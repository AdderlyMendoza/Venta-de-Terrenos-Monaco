from django.urls import path
from . import views
from .views import *    


app_name="web"

urlpatterns = [
   
    path('web/', views.appWeb, name = 'web'),
    path('listar/', views.listar, name = 'listarCompras'),
    path('separarLote/', views.separar_lote , name = 'separarLote'),
    path('pag_web/', views.pag_web, name = 'pag_web'),

    
]
    
