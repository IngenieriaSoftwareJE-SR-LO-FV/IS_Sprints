from .models import PropuestaCorporativo
from ventas.personas_juridicas.models import Juridica
import django_filters
from django import forms


class PropuestaCorporativoFilter(django_filters.FilterSet):
    ESTADO_CHOICES= [('SG','Seguimiento'),('PD','Pendiente'),('ACP','Aceptada'),('NACP','No aceptada'),]
    """empresa_nombre=django_filters.CharFilter(lookup_expr='icontains',label='Empresa')"""
    empresa = django_filters.ModelChoiceFilter(label="", empty_label="Empresa", queryset=Juridica.objects.all())
    estado = django_filters.ChoiceFilter(label="", empty_label="Estado", choices=ESTADO_CHOICES)
    cod_propuesta = django_filters.CharFilter(lookup_expr='icontains', label='', widget=forms.TextInput(attrs={'placeholder': 'Código de Propuesta'}))
    class Meta:
        model = PropuestaCorporativo
        
        fields=[
            'empresa',
            'estado',
            'cod_propuesta',
        ]
