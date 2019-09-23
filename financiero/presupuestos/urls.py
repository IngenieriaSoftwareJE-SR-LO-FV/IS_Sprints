from django.urls import path
from django.views import generic

from . import views
from . import forms
from .models import *
from ventas.personas_juridicas.models import Juridica
urlpatterns = [
    path('', views.index_presupuestos, name='index_presupuestos'),
    path('nuevo/', views.presupuestos_nuevo, name='nuevo_presupuestos'),
    path('editar/<pk>', views.presupuestos_editar, name='editar_presupuestos'),
 #   path('editar/<pk>', views.juridicas_view, name='editar_presupuestos'),
    path("aula-autocomplete/",views.AulaAutocomplete.as_view(model=Aula,create_field="nombre"),name="aula-autocomplete"),
    path("empresa-autocomplete/",views.EmpresaAutocomplete.as_view(model=Juridica),name="empresa-autocomplete"),
]
    

