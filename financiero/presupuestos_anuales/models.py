from django.db import models
import financiero.validaciones
from decimal import Decimal

# MODELO PARA FUNDESPOL
class Fundespol(models.Model):
	ESTADO_CHOICES = [("GRBD","Grabado"),("ENVD","Enviado"),("AUTR","Autorizado"),("ANLD","Anulado"),]
	año = models.PositiveIntegerField()
	nombre = models.CharField(max_length=100, blank=True)
	centro_costos = models.CharField(max_length=10, default='FUNDESPOL', blank=True, null=True)
	estado = models.CharField(max_length=5, default="GRBD", choices=ESTADO_CHOICES, blank=True, null=True)
	motivo_anular = models.CharField(max_length=500, blank=True, null=True)
	# ingresos
	se_maestrias = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) 
	se_curs_prog = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	se_conf_even = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	s_arriendos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	aporte_proy = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	cert_tasas_otros = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	dev_est_otros = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) 

	# egresos
	# -------- COSTO DEL SERVICIO - DEDUCIBLES --------
	# honorarios profesionales
	hd_locales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	hd_extranjeros = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	h_prof_dietas = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gasto de personal(docentes y coordinacion academica) en relacion de dependecia
	unif_salarial = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	h_extras = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	bonificaciones = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	dec_ter_sueldo = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	dec_cua_sueldo = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	f_reserva = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	vacaciones = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	aport_patronal = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	ccc_1 = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	ss_tiempo_parcial = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# sueldo personal con nombramiento
	s_pers_nomb = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# suministros y materiales
	md_fisico = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	md_digital = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	copias = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	suministros = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# licencias renovables 
	licencias = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# alimentacion
	s_alimentacion = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	com_salimentacion = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# hospedaje
	s_hopedaje = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	com_shopedaje = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	tasa_per = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# pasajes aereos
	p_nacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	seb_nacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	seguro_nacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	p_internacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	seb_internacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	seguro_internacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# transporte
	transporte = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# seguro estudiantil 
	seg_estud = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de viaje
	v_nacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	v_internacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# capacitacion a docentes 
	cap_docente = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# -------- GASTOS DEDUCIBLES --------
	# gasto de personal(docentes y coordinacion academica) en relacion de dependecia
	gd_unif_salarial = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_h_extras = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_bonificaciones = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_dec_ter_sueldo = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_dec_cua_sueldo = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_f_reserva = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_vacaciones = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_aport_patronal = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_ccc_1 = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_ss_tiempo_parcial = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# honorarios
	gd_h_prof_dietas = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	serv_ocasionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos en servicios administrativos
	correo = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	serv_telef = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	serv_internet = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	vigilancia = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	parqueo = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	unif_personal = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	seg_med = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	susc_memb = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	cap_per_admin = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	serv_biblioteca = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	pasajes_aereos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gastos_viaje = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_alimentacion = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# mantenimiento y reparaciones
	man_rep_generales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	man_rep_equipos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# materiales de ferretería y construccion
	mat_ferreteria = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	#provisiones 
	p_jubil_patr = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	p_desahucio = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	desp_intepestivo = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	prov_cuent_incobrables = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	prov_det_activos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	prov_otras = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# alquiler de equipos
	alq_equipos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# suministros y materiales
	sum_oficina = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	sum_limpieza = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_copias = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# transporte
	gd_transporte = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# seguros y reaseguros (primas y cesiones)
	seg_reaseg = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de jardinería y ornamentación
	mat_jardineria = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	serv_jardineria = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	alim_tortugas = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	med_tortugas = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de marketing
	mat_publicitario = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	pub_impresos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	pub_digitales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	cong_even_fer = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	#comisiones en ventas
	com_ventas = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de acreditacion
	aacsb = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gac_pmi = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	iso = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	amba = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de representacion
	gdrep_hospedaje = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_v_nacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_v_internacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_p_nacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_seb_nacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_seguro_nacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_p_internacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_seb_internacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_seguro_internacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	conv_eventos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de investigacion
	gdinv_capacitacion = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_v_nacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_v_internacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_p_nacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_seb_nacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_seguro_nacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_p_internacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_seb_internacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_seguro_internacionales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	gd_honorarios = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_alimentacion = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_hospedaje = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_susc_memb = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	publicaciones = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	conv_even_proy = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de intereses
	i_banc_local = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	i_pag_local = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	i_pag_no_local = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	#gastos de comisiones bancarias
	com_bancarias = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	com_tarj_cred = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# impuestos, contribuciones y otros
	imp_cont = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos por impuesto
	iva = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	isd = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	ice = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de depreciacion
	d_propiedades = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	d_revaluo_prop = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	d_prop_inversion = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de amortizacion
	g_amortizacion = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	#servicios publicos
	agua = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	luz = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	fono = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# aportes institucionales
	ap_espol = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	ap_fundespol = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# pago por otros bienes y servicios
	pago_otros = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])


	# para la columna de EJECUTADO
	#    |
	#    |
	#    |
	#    v

	# ingresos
	se_maestrias_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) 
	se_curs_prog_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	se_conf_even_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	s_arriendos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	aporte_proy_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	cert_tasas_otros_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	dev_est_otros_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) 

	# egresos
	# -------- COSTO DEL SERVICIO - DEDUCIBLES --------
	# honorarios profesionales
	hd_locales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	hd_extranjeros_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	h_prof_dietas_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gasto de personal(docentes y coordinacion academica) en relacion de dependecia
	unif_salarial_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	h_extras_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	bonificaciones_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	dec_ter_sueldo_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	dec_cua_sueldo_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	f_reserva_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	vacaciones_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	aport_patronal_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	ccc_1_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	ss_tiempo_parcial_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# sueldo personal con nombramiento
	s_pers_nomb_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# suministros y materiales
	md_fisico_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	md_digital_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	copias_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	suministros_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# licencias renovables 
	licencias_ejec= models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# alimentacion
	s_alimentacion_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	com_salimentacion_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# hospedaje
	s_hopedaje_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	com_shopedaje_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	tasa_per_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# pasajes aereos
	p_nacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	seb_nacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	seguro_nacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	p_internacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	seb_internacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	seguro_internacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# transporte
	transporte_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# seguro estudiantil 
	seg_estud_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de viaje
	v_nacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	v_internacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# capacitacion a docentes 
	cap_docente_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# -------- GASTOS DEDUCIBLES --------
	# gasto de personal(docentes y coordinacion academica) en relacion de dependecia
	gd_unif_salarial_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_h_extras_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_bonificaciones_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_dec_ter_sueldo_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_dec_cua_sueldo_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_f_reserva_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_vacaciones_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_aport_patronal_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_ccc_1_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_ss_tiempo_parcial_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# honorarios
	gd_h_prof_dietas_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	serv_ocasionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos en servicios administrativos
	correo_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	serv_telef_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	serv_internet_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	vigilancia_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	parqueo_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	unif_personal_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	seg_med_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	susc_memb_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	cap_per_admin_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	serv_biblioteca_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	pasajes_aereos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gastos_viaje_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_alimentacion_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# mantenimiento y reparaciones
	man_rep_generales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	man_rep_equipos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# materiales de ferretería y construccion
	mat_ferreteria_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	#provisiones 
	p_jubil_patr_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	p_desahucio_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	desp_intepestivo_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	prov_cuent_incobrables_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	prov_det_activos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	prov_otras_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# alquiler de equipos
	alq_equipos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# suministros y materiales
	sum_oficina_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	sum_limpieza_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_copias_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# transporte
	gd_transporte_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# seguros y reaseguros (primas y cesiones)
	seg_reaseg_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de jardinería y ornamentación
	mat_jardineria_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	serv_jardineria_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	alim_tortugas_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	med_tortugas_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de marketing
	mat_publicitario_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	pub_impresos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	pub_digitales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	cong_even_fer_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	com_ventas_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	
	# gastos de acreditacion
	aacsb_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gac_pmi_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	iso_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	amba_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de representacion
	gdrep_hospedaje_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_v_nacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_v_internacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_p_nacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_seb_nacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_seguro_nacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_p_internacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_seb_internacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdrep_seguro_internacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	conv_eventos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de investigacion
	gdinv_capacitacion_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_v_nacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_v_internacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_p_nacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_seb_nacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_seguro_nacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_p_internacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_seb_internacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gdinv_seguro_internacionales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	gd_honorarios_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_alimentacion_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_hospedaje_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	gd_susc_memb_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	publicaciones_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	conv_even_proy_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de intereses
	i_banc_local_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	i_pag_local_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	i_pag_no_local_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	#gastos de comisiones bancarias
	com_bancarias_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	com_tarj_cred_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# impuestos, contribuciones y otros
	imp_cont_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos por impuesto
	iva_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	isd_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	ice_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de depreciacion
	d_propiedades_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	d_revaluo_prop_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	d_prop_inversion_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# gastos de amortizacion
	g_amortizacion_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	#servicios publicos
	agua_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	luz_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	fono_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# aportes institucionales
	ap_espol_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	ap_fundespol_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])

	# pago por otros bienes y servicios
	pago_otros_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo])








# MODELO PARA ESPOLTECH
class Espoltech(models.Model):
	ESTADO_CHOICES = [("GRBD","Grabado"),("ENVD","Enviado"),("AUTR","Autorizado"),("ANLD","Anulado"),]
	año = models.PositiveIntegerField()
	nombre = models.CharField(max_length=100, blank=True)
	centro_costos = models.CharField(max_length=10, default='ESPOLTECH', blank=True, null=True)
	estado = models.CharField(max_length=5, default="GRBD", choices=ESTADO_CHOICES, blank=True, null=True)
	motivo_anular = models.CharField(max_length=500, blank=True, null=True)
	# ingresos corrientes
	vb_serv_tecnicos_espec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #14.03.99
	vb_curs_sem_maes = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #14.03.99
	td_prov_gobcen = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #18.01.01
	td_prov_entdesc = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #18.01.02
	td_prov_entpub = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #18.01.03
	td_prov_gobaut = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #18.01.04
	otros_ingCorr = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #19.04.99

	# ingresos de financimiento
	fondo_autogest = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #37.01.02
	cta_x_cobrar = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #38.01.01

	# ingresos de capital
	td_cap_prov_gobcen = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #28.01.01
	td_cap_prov_entdesc = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #28.01.02
	td_cap_prov_entpub = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #28.01.03
	td_cap_prov_gobaut = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #28.01.04
	don_cap_ext = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #28.03.02

	# gastos corrientes
	# gastos en personal 51
	rem_unificadas = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.01.05
	h_ext_supl = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.05.09
	encargos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.05.13
	dec_ter_sueldo = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.02.03
	dec_cua_sueldo = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.02.04
	aporte_patronal = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.06.01
	fondo_reserva = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.06.02
	comp_desahucio = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.07.04
	comp_vacaciones = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.07.07
	hp_director = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.05.07
	hp_coordinador = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.05.07
	hp_expertos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.05.07
	hp_otros = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.05.07
	hp_dict_clases = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.05.07
	ind_laborales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.07.11

	# bienes y servicios de consumo
	agua = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.01.01
	energia_elec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.01.04
	telecomunicaciones = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.01.05
	correo = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.01.06
	trans_personal = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.02.01
	impresion = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.02.04
	publicidad = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.02.07
	serv_seguridad = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.02.08
	serv_aseo = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.02.09
	membresias = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.02.39
	otros_serv_generales = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.02.99
	pasajes_int = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.03.01
	pasajes_ext = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.03.02
	viaticos_int = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.03.03
	viaticos_ext = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.03.04
	edificios = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.04.02
	gastos_mant_mobil = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.04.03
	gastos_mant_equipos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.04.04
	gastos_mant_vehic = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.04.05
	gastos_libros = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.04.09
	otros_gastos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.04.99
	arr_edificios = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.05.02
	arr_mobiliarios = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.05.03
	arr_maquinaria = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.05.04
	cont_estudios = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.06.01
	serv_capacitacion = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.06.03
	fiscalizacion = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.06.04
	arr_equipos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.07.03
	mant_equipos_info = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.07.04
	serv_alimentacion = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.01
	gastos_vestimenta = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.02
	combustible = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.03
	materiales_ofician = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.04
	materiales_aseo = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.05
	herramientas_53 = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.06
	mat_impresion = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.07
	medicinas = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.09
	mat_laboratorio = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.10
	mat_construccion = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.11
	mat_didacticos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.12
	respuestos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.13
	suministros_agrop = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.14
	otros_bienes = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.99
	mobiliarios_bienes = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.14.03
	maquinaria_equipos_bienes = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.14.04
	equipos_sist_paq_53 = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.14.07
	libros_53 = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.14.09
	partes_repuestos_53 = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.14.11

	# otros gastos corrientes
	iva = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #57.01.01
	tasas = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #57.01.02
	otros_imp = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #57.01.99
	seguros = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #57.02.01
	comisiones_banc = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #57.02.03
	devoluciones = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #57.02.19
	otros_gastos_fin = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #57.02.99

	# transferencias corrientes: aportaciones de acuerdo a lineamientos
	espoltech_ep = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #58.01.03
	part_espol = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #58.01.03
	part_unidad = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #58.01.03

	# gastos capital
	# activos fijos
	mobiliarios = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.03
	maquinaria_equipos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.04
	vehiculos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.05
	herramientas_84 = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.06
	equipos_sist_paq_84 = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.07
	bienes_artisticos = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.08
	libros_84 = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.09
	partes_repuestos_84 = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.11


	# para la columna de EJECUTADO
	#    |
	#    |
	#    |
	#    v


	# ingresos corrientes
	vb_serv_tecnicos_espec_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #14.03.99
	vb_curs_sem_maes_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #14.03.99
	td_prov_gobcen_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #18.01.01
	td_prov_entdesc_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #18.01.02
	td_prov_entpub_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #18.01.03
	td_prov_gobaut_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #18.01.04
	otros_ingCorr_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #19.04.99

	# ingresos de financimiento
	fondo_autogest_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #37.01.02
	cta_x_cobrar_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #38.01.01

	# ingresos de capital
	td_cap_prov_gobcen_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #28.01.01
	td_cap_prov_entdesc_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #28.01.02
	td_cap_prov_entpub_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #28.01.03
	td_cap_prov_gobaut_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #28.01.04
	don_cap_ext_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #28.03.02

	# gastos corrientes
	# gastos en personal 51
	rem_unificadas_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.01.05
	h_ext_supl_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.05.09
	encargos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.05.13
	dec_ter_sueldo_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.02.03
	dec_cua_sueldo_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.02.04
	aporte_patronal_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.06.01
	fondo_reserva_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.06.02
	comp_desahucio_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.07.04
	comp_vacaciones_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.07.07
	hp_director_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.05.07
	hp_coordinador_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.05.07
	hp_expertos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.05.07
	hp_otros_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.05.07
	hp_dict_clases_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.05.07
	ind_laborales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #51.07.11

	# bienes y servicios de consumo
	agua_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.01.01
	energia_elec_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.01.04
	telecomunicaciones_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.01.05
	correo_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.01.06
	trans_personal_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.02.01
	impresion_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.02.04
	publicidad_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.02.07
	serv_seguridad_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.02.08
	serv_aseo_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.02.09
	membresias_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.02.39
	otros_serv_generales_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.02.99
	pasajes_int_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.03.01
	pasajes_ext_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.03.02
	viaticos_int_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.03.03
	viaticos_ext_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.03.04
	edificios_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.04.02
	gastos_mant_mobil_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.04.03
	gastos_mant_equipos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.04.04
	gastos_mant_vehic_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.04.05
	gastos_libros_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.04.09
	otros_gastos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.04.99
	arr_edificios_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.05.02
	arr_mobiliarios_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.05.03
	arr_maquinaria_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.05.04
	cont_estudios_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.06.01
	serv_capacitacion_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.06.03
	fiscalizacion_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.06.04
	arr_equipos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.07.03
	mant_equipos_info_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.07.04
	serv_alimentacion_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.01
	gastos_vestimenta_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.02
	combustible_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.03
	materiales_ofician_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.04
	materiales_aseo_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.05
	herramientas_53_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.06
	mat_impresion_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.07
	medicinas_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.09
	mat_laboratorio_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.10
	mat_construccion_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.11
	mat_didacticos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.12
	respuestos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.13
	suministros_agrop_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.14
	otros_bienes_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.08.99
	mobiliarios_bienes_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.14.03
	maquinaria_equipos_bienes_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.14.04
	equipos_sist_paq_53_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.14.07
	libros_53_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.14.09
	partes_repuestos_53_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #53.14.11

	# otros gastos corrientes
	iva_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #57.01.01
	tasas_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #57.01.02
	otros_imp_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #57.01.99
	seguros_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #57.02.01
	comisiones_banc_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #57.02.03
	devoluciones_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #57.02.19
	otros_gastos_fin_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #57.02.99

	# transferencias corrientes: aportaciones de acuerdo a lineamientos
	espoltech_ep_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #58.01.03
	part_espol_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #58.01.03
	part_unidad_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #58.01.03

	# gastos capital
	# activos fijos
	mobiliarios_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.03
	maquinaria_equipos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.04
	vehiculos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.05
	herramientas_84_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.06
	equipos_sist_paq_84_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.07
	bienes_artisticos_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.08
	libros_84_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.09
	partes_repuestos_84_ejec = models.DecimalField(max_digits=10 ,decimal_places=2,default=Decimal('0.0'), blank=True, null=True, validators=[financiero.validaciones.validate_positivo]) #84.01.11



