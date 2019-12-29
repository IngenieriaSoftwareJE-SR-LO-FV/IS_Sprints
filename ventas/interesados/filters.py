from .models import *
import django_filters
from django import forms

class InteresadoFilter(django_filters.FilterSet):
    
    nombre = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Nombre'}),label="")
    apellido = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Apellido'}),label="")
    celular = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Celular'}),label="")
    correo = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Correo'}),label="")
    canal_de_contacto = django_filters.ModelChoiceFilter(queryset=CanalContacto.objects.all(),label="",empty_label="Selecionar canal de contacto")
    class Meta:
        model = Interesado
        
        fields="__all__"
