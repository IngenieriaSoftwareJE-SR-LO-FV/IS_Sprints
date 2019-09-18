from django import forms
from .models import OrdenIngreso

class OrdenIngresoForm(forms.ModelForm):
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
			'valor',
			'anexo',
		]

		labels={
			'fecha':'Fecha',
			'numeroTramite':'N° de Trámite',
			'numeroFactura':'No. Factura',
			'identificacion':'Identificación',
			'razonSocial':'Razón Social',
			'centroCosto':'Centro Costo',
			'descripcion':'Descripción',
			'valor':'Valor',
			'anexo':'Anexo',
		}

		widgets={
			'fecha':forms.DateInput(attrs={'class':'form-control','type':'date'}),
			'numeroTramite':forms.NumberInput(attrs={'class':'form-control'}),
			'numeroFactura':forms.NumberInput(attrs={'class':'form-control'}),
			'identificacion':forms.TextInput(attrs={'class':'form-control','type':'number'}),
			'razonSocial':forms.TextInput(attrs={'class':'form-control'}),
			'centroCosto':forms.TextInput(attrs={'class':'form-control'}),
			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
			'valor':forms.NumberInput(attrs={'class':'form-control'}),
			'anexo':forms.ClearableFileInput(attrs={'class':'form-control'}),
		}