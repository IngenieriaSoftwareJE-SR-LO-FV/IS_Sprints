from django import forms
from .models import *

ESTADO_CHOICES = [  
		('SLCE','Solicitud Enviada'),
		('ACPF', 'Autorizada por Financiero'),
		('CNCL','Cancelada'),
		('ANLD','Anulada'),
	]


class CambiarEventoForm(forms.ModelForm):
	class Meta:
		model = CambioEvento

		fields = '__all__'
		labels = {
			"evento_origen":"Evento origen",
			"evento_destino" : "Evento destino",
			"participante" : "Participante",
		}
		widgets = {
			"participante" : forms.Select(attrs={'class':'form-control select2'}),
			"evento_origen" : forms.Select(attrs={'class':'form-control select2'}),
			"evento_destino" : forms.Select(attrs={'class':'form-control select2'}),
		}

		


class NotaCreditoForm(forms.ModelForm):
	class Meta:
		model = NotaCredito

		fields = "__all__"

		labels = {
			"cod_nota_cred":"Código",
			"motivo":"Motivo",
			"concepto":"Concepto",
			"estado":"Estado",
			"documento":"Tipo Documento",
			"n_documento":"N° Documento",
			"evento":"Evento",
			"valor_evento":"Valor del evento",
			"descuento":"% de Descuento",
			"valor_pagar":"Valor a pagar",
			"anexo":"Anexo",
		}

		widgets = {
			"concepto":forms.Textarea(attrs={"class":"form-control", "rows":2}),
		}

