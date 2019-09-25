from django import forms
from .models import OrdenIngreso

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
		fields=[
			'fecha',
			'numeroTramite',
			'numeroFactura',
			'identificacion',
			'razonSocial',
			'centroCosto',
			'descripcion',
			'formaPago',
			'valor',
			'anexo',
			'estado',
			'fechaPago',
			'numeroDocumento',
			'banco',
			'emisoraTarjeta',
		]

		labels={
			'fecha':'Fecha',
			'numeroTramite':'N° de Trámite',
			'numeroFactura':'No. Factura',
			'identificacion':'Identificación',
			'razonSocial':'Razón Social',
			'centroCosto':'Centro Costo',
			'descripcion':'Descripción',
			'formaPago':'Forma de Pago',
			'valor':'Valor',
			'anexo':'Anexo',
			'estado':"Estado",
			'fechaPago':'Fecha Pago',
			'numeroDocumento':'N° Documento',
			'banco':"Banco",
			'emisoraTarjeta':"Emisora TC",
		}

		widgets={
			'fecha':forms.DateInput(attrs={'class':'form-control','type':'date'}),
			'fechaPago':forms.DateInput(attrs={'class':'form-control','type':'date'}),
			'numeroTramite':forms.NumberInput(attrs={'class':'form-control'}),
			'numeroFactura':forms.NumberInput(attrs={'class':'form-control'}),
			'identificacion':forms.TextInput(attrs={'class':'form-control','type':'number'}),
			'razonSocial':forms.TextInput(attrs={'class':'form-control'}),
			'centroCosto':forms.TextInput(attrs={'class':'form-control'}),
			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
			'valor':forms.NumberInput(attrs={'class':'form-control'}),
			'anexo':forms.ClearableFileInput(attrs={'class':'form-control'}),
			'numeroDocumento':forms.NumberInput(attrs={'class':'form-control'}),
			'banco':forms.TextInput(attrs={'class':'form-control'}),
			'emisoraTarjeta':forms.Select(attrs={'class':'form-control'}),
			'formaPago':forms.Select(attrs={'class':'form-control'})
		}