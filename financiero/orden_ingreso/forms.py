from django import forms
from .models import OrdenIngreso
from datetime import date

class OrdenIngresoForm(forms.ModelForm):

	class Meta:
		model=OrdenIngreso
		fields='__all__'

		labels={
			'tipo_cliente':'Cliente',
			'fecha':'Fecha',
			'ruc_ci':'RUC',
			'razon_nombres':'Razón Social',
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
			'fecha':forms.DateInput(attrs={'class':'form-control','type':'date','value':date.today}),
			'fechaPago':forms.DateInput(attrs={'class':'form-control','type':'date','value':date.today}),
			'razon_nombres':forms.Select(attrs={'class':'form-control select2'}),
            'ruc_ci':forms.Select(attrs={'class':'form-control select2'}),
			'descripcion':forms.Textarea(attrs={'rows':2}),
			'valor':forms.NumberInput(attrs={'class':'form-control'}),
			'anexo':forms.ClearableFileInput(attrs={'class':'form-control'}),
			'numeroDocumento':forms.NumberInput(attrs={'class':'form-control'}),
			'banco':forms.TextInput(attrs={'class':'form-control'}),
			'emisoraTarjeta':forms.Select(attrs={'class':'select form-control'}),
			'formaPago':forms.Select(attrs={'id':'seleccion',"onchange":"run()"})
			}
	def clean(self):
		
		cd = self.cleaned_data
		if(cd.get('valor')==None):
			self.add_error('valor', 'Valor excede máxima cantidad soportada')
		elif ((cd.get('orden_facturacion').valor_pendiente - cd.get('valor')) <0) :
			self.add_error('valor', 'El valor a pagar excede el valor pendiente de la orden de facturación, pendiente: $'+str(cd.get('orden_facturacion').valor_pendiente))
		return cd


class OrdenIngresoUpdateForm(forms.ModelForm):

	class Meta:
		model=OrdenIngreso
		fields='__all__'

		labels={
			'cod_orden_ing': 'Código Orden Ingreso',
			'tipo_cliente':'Cliente',
			'fecha':'Fecha',
			'n_tramite':'N° de Trámite',
			'ruc_ci':'RUC',
			'razon_nombres':'Razón Social',
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
			'cod_orden_ing':forms.TextInput(attrs={'readonly':True,'class':'form-control-plaintext'}),
			'fecha':forms.DateInput(attrs={'readonly':True,'class':'form-control-plaintext','type':'date','value':date.today}),
			'fechaPago':forms.DateInput(attrs={'readonly':True,'class':'form-control-plaintext','type':'date','value':date.today}),
			'n_tramite':forms.TextInput(attrs={'class':'form-control'}),
			'tipo_cliente':forms.TextInput(attrs={'readonly':True,'class':'form-control-plaintext'}),
			'razon_nombres':forms.TextInput(attrs={'readonly':True,'class':'form-control-plaintext form-control'}),
            'ruc_ci':forms.TextInput(attrs={'readonly':True,'class':'form-control-plaintext form-control'}),
			'descripcion':forms.Textarea(attrs={'readonly':True,'rows':2,'class':'form-control-plaintext'}),
			'valor':forms.NumberInput(attrs={'readonly':True,'class':'form-control-plaintext'}),
			'anexo':forms.ClearableFileInput(attrs={'class':'form-control'}),
			'numeroDocumento':forms.NumberInput(attrs={'readonly':True,'class':'form-control-plaintext form-control'}),
			'banco':forms.TextInput(attrs={'readonly':True,'class':'form-control-plaintext'}),
			'emisoraTarjeta':forms.TextInput(attrs={'readonly':True,'class':'select form-control-plaintext textinput textInput form-control'}),
			'formaPago':forms.TextInput(attrs={'readonly':True,'id':'seleccion'}),
			'orden_facturacion':forms.TextInput(attrs={'readonly':True,'class':'form-control-plaintext'})
		}
class OrdenIngresoPrintForm(forms.ModelForm):

	class Meta:
		model=OrdenIngreso
		fields='__all__'

		labels={
			'cod_orden_ing': 'Código',
			'tipo_cliente':'Cliente',
			'fecha':'Fecha',
			'n_tramite':'N° de Trámite',
			'ruc_ci':'RUC',
			'razon_nombres':'Razón Social',
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
			'cod_orden_ing':forms.TextInput(attrs={'readonly':True,'class':'form-control-plaintext'}),
			'fecha':forms.DateInput(attrs={'readonly':True,'class':'form-control-plaintext','type':'date','value':date.today}),
			'fechaPago':forms.DateInput(attrs={'readonly':True,'class':'form-control-plaintext','type':'date','value':date.today}),
			'n_tramite':forms.TextInput(attrs={'readonly':True, 'class':'form-control'}),
			'tipo_cliente':forms.TextInput(attrs={'readonly':True,'class':'form-control-plaintext'}),
			'razon_nombres':forms.TextInput(attrs={'readonly':True,'class':'form-control-plaintext form-control'}),
            'ruc_ci':forms.TextInput(attrs={'readonly':True,'class':'form-control-plaintext form-control'}),
			'descripcion':forms.Textarea(attrs={'readonly':True,'rows':2,'class':'form-control-plaintext'}),
			'valor':forms.NumberInput(attrs={'readonly':True,'class':'form-control-plaintext'}),
			'anexo':forms.ClearableFileInput(attrs={'class':'form-control'}),
			'numeroDocumento':forms.NumberInput(attrs={'readonly':True,'class':'form-control-plaintext form-control'}),
			'banco':forms.TextInput(attrs={'readonly':True,'class':'form-control-plaintext'}),
			'emisoraTarjeta':forms.TextInput(attrs={'readonly':True,'class':'select form-control-plaintext textinput textInput form-control'}),
			'formaPago':forms.TextInput(attrs={'readonly':True,'id':'seleccion'})
		}

