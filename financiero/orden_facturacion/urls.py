from django.urls import path
from django_filters.views import FilterView
from financiero.orden_facturacion import views
from .filters import OrdenFacturacionFilter


urlpatterns = [
    path('nuevo', views.OrdenFacturacionCreate.as_view(), name='orden_facturacion_nuevo'),
    path('ajax/load-personas',views.load_personas,name='ajax_load_personas'),
    path('ajax/load-modal-orden-fact',views.orden_fact_conf_elim,name='orden_facturacion_confirmar_eliminar'),
    path('ajax/verificar-campos',views.verificar_campos,name='ajax_verificar_campos'),
    path('ajax/info-cliente',views.load_info,name='ajax_info_id'),
    path('ajax/orden-ci',views.load_info_ci,name="ajax_orden_ci"),
    path('', views.index, name='orden_facturacion'),
    path('editar/<pk>/', views.OrdenFacturacionUpdate.as_view(), name='orden_facturacion_editar'),    
    path('eliminar/<pk>/', views.OrdenFacturacionDelete.as_view(), name='orden_facturacion_eliminar'),
    path('cambiar-estado/<pk>/', views.cambiar_estado, name='orden_facturacion_estado'),
    path('participante/nuevo/<pk>/',views.ParticipanteCreate.as_view(),name='participante_nuevo'),
    path('participante/editar/<pk>/<fk>/',views.ParticipanteUpdate.as_view(),name='participante_editar'),
    path('participante/eliminar/<pk>/<fk>/',views.ParticipanteDelete.as_view(),name='participante_eliminar'),
    path('ajax/confirmar-eliminar-par',views.participante_conf_elim,name='participante_confirmar_eliminar'),
    path('aprobar/<pk>',views.aprobar_orden_facturacion, name="orden_facturacion_aprobar"),
    path('anular/<pk>',views.anular_orden_facturacion, name="orden_facturacion_anular"),
]