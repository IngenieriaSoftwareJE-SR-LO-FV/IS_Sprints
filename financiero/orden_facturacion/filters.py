from .models import OrdenFacturacion
from financiero.orden_facturacion.models import OrdenFacturacion, ESTADO_CHOICES
import django_filters
from django import forms


class OrdenFacturacionFilter(django_filters.FilterSet):
    cod_orden_fact = django_filters.CharFilter(lookup_expr='icontains', label="", widget=forms.TextInput(attrs={'placeholder':'Código orden'}))
    fecha=django_filters.DateFilter(field_name='fecha', label='',widget=forms.DateInput(attrs={'placeholder':'Fecha','type':'date'}))
    ruc_ci=django_filters.CharFilter(lookup_expr='icontains',label="", widget=forms.TextInput(attrs={'placeholder':'RUC o CI'}))
    razon_nombres=django_filters.CharFilter(lookup_expr='icontains',label="", widget=forms.TextInput(attrs={'placeholder':'Nombre Cliente'}))
    estado = django_filters.ChoiceFilter(
        empty_label='Estado',
		choices=ESTADO_CHOICES,
        label=""
    )
    n_tramite=django_filters.CharFilter(lookup_expr='icontains', label="", widget=forms.TextInput(attrs={'placeholder':'# Trámite'}))
    n_factura=django_filters.CharFilter(lookup_expr='icontains', label="", widget=forms.TextInput(attrs={'placeholder':'# Factura'}))
    class Meta:
        model = OrdenFacturacion
        
        fields=[
            'cod_orden_fact',
            'fecha',
            'ruc_ci',
            'razon_nombres',
            'estado',
            'n_tramite',
            'n_factura',
        ]
