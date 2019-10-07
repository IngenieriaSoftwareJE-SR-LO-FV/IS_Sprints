from django import forms
from .models import OrdenIngreso
from datetime import date

class OrdenIngresoForm(forms.ModelForm):
	
	def clean(self):
	    forma = self.cleaned_data.get('formaPago')

	    if forma=="tarjeta":
	        msg = forms.ValidationError("Este campo es requerido.")
	        self.add_error('emisoraTarjeta', msg)
	    else:
	        # Keep the database consistent. The user may have
	        # submitted a shipping_destination even if shipping
	        # was not selected
	        self.cleaned_data['emisoraTarjeta'] = ''

	    return self.cleaned_data

	class Meta:
		model=OrdenIngreso
		fields='__all__'

		labels={
			'tipo_cliente':'Cliente',
			'fecha':'Fecha',
			'numeroTramite':'N° de Trámite',
			'numeroFactura':'No. Factura',
			'ruc_ci':'RUC',
			'razon_nombres':'Razón Social',
			'centroCosto':'Centro Costo',
			'descripcion':'Descripción',
			'formaPago':'Forma de Pago',
			'valor':'Valor',
			'anexo':'Anexo Comprobante de Pago',
			'fechaPago':'Fecha Pago',
			'numeroDocumento':'N° Documento',
			'banco':"Banco",
			'emisoraTarjeta':"Emisora TC",
		}

		widgets={
			'cod_orden_fact':forms.HiddenInput(),
            'estado':forms.HiddenInput(),
			'fecha':forms.DateInput(attrs={'class':'form-control','type':'date','value':date.today}),
			'fechaPago':forms.DateInput(attrs={'class':'form-control','type':'date','value':date.today}),
			'numeroTramite':forms.NumberInput(attrs={'class':'form-control'}),
			'numeroFactura':forms.NumberInput(attrs={'class':'form-control'}),
			'razon_nombres':forms.Select(attrs={'class':'form-control select2'}),
            'ruc_ci':forms.Select(attrs={'class':'form-control select2'}),
			'centroCosto':forms.TextInput(attrs={'class':'form-control'}),
			'descripcion':forms.Textarea(attrs={'rows':2}),
			'valor':forms.NumberInput(attrs={'class':'form-control'}),
			'anexo':forms.ClearableFileInput(attrs={'class':'form-control'}),
			'numeroDocumento':forms.NumberInput(attrs={'class':'form-control'}),
			'banco':forms.TextInput(attrs={'class':'form-control'}),
			'emisoraTarjeta':forms.Select(attrs={'class':'form-control'}),
			'formaPago':forms.Select(attrs={'class':'form-control'})
		}