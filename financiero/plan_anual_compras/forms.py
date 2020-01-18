from django import forms
from .models import PlanAnualCompras, Partida
from datetime import date

class PlanAnualComprasForm(forms.ModelForm):
	class Meta:
		model = PlanAnualCompras
		fields = '__all__'

		widgets = {
			"fecha":forms.DateInput(attrs={'class':'form-control',"type":"date", "value":date.today})
		}


class PartidaForm(forms.ModelForm):
	class Meta:
		model = Partida
		fields = '__all__'

		labes = {
			"codigo":"Código",
			"año":"Año",
			"centro_costos":"Centro de Costos",
			"partida":"Partida Presupuestaria",
			"tipo_compra":"Tipo de Compra",
			"producto":"Producto/Servicio",
			"cantidad_anual":"Cantidad Anual",
			"unidad_medida":"Unidad de medida",
			"costo_unitario":"Costo Unitario",
			"subtotal":"Subtotal",
			"total":"Valor total",
		}

