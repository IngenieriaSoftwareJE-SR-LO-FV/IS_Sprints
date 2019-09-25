from .models import OrdenIngreso
import django_filters
from django import forms

TRUE_FALSE_CHOICES = [
    (True, 'Aprobado'),
    (False, 'Rechazado')
]

class OrdenIngresoFilter(django_filters.FilterSet):
    fecha=django_filters.DateFilter(field_name='fecha', label='Fecha',
        widget=forms.DateInput(attrs={"type":"date"}))
    numeroTramite=django_filters.CharFilter(lookup_expr='icontains',label='Número de Trámite')
    numeroFactura=django_filters.CharFilter(lookup_expr='icontains',label='Número de Factura')
    estado = django_filters.ChoiceFilter(null_label="Pendiente",empty_label="-------",choices=TRUE_FALSE_CHOICES)
    class Meta:
        model = OrdenIngreso
        
        fields=[
            'fecha',
            'numeroTramite',
            'numeroFactura',
            'estado',
        ]
