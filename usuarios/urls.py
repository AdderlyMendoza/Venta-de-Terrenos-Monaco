from django.urls import path


from . import views
from .views import *

app_name="usuarios"

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('home/', HomeView.as_view(), name='home'),
    # PAGINAS DE LOGIN Y REGISTRO (VIDEO 5)
   
    
    
    # Your URL patterns here
]