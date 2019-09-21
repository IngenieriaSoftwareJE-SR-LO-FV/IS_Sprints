from django import forms
from django.forms import ModelForm
from .models import Persona_Natural

class Natural_NuevoForm(forms.ModelForm):
	class Meta:
		model = Persona_Natural
		fields = ['cedula','apellidos','nombres','fecha_nacimiento','tel_domicilio','celular','email','ci_domicilio','dir_domicilio','nivel_estudio',
		'ti_tercernivel','un_tercernivel','ti_postgrado','un_postgrado','profesion','forma_trabajo','empresa','cargo','ci_trabajo','area',
		'dir_trabajo','tel_trabajo','medios', 'novedad_medios']
		widgets = {
			'cedula': forms.TextInput(attrs={'type':'number'}),
			'nivel_estudio': forms.RadioSelect(attrs={'class':'required'}),
			'fecha_nacimiento': forms.DateInput(attrs={'type':'date'}),
			'novedad_medios': forms.Textarea(attrs={'rows':2}),
		}
		