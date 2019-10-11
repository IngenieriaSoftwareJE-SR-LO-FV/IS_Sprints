from ventas.reporte_contacto.models import ReporteContacto
from ventas.personas_juridicas.models import Juridica
import django_filters
from django import forms


class ReporteContactoFilter(django_filters.FilterSet):
    cod_reporte = django_filters.CharFilter(lookup_expr='icontains', label='', widget=forms.TextInput(attrs={'placeholder': 'Código de reporte'}))
    """empresa_nombre=django_filters.CharFilter(lookup_expr='icontains',label='Empresa')"""
    empresa = django_filters.ModelChoiceFilter(label="", empty_label="Empresa", queryset=Juridica.objects.all())
    canal_de_contacto = django_filters.CharFilter(label='', widget=forms.TextInput(attrs={'placeholder': 'Canal de contacto'}))
    fecha=django_filters.DateFilter(field_name='fecha', label='',widget=forms.DateInput(attrs={'placeholder':'Fecha','type':'date'}))

    class Meta:
        model = ReporteContacto
        
        fields=[
            'cod_reporte',
            'empresa',
            'canal_de_contacto',
            'fecha',
        ]

        
		