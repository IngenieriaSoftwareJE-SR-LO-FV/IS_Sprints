from financiero.orden_facturacion.models import OrdenFacturacion
from financiero.orden_ingreso.models import OrdenIngreso
import django_filters
from django import forms
from django.http import QueryDict
TRUE_FALSE_CHOICES = [
    (True, 'Aprobado'),
    (False, 'Rechazado')
]

class PagoEventosFilter(django_filters.FilterSet):
    cod_orden_fact = django_filters.CharFilter(lookup_expr='icontains', label="", widget=forms.TextInput(attrs={'placeholder':'Código orden'}))
    fecha=django_filters.DateFilter(field_name='fecha', label='',widget=forms.DateInput(attrs={'placeholder':'Fecha','type':'date'}))
    ruc_ci=django_filters.CharFilter(lookup_expr='icontains',label="", widget=forms.TextInput(attrs={'placeholder':'RUC o CI'}))
    razon_nombres=django_filters.CharFilter(lookup_expr='icontains',label="", widget=forms.TextInput(attrs={'placeholder':'Nombre Cliente'}))

    valor_pendiente = django_filters.NumberFilter(lookup_expr="gt")

    class Meta:
        model = OrdenFacturacion
        fields=[
            'cod_orden_fact',
            'fecha',
            'ruc_ci',
            'razon_nombres',
        ]
    def __init__(self, data=None, *args, **kwargs):
        # if filterset is bound, use initial values as defaults
        if data is not None:
            # get a mutable copy of the QueryDict
            data = data.copy()
            data["valor_pendiente"] = 0
        else:
            data = QueryDict('cod_orden_fact=&fecha=&ruc_ci=&razon_nombres=').copy()
            data["valor_pendiente"] = 0
        super().__init__(data, *args, **kwargs)
        #print(self.form.fields['valor_pendiente'])
    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        #self.form.fields['valor_pendiente'].value = 0
