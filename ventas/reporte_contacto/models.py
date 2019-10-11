from django.db import models
from ventas.personas_juridicas.models import Juridica
from multiselectfield import MultiSelectField

# Create your models here.
class ReporteContacto(models.Model):

	SERVICIOS_CHOICES=  [
                            ('CBR','Coffe Break'),
                            ('ALM','Almuerzo'),
                            ('MIP','Material impreso'),
                            ('MDG','Material digital'),
                        ]
						
	cod_reporte=models.CharField(max_length=20, blank=True)
	empresa=models.ForeignKey(Juridica, on_delete=models.SET_NULL, null=True, blank=True)
	#empresa=models.CharField(max_length=100)
	canal_de_contacto=models.CharField(max_length=100)
	motivo_de_contacto=models.CharField(max_length=500)
	lugar=models.CharField(max_length=100)
	fecha=models.CharField(max_length=12)
	hora_inicio=models.TimeField()
	hora_fin=models.TimeField()
	nombre_contacto=models.CharField(max_length=100)
	telefono=models.CharField(max_length=10)
	cargo=models.CharField(max_length=100)
	correo_electronico=models.EmailField(max_length=100)
	asistentes=models.CharField(max_length=100)
	situacion_actual=models.CharField(max_length=500)
	situacion_deseada=models.CharField(max_length=500)
	servicios_requeridos=MultiSelectField(choices=SERVICIOS_CHOICES,
                                            blank=True,
                                            null=True)

	def __str__(self):
		return '{} {}'.format(self.cod_reporte,self.empresa)

class Capacitacion(models.Model):
	CIUDADES_CHOICES = [("Alamor","Alamor"),("Alausí","Alausí"),("Amaluza","Amaluza"),("Ambato","Ambato"),("Arajuno","Arajuno"),("Archidona","Archidona"),("Arenillas","Arenillas"),("Atacames","Atacames"),("Atuntaquí","Atuntaquí"),("Azogues","Azogues"),("Baba","Baba"),("Babahoyo","Babahoyo"),("Baeza","Baeza"),("Bahía de Caráquez","Bahía de Caráquez"),("Balao","Balao"),("Balsas","Balsas"),("Balzar","Balzar"),("Baños de Agua Santa","Baños de Agua Santa"),("Biblián","Biblián"),("Bolívar","Bolívar"),("Bucay","Bucay"),("Buena Fe","Buena Fe"),("Cajabamba","Cajabamba"),("Calceta","Calceta"),("Caluma","Caluma"),("Camilo Ponce Enríquez","Camilo Ponce Enríquez"),("Cariamanga","Cariamanga"),("Carlos Julio Arosemena Tola","Carlos Julio Arosemena Tola"),("Catacocha","Catacocha"),("Catamayo","Catamayo"),("Catarama","Catarama"),("Cayambe","Cayambe"),("Cañar","Cañar"),("Celica","Celica"),("Cevallos","Cevallos"),("Chaguarpamba","Chaguarpamba"),("Chambo","Chambo"),("Chilla","Chilla"),("Chillanes","Chillanes"),("Chimbo","Chimbo"),("Chone","Chone"),("Chordeleg","Chordeleg"),("Chunchi","Chunchi"),("Cnel. Marcelino Maridueña","Cnel. Marcelino Maridueña"),("Colimes","Colimes"),("Cotacachi","Cotacachi"),("Cuenca","Cuenca"),("Cumandá","Cumandá"),("Daule","Daule"),("Durán","Durán"),("Déleg","Déleg"),("Echendía","Echendía"),("El Carmen","El Carmen"),("El Chaco","El Chaco"),("El Corazón","El Corazón"),("El Dorado de Cascales","El Dorado de Cascales"),("El Guabo","El Guabo"),("El Pan","El Pan"),("El Pangui","El Pangui"),("El Tambo","El Tambo"),("El Triunfo","El Triunfo"),("El Ángel","El Ángel"),("Esmeraldas","Esmeraldas"),("Flavio Alfaro","Flavio Alfaro"),("Girón","Girón"),("Gonzanamá","Gonzanamá"),("Guachapala","Guachapala"),("Gualaceo","Gualaceo"),("Gualaquiza","Gualaquiza"),("Guamote","Guamote"),("Guano","Guano"),("Guaranda","Guaranda"),("Guayaquil","Guayaquil"),("Guayzimi","Guayzimi"),("Huaca","Huaca"),("Huamboya","Huamboya"),("Huaquillas","Huaquillas"),("Ibarra","Ibarra"),("Ididrio Ayora","Ididrio Ayora"),("Jama","Jama"),("Jaramijó","Jaramijó"),("Jipijapa","Jipijapa"),("Jujan","Jujan"),("Junín","Junín"),("La Bonita","La Bonita"),("La Concordia","La Concordia"),("La Joya de los Sachas","La Joya de los Sachas"),("La Libertad","La Libertad"),("La Maná","La Maná"),("La Troncal","La Troncal"),("La Victoria","La Victoria"),("Las Naves","Las Naves"),("Latacunga","Latacunga"),("Limones","Limones"),("Limón","Limón"),("Logroño","Logroño"),("Loja","Loja"),("Lomaas de Sargentillo","Lomaas de Sargentillo"),("Loreto","Loreto"),("Lumbaqui","Lumbaqui"),("Macará","Macará"),("Macas","Macas"),("Machachi","Machachi"),("Machala","Machala"),("Manta","Manta"),("Marcabelí","Marcabelí"),("Mera","Mera"),("Milagro","Milagro"),("Mira","Mira"),("Mocache","Mocache"),("Mocha","Mocha"),("Montalvo","Montalvo"),("Montecristi","Montecristi"),("Muisne","Muisne"),("Nabón","Nabón"),("Naranjal","Naranjal"),("Naranjito","Naranjito"),("Nobol","Nobol"),("Nueva Loja","Nueva Loja"),("Nuevo Rocafuerte","Nuevo Rocafuerte"),("Olmedo","Olmedo"),("Olmedo","Olmedo"),("Otavalo","Otavalo"),("Oña","Oña"),("Pablo Sexto","Pablo Sexto"),("Paccha","Paccha"),("Paján","Paján"),("Palanda","Palanda"),("Palenque","Palenque"),("Palestina","Palestina"),("Pallatanga","Pallatanga"),("Palora","Palora"),("Paquisha","Paquisha"),("Pasaje","Pasaje"),("Patate","Patate"),("Paute","Paute"),("Pedernales","Pedernales"),("Pedro Carbo","Pedro Carbo"),("Pedro Vicendo Maldonado","Pedro Vicendo Maldonado"),("Pelileo","Pelileo"),("Penipe","Penipe"),("Pichincha","Pichincha"),("Pimampiro","Pimampiro"),("Pindal","Pindal"),("Piñas","Piñas"),("Playas","Playas"),("Portovelo","Portovelo"),("Portoviejo","Portoviejo"),("Pucará","Pucará"),("Puebloviejo","Puebloviejo"),("Puerto Ayora","Puerto Ayora"),("Puerto Bauerizo Moreno","Puerto Bauerizo Moreno"),("Puerto Francisco de Orellana","Puerto Francisco de Orellana"),("Puerto López","Puerto López"),("Puerto Quito","Puerto Quito"),("Puerto Villamil","Puerto Villamil"),("Pujulí","Pujulí"),("Putumayo","Putumayo"),("Puyo","Puyo"),("Píllaro","Píllaro"),("Quero","Quero"),("Quevedo","Quevedo"),("Quinindé","Quinindé"),("Quinsaloma","Quinsaloma"),("Quito","Quito"),("Riobamba","Riobamba"),("Rioverde","Rioverde"),("Rocafuerte","Rocafuerte"),("Salcedo","Salcedo"),("Salinas","Salinas"),("Salitre","Salitre"),("Samborondón","Samborondón"),("Samn Fernando","Samn Fernando"),("San Gabriel","San Gabriel"),("San Juan Bosco","San Juan Bosco"),("San Lorenzo","San Lorenzo"),("San Miguel","San Miguel"),("San Miguel de los Bancos","San Miguel de los Bancos"),("San Vicente","San Vicente"),("Sangolquí","Sangolquí"),("Santa Ana","Santa Ana"),("Santa Clara","Santa Clara"),("Santa Elena","Santa Elena"),("Santa Isabel","Santa Isabel"),("Santa Lucía","Santa Lucía"),("Santa Rosa","Santa Rosa"),("Santiago","Santiago"),("Santiago de Méndez","Santiago de Méndez"),("Santo Domingo","Santo Domingo"),("Saquisilí","Saquisilí"),("Saraguro","Saraguro"),("Sevilla de Oro","Sevilla de Oro"),("Shushufinfi","Shushufinfi"),("Sigchos","Sigchos"),("Simón Bolívar","Simón Bolívar"),("Sorozanga","Sorozanga"),("Sucre","Sucre"),("Sucúa","Sucúa"),("Suscal","Suscal"),("Sígsig","Sígsig"),("Tabacundo","Tabacundo"),("Taisha","Taisha"),("Tarapoa","Tarapoa"),("Tena","Tena"),("Tiputini","Tiputini"),("Tisaleo","Tisaleo"),("Tosagua","Tosagua"),("Tulcán","Tulcán"),("Urcuquí","Urcuquí"),("Valencia","Valencia"),("Velasco Ibarra","Velasco Ibarra"),("Ventanas","Ventanas"),("Vinces","Vinces"),("Yacuambi","Yacuambi"),("Yaguachi","Yaguachi"),("Yantzaza","Yantzaza"),("Zamora","Zamora"),("Zapotillo","Zapotillo"),("Zaruma","Zaruma"),("Zumba","Zumba"),("Zumbi","Zumbi")]

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
	ciudad=models.CharField(max_length=25,choices=CIUDADES_CHOICES)
	fecha_evento=models.CharField(max_length=12)
	horario_evento_inicio=models.TimeField()
	horario_evento_fin=models.TimeField()
	observaciones=models.CharField(max_length=500)
	acuerdos=models.CharField(max_length=500)
	exclusivo_acad=models.CharField(max_length=500, blank=True, null=True)
	reporte=models.ForeignKey(ReporteContacto, on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return '{}'.format(self.tema)


class Asesoria(models.Model):
	IMPLEMENTACION_CHOICES=	[
								('CI','Con implementación'),
								('SI','Sin implementación'),
							]

	tipo_servicio=models.CharField(max_length=25)
	descripcion=models.CharField(max_length=500)
	alcance=models.CharField(max_length=250)
	con_sin_imple=models.CharField(max_length=25,
									choices=IMPLEMENTACION_CHOICES,
									default='CI')
	fecha_inicio=models.CharField(max_length=12)
	fecha_fin=models.CharField(max_length=12)
	proveedor=models.CharField(max_length=25)
	entregables=models.CharField(max_length=500)
	observaciones=models.CharField(max_length=500)
	acuerdos=models.CharField(max_length=500)
	exclusivo_acad=models.CharField(max_length=500,blank=True, null=True)
	reporte=models.ForeignKey(ReporteContacto, on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return '{}'.format(self.tipo_servicio)