from django.urls import path
from django_filters.views import FilterView
from . import views
from .filters import ReporteContactoFilter


urlpatterns = [
    path('nuevo', views.ReporteContactoCreate.as_view(), name='reporte_nuevo'),
    path('', FilterView.as_view(filterset_class=ReporteContactoFilter,template_name="reporte_list.html"), name='reporte_contacto'),
    path('editar/<pk>/', views.ReporteContactoUpdate.as_view(), name='reporte_editar'),    
    path('eliminar/<pk>/', views.ReporteContactoDelete.as_view(), name='reporte_eliminar'),
    path('capacitacion/nuevo/<pk>/',views.CapacitacionCreate.as_view(),name='capacitacion_nuevo'),
    path('capacitacion/editar/<pk>/<fk>/',views.CapacitacionUpdate.as_view(),name='capacitacion_editar'),
    path('capacitacion/eliminar/<pk>/<fk>/',views.CapacitacionDelete.as_view(),name='capacitacion_eliminar'),
    path('asesoria/nuevo/<pk>/',views.AsesoriaCreate.as_view(),name='asesoria_nuevo'),
    path('asesoria/editar/<pk>/<fk>/',views.AsesoriaUpdate.as_view(),name='asesoria_editar'),
    path('asesoria/eliminar/<pk>/<fk>/',views.AsesoriaDelete.as_view(),name='asesoria_eliminar'),
    path('empresa-autocomplete/',views.EmpresaAutocomplete.as_view(),name='empresa-autocomplete'),
]