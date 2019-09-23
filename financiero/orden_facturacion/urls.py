from django.urls import path
from django_filters.views import FilterView
from financiero.orden_facturacion import views
from .filters import OrdenFacturacionFilter


urlpatterns = [
    path('nuevo', views.OrdenFacturacionCreate.as_view(), name='orden_facturacion_nuevo'),
    path('ajax/load-personas',views.load_personas,name='ajax_load_personas'),
    path('', FilterView.as_view(filterset_class=OrdenFacturacionFilter,template_name="orden_facturacion.html"), name='orden_facturacion'),
    #path('editar/<pk>/', views.ReporteContactoUpdate.as_view(), name='reporte_editar'),    
    #path('eliminar/<pk>/', views.ReporteContactoDelete.as_view(), name='reporte_eliminar'),
    #path('capacitacion/nuevo/<pk>/',views.CapacitacionCreate.as_view(),name='capacitacion_nuevo'),
    #path('capacitacion/editar/<pk>/<fk>/',views.CapacitacionUpdate.as_view(),name='capacitacion_editar'),
    #path('capacitacion/eliminar/<pk>/<fk>/',views.CapacitacionDelete.as_view(),name='capacitacion_eliminar'),
    #path('asesoria/nuevo/<pk>/',views.AsesoriaCreate.as_view(),name='asesoria_nuevo'),
    #path('asesoria/editar/<pk>/<fk>/',views.AsesoriaUpdate.as_view(),name='asesoria_editar'),
    #path('asesoria/eliminar/<pk>/<fk>/',views.AsesoriaDelete.as_view(),name='asesoria_eliminar'),

]