from django.urls import path
from django.views import generic
from django_filters.views import FilterView
from . import views
from . import forms
from .models import *
from .filters import *
urlpatterns = [
	path('nuevo', views.InteresadoCreate.as_view(), name='interesados_nuevo'),
    path('', FilterView.as_view(filterset_class=InteresadoFilter,template_name="interesados_list.html"), name='interesados'),
    path('editar/<pk>/', views.InteresadoUpdate.as_view(), name='interesados_editar'),    
    path('eliminar/<pk>/', views.InteresadoDelete.as_view(), name='interesado_eliminar'),
    path('cargar', views.cargar_interesados, name='interesados_cargar'),
    path('ajax/load-modal-interesado',views.interesado_conf_elim,name='interesado_confirmar_eliminar'),
]