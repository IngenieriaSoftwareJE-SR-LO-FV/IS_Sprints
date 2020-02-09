from .models import OrdenIngreso
import django_filters
from django import forms



class OrdenIngresoFilter(django_filters.FilterSet):
    fecha=django_filters.DateFilter(field_name='fecha', label='Fecha',
        widget=forms.DateInput(attrs={"type":"date"}))
    numeroTramite=django_filters.CharFilter(lookup_expr='icontains',label='Número de Trámite')
    numeroFactura=django_filters.CharFilter(lookup_expr='icontains',label='Número de Factura')
    class Meta:
        model = OrdenIngreso
        
        fields=[
            'fecha',
            'n_tramite',
            'numeroFactura',
        ]
