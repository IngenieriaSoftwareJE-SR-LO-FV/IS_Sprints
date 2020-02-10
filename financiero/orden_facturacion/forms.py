from django import forms
from financiero.orden_facturacion.models import OrdenFacturacion, OrdenFacturacionParticipante
from datetime import date


class OrdenFacturacionForm(forms.ModelForm):
    class Meta:
        model = OrdenFacturacion

        fields = '__all__'

        labels = {
            'tipo_cliente': 'Cliente',
            'n_tramite': 'N° de trámite',
            'n_factura': 'N° de factura',
            'anexo_factura': 'Anexo de factura',
            'fecha': 'Fecha',
            'ruc_ci': 'RUC',
            'razon_nombres': 'Razón social',
            'concepto': 'Concepto',
            'centro_costos': 'Contro de costos',
            'n_participantes': '# de participantes',
            'valor_total': 'Valor total',
            'observaciones': 'Observaciones',
            'comentarios': 'Comentarios',
            'subtotal': 'Subtotal',
            'descuento_fact': '% Descuentos',
            'descuento_total': '$ Descuento total',
            'valor_total': '$ Valor total',
            "motivo_anular":"Motivo de Anulación",
        }

        widgets = {
            'cod_orden_fact': forms.HiddenInput(),
            'estado': forms.HiddenInput(),
            'observaciones': forms.Textarea(attrs={'rows': 2}),
            'concepto': forms.Textarea(attrs={'rows': 2}),
            'n_participantes': forms.HiddenInput(),
            'comentarios': forms.Textarea(attrs={'rows': 2}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'value': date.today, 'readonly': True}),
            'razon_nombres': forms.Select(attrs={'class': 'form-control select2'}),
            'ruc_ci': forms.Select(attrs={'class': 'form-control select2'}),
            'n_tramite': forms.TextInput(attrs={'class': 'form-control textinput textInput form-control'}),
            'n_factura': forms.TextInput(attrs={'class': 'form-control textinput textInput form-control'}),
            'subtotal': forms.HiddenInput(),#NumberInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'descuento_fact': forms.HiddenInput(),#NumberInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'descuento_total': forms.HiddenInput(),#NumberInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'valor_total': forms.HiddenInput(),#NumberInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            "motivo_anular":forms.Textarea(attrs={"class":"form-control", "rows":2}),
        }


class OrdenFacturacionUpdateForm(forms.ModelForm):
    class Meta:
        model = OrdenFacturacion

        fields = '__all__'

        labels = {
            'tipo_cliente': 'Cliente',
            'n_tramite': 'N° de trámite',
            'n_factura': 'N° de factura',
            'anexo_factura': 'Anexo de factura',
            'fecha': 'Fecha',
            'ruc_ci': 'RUC',
            'razon_nombres': 'Razón social',
            'concepto': 'Concepto',
            'centro_costos': 'Contro de costos',
            'n_participantes': '# de participantes',
            'valor_total': 'Valor total',
            'observaciones': 'Observaciones',
            'comentarios': 'Comentarios',
            'participantes': 'Participantes',
            'subtotal': 'Subtotal',
            'descuento_fact': '% Descuentos',
            'descuento_total': '$ Descuento total',
            'valor_total': '$ Valor total',
            "motivo_anular":"Motivo de Anulación",
        }


        widgets = {
            'cod_orden_fact': forms.HiddenInput(),
            'estado': forms.HiddenInput(),
            'tipo_cliente': forms.TextInput(attrs={'readonly': True, 'class': 'form-control-plaintext'}),
            'centro_costos': forms.Select(attrs={'disabled': True, 'class': 'form-control-plaintext'}),
            'valor_total': forms.TextInput(attrs={'readonly': True, 'class': 'form-control-plaintext'}),
            'n_participantes': forms.TextInput(attrs={'readonly': True, 'class': 'form-control-plaintext'}),
            'valor': forms.TextInput(attrs={'readonly': True, 'class': 'form-control-plaintext'}),
            'observaciones': forms.Textarea(attrs={'rows': 2, 'readonly': True, 'class': 'form-control-plaintext'}),
            'concepto': forms.Textarea(attrs={'rows': 2, 'readonly': True, 'class': 'form-control-plaintext'}),
            'comentarios': forms.Textarea(attrs={'rows': 2}),
            'n_tramite': forms.TextInput(attrs={'class': 'form-control textinput textInput'}),
            'n_factura': forms.TextInput(attrs={'class': 'form-control textinput textInput'}),
            'fecha': forms.DateInput(attrs={'readonly': True, 'class': 'form-control-plaintext'}),
            'razon_nombres': forms.TextInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'ruc_ci': forms.TextInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'subtotal': forms.HiddenInput(),#NumberInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'descuento_fact': forms.HiddenInput(),#NumberInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'descuento_total': forms.HiddenInput(),#NumberInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'valor_total': forms.HiddenInput(),#NumberInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            "valor_pendiente":forms.HiddenInput(),
            "motivo_anular":forms.Textarea(attrs={'readonly': True, "class":"form-control", "rows":2}),
        }


class OrdenFacturacionFinalForm(forms.ModelForm):
    class Meta:
        model = OrdenFacturacion

        fields = '__all__'

        labels = {
            'tipo_cliente': 'Cliente',
            'n_tramite': 'N° de trámite',
            'n_factura': 'N° de factura',
            'anexo_factura': 'Anexo de factura',
            'fecha': 'Fecha',
            'ruc_ci': 'RUC',
            'razon_nombres': 'Razón social',
            'concepto': 'Concepto',
            'centro_costo': 'Contro de costo',
            'n_participantes': '# de participantes',
            'valor_total': 'Valor total',
            'observaciones': 'Observaciones',
            'comentarios': 'Comentarios',
            'subtotal':'Subtotal',
            'descuento_fact':'% Descuentos',
            'descuento_total':'$ Descuento total',
            'valor_total':'$ Valor total',
            "motivo_anular":"Motivo de Anulación",
        }
        widgets = {
            'cod_orden_fact': forms.HiddenInput(),
            'estado': forms.HiddenInput(),
            'tipo_cliente': forms.TextInput(attrs={'readonly': True, 'class': 'form-control-plaintext'}),
            'centro_costos': forms.Select(attrs={'disabled': True, 'class': 'form-control-plaintext'}),
            'valor_total': forms.TextInput(attrs={'readonly': True, 'class': 'form-control-plaintext'}),
            'n_participantes': forms.TextInput(attrs={'readonly': True, 'class': 'form-control-plaintext'}),
            'valor': forms.TextInput(attrs={'readonly': True, 'class': 'form-control-plaintext'}),
            'observaciones': forms.Textarea(attrs={'rows': 2, 'readonly': True, 'class': 'form-control-plaintext'}),
            'concepto': forms.Textarea(attrs={'rows': 2, 'readonly': True, 'class': 'form-control-plaintext'}),
            'comentarios': forms.Textarea(attrs={'rows': 2}),
            'n_tramite': forms.TextInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'n_factura': forms.TextInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'fecha': forms.DateInput(attrs={'readonly': True, 'class': 'form-control-plaintext'}),
            'razon_nombres': forms.TextInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'ruc_ci': forms.TextInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'subtotal': forms.HiddenInput(),#NumberInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'descuento_fact': forms.HiddenInput(),#NumberInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'descuento_total': forms.HiddenInput(),#NumberInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            'valor_total': forms.HiddenInput(),#NumberInput(attrs={'readonly': True, 'class': 'form-control-plaintext form-control'}),
            "motivo_anular":forms.Textarea(attrs={"class":"form-control", "rows":2}),
        }


class OrdenFacturacionParticipanteForm(forms.ModelForm):
    class Meta:
        model = OrdenFacturacionParticipante
        fields = "__all__"
        labels = {
            "participante": "Participante",
            "nombre_evento": "Nombre del evento",
            "cod_evento": "Código del Evento",
            "valor_evento": "Valor del Evento ($)",
            "descuento": "Descuento (%)",
            "valor": "Valor a Pagar ($) ",
        }
        widgets = {
            "participante": forms.Select(attrs={'class': 'select2 form-control'}),
            "descuento": forms.NumberInput(attrs={'min': 0.0, 'max': 100.0}),
            "valor_evento": forms.NumberInput(attrs={'min': 0.0}),
            "valor": forms.NumberInput(attrs={'min': 0.0, 'max': 100.0, 'readonly': True}),
        }
