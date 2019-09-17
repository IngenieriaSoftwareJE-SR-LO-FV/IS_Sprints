from .models import Proforma
import django_filters
from django import forms


class ProformaFilter(django_filters.FilterSet):
    codigo=django_filters.CharFilter(lookup_expr='icontains',label='Código')
    nombreProforma=django_filters.CharFilter(lookup_expr='icontains',label='Nombre')
    fechaSolicitud=django_filters.DateFilter(field_name='fechaSolicitud', label='Fecha Solicitud',widget=forms.DateInput(attrs={"type":"date"}))
    fechaEnvio=django_filters.DateFilter(field_name='fechaEnvio',label='Fecha Envío', widget=forms.DateInput(attrs={"type":"date"}))
    estado=django_filters.CharFilter(field_name='estado', lookup_expr='iexact',label='Estado')
    class Meta:
        model = Proforma
        
        fields=[
            'codigo',
            'nombreProforma',
            'fechaSolicitud',
            'fechaEnvio',
            'estado',
        ]
