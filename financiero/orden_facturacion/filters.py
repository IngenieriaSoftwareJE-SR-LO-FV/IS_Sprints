from .models import OrdenFacturacion
from financiero.orden_facturacion.models import OrdenFacturacion
import django_filters
from django import forms


class OrdenFacturacionFilter(django_filters.FilterSet):
    cod_orden_fact = django_filters.CharFilter(lookup_expr='icontains', label="", widget=forms.TextInput(attrs={'placeholder':'Código de Orden de Facturación'}))
    fecha=django_filters.DateFilter(field_name='fecha', label='',widget=forms.DateInput(attrs={'placeholder':'Fecha','type':'date'}))
    estado = django_filters.ChoiceFilter(label="", empty_label="Estado", choices=ESTADO_CHOICES)
    cod_propuesta = django_filters.CharFilter(lookup_expr='icontains', label='', widget=forms.TextInput(attrs={'placeholder': 'Código de Propuesta'}))
    class Meta:
        model = OrdenFacturacion
        
        fields=[
            'cod_orden_fact',
            'fecha',
            'ruc_ci',
            'razon_nombres',
        ]
