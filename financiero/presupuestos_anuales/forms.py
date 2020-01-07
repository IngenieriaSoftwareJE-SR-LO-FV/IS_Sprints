from django import forms
from .models import Fundespol, Espoltech
from datetime import date

class EspoltechForm(forms.ModelForm):
	class Meta:
		model = Espoltech
		fields = '__all__'


class FundespolForm(forms.ModelForm):
	class Meta:
		model = Fundespol
		fields = '__all__'
