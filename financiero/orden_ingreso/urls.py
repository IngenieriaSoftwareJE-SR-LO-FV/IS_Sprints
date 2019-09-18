from django.urls import path
from django_filters.views import FilterView
from . import views
from .filters import OrdenIngresoFilter



urlpatterns = [
    path('nuevo', views.OrdenIngresoCreate.as_view(), name='ordenIngreso_nuevo'),
    path('', FilterView.as_view(filterset_class=OrdenIngresoFilter,template_name="ordenIngreso_list.html"), name='ordenIngreso'),
    #path('editar/<pk>/', views.PropuestaCorporativoUpdate.as_view(), name='propuesta_editar'),    
    #path('eliminar/<pk>/', views.PropuestaCorporativoDelete.as_view(), name='propuesta_eliminar'),
]