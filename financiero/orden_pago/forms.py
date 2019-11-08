from django import forms
from financiero.orden_pago.models import OrdenPago
from datetime import date

class OrdenPagoForm(forms.ModelForm):
	class Meta:
		model = OrdenPago

		fields = "__all__"

		labels = {
			"cod_ord_pago":"Código",
			"fecha":"Fecha elaboracón",
			"estado":"Estado",
			"tipo_proveedor":"Tipo de proovedor",
			"proveedor":"Razón social/Nombre",
			"centro_costos":"Centro de costos",
			"egreso":"Egreso",
			"tipo_comprobante":"tipo de comprobante",
			"n_comprobante":"N° documento",
			"concepto":"Concepto",
			"forma_pago":"Forma de pago",
			"observacion":"Observación",
			"anexo":"Anexos",
		}

		widgets = {
			"cod_ord_pago":forms.TextInput(attrs={'class':'form-control'}),
			"fecha":forms.DateInput(attrs={'class':'form-control',"type":"date", "value":date.today}),
			"estado":forms.Select(attrs={"class":"form-control"}),
			"tipo_proveedor":forms.Select(attrs={"class":"form-control"}),
			"proveedor":forms.Select(attrs={"class":"form-control"}),
			"centro_costos":forms.Select(attrs={"class":"form-control"}),
			"egreso":forms.Select(attrs={"class":"form-control"}),
			"tipo_comprobante":forms.Select(attrs={"class":"form-control"}),
			"n_comprobante":forms.TextInput(attrs={"class":"form-control"}),
			"concepto":forms.Textarea(attrs={"class":"form-control", "rows":2}),
			"forma_pago":forms.Select(attrs={"class":"form-control"}),
			"observacion":forms.Textarea(attrs={"class":"form-control", "rows":2}),
			"anexo":forms.ClearableFileInput(attrs={"class":"form-control"}),
		}


class OrdenPagoFinalForm(forms.ModelForm):
	class Meta:
		model = OrdenPago

		fields = "__all__"

		labels = {
			"cod_ord_pago":"Código",
			"fecha":"Fecha elaboracón",
			"estado":"Estado",
			"tipo_proveedor":"Tipo de proovedor",
			"proveedor":"Razón social/Nombre",
			"centro_costos":"Centro de costos",
			"egreso":"Egreso",
			"tipo_comprobante":"tipo de comprobante",
			"n_comprobante":"N° documento",
			"concepto":"Concepto",
			"forma_pago":"Forma de pago",
			"observacion":"Observación",
			"anexo":"Anexos",
		}

		widgets = {
			"cod_ord_pago":forms.TextInput(attrs={"readonly":True, "class":"form-control"}),
			"fecha":forms.DateInput(attrs={"readonly":True, "class":"form-control","type":"date", "value":date.today}),
			"estado":forms.Select(attrs={"readonly":True, "class":"form-control"}),
			"tipo_proveedor":forms.Select(attrs={"readonly":True, "class":"form-control"}),
			"proveedor":forms.Select(attrs={"readonly":True, "class":"form-control"}),
			"centro_costos":forms.Select(attrs={"readonly":True, "class":"form-control"}),
			"egreso":forms.Select(attrs={"readonly":True, "class":"form-control"}),
			"tipo_comprobante":forms.Select(attrs={"readonly":True, "class":"form-control"}),
			"n_comprobante":forms.TextInput(attrs={"readonly":True, "class":"form-control"}),
			"concepto":forms.Textarea(attrs={"readonly":True, "class":"form-control", "rows":2}),
			"forma_pago":forms.Select(attrs={"readonly":True, "class":"form-control"}),
			"observacion":forms.Textarea(attrs={"readonly":True, "class":"form-control", "rows":2}),
			"anexo":forms.ClearableFileInput(attrs={"readonly":True, "class":"form-control"}),
		}
