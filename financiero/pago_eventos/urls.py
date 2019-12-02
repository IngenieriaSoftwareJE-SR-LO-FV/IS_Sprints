from django.urls import path
from django_filters.views import FilterView
from . import views
from .filters import PagoEventosFilter



urlpatterns = [
    path('', FilterView.as_view(filterset_class=PagoEventosFilter, template_name="pago_eventos.html"), name='pago_eventos_list'),
    #path('', views.index_pagos, name='pago_eventos_list'),
    
]