from .models import ReporteContacto
import django_filters


class ReporteContactoFilter(django_filters.FilterSet):
    empresa=django_filters.CharFilter(lookup_expr='icontains',label='Empresa')
    b_fecha=django_filters.DateFromToRangeFilter(field_name='fecha', lookup_expr='year')
    class Meta:
        model = ReporteContacto
        
        fields=[
            'empresa',
            'canal_de_contacto',
            'fecha',
        ]

        
		