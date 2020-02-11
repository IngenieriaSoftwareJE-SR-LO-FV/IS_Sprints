from django import forms
from .models import Fundespol, Espoltech
from datetime import date

class EspoltechForm(forms.ModelForm):
	class Meta:
		model = Espoltech
		fields = '__all__'

		widgets = {
			# ingresos corrientes
			"vb_serv_tecnicos_espec":forms.NumberInput(attrs={'class': "plan"}),
			"vb_curs_sem_maes":forms.NumberInput(attrs={'class': "plan"}),
			"td_prov_gobcen":forms.NumberInput(attrs={'class': "plan"}),
			"td_prov_entdesc":forms.NumberInput(attrs={'class': "plan"}),
			"td_prov_entpub":forms.NumberInput(attrs={'class': "plan"}),
			"td_prov_gobaut":forms.NumberInput(attrs={'class': "plan"}),
			"otros_ingCorr":forms.NumberInput(attrs={'class': "plan"}),

			# ingresos de financimiento
			"fondo_autogest":forms.NumberInput(attrs={'class': "plan"}),
			"cta_x_cobrar":forms.NumberInput(attrs={'class': "plan"}),

			# ingresos de capital
			"td_cap_prov_gobcen":forms.NumberInput(attrs={'class': "plan"}),
			"td_cap_prov_entdesc":forms.NumberInput(attrs={'class': "plan"}),
			"td_cap_prov_entpub":forms.NumberInput(attrs={'class': "plan"}),
			"td_cap_prov_gobaut":forms.NumberInput(attrs={'class': "plan"}),
			"don_cap_ext":forms.NumberInput(attrs={'class': "plan"}),

			# gastos corrientes
			# gastos en personal 51
			"rem_unificadas":forms.NumberInput(attrs={'class': "plan"}),
			"h_ext_supl":forms.NumberInput(attrs={'class': "plan"}),
			"encargos":forms.NumberInput(attrs={'class': "plan"}),
			"dec_ter_sueldo":forms.NumberInput(attrs={'class': "plan"}),
			"dec_cua_sueldo":forms.NumberInput(attrs={'class': "plan"}),
			"aporte_patronal":forms.NumberInput(attrs={'class': "plan"}),
			"fondo_reserva":forms.NumberInput(attrs={'class': "plan"}),
			"comp_desahucio":forms.NumberInput(attrs={'class': "plan"}),
			"comp_vacaciones":forms.NumberInput(attrs={'class': "plan"}),
			"hp_director":forms.NumberInput(attrs={'class': "plan"}),
			"hp_coordinador":forms.NumberInput(attrs={'class': "plan"}),
			"hp_expertos":forms.NumberInput(attrs={'class': "plan"}),
			"hp_otros":forms.NumberInput(attrs={'class': "plan"}),
			"hp_dict_clases":forms.NumberInput(attrs={'class': "plan"}),
			"ind_laborales":forms.NumberInput(attrs={'class': "plan"}),

			# bienes y servicios de consumo
			"agua":forms.NumberInput(attrs={'class': "plan"}),
			"energia_elec":forms.NumberInput(attrs={'class': "plan"}),
			"telecomunicaciones":forms.NumberInput(attrs={'class': "plan"}),
			"correo":forms.NumberInput(attrs={'class': "plan"}),
			"trans_personal":forms.NumberInput(attrs={'class': "plan"}),
			"impresion":forms.NumberInput(attrs={'class': "plan"}),
			"publicidad":forms.NumberInput(attrs={'class': "plan"}),
			"serv_seguridad":forms.NumberInput(attrs={'class': "plan"}),
			"serv_aseo":forms.NumberInput(attrs={'class': "plan"}),
			"membresias":forms.NumberInput(attrs={'class': "plan"}),
			"otros_serv_generales":forms.NumberInput(attrs={'class': "plan"}),
			"pasajes_int":forms.NumberInput(attrs={'class': "plan"}),
			"pasajes_ext":forms.NumberInput(attrs={'class': "plan"}),
			"viaticos_int":forms.NumberInput(attrs={'class': "plan"}),
			"viaticos_ext":forms.NumberInput(attrs={'class': "plan"}),
			"edificios":forms.NumberInput(attrs={'class': "plan"}),
			"gastos_mant_mobil":forms.NumberInput(attrs={'class': "plan"}),
			"gastos_mant_equipos":forms.NumberInput(attrs={'class': "plan"}),
			"gastos_mant_vehic":forms.NumberInput(attrs={'class': "plan"}),
			"gastos_libros":forms.NumberInput(attrs={'class': "plan"}),
			"otros_gastos":forms.NumberInput(attrs={'class': "plan"}),
			"arr_edificios":forms.NumberInput(attrs={'class': "plan"}),
			"arr_mobiliarios":forms.NumberInput(attrs={'class': "plan"}),
			"arr_maquinaria":forms.NumberInput(attrs={'class': "plan"}),
			"cont_estudios":forms.NumberInput(attrs={'class': "plan"}),
			"serv_capacitacion":forms.NumberInput(attrs={'class': "plan"}),
			"fiscalizacion":forms.NumberInput(attrs={'class': "plan"}),
			"arr_equipos":forms.NumberInput(attrs={'class': "plan"}),
			"mant_equipos_info":forms.NumberInput(attrs={'class': "plan"}),
			"serv_alimentacion":forms.NumberInput(attrs={'class': "plan"}),
			"gastos_vestimenta":forms.NumberInput(attrs={'class': "plan"}),
			"combustible":forms.NumberInput(attrs={'class': "plan"}),
			"materiales_ofician":forms.NumberInput(attrs={'class': "plan"}),
			"materiales_aseo":forms.NumberInput(attrs={'class': "plan"}),
			"herramientas_53":forms.NumberInput(attrs={'class': "plan"}),
			"mat_impresion":forms.NumberInput(attrs={'class': "plan"}),
			"medicinas":forms.NumberInput(attrs={'class': "plan"}),
			"mat_laboratorio":forms.NumberInput(attrs={'class': "plan"}),
			"mat_construccion":forms.NumberInput(attrs={'class': "plan"}),
			"mat_didacticos":forms.NumberInput(attrs={'class': "plan"}),
			"respuestos":forms.NumberInput(attrs={'class': "plan"}),
			"suministros_agrop":forms.NumberInput(attrs={'class': "plan"}),
			"otros_bienes":forms.NumberInput(attrs={'class': "plan"}),
			"mobiliarios_bienes":forms.NumberInput(attrs={'class': "plan"}),
			"maquinaria_equipos_bienes":forms.NumberInput(attrs={'class': "plan"}),
			"equipos_sist_paq_53":forms.NumberInput(attrs={'class': "plan"}),
			"libros_53":forms.NumberInput(attrs={'class': "plan"}),
			"partes_repuestos_53":forms.NumberInput(attrs={'class': "plan"}),

			# otros gastos corrientes
			"iva":forms.NumberInput(attrs={'class': "plan"}),
			"tasas":forms.NumberInput(attrs={'class': "plan"}),
			"otros_imp":forms.NumberInput(attrs={'class': "plan"}),
			"seguros":forms.NumberInput(attrs={'class': "plan"}),
			"comisiones_banc":forms.NumberInput(attrs={'class': "plan"}),
			"devoluciones":forms.NumberInput(attrs={'class': "plan"}),
			"otros_gastos_fin":forms.NumberInput(attrs={'class': "plan"}),

			# transferencias corrientes: aportaciones de acuerdo a lineamientos
			"espoltech_ep":forms.NumberInput(attrs={'class': "plan"}),
			"part_espol":forms.NumberInput(attrs={'class': "plan"}),
			"part_unidad":forms.NumberInput(attrs={'class': "plan"}),

			# gastos capital
			# activos fijos
			"mobiliarios":forms.NumberInput(attrs={'class': "plan"}),
			"maquinaria_equipos":forms.NumberInput(attrs={'class': "plan"}),
			"vehiculos":forms.NumberInput(attrs={'class': "plan"}),
			"herramientas_84":forms.NumberInput(attrs={'class': "plan"}),
			"equipos_sist_paq_84":forms.NumberInput(attrs={'class': "plan"}),
			"bienes_artisticos":forms.NumberInput(attrs={'class': "plan"}),
			"libros_84":forms.NumberInput(attrs={'class': "plan"}),
			"partes_repuestos_84":forms.NumberInput(attrs={'class': "plan"}),

			# para la columna de EJECUTADO
			#    |
			#    |
			#    |
			#    v

			# ingresos corrientes
			"vb_serv_tecnicos_espec_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"vb_curs_sem_maes_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"td_prov_gobcen_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"td_prov_entdesc_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"td_prov_entpub_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"td_prov_gobaut_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"otros_ingCorr_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# ingresos de financimiento
			"fondo_autogest_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"cta_x_cobrar_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# ingresos de capital
			"td_cap_prov_gobcen_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"td_cap_prov_entdesc_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"td_cap_prov_entpub_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"td_cap_prov_gobaut_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"don_cap_ext_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# gastos corrientes
			# gastos en personal 51
			"rem_unificadas_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"h_ext_supl_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"encargos_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"dec_ter_sueldo_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"dec_cua_sueldo_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"aporte_patronal_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"fondo_reserva_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"comp_desahucio_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"comp_vacaciones_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"hp_director_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"hp_coordinador_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"hp_expertos_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"hp_otros_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"hp_dict_clases_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"ind_laborales_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# bienes y servicios de consumo
			"agua_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"energia_elec_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"telecomunicaciones_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"correo_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"trans_personal_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"impresion_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"publicidad_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"serv_seguridad_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"serv_aseo_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"membresias_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"otros_serv_generales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"pasajes_int_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"pasajes_ext_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"viaticos_int_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"viaticos_ext_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"edificios_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gastos_mant_mobil_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gastos_mant_equipos_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gastos_mant_vehic_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gastos_libros_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"otros_gastos_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"arr_edificios_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"arr_mobiliarios_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"arr_maquinaria_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"cont_estudios_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"serv_capacitacion_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"fiscalizacion_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"arr_equipos_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"mant_equipos_info_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"serv_alimentacion_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gastos_vestimenta_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"combustible_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"materiales_ofician_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"materiales_aseo_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"herramientas_53_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"mat_impresion_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"medicinas_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"mat_laboratorio_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"mat_construccion_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"mat_didacticos_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"respuestos_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"suministros_agrop_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"otros_bienes_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"mobiliarios_bienes_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"maquinaria_equipos_bienes_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"equipos_sist_paq_53_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"libros_53_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"partes_repuestos_53_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# otros gastos corrientes
			"iva_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"tasas_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"otros_imp_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"seguros_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"comisiones_banc_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"devoluciones_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"otros_gastos_fin_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# transferencias corrientes: aportaciones de acuerdo a lineamientos
			"espoltech_ep_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"part_espol_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"part_unidad_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# gastos capital
			# activos fijos
			"mobiliarios_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"maquinaria_equipos_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"vehiculos_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"herramientas_84_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"equipos_sist_paq_84_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"bienes_artisticos_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"libros_84_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"partes_repuestos_84_ejec":forms.NumberInput(attrs={'class': "ejec"}),


		}



class FundespolForm(forms.ModelForm):
	class Meta:
		model = Fundespol
		fields = '__all__'

		widgets = {
			# ingresos
			"se_maestrias":forms.NumberInput(attrs={'class': "plan"}),
			"se_curs_prog":forms.NumberInput(attrs={'class': "plan"}),
			"se_conf_even":forms.NumberInput(attrs={'class': "plan"}),
			"s_arriendos":forms.NumberInput(attrs={'class': "plan"}),
			"aporte_proy":forms.NumberInput(attrs={'class': "plan"}),
			"cert_tasas_otros":forms.NumberInput(attrs={'class': "plan"}),
			"dev_est_otros":forms.NumberInput(attrs={'class': "plan"}),

			# egresos
			# -------- COSTO DEL SERVICIO - DEDUCIBLES --------
			# honorarios profesionales
			"hd_locales":forms.NumberInput(attrs={'class': "plan"}),
			"hd_extranjeros":forms.NumberInput(attrs={'class': "plan"}),
			"h_prof_dietas":forms.NumberInput(attrs={'class': "plan"}),

			# gasto de personal(docentes y coordinacion academica) en relacion de dependecia
			"unif_salarial":forms.NumberInput(attrs={'class': "plan"}),
			"h_extras":forms.NumberInput(attrs={'class': "plan"}),
			"bonificaciones":forms.NumberInput(attrs={'class': "plan"}),
			"dec_ter_sueldo":forms.NumberInput(attrs={'class': "plan"}),
			"dec_cua_sueldo":forms.NumberInput(attrs={'class': "plan"}),
			"f_reserva":forms.NumberInput(attrs={'class': "plan"}),
			"vacaciones":forms.NumberInput(attrs={'class': "plan"}),
			"aport_patronal":forms.NumberInput(attrs={'class': "plan"}),
			"ccc_1":forms.NumberInput(attrs={'class': "plan"}),
			"ss_tiempo_parcial":forms.NumberInput(attrs={'class': "plan"}),

			# sueldo personal con nombramiento
			"s_pers_nomb":forms.NumberInput(attrs={'class': "plan"}),

			# suministros y materiales
			"md_fisico":forms.NumberInput(attrs={'class': "plan"}),
			"md_digital":forms.NumberInput(attrs={'class': "plan"}),
			"copias":forms.NumberInput(attrs={'class': "plan"}),
			"suministros":forms.NumberInput(attrs={'class': "plan"}),

			# licencias renovables 
			"licencias":forms.NumberInput(attrs={'class': "plan"}),

			# alimentacion
			"s_alimentacion":forms.NumberInput(attrs={'class': "plan"}),
			"com_salimentacion":forms.NumberInput(attrs={'class': "plan"}),

			# hospedaje
			"s_hopedaje":forms.NumberInput(attrs={'class': "plan"}),
			"com_shopedaje":forms.NumberInput(attrs={'class': "plan"}),
			"tasa_per":forms.NumberInput(attrs={'class': "plan"}),

			# pasajes aereos
			"p_nacionales":forms.NumberInput(attrs={'class': "plan"}),
			"seb_nacionales":forms.NumberInput(attrs={'class': "plan"}),
			"seguro_nacionales":forms.NumberInput(attrs={'class': "plan"}),
			"p_internacionales":forms.NumberInput(attrs={'class': "plan"}),
			"seb_internacionales":forms.NumberInput(attrs={'class': "plan"}),
			"seguro_internacionales":forms.NumberInput(attrs={'class': "plan"}),

			# transporte
			"transporte":forms.NumberInput(attrs={'class': "plan"}),

			# seguro estudiantil 
			"seg_estud":forms.NumberInput(attrs={'class': "plan"}),

			# gastos de viaje
			"v_nacionales":forms.NumberInput(attrs={'class': "plan"}),
			"v_internacionales":forms.NumberInput(attrs={'class': "plan"}),

			# capacitacion a docentes 
			"cap_docente":forms.NumberInput(attrs={'class': "plan"}),

			# -------- GASTOS DEDUCIBLES --------
			# gasto de personal(docentes y coordinacion academica) en relacion de dependecia
			"gd_unif_salarial":forms.NumberInput(attrs={'class': "plan"}),
			"gd_h_extras":forms.NumberInput(attrs={'class': "plan"}),
			"gd_bonificaciones":forms.NumberInput(attrs={'class': "plan"}),
			"gd_dec_ter_sueldo":forms.NumberInput(attrs={'class': "plan"}),
			"gd_dec_cua_sueldo":forms.NumberInput(attrs={'class': "plan"}),
			"gd_f_reserva":forms.NumberInput(attrs={'class': "plan"}),
			"gd_vacaciones":forms.NumberInput(attrs={'class': "plan"}),
			"gd_aport_patronal":forms.NumberInput(attrs={'class': "plan"}),
			"gd_ccc_1":forms.NumberInput(attrs={'class': "plan"}),
			"gd_ss_tiempo_parcial":forms.NumberInput(attrs={'class': "plan"}),

			# honorarios
			"gd_h_prof_dietas":forms.NumberInput(attrs={'class': "plan"}),
			"serv_ocasionales":forms.NumberInput(attrs={'class': "plan"}),

			# gastos en servicios administrativos
			"correo":forms.NumberInput(attrs={'class': "plan"}),
			"serv_telef":forms.NumberInput(attrs={'class': "plan"}),
			"serv_internet":forms.NumberInput(attrs={'class': "plan"}),
			"vigilancia":forms.NumberInput(attrs={'class': "plan"}),
			"parqueo":forms.NumberInput(attrs={'class': "plan"}),
			"unif_personal":forms.NumberInput(attrs={'class': "plan"}),
			"seg_med":forms.NumberInput(attrs={'class': "plan"}),
			"susc_memb":forms.NumberInput(attrs={'class': "plan"}),
			"cap_per_admin":forms.NumberInput(attrs={'class': "plan"}),
			"serv_biblioteca":forms.NumberInput(attrs={'class': "plan"}),
			"pasajes_aereos":forms.NumberInput(attrs={'class': "plan"}),
			"gastos_viaje":forms.NumberInput(attrs={'class': "plan"}),
			"gd_alimentacion":forms.NumberInput(attrs={'class': "plan"}),

			# mantenimiento y reparaciones
			"man_rep_generales":forms.NumberInput(attrs={'class': "plan"}),
			"man_rep_equipos":forms.NumberInput(attrs={'class': "plan"}),

			# materiales de ferretería y construccion
			"mat_ferreteria":forms.NumberInput(attrs={'class': "plan"}),

			#provisiones 
			"p_jubil_patr":forms.NumberInput(attrs={'class': "plan"}),
			"p_desahucio":forms.NumberInput(attrs={'class': "plan"}),
			"desp_intepestivo":forms.NumberInput(attrs={'class': "plan"}),
			"prov_cuent_incobrables":forms.NumberInput(attrs={'class': "plan"}),
			"prov_det_activos":forms.NumberInput(attrs={'class': "plan"}),
			"prov_otras":forms.NumberInput(attrs={'class': "plan"}),

			# alquiler de equipos
			"alq_equipos":forms.NumberInput(attrs={'class': "plan"}),

			# suministros y materiales
			"sum_oficina":forms.NumberInput(attrs={'class': "plan"}),
			"sum_limpieza":forms.NumberInput(attrs={'class': "plan"}),
			"gd_copias":forms.NumberInput(attrs={'class': "plan"}),

			# transporte
			"gd_transporte":forms.NumberInput(attrs={'class': "plan"}),

			# seguros y reaseguros (primas y cesiones)
			"seg_reaseg":forms.NumberInput(attrs={'class': "plan"}),

			# gastos de jardinería y ornamentación
			"mat_jardineria":forms.NumberInput(attrs={'class': "plan"}),
			"serv_jardineria":forms.NumberInput(attrs={'class': "plan"}),
			"alim_tortugas":forms.NumberInput(attrs={'class': "plan"}),
			"med_tortugas":forms.NumberInput(attrs={'class': "plan"}),

			# gastos de marketing
			"mat_publicitario":forms.NumberInput(attrs={'class': "plan"}),
			"pub_impresos":forms.NumberInput(attrs={'class': "plan"}),
			"pub_digitales":forms.NumberInput(attrs={'class': "plan"}),
			"cong_even_fer":forms.NumberInput(attrs={'class': "plan"}),

			#comisiones en ventas
			"com_ventas":forms.NumberInput(attrs={'class': "plan"}),

			# gastos de acreditacio
			"aacsb":forms.NumberInput(attrs={'class': "plan"}),
			"gac_pmi":forms.NumberInput(attrs={'class': "plan"}),
			"iso":forms.NumberInput(attrs={'class': "plan"}),
			"amba":forms.NumberInput(attrs={'class': "plan"}),

			# gastos de representacion
			"gdrep_hospedaje":forms.NumberInput(attrs={'class': "plan"}),
			"gdrep_v_nacionales":forms.NumberInput(attrs={'class': "plan"}),
			"gdrep_v_internacionales":forms.NumberInput(attrs={'class': "plan"}),
			"gdrep_p_nacionales":forms.NumberInput(attrs={'class': "plan"}),
			"gdrep_seb_nacionales":forms.NumberInput(attrs={'class': "plan"}),
			"gdrep_seguro_nacionales":forms.NumberInput(attrs={'class': "plan"}),
			"gdrep_p_internacionales":forms.NumberInput(attrs={'class': "plan"}),
			"gdrep_seb_internacionales":forms.NumberInput(attrs={'class': "plan"}),
			"gdrep_seguro_internacionales":forms.NumberInput(attrs={'class': "plan"}),
			"conv_eventos":forms.NumberInput(attrs={'class': "plan"}),

			# gastos de investigacion
			"gdinv_capacitacion":forms.NumberInput(attrs={'class': "plan"}),
			"gdinv_v_nacionales":forms.NumberInput(attrs={'class': "plan"}),
			"gdinv_v_internacionales":forms.NumberInput(attrs={'class': "plan"}),
			"gdinv_p_nacionales":forms.NumberInput(attrs={'class': "plan"}),
			"gdinv_seb_nacionales":forms.NumberInput(attrs={'class': "plan"}),
			"gdinv_seguro_nacionales":forms.NumberInput(attrs={'class': "plan"}),
			"gdinv_p_internacionales":forms.NumberInput(attrs={'class': "plan"}),
			"gdinv_seb_internacionales":forms.NumberInput(attrs={'class': "plan"}),
			"gdinv_seguro_internacionales":forms.NumberInput(attrs={'class': "plan"}),

			"gd_honorarios":forms.NumberInput(attrs={'class': "plan"}),
			"gd_alimentacion":forms.NumberInput(attrs={'class': "plan"}),
			"gd_hospedaje":forms.NumberInput(attrs={'class': "plan"}),
			"gd_susc_memb":forms.NumberInput(attrs={'class': "plan"}),
			"publicaciones":forms.NumberInput(attrs={'class': "plan"}),
			"conv_even_proy":forms.NumberInput(attrs={'class': "plan"}),

			# gastos de intereses
			"i_banc_local":forms.NumberInput(attrs={'class': "plan"}),
			"i_pag_local":forms.NumberInput(attrs={'class': "plan"}),
			"i_pag_no_local":forms.NumberInput(attrs={'class': "plan"}),

			#gastos de comisiones bancarias
			"com_bancarias":forms.NumberInput(attrs={'class': "plan"}),
			"com_tarj_cred":forms.NumberInput(attrs={'class': "plan"}),

			# impuestos, contribuciones y otros
			"imp_cont":forms.NumberInput(attrs={'class': "plan"}),

			"# gastos por impuest":forms.NumberInput(attrs={'class': "plan"}),
			"iva":forms.NumberInput(attrs={'class': "plan"}),
			"isd":forms.NumberInput(attrs={'class': "plan"}),
			"ice":forms.NumberInput(attrs={'class': "plan"}),

			# gastos de depreciacion
			"d_propiedades":forms.NumberInput(attrs={'class': "plan"}),
			"d_revaluo_prop":forms.NumberInput(attrs={'class': "plan"}),
			"d_prop_inversion":forms.NumberInput(attrs={'class': "plan"}),

			# gastos de amortizacion
			"g_amortizacion":forms.NumberInput(attrs={'class': "plan"}),

			"#servicios publico":forms.NumberInput(attrs={'class': "plan"}),
			"agua":forms.NumberInput(attrs={'class': "plan"}),
			"luz":forms.NumberInput(attrs={'class': "plan"}),
			"fono":forms.NumberInput(attrs={'class': "plan"}),

			# aportes institucionales
			"ap_espol":forms.NumberInput(attrs={'class': "plan"}),
			"ap_fundespol":forms.NumberInput(attrs={'class': "plan"}),

			# pago por otros bienes y servicios
			"pago_otros":forms.NumberInput(attrs={'class': "plan"}),

			# para la columna de EJECUTADO
			#    |
			#    |
			#    |
			#    v

			# ingresos
			"se_maestrias_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"se_curs_prog_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"se_conf_even_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"s_arriendos_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"aporte_proy_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"cert_tasas_otros_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"dev_est_otros_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# egresos
			# -------- COSTO DEL SERVICIO - DEDUCIBLES --------
			# honorarios profesionales
			"hd_locales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"hd_extranjeros_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"h_prof_dietas_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# gasto de personal(docentes y coordinacion academica) en relacion de dependecia
			"unif_salarial_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"h_extras_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"bonificaciones_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"dec_ter_sueldo_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"dec_cua_sueldo_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"f_reserva_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"vacaciones_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"aport_patronal_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"ccc_1_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"ss_tiempo_parcial_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# sueldo personal con nombramiento
			"s_pers_nomb_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# suministros y materiales
			"md_fisico_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"md_digital_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"copias_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"suministros_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# licencias renovables 
			"licencias_eje":forms.NumberInput(attrs={'class': "ejec"}),

			# alimentacion
			"s_alimentacion_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"com_salimentacion_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# hospedaje
			"s_hopedaje_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"com_shopedaje_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"tasa_per_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# pasajes aereos
			"p_nacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"seb_nacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"seguro_nacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"p_internacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"seb_internacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"seguro_internacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# transporte
			"transporte_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# seguro estudiantil 
			"seg_estud_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# gastos de viaje
			"v_nacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"v_internacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# capacitacion a docentes 
			"cap_docente_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# -------- GASTOS DEDUCIBLES --------
			# gasto de personal(docentes y coordinacion academica) en relacion de dependecia
			"gd_unif_salarial_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gd_h_extras_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gd_bonificaciones_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gd_dec_ter_sueldo_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gd_dec_cua_sueldo_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gd_f_reserva_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gd_vacaciones_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gd_aport_patronal_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gd_ccc_1_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gd_ss_tiempo_parcial_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# honorarios
			"gd_h_prof_dietas_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"serv_ocasionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# gastos en servicios administrativos
			"correo_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"serv_telef_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"serv_internet_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"vigilancia_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"parqueo_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"unif_personal_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"seg_med_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"susc_memb_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"cap_per_admin_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"serv_biblioteca_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"pasajes_aereos_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gastos_viaje_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gd_alimentacion_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# mantenimiento y reparaciones
			"man_rep_generales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"man_rep_equipos_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# materiales de ferretería y construccion
			"mat_ferreteria_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			#provisiones 
			"p_jubil_patr_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"p_desahucio_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"desp_intepestivo_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"prov_cuent_incobrables_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"prov_det_activos_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"prov_otras_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# alquiler de equipos
			"alq_equipos_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# suministros y materiales
			"sum_oficina_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"sum_limpieza_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gd_copias_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# transporte
			"gd_transporte_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# seguros y reaseguros (primas y cesiones)
			"seg_reaseg_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# gastos de jardinería y ornamentación
			"mat_jardineria_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"serv_jardineria_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"alim_tortugas_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"med_tortugas_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# gastos de marketing
			"mat_publicitario_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"pub_impresos_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"pub_digitales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"cong_even_fer_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			"com_ventas_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			
			# gastos de acreditacion
			"aacsb_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gac_pmi_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"iso_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"amba_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# gastos de representacion
			"gdrep_hospedaje_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdrep_v_nacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdrep_v_internacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdrep_p_nacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdrep_seb_nacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdrep_seguro_nacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdrep_p_internacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdrep_seb_internacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdrep_seguro_internacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"conv_eventos_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# gastos de investigacion
			"gdinv_capacitacion_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdinv_v_nacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdinv_v_internacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdinv_p_nacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdinv_seb_nacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdinv_seguro_nacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdinv_p_internacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdinv_seb_internacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gdinv_seguro_internacionales_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			"gd_honorarios_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gd_alimentacion_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gd_hospedaje_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"gd_susc_memb_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"publicaciones_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"conv_even_proy_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# gastos de intereses
			"i_banc_local_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"i_pag_local_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"i_pag_no_local_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			#gastos de comisiones bancarias
			"com_bancarias_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"com_tarj_cred_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# impuestos, contribuciones y otros
			"imp_cont_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# gastos por impuesto
			"iva_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"isd_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"ice_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# gastos de depreciacion
			"d_propiedades_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"d_revaluo_prop_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"d_prop_inversion_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# gastos de amortizacion
			"g_amortizacion_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			#servicios publicos
			"agua_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"luz_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"fono_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# aportes institucionales
			"ap_espol_ejec":forms.NumberInput(attrs={'class': "ejec"}),
			"ap_fundespol_ejec":forms.NumberInput(attrs={'class': "ejec"}),

			# pago por otros bienes y servicios
			"pago_otros_ejec":forms.NumberInput(attrs={'class': "ejec"}),
		}
