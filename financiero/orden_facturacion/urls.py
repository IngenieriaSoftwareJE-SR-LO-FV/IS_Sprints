from django.urls import path
from django_filters.views import FilterView
from financiero.orden_facturacion import views
from .filters import OrdenFacturacionFilter


urlpatterns = [
    path('nuevo', views.OrdenFacturacionCreate.as_view(), name='orden_facturacion_nuevo'),
    path('ajax/load-personas',views.load_personas,name='ajax_load_personas'),
    path('', FilterView.as_view(filterset_class=OrdenFacturacionFilter,template_name="orden_facturacion.html"), name='orden_facturacion'),
    path('editar/<pk>/', views.OrdenFacturacionUpdate.as_view(), name='orden_facturacion_editar'),    
    path('eliminar/<pk>/', views.OrdenFacturacionDelete.as_view(), name='orden_facturacion_eliminar'),
]