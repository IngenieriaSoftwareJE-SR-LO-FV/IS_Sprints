from dal import autocomplete

from . import models
from django import forms
import django_filters
from .models import *

TRUE_FALSE_CHOICES = [
	(True, 'Aceptado'),
	(False, 'Rechazado')
	]
class DateInput(forms.DateInput):
    input_type = 'date'
class PresupuestoEventoForm(forms.ModelForm):
	#estado= 
	class Meta:
		model = PresupuestoEvento
		fields = "__all__"
		
		widgets={"fecha":forms.DateInput(format='%Y-%m-%d', attrs={'class': 'datepicker', "type":"date"})}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		"""self.fields["fecha"] = forms.DateField(
        widget=forms.DateInput(format='%Y/%m/%d', attrs={'class': 'datepicker',"type":"date"}),
        input_formats=('%Y/%m/%d', )
        )"""
        #self.fields["estado"].widgets.choices=TRUE_FALSE_CHOICES;
		#self.fields["estado"].widgets.choices=forms.ChoiceField(choices = TRUE_FALSE_CHOICES, 
		#			initial=None, widget=forms.Select());
		#self.fields["estado"].widgets.choices=TRUE_FALSE_CHOICES;

class PresupuestoEventoFilter(django_filters.FilterSet):
	fecha = django_filters.DateFilter(
        widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'date'
            }
        ))

	estado = django_filters.ChoiceFilter(
		#lookup_expr='isnull',
		null_label="Pendiente",
		empty_label="Todos",
		#null_value="null",

		choices=TRUE_FALSE_CHOICES
		)
	#non_estado = django_filters.BooleanFilter(field_name='estado', lookup_expr='isnull')

	class Meta:
		model = PresupuestoEvento
		fields = ["nombre","codigo","aula","modalidad","empresa","nombre_instructor",
		"fecha","horario","n_horas","costo_hora_instructor","n_dias",
		"n_participantes","estado"]
		"""
		widgets={"estado":forms.Select(choices=[
	(True, 'Aceptado'),
	(False, 'Rechazado'),
	(None, "Pendiente")]),
	"fecha":forms.DateInput(format='%Y-%m-%d', attrs={'class': 'date55ker', "type":"date"})}
	"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		#self.form.fields["estado"]=forms.ChoiceField(choices = TRUE_FALSE_CHOICES, widget=forms.Select());
		#self.form.fields["estado"].choices=TRUE_FALSE_CHOICES

