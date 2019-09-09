from .models import ReporteContacto
import django_filters


class ReporteContactoFilter(django_filters.FilterSet):
    cod_reporte=django_filters.CharFilter(lookup_expr='icontains',label='Código de reporte')
    empresa=django_filters.CharFilter(lookup_expr='icontains',label='Empresa')
    b_fecha=django_filters.DateFromToRangeFilter(field_name='fecha', lookup_expr='year')
    class Meta:
        model = ReporteContacto
        
        fields=[
            'cod_reporte',
            'empresa',
            'canal_de_contacto',
            'fecha',
        ]

        
		