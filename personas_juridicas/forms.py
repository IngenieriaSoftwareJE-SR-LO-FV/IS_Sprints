from . import models
from django import forms
import django_filters

class DateInput(forms.DateInput):
    input_type = 'date'
class JuridicaForm(forms.ModelForm):
	class Meta:
		model = models.Juridica
		fields = [
					"nombre",
					"ruc",
					"tipo_empresa",
					"sector",
					"direccion",
					"ciudad",
					"provincia",
					"telefono",
					"celular",
					"correo",
					"representante",
					"maximo_facturas",
					"forma_pago",
					"contacto_cedula",
					"contacto_nombres",
					"contacto_apellidos",
					"contacto_cargo",
					"contacto_telefono",
					"contacto_celular",
					"contacto_correo"
					]


		labels = {
					"nombre":"Razón social",
					"ruc": "RUC",
					"tipo_empresa": "Tipo de empresa",
					"sector": "Sector",
					"direccion": "Dirección",
					"ciudad": "Ciudad",
					"provincia": "Provincia",
					"telefono": "Teléfono",
					"celular": "Celular",
					"correo": "Correo electrónico",
					"representante": "Representante legal",
					"maximo_facturas": "Fecha máxima de recepción de facturas",
					"forma_pago": "Forma usual de pago",
					"contacto_cedula": "Cédula",
					"contacto_nombres": "Nombres",
					"contacto_apellidos":"Apellidos",
					"contacto_cargo": "Cargo",
					"contacto_telefono":"Teléfono",
					"contacto_celular": "Celular",
					"contacto_correo": "Correo electrónico"
					}
		widgets = {
				"nombre":forms.TextInput(attrs={"class":"form-control"}),
				"ruc":forms.TextInput(attrs={"class":"form-control","type":"number"}),
				"tipo_empresa":forms.TextInput(attrs={"class":"form-control"}),
				"sector":forms.TextInput(attrs={"class":"form-control"}),
				"direccion":forms.TextInput(attrs={"class":"form-control"}),
				"ciudad":forms.Select(attrs={"class":"form-control"}),
				"provincia":forms.Select(attrs={"class":"form-control"}),
				"telefono":forms.TextInput(attrs={"class":"form-control","type":"tel"}),
				"celular":forms.TextInput(attrs={"class":"form-control","type":"tel"}),
				"correo":forms.EmailInput(attrs={"class":"form-control"}),
				"representante":forms.TextInput(attrs={"class":"form-control"}),
				"maximo_facturas":forms.DateInput(attrs={"class":"form-control","type":"date"}),
				"forma_pago":forms.TextInput(attrs={"class":"form-control"}),
				"contacto_cedula":forms.TextInput(attrs={"class":"form-control"}),
				"contacto_nombres":forms.TextInput(attrs={"class":"form-control"}),
				"contacto_apellidos":forms.TextInput(attrs={"class":"form-control"}),
				"contacto_cargo":forms.TextInput(attrs={"class":"form-control"}),
				"contacto_telefono":forms.TextInput(attrs={"class":"form-control","type":"tel"}),
				"contacto_celular":forms.TextInput(attrs={"class":"form-control","type":"tel"}),
				"contacto_correo":forms.EmailInput(attrs={"class":"form-control"})


		}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['ciudad'].queryset = models.Ciudad.objects.none()
		#self.fields['ciudad'].choices = [("None","Select_")]
		if 'provincia' in self.data:
			try:
				provincia_id = int(self.data.get('provincia'))
				self.fields['ciudad'].queryset = models.Ciudad.objects.filter(provincia_id=provincia_id).order_by('nombre')
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['ciudad'].queryset = self.instance.provincia.city_set.order_by('nombre')
class JuridicaFilter(django_filters.FilterSet):
	class Meta:
		model = models.Juridica
		fields = [
					"nombre",
					"ruc",
					"tipo_empresa",
					"sector",
					"direccion",
					"ciudad",
					"provincia",
					"telefono",
					"celular",
					"correo",
					"forma_pago",
					"contacto_cedula",
					"contacto_nombres",
					"contacto_apellidos",
					"contacto_telefono",
					"contacto_celular",
					"contacto_correo"
					]


		labels = {
					"nombre":"Razón social",
					"ruc": "RUC",
					"tipo_empresa": "Tipo de empresa",
					"sector": "Sector",
					"direccion": "Dirección",
					"ciudad": "Ciudad",
					"provincia": "Provincia",
					"telefono": "Teléfono",
					"celular": "Celular",
					"correo": "Correo electrónico",
					"maximo_facturas": "Fecha máxima de recepción de facturas",
					"forma_pago": "Forma usual de pago",
					"contacto_cedula": "Cédula",
					"contacto_nombres": "Nombres",
					"contacto_apellidos":"Apellidos",
					"contacto_cargo": "Cargo",
					"contacto_telefono":"Teléfono",
					"contacto_celular": "Celular",
					"contacto_correo": "Correo electrónico"
					}
		widgets = {
				"nombre":forms.TextInput(attrs={"class":"form-control"}),
				"ruc":forms.TextInput(attrs={"class":"form-control","type":"number"}),
				"tipo_empresa":forms.TextInput(attrs={"class":"form-control"}),
				"sector":forms.TextInput(attrs={"class":"form-control"}),
				"direccion":forms.TextInput(attrs={"class":"form-control"}),
				"ciudad":forms.Select(attrs={"class":"form-control"}),
				"provincia":forms.Select(attrs={"class":"form-control"}),
				"telefono":forms.TextInput(attrs={"class":"form-control","type":"tel"}),
				"celular":forms.TextInput(attrs={"class":"form-control","type":"tel"}),
				"correo":forms.EmailInput(attrs={"class":"form-control"}),
				"maximo_facturas":forms.DateInput(attrs={"class":"form-control","type":"date"}),
				"forma_pago":forms.TextInput(attrs={"class":"form-control"}),
				"contacto_cedula":forms.TextInput(attrs={"class":"form-control"}),
				"contacto_nombres":forms.TextInput(attrs={"class":"form-control"}),
				"contacto_apellidos":forms.TextInput(attrs={"class":"form-control"}),
				"contacto_cargo":forms.TextInput(attrs={"class":"form-control"}),
				"contacto_telefono":forms.TextInput(attrs={"class":"form-control","type":"tel"}),
				"contacto_celular":forms.TextInput(attrs={"class":"form-control","type":"tel"}),
				"contacto_correo":forms.EmailInput(attrs={"class":"form-control"})


		}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.form.fields['ciudad'].queryset = models.Ciudad.objects.none()

