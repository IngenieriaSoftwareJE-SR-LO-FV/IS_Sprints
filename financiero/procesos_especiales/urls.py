from django.urls import path
from django.views import generic

from . import views
from .models import *

urlpatterns = [
    path('', views.index, name='procesos_especiales_index'),
    path('cambio_participante', views.cambio_participante_index, name='procesos_especiales_cambio_participante'),


    path('cambio_evento', views.cambio_evento_index, name='procesos_especiales_cambio_evento'),
    path('ajax/load-eventos',views.load_eventos_participante,name='ajax_load_eventos'),
    path('ajax/load-personas-evento',views.load_personas_evento,name='ajax_load_personas_evento'),
    path('ajax/cambio/', views.confirmar_cambio, name='confirmar_cambio'),

    path('cambio_evento_autorizar/<pk>', views.cambio_evento_autorizar, name='procesos_especiales_cambio_evento_autorizar'),
    path('cambio_evento_anular/<pk>', views.cambio_evento_anular, name='procesos_especiales_cambio_evento_anular'),

    path('devolucion', views.devolucion_nuevo, name='procesos_especiales_devolucion'),
    path('devolucion_editar/<pk>', views.devolucion_editar, name='procesos_especiales_devolucion_editar'),

    
]
    

