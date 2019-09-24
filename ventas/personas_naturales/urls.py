from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='natural_lista'),
    path('nuevo/', views.natural_nuevo, name='natural_nuevo'),
    path('editar/<pk>/', views.NaturalUpdate.as_view(), name='natural_editar'),
    path('eliminar/<pk>/', views.NaturalDelete.as_view(), name='natural_eliminar')
    
]