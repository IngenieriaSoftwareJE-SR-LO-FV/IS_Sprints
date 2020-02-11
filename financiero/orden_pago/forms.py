from django import forms
from financiero.orden_pago.models import OrdenPago, Centro_Costos, Egresos
from datetime import date

class OrdenPagoForm(forms.ModelForm):
	class Meta:
		model = OrdenPago

		fields = {
			"cod_ord_pago",
			"fecha",
			"estado",
			"tipo_proveedor",
			"proveedor",
			"centro_costos",
			"egreso",
			"tipo_comprobante",
			"n_comprobante",
			"concepto",
			"forma_pago",
			"observacion",
			"motivo_anular",
		}

		labels = {
			"cod_ord_pago":"Código",
			"fecha":"Fecha elaboración",
			"estado":"Estado",
			"tipo_proveedor":"Tipo de proveedor",
			"proveedor":"Razón social/Nombre",
			"centro_costos":"Centro de costos",
			"egreso":"Egreso",
			"tipo_comprobante":"Tipo de comprobante",
			"n_comprobante":"N° documento",
			"concepto":"Concepto",
			"forma_pago":"Forma de pago",
			"observacion":"Observaciones",
			"motivo_anular":"Motivo de Anulación",
		}

		widgets = {
			"cod_ord_pago":forms.TextInput(attrs={'class':'form-control'}),
			"fecha":forms.DateInput(attrs={"readonly":True,'class':'form-control',"type":"date", "value":date.today}),
			"estado":forms.Select(attrs={"class":"select form-control"}),
			"tipo_proveedor":forms.Select(attrs={"class":"form-control select2"}),
			"proveedor":forms.Select(attrs={"class":"form-control select2"}),
			"centro_costos":forms.Select(attrs={"class":"select form-control"}),
			"egreso":forms.Select(attrs={"class":"select form-control"}),
			"tipo_comprobante":forms.Select(attrs={"class":"select form-control"}),
			"n_comprobante":forms.TextInput(attrs={"class":"form-control"}),
			"concepto":forms.Textarea(attrs={"class":"form-control", "rows":2}),
			"forma_pago":forms.Select(attrs={"class":"select form-control"}),
			"observacion":forms.Textarea(attrs={"class":"form-control", "rows":2}),
			"motivo_anular":forms.Textarea(attrs={"class":"form-control", "rows":2}),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["centro_costos"].required = True
		self.fields["egreso"].required = True
		self.fields["n_comprobante"].required=True		
		self.fields["egreso"].queryset = Egresos.objects.none()
		if "centro_costos" in self.data:
			try:
				centros_id = int(self.data.get("centro_costos"))
				self.fields["egreso"].queryset = Egresos.objects.filter(centroc=centros_id).order_by("nombre")
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields["egreso"].queryset = self.instance.centro_costos.egresos_set.order_by("nombre") 


class OrdenPagoEditarFirstForm(forms.ModelForm):
	class Meta:
		model = OrdenPago

		fields = {
			"cod_ord_pago",
			"fecha",
			"estado",
			"tipo_proveedor",
			"proveedor",
			"centro_costos",
			"egreso",
			"tipo_comprobante",
			"n_comprobante",
			"concepto",
			"forma_pago",
			"observacion",
			"motivo_anular",
			"documentos",
		}

		labels = {
			"cod_ord_pago":"Código",
			"fecha":"Fecha elaboración",
			"estado":"Estado",
			"tipo_proveedor":"Tipo de proveedor",
			"proveedor":"Razón social/Nombre",
			"centro_costos":"Centro de costos",
			"egreso":"Egreso",
			"tipo_comprobante":"Tipo de comprobante",
			"n_comprobante":"N° documento",
			"concepto":"Concepto",
			"forma_pago":"Forma de pago",
			"observacion":"Observaciones",
			"motivo_anular":"Motivo de Anulación",
			"documentos":"Documentos",
		}

		widgets = {
			"cod_ord_pago":forms.TextInput(attrs={'class':'form-control'}),
			"fecha":forms.DateInput(attrs={"readonly":True,'class':'form-control',"type":"date", "value":date.today}),
			"estado":forms.Select(attrs={"class":"select form-control"}),
			"tipo_proveedor":forms.Select(attrs={"class":"form-control select2"}),
			"proveedor":forms.Select(attrs={"class":"form-control select2"}),
			"centro_costos":forms.Select(attrs={"class":"select form-control"}),
			"egreso":forms.Select(attrs={"class":"select form-control"}),
			"tipo_comprobante":forms.Select(attrs={"class":"select form-control"}),
			"n_comprobante":forms.TextInput(attrs={"class":"form-control"}),
			"concepto":forms.Textarea(attrs={"class":"form-control", "rows":2}),
			"forma_pago":forms.Select(attrs={"class":"select form-control"}),
			"observacion":forms.Textarea(attrs={"class":"form-control", "rows":2}),
			"motivo_anular":forms.Textarea(attrs={"class":"form-control", "rows":2}),
			"documentos":forms.Textarea(attrs={"class":"form-control", "rows":2}),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["centro_costos"].required = True
		self.fields["egreso"].required = True
		self.fields["n_comprobante"].required=True		
		self.fields["egreso"].queryset = Egresos.objects.none()
		if "centro_costos" in self.data:
			try:
				centros_id = int(self.data.get("centro_costos"))
				self.fields["egreso"].queryset = Egresos.objects.filter(centroc=centros_id).order_by("nombre")
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields["egreso"].queryset = self.instance.centro_costos.egresos_set.order_by("nombre") 



class OrdenPagoEditarSecondForm(forms.ModelForm):
	class Meta:
		model = OrdenPago

		fields = {
			"cod_ord_pago",
			"fecha",
			"estado",
			"tipo_proveedor",
			"proveedor",
			"centro_costos",
			"egreso",
			"tipo_comprobante",
			"n_comprobante",
			"concepto",
			"forma_pago",
			"observacion",
			"motivo_anular",
			"documentos",
		}

		labels = {
			"cod_ord_pago":"Código",
			"fecha":"Fecha Elaboración",
			"estado":"Estado",
			"tipo_proveedor":"Tipo de provedor",
			"proveedor":"Razón social/Nombre",
			"centro_costos":"Centro de costos",
			"egreso":"Egreso",
			"tipo_comprobante":"tipo de comprobante",
			"n_comprobante":"N° documento",
			"concepto":"Concepto",
			"forma_pago":"Forma de pago",
			"observacion":"Observaciones",
			"motivo_anular":"Motivo de Anulación",
			"documentos":"Documentos",

		}

		widgets = {
			"cod_ord_pago":forms.TextInput(attrs={"readonly":True, "class":"form-control"}),
			"fecha":forms.DateInput(attrs={"readonly":True, "class":"form-control","type":"date"}),
			"estado":forms.Select(attrs={"disabled":True, "class":"form-control form-control-plaintext"}),
			"tipo_proveedor":forms.Select(attrs={'disabled': True, 'class': 'form-control-plaintext'}),
			"proveedor":forms.Select(attrs={"disabled":True, "class":"form-control-plaintext form-control"}),
			"centro_costos":forms.Select(attrs={"readonly":True, "disabled":True, "class":"form-control form-control-plaintext"}),
			"egreso":forms.Select(attrs={"disabled":True, "class":"form-control form-control-plaintext"}),
			"tipo_comprobante":forms.Select(attrs={"readonly":True,"disabled":True, "class":"form-control form-control-plaintext"}),
			"n_comprobante":forms.TextInput(attrs={"readonly":True, "class":"form-control"}),
			"concepto":forms.Textarea(attrs={"readonly":True, "class":"form-control", "rows":2}),
			"forma_pago":forms.Select(attrs={"readonly":True,"disabled":True, "class":"form-control form-control-plaintext"}),
			"observacion":forms.Textarea(attrs={"class":"form-control", "rows":2}),
			"motivo_anular":forms.Textarea(attrs={"class":"form-control", "rows":2}),
			"documentos":forms.Textarea(attrs={"readonly":True,"class":"form-control", "rows":2}),
		}

class OrdenPagoEditarThirdForm(forms.ModelForm):
	class Meta:
		model = OrdenPago

		fields = {
			"cod_ord_pago",
			"fecha",
			"n_tramite",
			"fecha_tramite",
			"estado",
			"tipo_proveedor",
			"proveedor",
			"centro_costos",
			"egreso",
			"tipo_comprobante",
			"n_comprobante",
			"concepto",
			"forma_pago",
			"observacion",
			"anexo",
			"motivo_anular",
			"documentos",
			"fecha_pago",
		}

		labels = {
			"cod_ord_pago":"Código",
			"n_tramite":"N° trámite",
			"fecha":"Fecha elaboración",
			"fecha_tramite":"Fecha Trámite",
			"fecha_pago":"Fecha Pago",
			"estado":"Estado",
			"tipo_proveedor":"Tipo de proveedor",
			"proveedor":"Razón social/Nombre",
			"centro_costos":"Centro de costos",
			"egreso":"Egreso",
			"tipo_comprobante":"Tipo de comprobante",
			"n_comprobante":"N° documento",
			"concepto":"Concepto",
			"forma_pago":"Forma de pago",
			"observacion":"Observaciones",
			"anexo":"Anexos",
			"motivo_anular":"Motivo de Anulación",
			"documentos":"Documentos",
		}

		widgets = {
			"cod_ord_pago":forms.TextInput(attrs={"readonly":True, "class":"form-control"}),
			"n_tramite":forms.TextInput(attrs={"class":"form-control"}),
			"fecha":forms.DateInput(attrs={"readonly":True, "class":"form-control","type":"date"}),
			"fecha_tramite": forms.DateInput(attrs={"class":"form-control","type":"date", "value":date.today}),
			"fecha_pago": forms.DateInput(attrs={"class":"form-control","type":"date", "value":date.today}),
			"estado":forms.Select(attrs={"disabled":True, "class":"form-control form-control-plaintext"}),
			"tipo_proveedor":forms.Select(attrs={'disabled': True, 'class': 'form-control-plaintext'}),
			"proveedor":forms.Select(attrs={"disabled":True, "class":"form-control-plaintext form-control"}),
			"centro_costos":forms.Select(attrs={"readonly":True, "disabled":True, "class":"form-control form-control-plaintext"}),
			"egreso":forms.Select(attrs={"disabled":True, "class":"form-control form-control-plaintext"}),
			"tipo_comprobante":forms.Select(attrs={"readonly":True,"disabled":True, "class":"form-control form-control-plaintext"}),
			"n_comprobante":forms.TextInput(attrs={"readonly":True, "class":"form-control"}),
			"concepto":forms.Textarea(attrs={"readonly":True, "class":"form-control", "rows":2}),
			"forma_pago":forms.Select(attrs={"readonly":True,"disabled":True, "class":"form-control form-control-plaintext"}),
			"observacion":forms.Textarea(attrs={"class":"form-control", "rows":2}),
			"anexo":forms.ClearableFileInput(attrs={"class":"form-control"}),
			"motivo_anular":forms.Textarea(attrs={"class":"form-control", "rows":2}),
			"documentos":forms.Textarea(attrs={"class":"form-control", "rows":2}),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["fecha_tramite"].required=True
		self.fields["n_tramite"].required=True
		self.fields["documentos"].required=True
		self.fields["anexo"].required=True


class OrdenPagoEditarFinalForm(forms.ModelForm):
	class Meta:
		model = OrdenPago

		fields = "__all__"

		labels = {
			"cod_ord_pago":"Código",
			"n_tramite":"N° trámite",
			"fecha":"Fecha elaboración",
			"fecha":"Fecha elaboración",
			"fecha_tramite":"Fecha Trámite",
			"estado":"Estado",
			"tipo_proveedor":"Tipo de provedor",
			"proveedor":"Razón social/Nombre",
			"centro_costos":"Centro de costos",
			"egreso":"Egreso",
			"tipo_comprobante":"tipo de comprobante",
			"n_comprobante":"N° documento",
			"concepto":"Concepto",
			"forma_pago":"Forma de pago",
			"observacion":"Observaciones",
			"anexo":"Anexos",
			"motivo_anular":"Motivo de Anulación",
			"documentos":"Documentos",

		}

		widgets = {
			"cod_ord_pago":forms.TextInput(attrs={"readonly":True, "class":"form-control"}),
			"n_tramite":forms.TextInput(attrs={"readonly":True, "class":"form-control"}),
			"fecha":forms.DateInput(attrs={"readonly":True, "class":"form-control","type":"date"}),
			"fecha_tramite": forms.DateInput(attrs={"readonly":True, "class":"form-control","type":"date", "value":date.today}),
			"fecha_pago": forms.DateInput(attrs={"readonly":True, "class":"form-control","type":"date", "value":date.today}),
			"estado":forms.Select(attrs={"disabled":True, "class":"form-control form-control-plaintext"}),
			"tipo_proveedor":forms.Select(attrs={'disabled': True, 'class': 'form-control-plaintext'}),
			"proveedor":forms.Select(attrs={"disabled":True, "class":"form-control-plaintext form-control"}),
			"centro_costos":forms.Select(attrs={"readonly":True, "disabled":True, "class":"form-control form-control-plaintext"}),
			"egreso":forms.Select(attrs={"disabled":True, "class":"form-control form-control-plaintext"}),
			"tipo_comprobante":forms.Select(attrs={"readonly":True,"disabled":True, "class":"form-control form-control-plaintext"}),
			"n_comprobante":forms.TextInput(attrs={"readonly":True, "class":"form-control"}),
			"concepto":forms.Textarea(attrs={"readonly":True, "class":"form-control", "rows":2}),
			"forma_pago":forms.Select(attrs={"readonly":True,"disabled":True, "class":"form-control form-control-plaintext"}),
			"observacion":forms.Textarea(attrs={"class":"form-control", "rows":2}),
			"anexo":forms.ClearableFileInput(attrs={"disabled":True,"class":"form-control"}),
			"motivo_anular":forms.Textarea(attrs={"class":"form-control", "rows":2}),
			"documentos":forms.Textarea(attrs={"readonly":True,"class":"form-control", "rows":2}),
		}
