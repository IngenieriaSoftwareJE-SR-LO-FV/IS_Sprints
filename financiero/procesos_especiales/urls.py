from django.urls import path
from django.views import generic

from . import views
from .models import *

urlpatterns = [
    path('', views.index, name='procesos_especiales_index'),
    path('cambio_participante', views.cambio_participante_index, name='procesos_especiales_cambio_participante'),
    path('devolucion', views.devolucion_index, name='procesos_especiales_devolucion'),
    path('cambio_evento', views.cambio_evento_index, name='procesos_especiales_devolucion'),
    
]
    

