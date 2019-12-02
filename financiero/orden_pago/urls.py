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
    path("autorizar/<pk>", views.orden_pago_autorizar, name="orden_pago_autorizar"),
    path("anular/", views.orden_pago_anular, name="orden_pago_anular"),
    path("anular/<pk>", views.orden_pago_anular, name="orden_pago_anular"),
]