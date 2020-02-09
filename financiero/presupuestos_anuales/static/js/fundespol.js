$(document).ready(function(){

	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------

	//INGRESOS
	document.getElementById("id_total_ingresos").onclick = function(){
		var v1 = document.getElementById("id_se_maestrias").value;
		var v2 = document.getElementById("id_se_curs_prog").value;
		var v3 = document.getElementById("id_se_conf_even").value;
		var v4 = document.getElementById("id_s_arriendos").value;
		var v5 = document.getElementById("id_aporte_proy").value;
		var v6 = document.getElementById("id_cert_tasas_otros").value;
		var v7 = document.getElementById("id_dev_est_otros").value;
		document.getElementById("id_total_ingresos").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)-parseFloat(v7);
	};
	document.getElementById("id_total_ingresos_ejec").onclick = function(){
		var v1 = document.getElementById("id_se_maestrias_ejec").value;
		var v2 = document.getElementById("id_se_curs_prog_ejec").value;
		var v3 = document.getElementById("id_se_conf_even_ejec").value;
		var v4 = document.getElementById("id_s_arriendos_ejec").value;
		var v5 = document.getElementById("id_aporte_proy_ejec").value;
		var v6 = document.getElementById("id_cert_tasas_otros_ejec").value;
		var v7 = document.getElementById("id_dev_est_otros_ejec").value;
		document.getElementById("id_total_ingresos_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)-parseFloat(v7);
	};

	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------

	//COSTOS DEL SERVICIO - DEDUCIBLES
	document.getElementById("id_costos_deducibles").onclick = function(){
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
		document.getElementById("id_costos_deducibles").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7)+parseFloat(v8)+parseFloat(v9)+parseFloat(v10)+parseFloat(11)+parseFloat(v12);
	};
	document.getElementById("id_costos_deducibles_ejec").onclick = function(){
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
		document.getElementById("id_costos_deducibles_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7)+parseFloat(v8)+parseFloat(v9)+parseFloat(v10)+parseFloat(11)+parseFloat(v12);
	};

	//HONORARIOS PROFESIONALES - DOCENTES
	document.getElementById("id_hp_docentes").onclick = function(){
		var v1 = document.getElementById("id_hd_locales").value;
		var v2 = document.getElementById("id_hd_extranjeros").value;
		document.getElementById("id_hp_docentes").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_hp_docentes_ejec").onclick = function(){
		var v1 = document.getElementById("id_hd_locales_ejec").value;
		var v2 = document.getElementById("id_hd_extranjeros_ejec").value;
		document.getElementById("id_hp_docentes_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	//HONORARIOS PROFESIONALES
	document.getElementById("id_h_profesionales").onclick = function(){
		var v1 = document.getElementById("id_hp_docentes").value;
		var v2 = document.getElementById("id_h_prof_dietas").value;
		document.getElementById("id_h_profesionales").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_h_profesionales_ejec").onclick = function(){
		var v1 = document.getElementById("id_hp_docentes_ejec").value;
		var v2 = document.getElementById("id_h_prof_dietas_ejec").value;
		document.getElementById("id_h_profesionales_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	//SUELDOS, SALARIOS Y DEMÁS REMUNERACIONES
	document.getElementById("id_suel_sal_rem").onclick = function(){
		var v1 = document.getElementById("id_unif_salarial").value;
		var v2 = document.getElementById("id_h_extras").value;
		var v3 = document.getElementById("id_bonificaciones").value;
		document.getElementById("id_suel_sal_rem").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_suel_sal_rem_ejec").onclick = function(){
		var v1 = document.getElementById("id_unif_salarial_ejec").value;
		var v2 = document.getElementById("id_h_extras_ejec").value;
		var v3 = document.getElementById("id_bonificaciones_ejec").value;
		document.getElementById("id_suel_sal_rem_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//BENEFICIOS SOCIALES, INDEMNIZACIONES Y OTRAS REMUNERACIONES
	document.getElementById("id_ben_iden_rem").onclick = function(){
		var v1 = document.getElementById("id_dec_ter_sueldo").value;
		var v2 = document.getElementById("id_dec_cua_sueldo").value;
		var v3 = document.getElementById("id_f_reserva").value;
		var v4 = document.getElementById("id_vacaciones").value;
		document.getElementById("id_ben_iden_rem").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4);
	};
	document.getElementById("id_ben_iden_rem_ejec").onclick = function(){
		var v1 = document.getElementById("id_dec_ter_sueldo_ejec").value;
		var v2 = document.getElementById("id_dec_cua_sueldo_ejec").value;
		var v3 = document.getElementById("id_f_reserva_ejec").value;
		var v4 = document.getElementById("id_vacaciones_ejec").value;
		document.getElementById("id_ben_iden_rem_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4);
	};

	//APORTE A LA SEGURIDAD SOCIAL
	document.getElementById("id_ap_seg_soc").onclick = function(){
		var v1 = document.getElementById("id_aport_patronal").value;
		var v2 = document.getElementById("id_ccc_1").value;
		var v3 = document.getElementById("id_ss_tiempo_parcial").value;
		document.getElementById("id_ap_seg_soc").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_ap_seg_soc_ejec").onclick = function(){
		var v1 = document.getElementById("id_aport_patronal_ejec").value;
		var v2 = document.getElementById("id_ccc_1_ejec").value;
		var v3 = document.getElementById("id_ss_tiempo_parcial_ejec").value;
		document.getElementById("id_ap_seg_soc_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//GASTOS DE PERSONAL EN RELACION DE DEPENDENCIA
	document.getElementById("id_g_personal").onclick = function(){
		var v1 = document.getElementById("id_suel_sal_rem").value;
		var v2 = document.getElementById("id_ben_iden_rem").value;
		var v3 = document.getElementById("id_ap_seg_soc").value;
		document.getElementById("id_g_personal").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_g_personal_ejec").onclick = function(){
		var v1 = document.getElementById("id_suel_sal_rem_ejec").value;
		var v2 = document.getElementById("id_ben_iden_rem_ejec").value;
		var v3 = document.getElementById("id_ap_seg_soc_ejec").value;
		document.getElementById("id_g_personal_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//SUMINISTROS Y MATERIALES
	document.getElementById("id_sum_mat").onclick = function(){
		var v1 = document.getElementById("id_md_fisico").value;
		var v2 = document.getElementById("id_md_digital").value;
		var v3 = document.getElementById("id_copias").value;
		var v4 = document.getElementById("id_suministros").value;
		document.getElementById("id_sum_mat").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4);
	};
	document.getElementById("id_sum_mat_ejec").onclick = function(){
		var v1 = document.getElementById("id_md_fisico_ejec").value;
		var v2 = document.getElementById("id_md_digital_ejec").value;
		var v3 = document.getElementById("id_copias_ejec").value;
		var v4 = document.getElementById("id_suministros_ejec").value;
		document.getElementById("id_sum_mat_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4);
	};

	//ALIMENTACIÓN
	document.getElementById("id_alimentacion").onclick = function(){
		var v1 = document.getElementById("id_s_alimentacion").value;
		var v2 = document.getElementById("id_com_salimentacion").value;
		document.getElementById("id_alimentacion").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_alimentacion_ejec").onclick = function(){
		var v1 = document.getElementById("id_s_alimentacion_ejec").value;
		var v2 = document.getElementById("id_com_salimentacion_ejec").value;
		document.getElementById("id_alimentacion_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	//HOSPEDAJE
	document.getElementById("id_hosp").onclick = function(){
		var v1 = document.getElementById("id_s_hopedaje").value;
		var v2 = document.getElementById("id_com_shopedaje").value;
		var v3 = document.getElementById("id_tasa_per").value;
		document.getElementById("id_hosp").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_hosp_ejec").onclick = function(){
		var v1 = document.getElementById("id_s_hopedaje_ejec").value;
		var v2 = document.getElementById("id_com_shopedaje_ejec").value;
		var v3 = document.getElementById("id_tasa_per_ejec").value;
		document.getElementById("id_hosp_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//PASAJES NACIONALES
	document.getElementById("id_pnacional").onclick = function(){
		var v1 = document.getElementById("id_p_nacionales").value;
		var v2 = document.getElementById("id_seb_nacionales").value;
		var v3 = document.getElementById("id_seguro_nacionales").value;
		document.getElementById("id_pnacional").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_pnacional_ejec").onclick = function(){
		var v1 = document.getElementById("id_p_nacionales_ejec").value;
		var v2 = document.getElementById("id_seb_nacionales_ejec").value;
		var v3 = document.getElementById("id_seguro_nacionales_ejec").value;
		document.getElementById("id_pnacional_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//PASAJES INTERNACIONALES
	document.getElementById("id_pinternacional").onclick = function(){
		var v1 = document.getElementById("id_p_internacionales").value;
		var v2 = document.getElementById("id_seb_internacionales").value;
		var v3 = document.getElementById("id_seguro_internacionales").value;
		document.getElementById("id_pinternacional").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_pinternacional_ejec").onclick = function(){
		var v1 = document.getElementById("id_p_internacionales_ejec").value;
		var v2 = document.getElementById("id_seb_internacionales_ejec").value;
		var v3 = document.getElementById("id_seguro_internacionales_ejec").value;
		document.getElementById("id_pinternacional_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//PASAJES AREOS
	document.getElementById("id_pareos").onclick = function(){
		var v1 = document.getElementById("id_pnacional").value;
		var v2 = document.getElementById("id_pinternacional").value;
		document.getElementById("id_pareos").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_pareos_ejec").onclick = function(){
		var v1 = document.getElementById("id_pnacional_ejec").value;
		var v2 = document.getElementById("id_pinternacional_ejec").value;
		document.getElementById("id_pareos_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	//GASTOS DE VIAJE
	document.getElementById("id_gastosviaje").onclick = function(){
		var v1 = document.getElementById("id_v_nacionales").value;
		var v2 = document.getElementById("id_v_internacionales").value;
		document.getElementById("id_gastosviaje").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_gastosviaje_ejec").onclick = function(){
		var v1 = document.getElementById("id_v_nacionales_ejec").value;
		var v2 = document.getElementById("id_v_internacionales_ejec").value;
		document.getElementById("id_gastosviaje_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	
	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------
	
	//GASTOS DEDUCIBLES
	document.getElementById("id_gdeducibles").onclick = function(){
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
		document.getElementById("id_gdeducibles").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7)+parseFloat(v8)+parseFloat(v9)+parseFloat(v10)+parseFloat(11)+parseFloat(v12)+parseFloat(v13)+parseFloat(v14)+parseFloat(v15)+parseFloat(v16)+parseFloat(v17)+parseFloat(v18)+parseFloat(v19)+parseFloat(v20)+parseFloat(v21)+parseFloat(v22)+parseFloat(v23)+parseFloat(v24);
	};
	document.getElementById("id_gdeducibles_ejec").onclick = function(){
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
		document.getElementById("id_gdeducibles_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7)+parseFloat(v8)+parseFloat(v9)+parseFloat(v10)+parseFloat(v11)+parseFloat(v12)+parseFloat(v13)+parseFloat(v14)+parseFloat(v15)+parseFloat(v16)+parseFloat(v17)+parseFloat(v18)+parseFloat(v19)+parseFloat(v20)+parseFloat(v21)+parseFloat(v22)+parseFloat(v23)+parseFloat(v24);
	};

	//SUELDO, SALARIOS  Y DEMAS REMUNERACIONES
	document.getElementById("id_gd_suel_sal_rem").onclick = function(){
		var v1 = document.getElementById("id_gd_unif_salarial").value;
		var v2 = document.getElementById("id_gd_h_extras").value;
		var v3 = document.getElementById("id_gd_bonificaciones").value;
		document.getElementById("id_gd_suel_sal_rem").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_gd_suel_sal_rem_ejec").onclick = function(){
		var v1 = document.getElementById("id_gd_unif_salarial_ejec").value;
		var v2 = document.getElementById("id_gd_h_extras_ejec").value;
		var v3 = document.getElementById("id_gd_bonificaciones_ejec").value;
		document.getElementById("id_gd_suel_sal_rem_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	
	//BENEFICIOS SOCIALES, INDEMNIZACIONES Y OTRAS REMUNERACIONES
	document.getElementById("id_gd_ben_iden_rem").onclick = function(){
		var v1 = document.getElementById("id_gd_dec_ter_sueldo").value;
		var v2 = document.getElementById("id_gd_dec_cua_sueldo").value;
		var v3 = document.getElementById("id_gd_f_reserva").value;
		var v4 = document.getElementById("id_gd_vacaciones").value;
		document.getElementById("id_gd_ben_iden_rem").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4);
	};
	document.getElementById("id_gd_ben_iden_rem_ejec").onclick = function(){
		var v1 = document.getElementById("id_gd_dec_ter_sueldo_ejec").value;
		var v2 = document.getElementById("id_gd_dec_cua_sueldo_ejec").value;
		var v3 = document.getElementById("id_gd_f_reserva_ejec").value;
		var v4 = document.getElementById("id_gd_vacaciones_ejec").value;
		document.getElementById("id_gd_ben_iden_rem_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4);
	};

	//APORTE A LA SEGURIDAD SOCIAL 
	document.getElementById("id_gd_ap_seg_soc").onclick = function(){
		var v1 = document.getElementById("id_gd_aport_patronal").value;
		var v2 = document.getElementById("id_gd_ccc_1").value;
		var v3 = document.getElementById("id_gd_ss_tiempo_parcial").value;
		document.getElementById("id_gd_ap_seg_soc").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_gd_ap_seg_soc_ejec").onclick = function(){
		var v1 = document.getElementById("id_gd_aport_patronal_ejec").value;
		var v2 = document.getElementById("id_gd_ccc_1_ejec").value;
		var v3 = document.getElementById("id_gd_ss_tiempo_parcial_ejec").value;
		document.getElementById("id_gd_ap_seg_soc_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//GASTOS DE PERSONAL CON RELACION DE DEPENDENCIA - GASTOS DEDUCIBLES
	document.getElementById("id_gd_gast_pers").onclick = function(){
		var v1 = document.getElementById("id_gd_suel_sal_rem").value;
		var v2 = document.getElementById("id_gd_ben_iden_rem").value;
		var v3 = document.getElementById("id_gd_ap_seg_soc").value;
		document.getElementById("id_gd_gast_pers").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_gd_gast_pers_ejec").onclick = function(){
		var v1 = document.getElementById("id_gd_suel_sal_rem_ejec").value;
		var v2 = document.getElementById("id_gd_ben_iden_rem_ejec").value;
		var v3 = document.getElementById("id_gd_ap_seg_soc_ejec").value;
		document.getElementById("id_gd_gast_pers_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//HONORARIOS
	document.getElementById("id_honorarios").onclick = function(){
		var v1 = document.getElementById("id_gd_h_prof_dietas").value;
		var v2 = document.getElementById("id_serv_ocasionales").value;
		document.getElementById("id_honorarios").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_honorarios_ejec").onclick = function(){
		var v1 = document.getElementById("id_gd_h_prof_dietas_ejec").value;
		var v2 = document.getElementById("id_serv_ocasionales_ejec").value;
		document.getElementById("id_honorarios_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	//GASTOS EN SERVICIOS ADMINISTRATIVOS
	document.getElementById("id_gas_ser_admin").onclick = function(){
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
		document.getElementById("id_gas_ser_admin").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7)+parseFloat(v8)+parseFloat(v9)+parseFloat(v10)+parseFloat(v11)+parseFloat(v12)+parseFloat(v13);
	};
	document.getElementById("id_gas_ser_admin_ejec").onclick = function(){
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
		document.getElementById("id_gas_ser_admin_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7)+parseFloat(v8)+parseFloat(v9)+parseFloat(v10)+parseFloat(v11)+parseFloat(v12)+parseFloat(v13);
	};

	//MANTENIMIENTO Y REPARACIONES
	document.getElementById("id_mant_rep").onclick = function(){
		var v1 = document.getElementById("id_man_rep_generales").value;
		var v2 = document.getElementById("id_man_rep_equipos").value;
		document.getElementById("id_mant_rep").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_mant_rep_ejec").onclick = function(){
		var v1 = document.getElementById("id_man_rep_generales_ejec").value;
		var v2 = document.getElementById("id_man_rep_equipos_ejec").value;
		document.getElementById("id_mant_rep_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	//PROVISIONES
	document.getElementById("id_prov").onclick = function(){
		var v1 = document.getElementById("id_p_jubil_patr").value;
		var v2 = document.getElementById("id_p_desahucio").value;
		var v3 = document.getElementById("id_desp_intepestivo").value;
		var v4 = document.getElementById("id_prov_cuent_incobrables").value;
		var v5 = document.getElementById("id_prov_det_activos").value;
		var v6 = document.getElementById("id_prov_otras").value;
		document.getElementById("id_prov").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6);
	};
	document.getElementById("id_prov_ejec").onclick = function(){
		var v1 = document.getElementById("id_p_jubil_patr_ejec").value;
		var v2 = document.getElementById("id_p_desahucio_ejec").value;
		var v3 = document.getElementById("id_desp_intepestivo_ejec").value;
		var v4 = document.getElementById("id_prov_cuent_incobrables_ejec").value;
		var v5 = document.getElementById("id_prov_det_activos_ejec").value;
		var v6 = document.getElementById("id_prov_otras_ejec").value;
		document.getElementById("id_prov_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6);
	};
	
	//ALQUILER DE EQUIPOS
	document.getElementById("id_alq_eqpos").onclick = function(){
		var v1 = document.getElementById("id_alq_equipos").value;
		document.getElementById("id_alq_eqpos").value = parseFloat(v1);
	};
	document.getElementById("id_alq_eqpos_ejec").onclick = function(){
		var v1 = document.getElementById("id_alq_equipos_ejec").value;
		document.getElementById("id_alq_eqpos_ejec").value = parseFloat(v1);
	};

	//SUMINISTROS Y MATERIALES
	document.getElementById("id_gd_sum_mat").onclick = function(){
		var v1 = document.getElementById("id_sum_oficina").value;
		var v2 = document.getElementById("id_sum_limpieza").value;
		var v3 = document.getElementById("id_gd_copias").value;
		document.getElementById("id_gd_sum_mat").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_gd_sum_mat_ejec").onclick = function(){
		var v1 = document.getElementById("id_sum_oficina_ejec").value;
		var v2 = document.getElementById("id_sum_limpieza_ejec").value;
		var v3 = document.getElementById("id_gd_copias_ejec").value;
		document.getElementById("id_gd_sum_mat_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//GASTOS DE JARDINERIA Y ORNAMENTACION
	document.getElementById("id_gas_jar_orn").onclick = function(){
		var v1 = document.getElementById("id_mat_jardineria").value;
		var v2 = document.getElementById("id_serv_jardineria").value;
		var v3 = document.getElementById("id_alim_tortugas").value;
		var v4 = document.getElementById("id_med_tortugas").value;
		document.getElementById("id_gas_jar_orn").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4);
	};
	document.getElementById("id_gas_jar_orn_ejec").onclick = function(){
		var v1 = document.getElementById("id_mat_jardineria_ejec").value;
		var v2 = document.getElementById("id_serv_jardineria_ejec").value;
		var v3 = document.getElementById("id_alim_tortugas_ejec").value;
		var v4 = document.getElementById("id_med_tortugas_ejec").value;
		document.getElementById("id_gas_jar_orn_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4);
	};

	//PROMOCION Y PUBLICIDAD
	document.getElementById("id_prom_pub").onclick = function(){
		var v1 = document.getElementById("id_mat_publicitario").value;
		var v2 = document.getElementById("id_pub_impresos").value;
		var v3 = document.getElementById("id_pub_digitales").value;
		var v4 = document.getElementById("id_cong_even_fer").value;
		document.getElementById("id_prom_pub").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4);
	};
	document.getElementById("id_prom_pub_ejec").onclick = function(){
		var v1 = document.getElementById("id_mat_publicitario_ejec").value;
		var v2 = document.getElementById("id_pub_impresos_ejec").value;
		var v3 = document.getElementById("id_pub_digitales_ejec").value;
		var v4 = document.getElementById("id_cong_even_fer_ejec").value;
		document.getElementById("id_prom_pub_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4);
	};

	//GASTOS DE MARKETING
	document.getElementById("id_gast_mark").onclick = function(){
		var v1 = document.getElementById("id_prom_pub").value;
		var v2 = document.getElementById("id_com_ventas").value;
		document.getElementById("id_gast_mark").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_gast_mark_ejec").onclick = function(){
		var v1 = document.getElementById("id_prom_pub_ejec").value;
		var v2 = document.getElementById("id_com_ventas_ejec").value;
		document.getElementById("id_gast_mark_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	//GASTOS DE ACREDITACION
	document.getElementById("id_gast_acred").onclick = function(){
		var v1 = document.getElementById("id_aacsb").value;
		var v2 = document.getElementById("id_gac_pmi").value;
		var v3 = document.getElementById("id_iso").value;
		var v4 = document.getElementById("id_amba").value;
		document.getElementById("id_gast_acred").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4);
	};
	document.getElementById("id_gast_acred_ejec").onclick = function(){
		var v1 = document.getElementById("id_aacsb_ejec").value;
		var v2 = document.getElementById("id_gac_pmi_ejec").value;
		var v3 = document.getElementById("id_iso_ejec").value;
		var v4 = document.getElementById("id_amba_ejec").value;
		document.getElementById("id_gast_acred_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4);
	};

	//PASAJES NACIONALES
	document.getElementById("id_gd_pnacional").onclick = function(){
		var v1 = document.getElementById("id_gdrep_p_nacionales").value;
		var v2 = document.getElementById("id_gdrep_seb_nacionales").value;
		var v3 = document.getElementById("id_gdrep_seguro_nacionales").value;
		document.getElementById("id_gd_pnacional").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_gd_pnacional_ejec").onclick = function(){
		var v1 = document.getElementById("id_gdrep_p_nacionales_ejec").value;
		var v2 = document.getElementById("id_gdrep_seb_nacionales_ejec").value;
		var v3 = document.getElementById("id_gdrep_seguro_nacionales_ejec").value;
		document.getElementById("id_gd_pnacional_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//PASAJES INTERNACIONALES
	document.getElementById("id_gd_pinternacional").onclick = function(){
		var v1 = document.getElementById("id_gdrep_p_internacionales").value;
		var v2 = document.getElementById("id_gdrep_seb_internacionales").value;
		var v3 = document.getElementById("id_gdrep_seguro_internacionales").value;
		document.getElementById("id_gd_pinternacional").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_gd_pinternacional_ejec").onclick = function(){
		var v1 = document.getElementById("id_gdrep_p_internacionales_ejec").value;
		var v2 = document.getElementById("id_gdrep_seb_internacionales_ejec").value;
		var v3 = document.getElementById("id_gdrep_seguro_internacionales_ejec").value;
		document.getElementById("id_gd_pinternacional_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	
	//PASAJES AEREOS
	document.getElementById("id_gd_pareos").onclick = function(){
		var v1 = document.getElementById("id_gd_pnacional").value;
		var v2 = document.getElementById("id_gd_pinternacional").value;
		document.getElementById("id_gd_pareos").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_gd_pareos_ejec").onclick = function(){
		var v1 = document.getElementById("id_gd_pnacional_ejec").value;
		var v2 = document.getElementById("id_gd_pinternacional_ejec").value;
		document.getElementById("id_gd_pareos_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	//GASTOS DE VIAJE
	document.getElementById("id_gas_viaje").onclick = function(){
		var v1 = document.getElementById("id_gdrep_v_nacionales").value;
		var v2 = document.getElementById("id_gdrep_v_internacionales").value;
		var v3 = document.getElementById("id_gd_pareos").value;
		document.getElementById("id_gas_viaje").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_gas_viaje_ejec").onclick = function(){
		var v1 = document.getElementById("id_gdrep_v_nacionales_ejec").value;
		var v2 = document.getElementById("id_gdrep_v_internacionales_ejec").value;
		var v3 = document.getElementById("id_gd_pareos_ejec").value;
		document.getElementById("id_gas_viaje_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//GASTOS DE REPRESENTACION
	document.getElementById("id_gas_repre").onclick = function(){
		var v1 = document.getElementById("id_gdrep_hospedaje").value;
		var v2 = document.getElementById("id_gas_viaje").value;
		var v3 = document.getElementById("id_conv_eventos").value;
		document.getElementById("id_gas_repre").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_gas_repre_ejec").onclick = function(){
		var v1 = document.getElementById("id_gdrep_hospedaje_ejec").value;
		var v2 = document.getElementById("id_gas_viaje_ejec").value;
		var v3 = document.getElementById("id_conv_eventos_ejec").value;
		document.getElementById("id_gas_repre_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//GASTOS DE VIAJE - GASTOS DE INVESTIGACION
	document.getElementById("id_inv_gas_viaje").onclick = function(){
		var v1 = document.getElementById("id_gdinv_v_nacionales").value;
		var v2 = document.getElementById("id_gdinv_v_internacionales").value;
		document.getElementById("id_inv_gas_viaje").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_inv_gas_viaje_ejec").onclick = function(){
		var v1 = document.getElementById("id_gdinv_v_nacionales_ejec").value;
		var v2 = document.getElementById("id_gdinv_v_internacionales_ejec").value;
		document.getElementById("id_inv_gas_viaje_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	//PASAJES NACIONALES - GASTOS DE INVESTIGACION
	document.getElementById("id_gdinv_pnacional").onclick = function(){
		var v1 = document.getElementById("id_gdinv_p_nacionales").value;
		var v2 = document.getElementById("id_gdinv_seb_nacionales").value;
		var v3 = document.getElementById("id_gdinv_seguro_nacionales").value;
		document.getElementById("id_gdinv_pnacional").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_gdinv_pnacional_ejec").onclick = function(){
		var v1 = document.getElementById("id_gdinv_p_nacionales_ejec").value;
		var v2 = document.getElementById("id_gdinv_seb_nacionales_ejec").value;
		var v3 = document.getElementById("id_gdinv_seguro_nacionales_ejec").value;
		document.getElementById("id_gdinv_pnacional_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//PASAJES INTERNACIONALES - GASTOS DE INVESTIGACION 
	document.getElementById("id_gdinv_pinternacional").onclick = function(){
		var v1 = document.getElementById("id_gdinv_p_internacionales").value;
		var v2 = document.getElementById("id_gdinv_seb_internacionales").value;
		var v3 = document.getElementById("id_gdinv_seguro_internacionales").value;
		document.getElementById("id_gdinv_pinternacional").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_gdinv_pinternacional_ejec").onclick = function(){
		var v1 = document.getElementById("id_gdinv_p_internacionales_ejec").value;
		var v2 = document.getElementById("id_gdinv_seb_internacionales_ejec").value;
		var v3 = document.getElementById("id_gdinv_seguro_internacionales_ejec").value;
		document.getElementById("id_gdinv_pinternacional_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//PASAJES AEREOS - GASTOS DE INVESTIGACION
	document.getElementById("id_gdinv_paereos").onclick = function(){
		var v1 = document.getElementById("id_gdinv_pnacional").value;
		var v2 = document.getElementById("id_gdinv_pinternacional").value;
		document.getElementById("id_gdinv_paereos").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_gdinv_paereos_ejec").onclick = function(){
		var v1 = document.getElementById("id_gdinv_pnacional_ejec").value;
		var v2 = document.getElementById("id_gdinv_pinternacional_ejec").value;
		document.getElementById("id_gdinv_paereos_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	//GASTOS DE INVESTIGACION
	document.getElementById("id_gdinv").onclick = function(){
		var v1 = document.getElementById("id_gdinv_capacitacion").value;
		var v2 = document.getElementById("id_inv_gas_viaje").value;
		var v3 = document.getElementById("id_gdinv_paereos").value;
		var v4 = document.getElementById("id_gd_honorarios").value;
		var v5 = document.getElementById("id_gd_alimentacion").value;
		var v6 = document.getElementById("id_gd_hospedaje").value;
		var v7 =document.getElementById("id_gd_susc_memb").value;
		var v8 = document.getElementById("id_publicaciones").value;
		var v9 = document.getElementById("id_conv_even_proy").value;
		document.getElementById("id_gdinv").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7)+parseFloat(v8)+parseFloat(v9);
	};
	document.getElementById("id_gdinv_ejec").onclick = function(){
		var v1 = document.getElementById("id_gdinv_capacitacion_ejec").value;
		var v2 = document.getElementById("id_inv_gas_viaje_ejec").value;
		var v3 = document.getElementById("id_gdinv_paereos_ejec").value;
		var v4 = document.getElementById("id_gd_honorarios_ejec").value;
		var v5 = document.getElementById("id_gd_alimentacion_ejec").value;
		var v6 = document.getElementById("id_gd_hospedaje_ejec").value;
		var v7 =document.getElementById("id_gd_susc_memb_ejec").value;
		var v8 = document.getElementById("id_publicaciones_ejec").value;
		var v9 = document.getElementById("id_conv_even_proy_ejec").value;
		document.getElementById("id_gdinv_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7)+parseFloat(v8)+parseFloat(v9);
	};

	//GASTOS DE INTERES
	document.getElementById("id_gast_interes").onclick = function(){
		var v1 = document.getElementById("id_i_banc_local").value;
		var v2 = document.getElementById("id_i_pag_local").value;
		var v3 = document.getElementById("id_i_pag_no_local").value;
		document.getElementById("id_gast_interes").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_gast_interes_ejec").onclick = function(){
		var v1 = document.getElementById("id_i_banc_local_ejec").value;
		var v2 = document.getElementById("id_i_pag_local_ejec").value;
		var v3 = document.getElementById("id_i_pag_no_local_ejec").value;
		document.getElementById("id_gast_interes_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//GASTOS DE COMISIONES BANCARIAS
	document.getElementById("id_gas_com_ban").onclick = function(){
		var v1 = document.getElementById("id_com_bancarias").value;
		var v2 = document.getElementById("id_com_tarj_cred").value;
		document.getElementById("id_gas_com_ban").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_gas_com_ban_ejec").onclick = function(){
		var v1 = document.getElementById("id_com_bancarias_ejec").value;
		var v2 = document.getElementById("id_com_tarj_cred_ejec").value;
		document.getElementById("id_gas_com_ban_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	//GASTOS POR IMPUESTO
	document.getElementById("id_gas_impu").onclick = function(){
		var v1 = document.getElementById("id_iva").value;
		var v2 = document.getElementById("id_isd").value;
		var v3 = document.getElementById("id_ice").value;
		document.getElementById("id_gas_impu").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_gas_impu_ejec").onclick = function(){
		var v1 = document.getElementById("id_iva_ejec").value;
		var v2 = document.getElementById("id_isd_ejec").value;
		var v3 = document.getElementById("id_ice_ejec").value;
		document.getElementById("id_gas_impu_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//GASTOS DE DEPRECIACION
	document.getElementById("id_gas_depre").onclick = function(){
		var v1 = document.getElementById("id_d_propiedades").value;
		var v2 = document.getElementById("id_d_revaluo_prop").value;
		var v3 = document.getElementById("id_d_prop_inversion").value;
		document.getElementById("id_gas_depre").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_gas_depre_ejec").onclick = function(){
		var v1 = document.getElementById("id_d_propiedades_ejec").value;
		var v2 = document.getElementById("id_d_revaluo_prop_ejec").value;
		var v3 = document.getElementById("id_d_prop_inversion_ejec").value;
		document.getElementById("id_gas_depre_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//SERVICIOS PUBLICOS
	document.getElementById("id_serv_pub").onclick = function(){
		var v1 = document.getElementById("id_agua").value;
		var v2 = document.getElementById("id_luz").value;
		var v3 = document.getElementById("id_fono").value;
		document.getElementById("id_serv_pub").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_serv_pub_ejec").onclick = function(){
		var v1 = document.getElementById("id_agua_ejec").value;
		var v2 = document.getElementById("id_luz_ejec").value;
		var v3 = document.getElementById("id_fono_ejec").value;
		document.getElementById("id_serv_pub_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//APORTES INSTITUCIONALES
	document.getElementById("id_aport_inst").onclick = function(){
		var v1 = document.getElementById("id_ap_espol").value;
		var v2 = document.getElementById("id_ap_fundespol").value;
		document.getElementById("id_aport_inst").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_aport_inst_ejec").onclick = function(){
		var v1 = document.getElementById("id_ap_espol_ejec").value;
		var v2 = document.getElementById("id_ap_fundespol_ejec").value;
		document.getElementById("id_aport_inst_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	//TOTAL DE COSTOS Y GASTOS DEDUCIBLES
	document.getElementById("id_total_gastos").onclick = function(){
		var v1 = document.getElementById("id_costos_deducibles").value;
		var v2 = document.getElementById("id_gdeducibles").value;
		document.getElementById("id_total_gastos").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_total_gastos_ejec").onclick = function(){
		var v1 = document.getElementById("id_costos_deducibles_ejec").value;
		var v2 = document.getElementById("id_gdeducibles_ejec").value;
		document.getElementById("id_total_gastos_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	//RESULTADOS
	document.getElementById("id_resultados").onclick = function(){
		var v1 = document.getElementById("id_total_ingresos").value;
		var v2 = document.getElementById("id_total_gastos").value;
		document.getElementById("id_resultados").value = parseFloat(v1)-parseFloat(v2);
	};
	document.getElementById("id_resultados_ejec").onclick = function(){
		var v1 = document.getElementById("id_total_ingresos_ejec").value;
		var v2 = document.getElementById("id_total_gastos_ejec").value;
		document.getElementById("id_resultados_ejec").value = parseFloat(v1)-parseFloat(v2);
	};
	
});