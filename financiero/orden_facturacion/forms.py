from django import forms
from financiero.orden_facturacion.models import OrdenFacturacion
from datetime import date
from dal import autocomplete


class DateInput(forms.DateInput):
    input_type = 'date'

class OrdenFacturacionForm(forms.ModelForm):
    class Meta:
        model = OrdenFacturacion

        fields=[
            'n_tramite',
            'n_factura',
            'anexo_factura',
            'fecha',
            'ruc_ci',
            'razon_nombres',
            'contacto',
            'direccion',
            'telefono',
            'concepto',
            'centro_costo',
            'n_participantes',
            'valor_total',
            'observaciones',
            'comentarios',
            'participantes',
        ]

        labels={
            'n_tramite':'N° de trámite',
            'n_factura':'N° de factura',
            'anexo_factura':'Anexo de factura',
            'fecha':'Fecha',
            'ruc_ci':'RUC',
            'razon_nombres':'Razon social',
            'contacto':'Contacto',
            'direccion':'Dirección',
            'telefono':'Teléfono',
            'concepto':'Concepto',
            'centro_costo':'Contro de costo',
            'n_participantes':'# de participantes',
            'valor_total':'Valor total',
            'observaciones':'Observaciones',
            'comentarios':'Comentarios',
            'participantes':'Participantes',
        }

        widgets={
            'observaciones':forms.Textarea(attrs={'rows':2}),
            'n_tramite':forms.NumberInput(attrs={'min':0}),
            'n_factura':forms.NumberInput(attrs={'min':0}),
            'fecha':forms.DateInput(attrs={'type':'date','value':date.today}),
            'razon_nombres':forms.Select(attrs={'class':'form-control select2'}),
            'ruc_ci':forms.Select(attrs={'class':'form-control select2'})
        }
