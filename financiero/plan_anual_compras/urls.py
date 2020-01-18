from django.urls import path
from django_filters.views import FilterView
from . import views

urlpatterns = [
	path("", views.index, name="pac_index"),
	path("nuevo/", views.PACCreate.as_view(), name="pac_nuevo"),
	path("editar/<pk>/", views.PACUpdate.as_view(), name="pac_editar"),
	path("eliminar/", views.PACDelete, name="pac_eliminar"),
	path("eliminar/<pk>/", views.PACDelete, name="pac_eliminar"),
	path('partida/nuevo/<pk>/',views.PartidaCreate.as_view(),name='partida_nuevo'),
	path('partida/editar/<pk>/<fk>/',views.PartidaUpdate.as_view(),name='partida_editar'),
	path('partida/eliminar/<pk>/<fk>/',views.PartidaDelete.as_view(),name='partida_eliminar'),
]