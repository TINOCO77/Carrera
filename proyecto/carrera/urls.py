# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Definir las rutas de acceso a las vistas
urlpatterns = [
    path('', views.registro, name='registro'),
  path('exito/', views.exito, name='exito'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
