from django.urls import path
from django.views import generic

from . import views
from . import forms
from .models import *
urlpatterns = [
    path('', views.index_juridicas, name='index_juridicas'),
    path('nuevo/', views.juridicas_view, name='juridicas_view'),
    path("ajax/load-ciudades/",views.load_ciudades, name="ajax_load_ciudades"),
    path("tipo-autocomplete/",views.TipoAutocomplete.as_view(model=TipoEmpresa,create_field="nombre"),name="tipo-autocomplete"),
    path("sector-autocomplete/",views.SectorAutocomplete.as_view(model=Sector,create_field="nombre"),name="sector-autocomplete"),

]
