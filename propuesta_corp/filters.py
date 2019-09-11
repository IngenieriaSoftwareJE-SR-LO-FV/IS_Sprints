from .models import PropuestaCorporativo
import django_filters


class PropuestaCorporativoFilter(django_filters.FilterSet):
    empresa_nombre=django_filters.CharFilter(lookup_expr='icontains',label='Empresa')
    estado=django_filters.CharFilter(lookup_expr='icontains',label='Estado')
    cod_propuesta=django_filters.CharFilter(lookup_expr='icontains',label='Código de Propuesta')
    class Meta:
        model = PropuestaCorporativo
        
        fields=[
            'empresa',
            'estado',
            'cod_propuesta',
        ]
