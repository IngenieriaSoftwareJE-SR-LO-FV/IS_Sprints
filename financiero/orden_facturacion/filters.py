from .models import OrdenFacturacion
from financiero.orden_facturacion.models import OrdenFacturacion
from financiero.orden_facturacion.forms import TRUE_FALSE_CHOICES
import django_filters
from django import forms


class OrdenFacturacionFilter(django_filters.FilterSet):
    cod_orden_fact = django_filters.CharFilter(lookup_expr='icontains', label="", widget=forms.TextInput(attrs={'placeholder':'Código de Orden de Facturación'}))
    fecha=django_filters.DateFilter(field_name='fecha', label='',widget=forms.DateInput(attrs={'placeholder':'Fecha','type':'date'}))
    ruc_ci=django_filters.CharFilter(lookup_expr='icontains',label="", widget=forms.TextInput(attrs={'placeholder':'RUC o CI del Cliente'}))
    razon_nombres=django_filters.CharFilter(lookup_expr='icontains',label="", widget=forms.TextInput(attrs={'placeholder':'Nombre o Razón Social del Cliente'}))
    estado = django_filters.ChoiceFilter(
		null_label="Pendiente",
		empty_label="Todos",
		choices=TRUE_FALSE_CHOICES,
        label=""
    )
    class Meta:
        model = OrdenFacturacion
        
        fields=[
            'cod_orden_fact',
            'fecha',
            'ruc_ci',
            'razon_nombres',
            'estado',
        ]
