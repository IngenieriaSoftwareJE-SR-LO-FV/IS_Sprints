from django import forms
from .models import *

class InteresadoForm(forms.ModelForm):
	class Meta:
		model = Interesado
		fields = "__all__"


class InteresadoCargarForm(forms.Form):
	archivo = forms.FileField(label="Archivo a cargar")
		