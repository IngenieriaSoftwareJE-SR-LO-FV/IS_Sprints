from .models import Espoltech, Fundespol
import django_filters
from django import forms

class EspoltechFilter(django_filters.FilterSet):
	año = django_filters.CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Año'}))
	nombre = django_filters.CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Nombre de Presupuesto'}))
	centro_costos = django_filters.CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Centro de Costos'}))
	class Meta:
		model = Espoltech
		fields = ['año','nombre','centro_costos']

class FundespolFilter(django_filters.FilterSet):
	año = django_filters.CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Año'}))
	nombre = django_filters.CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Nombre de Presupuesto'}))
	centro_costos = django_filters.CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Centro de Costos'}))
	class Meta:
		model = Espoltech
		fields = ['año','nombre','centro_costos']