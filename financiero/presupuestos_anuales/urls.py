from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="presupuesto_anual_lista"),
    path("nuevo/", views.presupuestos_anuales_nuevo, name="presupuesto_anual_nuevo"),
    path("editar/<pk>", views.presupuesto_anual_editar, name="presupuesto_anual_editar"),
    path("editar_autr/<pk>", views.presupuesto_anual_editarAUTR, name="presupuesto_anual_editarAUTR"),
    path("enviar_solicitud/<pk>", views.presupuesto_anual_enviar, name="presupuesto_anual_enviar"),
    path("autorizar/<pk>", views.presupuesto_anual_autorizar, name="presupuesto_anual_autorizar"),
    path("anular/", views.presupuesto_anual_anular, name="presupuesto_anual_anular"),
    path("anular/<pk>", views.presupuesto_anual_anular, name="presupuesto_anual_anular"),
    path("nuevo_f/", views.presupuestos_anuales_nuevo_fundespol, name="presupuestos_anuales_nuevo_fundespol"),
    path("editar_f/<pk>", views.presupuesto_anual_editar_fundespol, name="presupuesto_anual_editar_fundespol"),
    path("editar_autr_f/<pk>", views.presupuesto_anual_editarAUTR_fundespol, name="presupuesto_anual_editarAUTR_fundespol"),
    path("enviar_solicitud_f/<pk>", views.presupuesto_anual_enviar_fundespol, name="presupuesto_anual_enviar_fundespol"),
    path("autorizar_f/<pk>", views.presupuesto_anual_autorizar_fundespol, name="presupuesto_anual_autorizar_fundespol"),
    path("anular_f/", views.presupuesto_anual_anular_fundespol, name="presupuesto_anual_anular_fundespol"),
    path("anular_f/<pk>", views.presupuesto_anual_anular_fundespol, name="presupuesto_anual_anular_fundespol"),
]