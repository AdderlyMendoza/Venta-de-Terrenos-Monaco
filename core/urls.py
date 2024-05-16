
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls', namespace='usuarios')),
    path('clientes/', include('clientes.urls', namespace='clientes')),
    path('finanzas/', include('finanzas.urls', namespace='finanzas')),
    path('proyectos/', include('proyectos.urls', namespace='proyectos')),
    path('reportes/', include('reportes.urls', namespace='reportes')),
    path('rrhh/', include('rrhh.urls', namespace='rrhh')),
    path('socios/', include('socios.urls', namespace='socios')),
    path('web/', include('web.urls', namespace='web')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)