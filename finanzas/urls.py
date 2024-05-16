from django.urls import path
from . import views
from .views import *

app_name="finanzas"

urlpatterns = [
   
    path('finanzas_panel/', views.app_finanzas, name='finanzas_panel'),
]