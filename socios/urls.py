from django.urls import path
from . import views
from .views import *

app_name="socios"

urlpatterns = [
   
    path('socios_panel/', views.app_socios, name='socios_panel'),

    path('', SocioListView.as_view(), name='socio_list'),
    path('<int:pk>/', SocioDetailView.as_view(), name='socio_detail'),
    path('crear/', SocioCreateView.as_view(), name='socio_create'),
    path('<int:pk>/editar/', SocioUpdateView.as_view(), name='socio_update'),
    path('<int:pk>/eliminar/', SocioDeleteView.as_view(), name='socio_delete'),


   #inversiones
    
    path('listar_inversiones/', listar_inversiones, name='listar_inversiones'),
    path('inversiones/crear/', crear_inversion, name='crear_inversion'),
    path('inversiones/<int:inversion_id>/actualizar/', actualizar_inversion, name='actualizar_inversion'),
    path('detalle_inversion/<int:inversion_id>/', views.detalle_inversion, name='detalle_inversion'),
    path('eliminar/<int:inversion_id>/', eliminar_inversion, name='eliminar_inversion'),
    
]
