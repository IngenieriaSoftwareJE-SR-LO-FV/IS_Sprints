from django.urls import path
from django_filters.views import FilterView
from .filters import ProformaFilter
from . import views
import ventas.reporte_contacto.views

urlpatterns = [
    path('nuevo', views.proforma_view, name='proforma_nuevo'),
    path('', FilterView.as_view(filterset_class=ProformaFilter,template_name="proforma_list.html"), name='proforma_lista'),
    path('editar/<pk>/', views.ProformaUpdate.as_view(), name='proforma_editar'),    
    path('eliminar/<pk>/', views.ProformaDelete.as_view(), name='proforma_eliminar'),
]