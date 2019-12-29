from dal import autocomplete

from . import models
from django import forms
import django_filters
from .models import *

TRUE_FALSE_CHOICES = [
	(True, 'Aprobado'),
	(False, 'Rechazado')
	]
class DateInput(forms.DateInput):
    input_type = 'date'
class PresupuestoEventoForm(forms.ModelForm):
	#estado= 
	class Meta:
		model = PresupuestoEvento
		fields = "__all__"
		labels = { 'estado':'¿Aprobar presupuesto?'}
		
		widgets={"fecha":forms.DateInput(format='%Y-%m-%d', attrs={'class': 'datepicker', "type":"date"})}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

class PresupuestoTarifario(forms.ModelForm):
	class Meta:
		model = Tarifario
		fields = "__all__"
		widgets = {"docente": forms.Select(attrs={"class":"form-control"}),}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

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
		empty_label="-------",
		#null_value="null",

		choices=TRUE_FALSE_CHOICES
		)
	#non_estado = django_filters.BooleanFilter(field_name='estado', lookup_expr='isnull')

	class Meta:
		model = PresupuestoEvento
		fields = ["nombre","codigo","aula","modalidad","empresa","nombre_instructor",
		"fecha","horario","n_horas","costo_hora_instructor","n_dias",
		"n_participantes","estado"]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	

