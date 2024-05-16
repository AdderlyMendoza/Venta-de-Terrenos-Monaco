from django.urls import path
from . import views
from .views import *

app_name="reportes"

urlpatterns = [
   
    path('reportes_panel/', views.app_reportes, name='reportes_panel'),
]