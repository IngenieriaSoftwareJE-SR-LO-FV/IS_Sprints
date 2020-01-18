from django.urls import path
from django_filters.views import FilterView
from . import views

urlpatterns = [
	path("", views.index, name="pac_index"),
]