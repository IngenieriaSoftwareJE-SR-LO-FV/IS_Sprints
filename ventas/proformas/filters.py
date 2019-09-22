from .models import Proforma
import django_filters
from django import forms


class ProformaFilter(django_filters.FilterSet):
    "quité type:date de ambos campos de fecha"
    ESTADO_CHOICES= [("Aceptada","Aceptada"),("No aceptada","No aceptada"), ("Seguimiento","Seguimiento") ,("Por Enviar","Por Enviar")]
    codigo=django_filters.CharFilter(lookup_expr='icontains',label='', widget=forms.TextInput(attrs={'placeholder': 'Código'}))
    nombreProforma=django_filters.CharFilter(lookup_expr='icontains',label='', widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    fechaSolicitud=django_filters.DateFilter(field_name='fechaSolicitud', label='', widget=forms.DateInput(attrs={'placeholder':'Fecha Solicitud: dd-mm-aaaa'}))
    fechaEnvio=django_filters.DateFilter(field_name='fechaEnvio',label='', widget=forms.DateInput(attrs={'placeholder':'Fecha Envío: dd-mm-aaaa'}))
    estado=django_filters.ChoiceFilter(label="", empty_label="Estado", choices=ESTADO_CHOICES)
    class Meta:
        model = Proforma
        
        fields=[
            'codigo',
            'nombreProforma',
            'fechaSolicitud',
            'fechaEnvio',
            'estado',
        ]

