from django import forms
from .models import *


"""class CambiarEventoForm(forms.Form):
	pass"""


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