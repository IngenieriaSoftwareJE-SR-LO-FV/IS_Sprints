function suma_valores(){
	var res = 0.0;
	for(i = 0; i < arguments.length; i++){
		if(arguments[i]!=""){
			res = res+parseFloat(arguments[i]);
		}
	}
	return res;
}

	//INGRESOS
	$(document).ready(function(){
		var v1 = document.getElementById("id_se_maestrias").value;
		var v2 = document.getElementById("id_se_curs_prog").value;
		var v3 = document.getElementById("id_se_conf_even").value;
		var v4 = document.getElementById("id_s_arriendos").value;
		var v5 = document.getElementById("id_aporte_proy").value;
		var v6 = document.getElementById("id_cert_tasas_otros").value;
		var v7 = document.getElementById("id_dev_est_otros").value;
		var res = suma_valores(v1,v2,v3,v4,v5,v6,v7);
		document.getElementById("id_total_ingresos").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_se_maestrias_ejec").value;
		var v2 = document.getElementById("id_se_curs_prog_ejec").value;
		var v3 = document.getElementById("id_se_conf_even_ejec").value;
		var v4 = document.getElementById("id_s_arriendos_ejec").value;
		var v5 = document.getElementById("id_aporte_proy_ejec").value;
		var v6 = document.getElementById("id_cert_tasas_otros_ejec").value;
		var v7 = document.getElementById("id_dev_est_otros_ejec").value;
		var res = suma_valores(v1,v2,v3,v4,v5,v6,v7);
		document.getElementById("id_total_ingresos_ejec").value = res;
	});

	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------

	//COSTOS DEL SERVICIO - DEDUCIBLES
	$(document).ready(function(){
		var v1 = document.getElementById("id_h_profesionales").value;
		var v2 = document.getElementById("id_g_personal").value;
		var v3 = document.getElementById("id_s_pers_nomb").value;
		var v4 = document.getElementById("id_sum_mat").value;
		var v5 = document.getElementById("id_licencias").value;
		var v6 = document.getElementById("id_alimentacion").value;
		var v7 = document.getElementById("id_hosp").value;
		var v8 = document.getElementById("id_pareos").value;
		var v9 = document.getElementById("id_transporte").value;
		var v10 = document.getElementById("id_seg_estud").value;
		var v11 = document.getElementById("id_gastosviaje").value;
		var v12 = document.getElementById("id_cap_docente").value;
		var res = suma_valores(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12);
		document.getElementById("id_costos_deducibles").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_h_profesionales_ejec").value;
		var v2 = document.getElementById("id_g_personal_ejec").value;
		var v3 = document.getElementById("id_s_pers_nomb_ejec").value;
		var v4 = document.getElementById("id_sum_mat_ejec").value;
		var v5 = document.getElementById("id_licencias_ejec").value;
		var v6 = document.getElementById("id_alimentacion_ejec").value;
		var v7 = document.getElementById("id_hosp_ejec").value;
		var v8 = document.getElementById("id_pareos_ejec").value;
		var v9 = document.getElementById("id_transporte_ejec").value;
		var v10 = document.getElementById("id_seg_estud_ejec").value;
		var v11 = document.getElementById("id_gastosviaje_ejec").value;
		var v12 = document.getElementById("id_cap_docente_ejec").value;
		var res = suma_valores(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12);
		document.getElementById("id_costos_deducibles_ejec").value = res;
	});

	//HONORARIOS PROFESIONALES - DOCENTES
	$(document).ready(function(){
		var v1 = document.getElementById("id_hd_locales").value;
		var v2 = document.getElementById("id_hd_extranjeros").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_hp_docentes").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_hd_locales_ejec").value;
		var v2 = document.getElementById("id_hd_extranjeros_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_hp_docentes_ejec").value = res;
	});

	//HONORARIOS PROFESIONALES
	$(document).ready(function(){
		var v1 = document.getElementById("id_hp_docentes").value;
		var v2 = document.getElementById("id_h_prof_dietas").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_h_profesionales").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_hp_docentes_ejec").value;
		var v2 = document.getElementById("id_h_prof_dietas_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_h_profesionales_ejec").value = res;
	});

	//SUELDOS, SALARIOS Y DEMÁS REMUNERACIONES
	$(document).ready(function(){
		var v1 = document.getElementById("id_unif_salarial").value;
		var v2 = document.getElementById("id_h_extras").value;
		var v3 = document.getElementById("id_bonificaciones").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_suel_sal_rem").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_unif_salarial_ejec").value;
		var v2 = document.getElementById("id_h_extras_ejec").value;
		var v3 = document.getElementById("id_bonificaciones_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_suel_sal_rem_ejec").value = res;
	});

	//BENEFICIOS SOCIALES, INDEMNIZACIONES Y OTRAS REMUNERACIONES
	$(document).ready(function(){
		var v1 = document.getElementById("id_dec_ter_sueldo").value;
		var v2 = document.getElementById("id_dec_cua_sueldo").value;
		var v3 = document.getElementById("id_f_reserva").value;
		var v4 = document.getElementById("id_vacaciones").value;
		var res = suma_valores(v1,v2,v3,v4);
		document.getElementById("id_ben_iden_rem").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_dec_ter_sueldo_ejec").value;
		var v2 = document.getElementById("id_dec_cua_sueldo_ejec").value;
		var v3 = document.getElementById("id_f_reserva_ejec").value;
		var v4 = document.getElementById("id_vacaciones_ejec").value;
		var res = suma_valores(v1,v2,v3,v4);
		document.getElementById("id_ben_iden_rem_ejec").value = res;
	});

	//APORTE A LA SEGURIDAD SOCIAL
	$(document).ready(function(){
		var v1 = document.getElementById("id_aport_patronal").value;
		var v2 = document.getElementById("id_ccc_1").value;
		var v3 = document.getElementById("id_ss_tiempo_parcial").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_ap_seg_soc").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_aport_patronal_ejec").value;
		var v2 = document.getElementById("id_ccc_1_ejec").value;
		var v3 = document.getElementById("id_ss_tiempo_parcial_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_ap_seg_soc_ejec").value = res;
	});

	//GASTOS DE PERSONAL EN RELACION DE DEPENDENCIA
	$(document).ready(function(){
		var v1 = document.getElementById("id_suel_sal_rem").value;
		var v2 = document.getElementById("id_ben_iden_rem").value;
		var v3 = document.getElementById("id_ap_seg_soc").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_g_personal").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_suel_sal_rem_ejec").value;
		var v2 = document.getElementById("id_ben_iden_rem_ejec").value;
		var v3 = document.getElementById("id_ap_seg_soc_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_g_personal_ejec").value = res;
	});

	//SUMINISTROS Y MATERIALES
	$(document).ready(function(){
		var v1 = document.getElementById("id_md_fisico").value;
		var v2 = document.getElementById("id_md_digital").value;
		var v3 = document.getElementById("id_copias").value;
		var v4 = document.getElementById("id_suministros").value;
		var res = suma_valores(v1,v2,v3,v4);
		document.getElementById("id_sum_mat").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_md_fisico_ejec").value;
		var v2 = document.getElementById("id_md_digital_ejec").value;
		var v3 = document.getElementById("id_copias_ejec").value;
		var v4 = document.getElementById("id_suministros_ejec").value;
		var res = suma_valores(v1,v2,v3,v4);
		document.getElementById("id_sum_mat_ejec").value = res;
	});

	//ALIMENTACIÓN
	$(document).ready(function(){
		var v1 = document.getElementById("id_s_alimentacion").value;
		var v2 = document.getElementById("id_com_salimentacion").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_alimentacion").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_s_alimentacion_ejec").value;
		var v2 = document.getElementById("id_com_salimentacion_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_alimentacion_ejec").value = res;
	});

	//HOSPEDAJE
	$(document).ready(function(){
		var v1 = document.getElementById("id_s_hopedaje").value;
		var v2 = document.getElementById("id_com_shopedaje").value;
		var v3 = document.getElementById("id_tasa_per").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_hosp").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_s_hopedaje_ejec").value;
		var v2 = document.getElementById("id_com_shopedaje_ejec").value;
		var v3 = document.getElementById("id_tasa_per_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_hosp_ejec").value = res;
	});

	//PASAJES NACIONALES
	$(document).ready(function(){
		var v1 = document.getElementById("id_p_nacionales").value;
		var v2 = document.getElementById("id_seb_nacionales").value;
		var v3 = document.getElementById("id_seguro_nacionales").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_pnacional").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_p_nacionales_ejec").value;
		var v2 = document.getElementById("id_seb_nacionales_ejec").value;
		var v3 = document.getElementById("id_seguro_nacionales_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_pnacional_ejec").value = res;
	});

	//PASAJES INTERNACIONALES
	$(document).ready(function(){
		var v1 = document.getElementById("id_p_internacionales").value;
		var v2 = document.getElementById("id_seb_internacionales").value;
		var v3 = document.getElementById("id_seguro_internacionales").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_pinternacional").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_p_internacionales_ejec").value;
		var v2 = document.getElementById("id_seb_internacionales_ejec").value;
		var v3 = document.getElementById("id_seguro_internacionales_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_pinternacional_ejec").value = res;
	});

	//PASAJES AREOS
	$(document).ready(function(){
		var v1 = document.getElementById("id_pnacional").value;
		var v2 = document.getElementById("id_pinternacional").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_pareos").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_pnacional_ejec").value;
		var v2 = document.getElementById("id_pinternacional_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_pareos_ejec").value = res;
	});

	//GASTOS DE VIAJE
	$(document).ready(function(){
		var v1 = document.getElementById("id_v_nacionales").value;
		var v2 = document.getElementById("id_v_internacionales").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_gastosviaje").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_v_nacionales_ejec").value;
		var v2 = document.getElementById("id_v_internacionales_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_gastosviaje_ejec").value = res;
	});

	
	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------
	
	//GASTOS DEDUCIBLES
	$(document).ready(function(){
		var v1 = document.getElementById("id_gd_gast_pers").value;
		var v2 = document.getElementById("id_honorarios").value;
		var v3 = document.getElementById("id_gas_ser_admin").value;
		var v4 = document.getElementById("id_mant_rep").value;
		var v5 = document.getElementById("id_mat_ferreteria").value;
		var v6 = document.getElementById("id_prov").value;
		var v7 = document.getElementById("id_alq_eqpos").value;
		var v8 = document.getElementById("id_gd_sum_mat").value;
		var v9 = document.getElementById("id_gd_transporte").value;
		var v10 = document.getElementById("id_seg_reaseg").value;
		var v11 = document.getElementById("id_gas_jar_orn").value;
		var v12 = document.getElementById("id_gast_mark").value;
		var v13 = document.getElementById("id_gast_acred").value;
		var v14 = document.getElementById("id_gas_repre").value;
		var v15 = document.getElementById("id_gdinv").value;
		var v16 = document.getElementById("id_gast_interes").value;
		var v17 = document.getElementById("id_gas_com_ban").value;
		var v18 = document.getElementById("id_imp_cont").value;
		var v19 = document.getElementById("id_gas_impu").value;
		var v20 = document.getElementById("id_gas_depre").value;
		var v21 = document.getElementById("id_g_amortizacion").value;
		var v22 = document.getElementById("id_serv_pub").value;
		var v23 = document.getElementById("id_aport_inst").value;
		var v24 = document.getElementById("id_pago_otros").value;
		var res = suma_valores(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24);
		document.getElementById("id_gdeducibles").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gd_gast_pers_ejec").value;
		var v2 = document.getElementById("id_honorarios_ejec").value;
		var v3 = document.getElementById("id_gas_ser_admin_ejec").value;
		var v4 = document.getElementById("id_mant_rep_ejec").value;
		var v5 = document.getElementById("id_mat_ferreteria_ejec").value;
		var v6 = document.getElementById("id_prov_ejec").value;
		var v7 = document.getElementById("id_alq_eqpos_ejec").value;
		var v8 = document.getElementById("id_gd_sum_mat_ejec").value;
		var v9 = document.getElementById("id_gd_transporte_ejec").value;
		var v10 = document.getElementById("id_seg_reaseg_ejec").value;
		var v11 = document.getElementById("id_gas_jar_orn_ejec").value;
		var v12 = document.getElementById("id_gast_mark_ejec").value;
		var v13 = document.getElementById("id_gast_acred_ejec").value;
		var v14 = document.getElementById("id_gas_repre_ejec").value;
		var v15 = document.getElementById("id_gdinv_ejec").value;
		var v16 = document.getElementById("id_gast_interes_ejec").value;
		var v17 = document.getElementById("id_gas_com_ban_ejec").value;
		var v18 = document.getElementById("id_imp_cont_ejec").value;
		var v19 = document.getElementById("id_gas_impu_ejec").value;
		var v20 = document.getElementById("id_gas_depre_ejec").value;
		var v21 = document.getElementById("id_g_amortizacion_ejec").value;
		var v22 = document.getElementById("id_serv_pub_ejec").value;
		var v23 = document.getElementById("id_aport_inst_ejec").value;
		var v24 = document.getElementById("id_pago_otros_ejec").value;
		var res = suma_valores(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24);
		document.getElementById("id_gdeducibles_ejec").value = res;
	});

	//SUELDO, SALARIOS  Y DEMAS REMUNERACIONES
	$(document).ready(function(){
		var v1 = document.getElementById("id_gd_unif_salarial").value;
		var v2 = document.getElementById("id_gd_h_extras").value;
		var v3 = document.getElementById("id_gd_bonificaciones").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gd_suel_sal_rem").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gd_unif_salarial_ejec").value;
		var v2 = document.getElementById("id_gd_h_extras_ejec").value;
		var v3 = document.getElementById("id_gd_bonificaciones_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gd_suel_sal_rem_ejec").value = res;
	});
	
	//BENEFICIOS SOCIALES, INDEMNIZACIONES Y OTRAS REMUNERACIONES
	$(document).ready(function(){
		var v1 = document.getElementById("id_gd_dec_ter_sueldo").value;
		var v2 = document.getElementById("id_gd_dec_cua_sueldo").value;
		var v3 = document.getElementById("id_gd_f_reserva").value;
		var v4 = document.getElementById("id_gd_vacaciones").value;
		var res = suma_valores(v1,v2,v3,v4);
		document.getElementById("id_gd_ben_iden_rem").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gd_dec_ter_sueldo_ejec").value;
		var v2 = document.getElementById("id_gd_dec_cua_sueldo_ejec").value;
		var v3 = document.getElementById("id_gd_f_reserva_ejec").value;
		var v4 = document.getElementById("id_gd_vacaciones_ejec").value;
		var res = suma_valores(v1,v2,v3,v4);
		document.getElementById("id_gd_ben_iden_rem_ejec").value = res;
	});

	//APORTE A LA SEGURIDAD SOCIAL 
	$(document).ready(function(){
		var v1 = document.getElementById("id_gd_aport_patronal").value;
		var v2 = document.getElementById("id_gd_ccc_1").value;
		var v3 = document.getElementById("id_gd_ss_tiempo_parcial").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gd_ap_seg_soc").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gd_aport_patronal_ejec").value;
		var v2 = document.getElementById("id_gd_ccc_1_ejec").value;
		var v3 = document.getElementById("id_gd_ss_tiempo_parcial_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gd_ap_seg_soc_ejec").value = res;
	});

	//GASTOS DE PERSONAL CON RELACION DE DEPENDENCIA - GASTOS DEDUCIBLES
	$(document).ready(function(){
		var v1 = document.getElementById("id_gd_suel_sal_rem").value;
		var v2 = document.getElementById("id_gd_ben_iden_rem").value;
		var v3 = document.getElementById("id_gd_ap_seg_soc").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gd_gast_pers").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gd_suel_sal_rem_ejec").value;
		var v2 = document.getElementById("id_gd_ben_iden_rem_ejec").value;
		var v3 = document.getElementById("id_gd_ap_seg_soc_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gd_gast_pers_ejec").value = res;
	});

	//HONORARIOS
	$(document).ready(function(){
		var v1 = document.getElementById("id_gd_h_prof_dietas").value;
		var v2 = document.getElementById("id_serv_ocasionales").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_honorarios").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gd_h_prof_dietas_ejec").value;
		var v2 = document.getElementById("id_serv_ocasionales_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_honorarios_ejec").value = res;
	});

	//GASTOS EN SERVICIOS ADMINISTRATIVOS
	$(document).ready(function(){
		var v1 = document.getElementById("id_correo").value;
		var v2 = document.getElementById("id_serv_telef").value;
		var v3 = document.getElementById("id_serv_internet").value;
		var v4 = document.getElementById("id_vigilancia").value;
		var v5 = document.getElementById("id_parqueo").value;
		var v6 = document.getElementById("id_unif_personal").value;
		var v7 = document.getElementById("id_seg_med").value;
		var v8 = document.getElementById("id_susc_memb").value;
		var v9 = document.getElementById("id_cap_per_admin").value;
		var v10 = document.getElementById("id_serv_biblioteca").value;
		var v11 = document.getElementById("id_pasajes_aereos").value;
		var v12 = document.getElementById("id_gastos_viaje").value;
		var v13 = document.getElementById("id_gd_alimentacion").value;
		var res = suma_valores(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13);
		document.getElementById("id_gas_ser_admin").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_correo_ejec").value;
		var v2 = document.getElementById("id_serv_telef_ejec").value;
		var v3 = document.getElementById("id_serv_internet_ejec").value;
		var v4 = document.getElementById("id_vigilancia_ejec").value;
		var v5 = document.getElementById("id_parqueo_ejec").value;
		var v6 = document.getElementById("id_unif_personal_ejec").value;
		var v7 = document.getElementById("id_seg_med_ejec").value;
		var v8 = document.getElementById("id_susc_memb_ejec").value;
		var v9 = document.getElementById("id_cap_per_admin_ejec").value;
		var v10 = document.getElementById("id_serv_biblioteca_ejec").value;
		var v11 = document.getElementById("id_pasajes_aereos_ejec").value;
		var v12 = document.getElementById("id_gastos_viaje_ejec").value;
		var v13 = document.getElementById("id_gd_alimentacion_ejec").value;
		var res = suma_valores(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13);
		document.getElementById("id_gas_ser_admin_ejec").value = res;
	});

	//MANTENIMIENTO Y REPARACIONES
	$(document).ready(function(){
		var v1 = document.getElementById("id_man_rep_generales").value;
		var v2 = document.getElementById("id_man_rep_equipos").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_mant_rep").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_man_rep_generales_ejec").value;
		var v2 = document.getElementById("id_man_rep_equipos_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_mant_rep_ejec").value = res;
	});

	//PROVISIONES
	$(document).ready(function(){
		var v1 = document.getElementById("id_p_jubil_patr").value;
		var v2 = document.getElementById("id_p_desahucio").value;
		var v3 = document.getElementById("id_desp_intepestivo").value;
		var v4 = document.getElementById("id_prov_cuent_incobrables").value;
		var v5 = document.getElementById("id_prov_det_activos").value;
		var v6 = document.getElementById("id_prov_otras").value;
		var res = suma_valores(v1,v2,v3,v4,v5,v6);
		document.getElementById("id_prov").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_p_jubil_patr_ejec").value;
		var v2 = document.getElementById("id_p_desahucio_ejec").value;
		var v3 = document.getElementById("id_desp_intepestivo_ejec").value;
		var v4 = document.getElementById("id_prov_cuent_incobrables_ejec").value;
		var v5 = document.getElementById("id_prov_det_activos_ejec").value;
		var v6 = document.getElementById("id_prov_otras_ejec").value;
		var res = suma_valores(v1,v2,v3,v4,v5,v6);
		document.getElementById("id_prov_ejec").value = res;
	});
	
	//ALQUILER DE EQUIPOS
	$(document).ready(function(){
		var v1 = document.getElementById("id_alq_equipos").value;
		var res = suma_valores(v1);
		document.getElementById("id_alq_eqpos").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_alq_equipos_ejec").value;
		var res = suma_valores(v1);
		document.getElementById("id_alq_eqpos_ejec").value = res;
	});

	//SUMINISTROS Y MATERIALES
	$(document).ready(function(){
		var v1 = document.getElementById("id_sum_oficina").value;
		var v2 = document.getElementById("id_sum_limpieza").value;
		var v3 = document.getElementById("id_gd_copias").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gd_sum_mat").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_sum_oficina_ejec").value;
		var v2 = document.getElementById("id_sum_limpieza_ejec").value;
		var v3 = document.getElementById("id_gd_copias_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gd_sum_mat_ejec").value = res;
	});

	//GASTOS DE JARDINERIA Y ORNAMENTACION
	$(document).ready(function(){
		var v1 = document.getElementById("id_mat_jardineria").value;
		var v2 = document.getElementById("id_serv_jardineria").value;
		var v3 = document.getElementById("id_alim_tortugas").value;
		var v4 = document.getElementById("id_med_tortugas").value;
		var res = suma_valores(v1,v2,v3,v4);
		document.getElementById("id_gas_jar_orn").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_mat_jardineria_ejec").value;
		var v2 = document.getElementById("id_serv_jardineria_ejec").value;
		var v3 = document.getElementById("id_alim_tortugas_ejec").value;
		var v4 = document.getElementById("id_med_tortugas_ejec").value;
		var res = suma_valores(v1,v2,v3,v4);
		document.getElementById("id_gas_jar_orn_ejec").value = res;
	});

	//PROMOCION Y PUBLICIDAD
	$(document).ready(function(){
		var v1 = document.getElementById("id_mat_publicitario").value;
		var v2 = document.getElementById("id_pub_impresos").value;
		var v3 = document.getElementById("id_pub_digitales").value;
		var v4 = document.getElementById("id_cong_even_fer").value;
		var res = suma_valores(v1,v2,v3,v4);
		document.getElementById("id_prom_pub").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_mat_publicitario_ejec").value;
		var v2 = document.getElementById("id_pub_impresos_ejec").value;
		var v3 = document.getElementById("id_pub_digitales_ejec").value;
		var v4 = document.getElementById("id_cong_even_fer_ejec").value;
		var res = suma_valores(v1,v2,v3,v4);
		document.getElementById("id_prom_pub_ejec").value = res;
	});

	//GASTOS DE MARKETING
	$(document).ready(function(){
		var v1 = document.getElementById("id_prom_pub").value;
		var v2 = document.getElementById("id_com_ventas").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_gast_mark").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_prom_pub_ejec").value;
		var v2 = document.getElementById("id_com_ventas_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_gast_mark_ejec").value = res;
	});

	//GASTOS DE ACREDITACION
	$(document).ready(function(){
		var v1 = document.getElementById("id_aacsb").value;
		var v2 = document.getElementById("id_gac_pmi").value;
		var v3 = document.getElementById("id_iso").value;
		var v4 = document.getElementById("id_amba").value;
		var res = suma_valores(v1,v2,v3,v4);		
		document.getElementById("id_gast_acred").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_aacsb_ejec").value;
		var v2 = document.getElementById("id_gac_pmi_ejec").value;
		var v3 = document.getElementById("id_iso_ejec").value;
		var v4 = document.getElementById("id_amba_ejec").value;
		var res = suma_valores(v1,v2,v3,v4);
		document.getElementById("id_gast_acred_ejec").value = res;
	});

	//PASAJES NACIONALES
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdrep_p_nacionales").value;
		var v2 = document.getElementById("id_gdrep_seb_nacionales").value;
		var v3 = document.getElementById("id_gdrep_seguro_nacionales").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gd_pnacional").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdrep_p_nacionales_ejec").value;
		var v2 = document.getElementById("id_gdrep_seb_nacionales_ejec").value;
		var v3 = document.getElementById("id_gdrep_seguro_nacionales_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gd_pnacional_ejec").value = res;
	});

	//PASAJES INTERNACIONALES
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdrep_p_internacionales").value;
		var v2 = document.getElementById("id_gdrep_seb_internacionales").value;
		var v3 = document.getElementById("id_gdrep_seguro_internacionales").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gd_pinternacional").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdrep_p_internacionales_ejec").value;
		var v2 = document.getElementById("id_gdrep_seb_internacionales_ejec").value;
		var v3 = document.getElementById("id_gdrep_seguro_internacionales_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gd_pinternacional_ejec").value = res;
	});
	
	//PASAJES AEREOS
	$(document).ready(function(){
		var v1 = document.getElementById("id_gd_pnacional").value;
		var v2 = document.getElementById("id_gd_pinternacional").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_gd_pareos").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gd_pnacional_ejec").value;
		var v2 = document.getElementById("id_gd_pinternacional_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_gd_pareos_ejec").value = res;
	});

	//GASTOS DE VIAJE
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdrep_v_nacionales").value;
		var v2 = document.getElementById("id_gdrep_v_internacionales").value;
		var v3 = document.getElementById("id_gd_pareos").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gas_viaje").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdrep_v_nacionales_ejec").value;
		var v2 = document.getElementById("id_gdrep_v_internacionales_ejec").value;
		var v3 = document.getElementById("id_gd_pareos_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gas_viaje_ejec").value = res;
	});

	//GASTOS DE REPRESENTACION
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdrep_hospedaje").value;
		var v2 = document.getElementById("id_gas_viaje").value;
		var v3 = document.getElementById("id_conv_eventos").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gas_repre").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdrep_hospedaje_ejec").value;
		var v2 = document.getElementById("id_gas_viaje_ejec").value;
		var v3 = document.getElementById("id_conv_eventos_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gas_repre_ejec").value = res;
	});

	//GASTOS DE VIAJE - GASTOS DE INVESTIGACION
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdinv_v_nacionales").value;
		var v2 = document.getElementById("id_gdinv_v_internacionales").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_inv_gas_viaje").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdinv_v_nacionales_ejec").value;
		var v2 = document.getElementById("id_gdinv_v_internacionales_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_inv_gas_viaje_ejec").value = res;
	});

	//PASAJES NACIONALES - GASTOS DE INVESTIGACION
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdinv_p_nacionales").value;
		var v2 = document.getElementById("id_gdinv_seb_nacionales").value;
		var v3 = document.getElementById("id_gdinv_seguro_nacionales").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gdinv_pnacional").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdinv_p_nacionales_ejec").value;
		var v2 = document.getElementById("id_gdinv_seb_nacionales_ejec").value;
		var v3 = document.getElementById("id_gdinv_seguro_nacionales_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gdinv_pnacional_ejec").value = res;
	});

	//PASAJES INTERNACIONALES - GASTOS DE INVESTIGACION 
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdinv_p_internacionales").value;
		var v2 = document.getElementById("id_gdinv_seb_internacionales").value;
		var v3 = document.getElementById("id_gdinv_seguro_internacionales").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gdinv_pinternacional").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdinv_p_internacionales_ejec").value;
		var v2 = document.getElementById("id_gdinv_seb_internacionales_ejec").value;
		var v3 = document.getElementById("id_gdinv_seguro_internacionales_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gdinv_pinternacional_ejec").value = res;
	});

	//PASAJES AEREOS - GASTOS DE INVESTIGACION
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdinv_pnacional").value;
		var v2 = document.getElementById("id_gdinv_pinternacional").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_gdinv_paereos").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdinv_pnacional_ejec").value;
		var v2 = document.getElementById("id_gdinv_pinternacional_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_gdinv_paereos_ejec").value = res;
	});

	//GASTOS DE INVESTIGACION
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdinv_capacitacion").value;
		var v2 = document.getElementById("id_inv_gas_viaje").value;
		var v3 = document.getElementById("id_gdinv_paereos").value;
		var v4 = document.getElementById("id_gd_honorarios").value;
		var v5 = document.getElementById("id_gd_alimentacion").value;
		var v6 = document.getElementById("id_gd_hospedaje").value;
		var v7 =document.getElementById("id_gd_susc_memb").value;
		var v8 = document.getElementById("id_publicaciones").value;
		var v9 = document.getElementById("id_conv_even_proy").value;
		var res = suma_valores(v1,v2,v3,v4,v5,v6,v7,v8,v9);
		document.getElementById("id_gdinv").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_gdinv_capacitacion_ejec").value;
		var v2 = document.getElementById("id_inv_gas_viaje_ejec").value;
		var v3 = document.getElementById("id_gdinv_paereos_ejec").value;
		var v4 = document.getElementById("id_gd_honorarios_ejec").value;
		var v5 = document.getElementById("id_gd_alimentacion_ejec").value;
		var v6 = document.getElementById("id_gd_hospedaje_ejec").value;
		var v7 =document.getElementById("id_gd_susc_memb_ejec").value;
		var v8 = document.getElementById("id_publicaciones_ejec").value;
		var v9 = document.getElementById("id_conv_even_proy_ejec").value;
		var res = suma_valores(v1,v2,v3,v4,v5,v6,v7,v8,v9);
		document.getElementById("id_gdinv_ejec").value = res;
	});

	//GASTOS DE INTERES
	$(document).ready(function(){
		var v1 = document.getElementById("id_i_banc_local").value;
		var v2 = document.getElementById("id_i_pag_local").value;
		var v3 = document.getElementById("id_i_pag_no_local").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gast_interes").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_i_banc_local_ejec").value;
		var v2 = document.getElementById("id_i_pag_local_ejec").value;
		var v3 = document.getElementById("id_i_pag_no_local_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gast_interes_ejec").value = res;
	});

	//GASTOS DE COMISIONES BANCARIAS
	$(document).ready(function(){
		var v1 = document.getElementById("id_com_bancarias").value;
		var v2 = document.getElementById("id_com_tarj_cred").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_gas_com_ban").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_com_bancarias_ejec").value;
		var v2 = document.getElementById("id_com_tarj_cred_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_gas_com_ban_ejec").value = res;
	});

	//GASTOS POR IMPUESTO
	$(document).ready(function(){
		var v1 = document.getElementById("id_iva").value;
		var v2 = document.getElementById("id_isd").value;
		var v3 = document.getElementById("id_ice").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gas_impu").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_iva_ejec").value;
		var v2 = document.getElementById("id_isd_ejec").value;
		var v3 = document.getElementById("id_ice_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gas_impu_ejec").value = res;
	});

	//GASTOS DE DEPRECIACION
	$(document).ready(function(){
		var v1 = document.getElementById("id_d_propiedades").value;
		var v2 = document.getElementById("id_d_revaluo_prop").value;
		var v3 = document.getElementById("id_d_prop_inversion").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gas_depre").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_d_propiedades_ejec").value;
		var v2 = document.getElementById("id_d_revaluo_prop_ejec").value;
		var v3 = document.getElementById("id_d_prop_inversion_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_gas_depre_ejec").value = res;
	});

	//SERVICIOS PUBLICOS
	$(document).ready(function(){
		var v1 = document.getElementById("id_agua").value;
		var v2 = document.getElementById("id_luz").value;
		var v3 = document.getElementById("id_fono").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_serv_pub").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_agua_ejec").value;
		var v2 = document.getElementById("id_luz_ejec").value;
		var v3 = document.getElementById("id_fono_ejec").value;
		var res = suma_valores(v1,v2,v3);
		document.getElementById("id_serv_pub_ejec").value = res;
	});

	//APORTES INSTITUCIONALES
	$(document).ready(function(){
		var v1 = document.getElementById("id_ap_espol").value;
		var v2 = document.getElementById("id_ap_fundespol").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_aport_inst").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_ap_espol_ejec").value;
		var v2 = document.getElementById("id_ap_fundespol_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_aport_inst_ejec").value = res;
	});

	//TOTAL DE COSTOS Y GASTOS DEDUCIBLES
	$(document).ready(function(){
		var v1 = document.getElementById("id_costos_deducibles").value;
		var v2 = document.getElementById("id_gdeducibles").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_total_gastos").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_costos_deducibles_ejec").value;
		var v2 = document.getElementById("id_gdeducibles_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_total_gastos_ejec").value = res;
	});

	//RESULTADOS
	$(document).ready(function(){
		var v1 = document.getElementById("id_total_ingresos").value;
		var v2 = document.getElementById("id_total_gastos").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_resultados").value = res;
	});
	$(document).ready(function(){
		var v1 = document.getElementById("id_total_ingresos_ejec").value;
		var v2 = document.getElementById("id_total_gastos_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_resultados_ejec").value = res;
	});
	
