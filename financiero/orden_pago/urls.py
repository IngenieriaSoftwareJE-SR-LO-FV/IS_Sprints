from django.urls import path
from django_filters.views import FilterView
from . import views
from .filters import OrdenPagoFilter

urlpatterns = [
    path("", views.index, name="orden_pago_lista"),
    path("ajax/load-egresos/", views.load_egresos, name="ajax_load_egresos"),
    path("ajax/load-proveedor/", views.load_proveedor, name="ajax_load_proveedor"),
    path("nuevo/", views.orden_pago_nuevo, name="orden_pago_nuevo"),
]