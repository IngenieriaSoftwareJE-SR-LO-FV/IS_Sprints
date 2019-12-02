from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='financiero'),   
    path('analista/', views.index_analista, name='financiero_analista'),  
    path('coordinador/', views.index_coordinador, name='financiero_coordinador'),
    path('pendiente_aprobacion/', views.por_aprobar, name='pendiente_aprobacion'),
    path('ajax/aprobar_factura/<pk>',views.aprobar_orden_fact, name="aprobar_orden_fact"),
    path('ajax/anular_factura/<pk>',views.anular_orden_fact, name="anular_orden_fact"),

]
