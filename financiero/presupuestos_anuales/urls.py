from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="presupuesto_anual_lista"),
    path("nuevo/", views.presupuestos_anuales_nuevo, name="presupuesto_anual_nuevo"),
    path("editar/<pk>", views.presupuesto_anual_editar, name="presupuesto_anual_editar"),
    path("editar_autr/<pk>", views.presupuesto_anual_editarAUTR, name="presupuesto_anual_editarAUTR"),
    path("enviar_solicitud/<pk>", views.presupuesto_anual_enviar, name="presupuesto_anual_enviar"),
    path("autorizar/<pk>", views.presupuesto_anual_autorizar, name="presupuesto_anual_autorizar"),
    #path("eliminar/", views.presupuesto_anual_eliminar, name="presupuesto_anual_eliminar"),
    #path("eliminar/<pk>", views.presupuesto_anual_eliminar, name="presupuesto_anual_eliminar"),
]