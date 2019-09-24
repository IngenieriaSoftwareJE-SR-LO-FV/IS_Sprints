from django.db import models
from ventas.personas_juridicas.models import Juridica
import financiero.validaciones

class Aula(models.Model):
	nombre = models.CharField(max_length=100)
	def __str__(self):
		return self.nombre
class Modalidad(models.Model):
	nombre = models.CharField(max_length=100)
	def __str__(self):
		return self.nombre

class PresupuestoEvento(models.Model):
	nombre = models.CharField(max_length=200,
		verbose_name="Nombre de Evento", 
		help_text="Ingresar nombre de evento")
	codigo = models.CharField(max_length=200,
		verbose_name="Código")
	aula = models.ForeignKey(Aula,on_delete=models.SET_NULL, null=True, blank=True,verbose_name="Aula")
	modalidad = models.ForeignKey(Modalidad,on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Modalidad")
	empresa = models.ForeignKey(Juridica,on_delete=models.SET_NULL, null=True, blank=True,verbose_name="Empresa")
	nombre_instructor = models.CharField(max_length=200,
		verbose_name="Nombre del instructor")
	fecha = models.DateField(verbose_name="Fecha")
	horario = models.CharField(max_length=200)
	n_horas = models.IntegerField(verbose_name="No. Horas",validators=[financiero.validaciones.validate_positivo])
	costo_hora_instructor = models.DecimalField(max_digits=7,decimal_places=3,verbose_name="Costo Hora Instructor",validators=[financiero.validaciones.validate_positivo])
	n_dias = models.IntegerField(verbose_name="No. Dias",validators=[financiero.validaciones.validate_positivo])
	n_participantes = models.IntegerField(verbose_name="No. Participantes",validators=[financiero.validaciones.validate_positivo])
	ingresos = models.DecimalField(max_digits=14,decimal_places=3,verbose_name="Ingresos sin descuento",validators=[financiero.validaciones.validate_positivo])
	honorario_instructor = models.DecimalField(max_digits=7,decimal_places=3,
		verbose_name="Honorario Instructor",validators=[financiero.validaciones.validate_positivo])
	movilizacion_personal = models.DecimalField(max_digits=10,decimal_places=3,
		verbose_name="Movilización del personal",validators=[financiero.validaciones.validate_positivo])

	lapiz =  models.DecimalField(max_digits=8,decimal_places=3,	verbose_name="Lápiz",validators=[financiero.validaciones.validate_positivo])
	pendrives =  models.DecimalField(max_digits=8,decimal_places=3,verbose_name="Pendrives",validators=[financiero.validaciones.validate_positivo])
	otros_materiales = models.DecimalField(max_digits=8,decimal_places=3,verbose_name="Otros materiales",validators=[financiero.validaciones.validate_positivo])
	movilizacion_personal_ciudad = models.DecimalField(max_digits=10,decimal_places=3,verbose_name="Movilización del personal (dentro de la ciudad",validators=[financiero.validaciones.validate_positivo])
	estado = models.BooleanField(default=None,null=True,blank=True)
	"""@property
	def price_display(self):
		return "$%s" % self.price"""
	def __str__(self):
		return self.codigo+" - "+self.nombre




