from django.db import models

# Create your models here.
class ReporteContacto(models.Model):
	empresa=models.CharField(max_length=50)
	canal_de_contacto=models.CharField(max_length=100)
	motivo_de_contacto=models.CharField(max_length=500)
	lugar=models.CharField(max_length=100)
	fecha=models.DateField()
	hora_inicio=models.TimeField()
	hora_fin=models.TimeField()
	nombre_contacto=models.CharField(max_length=100)
	telefono=models.CharField(max_length=10)
	cargo=models.CharField(max_length=100)
	correo_electronico=models.CharField(max_length=100)
	asistentes=models.CharField(max_length=100)
	situacion_actual=models.CharField(max_length=500)
	situacion_deseada=models.CharField(max_length=500)
	servicios_requeridos=models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.empresa)

class Capacitacion(models.Model):
	TIPO_CHOICES=	[
						('CR','Curso'),
						('CNF','Conferencia'),
						('WB','Webinario'),
						('TLL','Taller'),
						('MOD','Módulo'),
						('PRG','Programa'),
						('DPL','Diplomado')
					]	

	AREA_CHOICES=	[
						('A','ADMINISTRACIÓN Y LEGISLACIÓN'),
						('B','AGRONOMÍA'),
						('C','ZOOTECNIA'),
						('D','ALIMENTACIÓN, GASTRONOMÍA Y TURISMO'),
						('E','TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIÓN'),
						('F','FINANZAS, COMERCIO Y VENTAS'),
						('H','CONSTRUCCIÓN E INFRAESTRUCTURA'),
						('I','FORESTAL, ECOLOGÍA Y AMBIENTE'),
						('J','EDUCACIÓN Y CAPACITACIÓN'),
						('K','ELECTRICIDAD Y ELECTRÓNICA'),
						('L','ESPECIES ACUÁTICAS Y PESCA'),
						('M','COMUNICACIÓN Y ARTES GRÁFICAS'),
						('N','MECÁNICA AUTOMOTRIZ'),
						('O','MECÁNICA INDUSTRIAL Y MINERÍA'),
						('P','PROCESOS INDUSTRIALES'),
						('Q','TRANSPORTE Y LOGÍSTICA'),
						('R','ARTES Y ARTESANÍA'),
						('S','SERVICIOS SOCIOCULTURALES Y A LA COMUNIDAD'),
						('T','INDUSTRIA AGROPECUARIA '),

						
					]

	MODALIDAD_CHOICES=	[	
							('PRS','Presencial'),
							('SPRS','Semi-presencial'),
							('VRT','Virtual'),
						]

	NIVEL_ORGANIZACION_CHOICES=	[
									('OP','Operativos'),
									('MM','Mandos medios'),
									('D/G','Directivos/Gerentes'),
								]

	NIVEL_EDUCACION=	[
							('SE','Sin escolaridad'),
							('PRI','Primaria'),
							('BCH','Bachillerato'),
							('TN','Tercer Nivel'),
							('CN','Cuarto Nivel'),
							('NEMV','Nivel de educación muy variado'),
						]
	
	EDAD_PROMEDIO_CHOICES=	[
								('18_25','Entre 18 a 25 años'),
								('26_35','Entre 26 a 35 años'),
								('36_55','Entre 36 a 55 años'),
								('56_65','Entre 56 a 65 años'),
								('+65','Más de 65 años'),
							]
	tema=models.CharField(max_length=25)
	tipo=models.CharField(max_length=25,
							choices=TIPO_CHOICES,
							default='CR')
	modalidad=models.CharField(max_length=25,
								choices=MODALIDAD_CHOICES,
								default='PRS')
	area=models.CharField(max_length=100,
							choices=AREA_CHOICES)
	nivel_organizacion=models.CharField(max_length=25,
										choices=NIVEL_ORGANIZACION_CHOICES,
										default='OP')
	numero_participantes=models.PositiveIntegerField()
	horario_trabajo=models.CharField(max_length=50)
	nivel_educacion=models.CharField(max_length=25,
									choices=NIVEL_EDUCACION,
									default='BCH')
	edad_promedio=models.CharField(max_length=25,
									choices=EDAD_PROMEDIO_CHOICES)
	lugar=models.CharField(max_length=50)
	ciudad=models.CharField(max_length=25)
	fecha_evento=models.DateField()
	horario_evento_inicio=models.TimeField()
	horario_evento_fin=models.TimeField()
	observaciones=models.CharField(max_length=500)
	acuerdos=models.CharField(max_length=500)
	exclusivo_acad=models.CharField(max_length=500, blank=True, null=True)
	reporte=models.ForeignKey(ReporteContacto, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return '{}'.format(self.tema)


class Asesoria(models.Model):
	IMPLEMENTACION_CHOICES=	[
								('CI','Con implementación'),
								('SI','Sin implementación'),
							]

	tipo=models.CharField(max_length=25)
	descripcion=models.CharField(max_length=500)
	alcance=models.CharField(max_length=250)
	con_sin_imple=models.CharField(max_length=25)
	fecha_inicio=models.DateField()
	fecha_fin=models.DateField()
	proveedor=models.CharField(max_length=25)
	entregables=models.CharField(max_length=500)
	observaciones=models.CharField(max_length=500)
	acuerdos=models.CharField(max_length=500)
	exclusivo_acad=models.CharField(max_length=500,blank=True, null=True)
	reporte=models.ForeignKey(ReporteContacto, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return '{}'.format(self.tipo)