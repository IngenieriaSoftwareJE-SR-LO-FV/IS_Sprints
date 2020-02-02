from django.urls import path
from django_filters.views import FilterView
from . import views
from .filters import OrdenIngresoFilter



urlpatterns = [
    path('nuevo', views.OrdenIngresoCreate.as_view(), name='ordenIngreso_nuevo'),
    path('nuevo/<pk>/', views.OrdenIngresoCreate.as_view(), name='ordenIngreso_nuevo'),
    path('', FilterView.as_view(filterset_class=OrdenIngresoFilter,template_name="ordenIngreso_list.html"), name='ordenIngreso'),
    path('editar/<pk>/', views.OrdenIngresoUpdate.as_view(), name='ordenIngreso_editar'),
    path('imprimir/<pk>/', views.OrdenIngresoPrint.as_view(), name='ordenIngreso_print'),        
    path('eliminar/<pk>/', views.OrdenIngresoDelete.as_view(), name='ordenIngreso_eliminar'),
    path('ajax/load-modal-orden-ing',views.orden_ing_conf_elim,name='orden_ingreso_confirmar_eliminar'),
]