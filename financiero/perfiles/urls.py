from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='financiero'),   
    path('analista/', views.index_analista, name='financiero_analista'),  
    path('coordinador/', views.index_coordinador, name='financiero_coordinador'),
    path('pendiente_aprobacion/', views.por_aprobar, name='pendiente_aprobacion'),
]
