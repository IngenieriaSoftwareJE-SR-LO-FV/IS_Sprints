from dal import autocomplete

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
				"tipo_empresa":forms.Select(attrs={"class":"form-control"}),
				"sector":forms.Select(attrs={"class":"form-control"}),
				"direccion":forms.TextInput(attrs={"class":"form-control"}),
				"ciudad":forms.Select(attrs={"class":"form-control"}),
				"provincia":forms.Select(attrs={"class":"form-control"}),
				"telefono":forms.TextInput(attrs={"class":"form-control","type":"tel"}),
				"celular":forms.TextInput(attrs={"class":"form-control","type":"tel"}),
				"correo":forms.EmailInput(attrs={"class":"form-control"}),
				"representante":forms.TextInput(attrs={"class":"form-control"}),
				"maximo_facturas":forms.DateInput(format='%Y-%m-%d', attrs={'class': 'datepicker', "type":"date"}),
				"forma_pago":forms.Select(attrs={"class":"form-control"}),
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
		if 'provincia' in self.data:
			try:
				provincia_id = int(self.data.get('provincia'))
				self.fields['ciudad'].queryset = models.Ciudad.objects.filter(provincia_id=provincia_id).order_by('nombre')
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['ciudad'].queryset = self.instance.provincia.ciudad_set.order_by('nombre')

class JuridicaFilter(django_filters.FilterSet):
	nombre = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Razón Social'}))
	ruc = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control","type":"number",'placeholder': 'RUC'}))
	tipo_empresa = django_filters.ModelChoiceFilter(label="", empty_label="Tipo de Empresa", queryset=models.TipoEmpresa.objects.all())
	sector = django_filters.ModelChoiceFilter(label="", empty_label="Sector", queryset=models.Sector.objects.all())
	direccion = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Dirección'}))
	telefono = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control","type":"tel",'placeholder': 'Teléfono'}))
	celular = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control","type":"tel",'placeholder': 'Celular'}))
	correo = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Correo electrónico'}))
	forma_pago = django_filters.ModelChoiceFilter(label="", empty_label="Forma usual de pago", queryset=models.FormaPago.objects.all())
	contacto_cedula = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Cédula'}))
	contacto_nombres = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Nombres'}))
	contacto_apellidos = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Apellidos'}))
	contacto_telefono = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control","type":"tel",'placeholder': 'Teléfono'}))
	contacto_celular = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control","type":"tel",'placeholder': 'Celular'}))
	contacto_correo = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Correo Electrónico'}))
	provincia = django_filters.ModelChoiceFilter(label="", empty_label="Provincia", queryset=models.Provincia.objects.all())

	def ciudades(request):
		if request is None:
			return models.Ciudad.objects.none()
		else:
			return request.provincia.city_set.order_by('name')

	ciudad = django_filters.ModelChoiceFilter(label="", empty_label="Ciudad", queryset=ciudades)

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

		widgets = {
				"maximo_facturas":forms.DateInput(format='%Y-%m-%d', attrs={'class': 'datepicker', "type":"date"}),
		}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.form.fields['ciudad'].queryset = models.Ciudad.objects.none()

