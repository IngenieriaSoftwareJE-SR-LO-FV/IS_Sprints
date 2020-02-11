from django.urls import path
from django_filters.views import FilterView
from . import views
from .filters import OrdenPagoFilter

urlpatterns = [
    path("", views.index, name="orden_pago_lista"),
    path("ajax/load-egresos/", views.load_egresos, name="ajax_load_egresos"),
    path("ajax/load-proveedor/", views.load_proveedor, name="ajax_load_proveedor"),
    path("nuevo/", views.orden_pago_nuevo, name="orden_pago_nuevo"),
    path("editar/<pk>", views.orden_pago_editar, name="orden_pago_editar"),
    path("editar_autrAnalista/<pk>",views.orden_pago_editarAUTR_analista, name="orden_pago_editarAUTR_analista"),
    path("editar_postAUTR/<pk>",views.orden_pago_editarPOST_AUTR, name="orden_pago_editarPOST_AUTR"),
    path("editar_PGDO/<pk>",views.orden_pago_editarPGDO, name="orden_pago_editarPGDO"),
    path("editar_autr/<pk>", views.orden_pago_editarAUTR, name="orden_pago_editarAUTR"),
    path("enviar_solicitud/<pk>", views.orden_pago_enviar, name="orden_pago_enviar"),
    path("autorizar/<pk>", views.orden_pago_autorizar, name="orden_pago_autorizar"),
    path("anular/", views.orden_pago_anular, name="orden_pago_anular"),
    path("anular/<pk>", views.orden_pago_anular, name="orden_pago_anular"),
]