from django.db import models
import financiero.validaciones

# MODELO PARA FUNDESPOL
class Fundespol(models.Model):
	# ingresos
	se_maestrias = 
	se_curs_prog =
	se_conf_even =
	s_arriendos =
	aporte_proy =
	cert_tasas_otros =
	dev_est_otros = 

	# egresos
	# -------- COSTO DEL SERVICIO - DEDUCIBLES --------
	# honorarios profesionales
	hd_locales =
	hd_extranjeros =
	h_prof_dietas =

	# gasto de personal(docentes y coordinacion academica) en relacion de dependecia
	unif_salarial =
	h_extras =
	bonificaciones =
	dec_ter_sueldo =
	dec_cua_sueldo =
	f_reserva =
	vacaciones =
	aport_patronal =
	ccc_1 =
	ss_tiempo_parcial =

	# sueldo personal con nombramiento
	s_pers_nomb =

	# suministros y materiales
	md_fisico =
	md_digital =
	copias =
	suministros =

	# licencias renovables 
	licencias =

	# alimentacion
	s_alimentacion =
	com_salimentacion =

	# hospedaje
	s_hopedaje =
	com_shopedaje =
	tasa_per =

	# pasajes aereos
	p_nacionales =
	seb_nacionales =
	seguro_nacionales
	p_internacionales =
	seb_internacionales =
	seguro_internacionales =

	# transporte
	transporte =

	# seguro estudiantil 
	seg_estud =

	# gastos de viaje
	v_nacionales =
	v_internacionales =

	# capacitacion a docentes 
	cap_docente =

	# -------- GASTOS DEDUCIBLES --------
	# gasto de personal(docentes y coordinacion academica) en relacion de dependecia
	gd_unif_salarial =
	gd_h_extras =
	gd_bonificaciones =
	gd_dec_ter_sueldo =
	gd_dec_cua_sueldo =
	gd_f_reserva =
	gd_vacaciones =
	gd_aport_patronal =
	gd_ccc_1 =
	gd_ss_tiempo_parcial =

	# honorarios
	gd_h_prof_dietas =
	serv_ocasionales =

	# gastos en servicios administrativos
	correo =
	serv_telef =
	serv_internet =
	vigilancia =
	parqueo =
	unif_personal =
	seg_med =
	susc_memb =
	cap_per_admin =
	serv_biblioteca =
	pasajes_aereos =
	gd_alimentacion =

	# mantenimiento y reparaciones
	man_rep_generales =
	man_rep_equipos =

	# materiales de ferretería y construccion
	mat_ferreteria =

	#provisiones 
	p_jubil_patr =
	p_desahucio =
	desp_intepestivo =
	prov_cuent_incobrables =
	prov_det_activos =
	prov_otras =

	# alquiler de equipos
	alq_equipos =

	# suministros y materiales
	sum_oficina =
	sum_limpieza =
	gd_copias =

	# transporte
	gd_transporte =

	# seguros y reaseguros (primas y cesiones)
	seg_reaseg =

	# gastos de jardinería y ornamentación
	mat_jardineria =
	serv_jardineria =
	alim_tortugas =
	med_tortugas =

	# gastos de marketing
	mat_publicitario =
	pub_impresos =
	pub_digitales =
	cong_even_fer =

	# gastos de acreditacion
	aacsb =
	gac_pmi =
	iso =
	amba =

	# gastos de representacion
	gdrep_hospedaje =
	gdrep_v_nacionales =
	gdrep_v_internacionales =
	gdrep_p_nacionales =
	gdrep_seb_nacionales =
	gdrep_seguro_nacionales
	gdrep_p_internacionales =
	gdrep_seb_internacionales =
	gdrep_seguro_internacionales =
	conv_eventos =

	# gastos de investigacion
	gdinv_capacitacion =
	gdinv_v_nacionales =
	gdinv_v_internacionales =
	gdinv_p_nacionales =
	gdinv_seb_nacionales =
	gdinv_seguro_nacionales
	gdinv_p_internacionales =
	gdinv_seb_internacionales =
	gdinv_seguro_internacionales =

	gd_honorarios =
	gd_alimentacion =
	gd_hospedaje =
	gd_susc_memb =
	publicaciones =
	conv_even_proy =

	# gastos de intereses
	i_banc_local =
	i_pag_local =
	i_pag_no_local =

	#gastos de comisiones bancarias
	com_bancarias =
	com_tarj_cred =

	# impuestos, contribuciones y otros
	imp_cont =

	# gastos por impuesto
	iva =
	isd =
	ice =

	# gastos de depreciacion
	d_propiedades =
	d_revaluo_prop =
	d_prop_inversion =

	# gastos de amortizacion
	g_amortizacion =

	#servicios publicos
	agua =
	luz =
	fono =

	# aportes institucionales
	ap_espol =
	ap_fundespol =

	#pago por otros bienes y servicios
	pago_otros =


# MODELO PARA ESPOLTECH
class Espoltech(models.Model):
	# ingresos corrientes
	vb_serv_tecnicos_espec = #14.03.99
	vb_curs_sem_maes = #14.03.99
	td_prov_gobcen = #18.01.01
	td_prov_entdesc = #18.01.02
	td_prov_entpub = #18.01.03
	td_prov_gobaut = #18.01.04
	otros_ingCorr = #19.04.99

	# ingresos de financimiento
	fondo_autogest = #37.01.02
	cta_x_cobrar = #38.01.01

	# ingresos de capital
	td_cap_prov_gobcen = #28.01.01
	td_cap_prov_entdesc = #28.01.02
	td_cap_prov_entpub = #28.01.03
	td_cap_prov_gobaut = #28.01.04
	don_cap_ext = #28.03.02

	# gastos corrientes
	# gastos en personal 51
	rem_unificadas = #51.01.05
	h_ext_supl = #51.05.09
	encargos = #51.05.13
	dec_ter_sueldo = #51.02.03
	dec_cua_sueldo = #51.02.04
	aporte_patronal = #51.06.01
	fondo_reserva = #51.06.02
	comp_desahucio = #51.07.04
	comp_vacaciones = #51.07.07
	hp_director = #51.05.07
	hp_coordinador = #51.05.07
	hp_expertos = #51.05.07
	hp_otros = #51.05.07
	hp_dict_clases = #51.05.07
	ind_laborales = #51.07.11

	# bienes y servicios de consumo
	agua = #53.01.01
	energia_elec = #53.01.04
	telecomunicaciones = #53.01.05
	correo = #53.01.06
	trans_personal = #53.02.01
	impresion = #53.02.04
	publicidad = #53.02.07
	serv_seguridad = #53.02.08
	serv_aseo = #53.02.09
	membresias = #53.02.39
	otros_serv_generales = #53.02.99
	pasajes_int = #53.03.01
	pasajes_ext = #53.03.02
	viaticos_int = #53.03.03
	viaticos_ext = #53.03.04
	edificios = #53.04.02
	gastos_mant_mobil = #53.04.03
	gastos_mant_equipos = #53.04.04
	gastos_mant_vehic = #53.04.05
	gastos_libros = #53.04.09
	otros_gastos = #53.04.99
	arr_edificios = #53.05.02
	arr_mobiliarios = #53.05.03
	arr_maquinaria = #53.05.04
	cont_estudios = #53.06.01
	serv_capacitacion = #53.06.03
	fiscalizacion = #53.06.04
	arr_equipos = #53.07.03
	mant_equipos_info = #53.07.04
	serv_alimentacion = #53.08.01
	gastos_vestimenta = #53.08.02
	combustible = #53.08.03
	materiales_ofician = #53.08.04
	materiales_aseo = #53.08.05
	herramientas_53 = #53.08.06
	mat_impresion = #53.08.07
	medicinas = #53.08.09
	mat_laboratorio = #53.08.10
	mat_construccion = #53.08.11
	mat_didacticos = #53.08.12
	respuestos = #53.08.13
	suministros_agrop = #53.08.14
	otros_bienes = #53.08.99
	mobiliarios_bienes = #53.14.03
	maquinaria_equipos_bienes = #53.14.04
	equipos_sist_paq_53 = #53.14.07
	libros_53 = #53.14.09
	partes_repuestos_53 = #53.14.11

	# otros gastos corrientes
	iva = #57.01.01
	tasas = #57.01.02
	otros_imp = #57.01.99
	seguros = #57.02.01
	comisiones_banc = #57.02.03
	devoluciones = #57.02.19
	otros_gastos_fin = #57.02.99

	# transferencias corrientes: aportaciones de acuerdo a lineamientos
	espoltech_ep = #58.01.03
	part_espol = #58.01.03
	part_unidad = #58.01.03

	# gastos capital
	# activos fijos
	mobiliarios = #84.01.03
	maquinaria_equipos = #84.01.04
	vehiculos = #84.01.05
	herramientas_84 = #84.01.06
	equipos_sist_paq_84 = #84.01.07
	bienes_artisticos = #84.01.08
	libros_84 = #84.01.09
	partes_repuestos_84 = #84.01.11






