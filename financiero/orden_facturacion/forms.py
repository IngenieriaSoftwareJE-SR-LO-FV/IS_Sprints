from django import forms
from financiero.orden_facturacion.models import OrdenFacturacion
from datetime import date

TRUE_FALSE_CHOICES = [
	(True, 'Aceptado'),
	(False, 'Rechazado')
	]

class DateInput(forms.DateInput):
    input_type = 'date'

class OrdenFacturacionForm(forms.ModelForm):
    class Meta:
        model = OrdenFacturacion

        fields='__all__'

        labels={
            'tipo_cliente': 'Cliente',
            'n_tramite':'N° de trámite',
            'n_factura':'N° de factura',
            'anexo_factura':'Anexo de factura',
            'fecha':'Fecha',
            'ruc_ci':'RUC',
            'razon_nombres':'Razón social',
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
            'concepto':forms.Textarea(attrs={'rows':2}),
            'comentarios':forms.Textarea(attrs={'rows':2}),
            'fecha':forms.DateInput(attrs={'type':'date','value':date.today}),
            'razon_nombres':forms.Select(attrs={'class':'form-control select2'}),
            'ruc_ci':forms.Select(attrs={'class':'form-control select2'}),
            'participantes':forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
        }

class OrdenFacturacionUpdateForm(forms.ModelForm):
    class Meta:
        model = OrdenFacturacion

        fields='__all__'

        labels={
            'tipo_cliente': 'Cliente',
            'n_tramite':'N° de trámite',
            'n_factura':'N° de factura',
            'anexo_factura':'Anexo de factura',
            'fecha':'Fecha',
            'ruc_ci':'RUC',
            'razon_nombres':'Razón social',
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
            'cod_orden_fact':forms.HiddenInput(),
            'estado':forms.HiddenInput(),
            'tipo_cliente':forms.TextInput(attrs={'readonly':True, 'class':'form-control-plaintext'}),
            'contacto':forms.TextInput(attrs={'readonly':True, 'class':'form-control-plaintext'}),
            'direccion':forms.TextInput(attrs={'readonly':True,'class':'form-control-plaintext'}),
            'centro_costo':forms.TextInput(attrs={'readonly':True}),
            'valor_total':forms.TextInput(attrs={'readonly':True}),
            'telefono':forms.TextInput(attrs={'readonly':True}),
            'n_participantes':forms.TextInput(attrs={'readonly':True}),
            'valor':forms.TextInput(attrs={'readonly':True}),
            'observaciones':forms.Textarea(attrs={'rows':2,'readonly':True}),
            'concepto':forms.Textarea(attrs={'rows':2,'readonly':True}),
            'comentarios':forms.Textarea(attrs={'rows':2}),
            'n_tramite':forms.TextInput(attrs={'class':'form-control textinput textInput form-control'}),
            'n_factura':forms.TextInput(attrs={'class':'form-control textinput textInput form-control'}),
            'fecha':forms.TextInput(attrs={'readonly':True}),
            'razon_nombres':forms.TextInput(attrs={'readonly':True}),
            'ruc_ci':forms.TextInput(attrs={'readonly':True}),
            'participantes':forms.CheckboxSelectMultiple(attrs={'readonly':True,'class':'form-control'}),
        }
