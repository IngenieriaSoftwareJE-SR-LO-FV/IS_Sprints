from ventas.reporte_contacto.models import ReporteContacto
import django_filters
from django import forms


class ReporteContactoFilter(django_filters.FilterSet):
    id=django_filters.CharFilter(lookup_expr='icontains',label='Código de reporte')
    empresa_nombre=django_filters.CharFilter(lookup_expr='icontains',label='Empresa')
    fecha=django_filters.DateFilter(field_name='fecha', widget=forms.DateInput(attrs={"type":"date"}))

    class Meta:
        model = ReporteContacto
        
        fields=[
            'id',
            'empresa',
            'canal_de_contacto',
            'fecha',
        ]

        
		