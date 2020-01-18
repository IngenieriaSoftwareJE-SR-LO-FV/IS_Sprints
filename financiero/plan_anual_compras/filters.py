from .models import PlanAnualCompras
import django_filters
from django import forms

class PlanAnualComprasFilter(django_filters.FilterSet):

	año = django_filters.CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Año'}))
	nombre = django_filters.CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Nombre Plan Anual de Compras'}))

	class Meta:
		model = PlanAnualCompras
		fields = ["año", "nombre",]