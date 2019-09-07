from django.urls import path

from . import views

urlpatterns = [
    path('nuevo', views.ReporteContactoCreate.as_view(), name='reporte_nuevo'),
    path('', views.ReporteContactoList.as_view(), name='index'),
    path('editar/<pk>/', views.ReporteContactoUpdate.as_view(), name='reporte_editar'),    
    path('eliminar/<pk>/', views.ReporteContactoDelete.as_view(), name='reporte_eliminar'),    


]