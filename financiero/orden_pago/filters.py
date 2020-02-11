from .models import OrdenPago
import django_filters
from django import forms

class OrdenPagoFilter(django_filters.FilterSet):
	ESTADO_CHOICES = [("GRBD","Grabado"),("ENVD","Enviado"),("AUTR","Autorizado"),("ANLD","Anulado"),("PGDO","Pagado")]

	cod_ord_pago = django_filters.CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Código orden pago'}))
	estado = django_filters.ChoiceFilter(label="", empty_label='Estado', choices=ESTADO_CHOICES)
	fecha = django_filters.DateFilter(label="", widget=forms.DateInput(attrs={'placeholder':'Fecha: dd-mm-aaaa','type':'date'}))
	proveedor = django_filters.CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Razón social/Nombre del proveedor'}))
	#Falta agregar filtro por codigo de evento

	class Meta:
		model = OrdenPago
		fields = ["cod_ord_pago", "estado", "fecha", "proveedor",]	