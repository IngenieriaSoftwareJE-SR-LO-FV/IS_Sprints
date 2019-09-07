from .models import Persona_Natural
import django_filters

class NaturalBusquedaFilter(django_filters.FilterSet):
	class Meta:
		model = Persona_Natural
		fields = ['cedula', 'nombres', 'apellidos', 'empresa', 'un_tercernivel', 'cargo', 'profesion', 
		'ci_domicilio', 'tel_domicilio', 'celular', 'email',]
		