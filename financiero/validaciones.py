from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_positivo(value):
	if(int(value)<0):
		raise ValidationError(
			_("Valor no puede ser negativo"),
			code="valor_negativo"
		)