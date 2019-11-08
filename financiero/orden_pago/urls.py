from django.urls import path
from django_filters.views import FilterView
from . import views
from .filters import OrdenPagoFilter

urlpatterns = [
    path("", views.index, name="orden_pago_lista"),
]