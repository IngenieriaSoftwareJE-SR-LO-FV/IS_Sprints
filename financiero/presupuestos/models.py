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

class TarifarioDocente(models.Model):
	descripcion = models.CharField(max_length=100);
	costo = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	version = models.IntegerField(null=True,blank=True);

class TarifarioHospedajeAlimentacionDocente(models.Model):
	descripcion = models.CharField(max_length=100);
	costo = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	version = models.IntegerField(null=True,blank=True);

class TarifarioHospedajeAlimentacionPersonal(models.Model):
	descripcion = models.CharField(max_length=100);
	costo = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	version = models.IntegerField(null=True,blank=True);

class TarifarioServicioAereo(models.Model):
	descripcion = models.CharField(max_length=100);
	costo = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	version = models.IntegerField(null=True,blank=True);
	
class TarifarioInstalacion(models.Model):
	descripcion = models.CharField(max_length=100);
	costo = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	version = models.IntegerField(null=True,blank=True);

class TarifarioPlantillaDelPersonal(models.Model):
	descripcion = models.CharField(max_length=100);
	costo = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	version = models.IntegerField(null=True,blank=True);

class TarifarioMaterial(models.Model):
	costo_con_iva = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	descripcion = models.CharField(max_length=100);
	costo = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	version = models.IntegerField(null=True,blank=True);
class TarifarioServicioAlimentacion(models.Model):
	incluye_iva = models.BooleanField(default=False)
	descripcion = models.CharField(max_length=100);
	costo = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	version = models.IntegerField(null=True,blank=True);
class TarifarioPrecio(models.Model):
	descripcion = models.CharField(max_length=100);
	costo = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	version = models.IntegerField(null=True,blank=True);

class TarifarioAportacion(models.Model):
	descripcion = models.CharField(max_length=100);
	costo = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	version = models.IntegerField(null=True,blank=True);
	porcentaje_facultades = models.BooleanField(default=False);

class TarifarioProducto(models.Model):
	descripcion = models.CharField(max_length=100);
	costo = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	version = models.IntegerField(null=True,blank=True);

class TarifarioProspecto(models.Model):
	descripcion = models.CharField(max_length=100);
	costo = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	version = models.IntegerField(null=True,blank=True);

class TarifarioPublicidad(models.Model):
	descripcion = models.CharField(max_length=100);
	costo = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	version = models.IntegerField(null=True,blank=True);

class TarifarioOtroSuministro(models.Model):
	descripcion = models.CharField(max_length=100);
	costo = models.DecimalField(max_digits=10,decimal_places=3,validators=[financiero.validaciones.validate_positivo]);
	version = models.IntegerField(null=True,blank=True);



class Tarifario(models.Model):
	docente = models.ManyToManyField(TarifarioDocente)
	hospedaje_alimentacion_docente = models.ManyToManyField(TarifarioHospedajeAlimentacionDocente, verbose_name="Hospedaje y alimentación docente")
	hospedaje_alimentacion_personal = models.ManyToManyField(TarifarioHospedajeAlimentacionPersonal, verbose_name="Hospedaje y alimentación personal ejecución")
	servicios_aereos = models.ManyToManyField(TarifarioServicioAereo, verbose_name="Servicios Aéreos")
	instalaciones = models.ManyToManyField(TarifarioInstalacion)
	plantilla_del_personal = models.ManyToManyField(TarifarioPlantillaDelPersonal)
	materiales_del_evento = models.ManyToManyField(TarifarioMaterial)
	servicio_de_alimentacion = models.ManyToManyField(TarifarioServicioAlimentacion, verbose_name="Servicio de alimentación")
	aportaciones = models.ManyToManyField(TarifarioAportacion)
	precios = models.ManyToManyField(TarifarioPrecio)
	productos = models.ManyToManyField(TarifarioProducto)
	prospecto = models.ManyToManyField(TarifarioProspecto)
	publicidad = models.ManyToManyField(TarifarioPublicidad)
	otros_suministros = models.ManyToManyField(TarifarioOtroSuministro)
	version = models.IntegerField(null=True,blank=True);

class PresupuestoEvento(models.Model):
	nombre = models.CharField(max_length=200,
		verbose_name="Nombre de Evento", 
		help_text="Ingresar nombre de evento")
	codigo = models.CharField(max_length=200,
		verbose_name="Código")
	aula = models.ForeignKey(Aula,on_delete=models.SET_NULL, null=True, blank=True,verbose_name="Aula")
	modalidad = models.ForeignKey(Modalidad,on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Modalidad")
	empresa = models.ForeignKey(Juridica,on_delete=models.SET_NULL, null=True, blank=True,verbose_name="Empresa")
	nombre_instructor = models.CharField(max_length=200,verbose_name="Nombre del instructor")
	fecha = models.DateField(verbose_name="Fecha",null=True, blank=True)
	horario = models.CharField(max_length=200,null=True, blank=True)
	n_horas = models.IntegerField(verbose_name="No. Horas",validators=[financiero.validaciones.validate_positivo])
	costo_hora_instructor = models.DecimalField(max_digits=7,decimal_places=3,verbose_name="Costo Hora Instructor",validators=[financiero.validaciones.validate_positivo])
	n_dias = models.IntegerField(verbose_name="No. Dias",validators=[financiero.validaciones.validate_positivo])
	n_participantes = models.IntegerField(verbose_name="No. Participantes",validators=[financiero.validaciones.validate_positivo],null=True, blank=True)
	ingresos = models.DecimalField(max_digits=14,decimal_places=3,verbose_name="Ingresos sin descuento",validators=[financiero.validaciones.validate_positivo])
	honorario_instructor = models.DecimalField(max_digits=7,decimal_places=3,
		verbose_name="Honorario Instructor",validators=[financiero.validaciones.validate_positivo])
	movilizacion_personal = models.DecimalField(max_digits=10,decimal_places=3,
		verbose_name="Movilización del personal",validators=[financiero.validaciones.validate_positivo])

	lapiz =  models.BooleanField(default=False)
	pendrives =  models.BooleanField(default=False)
	otros_materiales = models.BooleanField(default=False)

	movilizacion_personal_ciudad = models.DecimalField(max_digits=10,decimal_places=3,verbose_name="Movilización del personal (dentro de la ciudad",validators=[financiero.validaciones.validate_positivo])
	estado = models.BooleanField(default=None,null=True,blank=True)
	"""@property
	def price_display(self):
		return "$%s" % self.price"""
	def __str__(self):
		return self.codigo+" - "+self.nombre




