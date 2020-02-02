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

		