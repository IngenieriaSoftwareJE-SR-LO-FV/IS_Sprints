from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_cedula(value):
	if(len(value)!=10 or not value.isdigit()):
		raise ValidationError(
            _('%(value)s no es una cédula válida'),
            code="invalid",
            params={'value': value},
        )
	else:
		impares = int(value[1]) + int(value[3]) + int(value[5]) + int(value[7])
		pares = 0
		for i in range(0,9):
			if(i%2==0):
				res = int(value[i])*2
				if(res>=10):
					res = res-9
				pares = pares+res
		total = impares+pares
		dig_validador = (((total+10)//10)*10)-total
		if(dig_validador==10):
			dig_validador = 0
		if (not(int(value[0:2])>=1 and int(value[0:2])<=24 and int(value[-1])==dig_validador)):
			raise ValidationError(
	            _('%(value)s no es una cédula válida'),
	            code="invalid",
	            params={'value': value},
	        )

def ruc_natural(value):
	impares = int(value[1]) + int(value[3]) + int(value[5]) + int(value[7])
	pares = 0
	for i in range(0,9):
		if(i%2==0):
			res = int(value[i])*2
			if(res>=10):
				res = res-9
			pares = pares+res
	total = impares+pares
	dig_validador = (((total+10)//10)*10)-total
	if(dig_validador==10):
		dig_validador = 0
	return int(value[0:2])>=1 and int(value[0:2])<=24 and int(value[9])==dig_validador and int(value[10:13])>=1

#Tercer dígito 9
def ruc_juridica(value):
	d1 = int(value[0])*4
	d2 = int(value[1])*3
	d3 = int(value[2])*2
	d4 = int(value[3])*7
	d5 = int(value[4])*6
	d6 = int(value[5])*5
	d7 = int(value[6])*4
	d8 = int(value[7])*3
	d9 = int(value[8])*2
	total = d1+d2+d3+d4+d5+d6+d7+d8+d9
	dig_validador = 0
	residuo = total%11
	if(residuo!=0):
		dig_validador = 11-residuo
	return int(value[0:2])>=1 and int(value[0:2])<=24 and int(value[2])==9 and int(value[9])==dig_validador and int(value[10:13])>=1

#Tercer dígito 6
def ruc_publica(value):
	d1 = int(value[0])*3
	d2 = int(value[1])*2
	d3 = int(value[2])*7
	d4 = int(value[3])*6
	d5 = int(value[4])*5
	d6 = int(value[5])*4
	d7 = int(value[6])*3
	d8 = int(value[7])*2
	total = d1+d2+d3+d4+d5+d6+d7+d8
	dig_validador = 0
	residuo = total%11
	if(residuo!=0):
		dig_validador = 11-residuo
	return int(value[0:2])>=1 and int(value[0:2])<=24 and int(value[2])==6 and int(value[8])==dig_validador and int(value[9:13])>=1

def validate_ruc(value):
	if (not value.isdigit() or not len(value)==13 or not(ruc_natural(value) or ruc_juridica(value) or ruc_publica(value))):
		raise ValidationError(
            _('%(value)s no es un RUC válido'),
            code="invalid",
            params={'value': value},
        )

def validate_letras(value):
	if (not all(x.isalpha() or x.isspace() for x in value)):
		raise ValidationError(
            _('%(value)s no contiene únicamente letras'),
            code="invalid",
            params={'value': value},
        )

def validate_fono_convencional(value):
	if (not value.isdigit() or not(len(value)==7 or len(value)==9)):
		raise ValidationError(
			_('%(value)s no es un teléfono convencional correcto'),
            code="invalid",
            params={'value': value},
		)

def validate_celular(value):
	if (not value.isdigit() or not len(value)>=10):
		raise ValidationError(
			_('%(value)s no es un celular correcto'),
            code="invalid",
            params={'value': value},
		)		

def validate_fecha(value):
	"""ToDo"""

def validate_positive(value):
	print(value)
	if(value<0):
		raise ValidationError(
			_('%(values)s no es un numero positivo'),
			code="invalid",
            params={'value': value},
		)
	