function suma_valores(){
	var res = 0.0;
	for(i = 0; i < arguments.length; i++){
		if(arguments[i]!=""){
			res = res+parseFloat(arguments[i]);
		}
	}
	return res;
}

$(document).ready(function(){

	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------

	//INGRESOS
	$("#total_ingresos_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_se_maestrias").value;
			var v2 = document.getElementById("id_se_curs_prog").value;
			var v3 = document.getElementById("id_se_conf_even").value;
			var v4 = document.getElementById("id_s_arriendos").value;
			var v5 = document.getElementById("id_aporte_proy").value;
			var v6 = document.getElementById("id_cert_tasas_otros").value;
			var v7 = document.getElementById("id_dev_est_otros").value;
			var res = suma_valores(v1,v2,v3,v4,v5,v6);
			if(v7!=""){
				res = res - v7;
			}
			document.getElementById("id_total_ingresos").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_se_maestrias_ejec").value;
			var v2 = document.getElementById("id_se_curs_prog_ejec").value;
			var v3 = document.getElementById("id_se_conf_even_ejec").value;
			var v4 = document.getElementById("id_s_arriendos_ejec").value;
			var v5 = document.getElementById("id_aporte_proy_ejec").value;
			var v6 = document.getElementById("id_cert_tasas_otros_ejec").value;
			var v7 = document.getElementById("id_dev_est_otros_ejec").value;
			var res = suma_valores(v1,v2,v3,v4,v5,v6);
			if(v7!=""){
				res = res - v7;
			}
			document.getElementById("id_total_ingresos_ejec").value = res;
		}					
	});

	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------

	//HONORARIOS PROFESIONALES - DOCENTES
	$("#h_profesionales_doc_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_hd_locales").value;
			var v2 = document.getElementById("id_hd_extranjeros").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_hp_docentes").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_hd_locales_ejec").value;
			var v2 = document.getElementById("id_hd_extranjeros_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_hp_docentes_ejec").value = res;
		}					
	});

	// ------------------------------------------------------------------------------------------------------------------------
	// ---------------------------------------------------- PENDIENTE ---------------------------------------------------------
	//HONORARIOS PROFESIONALES
	$("#h_prof_doc_total_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_hp_docentes") || idc.localeCompare("id_h_prof_dietas"))){
			var v1 = document.getElementById("id_hp_docentes").value;
			var v2 = document.getElementById("id_h_prof_dietas").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_h_profesionales").value = res;
		}
		else{
			var v1 = document.getElementById("id_hp_docentes_ejec").value;
			var v2 = document.getElementById("id_h_prof_dietas_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_h_profesionales_ejec").value = res;
			/*if(idc.localeCompare("id_hp_docentes_ejec") || idc.localeCompare("id_h_prof_dietas_ejec")){
				
			}*/
		}					
	});	
	// ------------------------------------------------------------------------------------------------------------------------
	// ------------------------------------------------------------------------------------------------------------------------

	//SUELDOS, SALARIOS Y DEMÁS REMUNERACIONES
	$("#ssrem_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_unif_salarial").value;
			var v2 = document.getElementById("id_h_extras").value;
			var v3 = document.getElementById("id_bonificaciones").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_suel_sal_rem").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_unif_salarial_ejec").value;
			var v2 = document.getElementById("id_h_extras_ejec").value;
			var v3 = document.getElementById("id_bonificaciones_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_suel_sal_rem_ejec").value = res;
		}					
	});

	//BENEFICIOS SOCIALES, INDEMNIZACIONES Y OTRAS REMUNERACIONES
	$("#bsirem_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_dec_ter_sueldo").value;
			var v2 = document.getElementById("id_dec_cua_sueldo").value;
			var v3 = document.getElementById("id_f_reserva").value;
			var v4 = document.getElementById("id_vacaciones").value;
			var res = suma_valores(v1,v2,v3,v4);
			document.getElementById("id_ben_iden_rem").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_dec_ter_sueldo_ejec").value;
			var v2 = document.getElementById("id_dec_cua_sueldo_ejec").value;
			var v3 = document.getElementById("id_f_reserva_ejec").value;
			var v4 = document.getElementById("id_vacaciones_ejec").value;
			var res = suma_valores(v1,v2,v3,v4);
			document.getElementById("id_ben_iden_rem_ejec").value = res;
		}					
	});

	//APORTE A LA SEGURIDAD SOCIAL
	$("#ing_capital_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_aport_patronal").value;
			var v2 = document.getElementById("id_ccc_1").value;
			var v3 = document.getElementById("id_ss_tiempo_parcial").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_ap_seg_soc").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_aport_patronal_ejec").value;
			var v2 = document.getElementById("id_ccc_1_ejec").value;
			var v3 = document.getElementById("id_ss_tiempo_parcial_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_ap_seg_soc_ejec").value = res;
		}					
	});

	//GASTOS DE PERSONAL EN RELACION DE DEPENDENCIA
	$("#g_pers_total_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_suel_sal_rem") || idc.localeCompare("id_ben_iden_rem") || idc.localeCompare("id_ap_seg_soc"))){
			var v1 = document.getElementById("id_suel_sal_rem").value;
			var v2 = document.getElementById("id_ben_iden_rem").value;
			var v3 = document.getElementById("id_ap_seg_soc").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_g_personal").value = res;
		}
		else{
			var v1 = document.getElementById("id_suel_sal_rem_ejec").value;
			var v2 = document.getElementById("id_ben_iden_rem_ejec").value;
			var v3 = document.getElementById("id_ap_seg_soc_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_g_personal_ejec").value = res;
			/*if(idc.localeCompare("id_suel_sal_rem_ejec") || idc.localeCompare("id_ben_iden_rem_ejec") || idc.localeCompare("id_ap_seg_soc_ejec")){
				
			}*/
		}					
	});	

	//SUMINISTROS Y MATERIALES
	$("#sum_mat_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_md_fisico").value;
			var v2 = document.getElementById("id_md_digital").value;
			var v3 = document.getElementById("id_copias").value;
			var v4 = document.getElementById("id_suministros").value;
			var res = suma_valores(v1,v2,v3,v4);
			document.getElementById("id_sum_mat").value = res;
		}else{
			console.log('ejec');
			var ac = document.getElementById("id_ing_capital_ejec").value;
			var v1 = document.getElementById("id_md_fisico_ejec").value;
			var v2 = document.getElementById("id_md_digital_ejec").value;
			var v3 = document.getElementById("id_copias_ejec").value;
			var v4 = document.getElementById("id_suministros_ejec").value;
			var res = suma_valores(v1,v2,v3,v4);
			document.getElementById("id_sum_mat_ejec").value = res;
		}					
	});

	//ALIMENTACIÓN
	$("#alm_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var ac = document.getElementById("id_ing_capital").value;
			var v1 = document.getElementById("id_s_alimentacion").value;
			var v2 = document.getElementById("id_com_salimentacion").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_alimentacion").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_s_alimentacion_ejec").value;
			var v2 = document.getElementById("id_com_salimentacion_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_alimentacion_ejec").value = res;
		}					
	});
	

	//HOSPEDAJE
	$("#hosp_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_s_hopedaje").value;
			var v2 = document.getElementById("id_com_shopedaje").value;
			var v3 = document.getElementById("id_tasa_per").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_hosp").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_s_hopedaje_ejec").value;
			var v2 = document.getElementById("id_com_shopedaje_ejec").value;
			var v3 = document.getElementById("id_tasa_per_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_hosp_ejec").value = res;
		}					
	});
	
	//PASAJES NACIONALES
	$("#p_nac_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_p_nacionales").value;
			var v2 = document.getElementById("id_seb_nacionales").value;
			var v3 = document.getElementById("id_seguro_nacionales").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_pnacional").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_p_nacionales_ejec").value;
			var v2 = document.getElementById("id_seb_nacionales_ejec").value;
			var v3 = document.getElementById("id_seguro_nacionales_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_pnacional_ejec").value = res;
		}					
	});

	//PASAJES INTERNACIONALES
	$("#p_int_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_p_internacionales").value;
			var v2 = document.getElementById("id_seb_internacionales").value;
			var v3 = document.getElementById("id_seguro_internacionales").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_pinternacional").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_p_internacionales_ejec").value;
			var v2 = document.getElementById("id_seb_internacionales_ejec").value;
			var v3 = document.getElementById("id_seguro_internacionales_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_pinternacional_ejec").value = res;
		}					
	});

	//PASAJES AREOS
	$("#p_ar_total_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_pnacional") || idc.localeCompare("id_pinternacional"))){
			var v1 = document.getElementById("id_pnacional").value;
			var v2 = document.getElementById("id_pinternacional").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_pareos").value = res;
		}
		else{
			var v1 = document.getElementById("id_pnacional_ejec").value;
			var v2 = document.getElementById("id_pinternacional_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_pareos_ejec").value = res;
			/*if(idc.localeCompare("id_pnacional_ejec") || idc.localeCompare("id_pinternacional_ejec")){
				
			}*/
		}					
	});	

	//GASTOS DE VIAJE
	$("#gas_v_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_v_nacionales").value;
			var v2 = document.getElementById("id_v_internacionales").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_gastosviaje").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_v_nacionales_ejec").value;
			var v2 = document.getElementById("id_v_internacionales_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_gastosviaje_ejec").value = res;
		}					
	});

	//COSTOS DEL SERVICIO - DEDUCIBLES
	$("#costo_serv_total_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_h_profesionales") || idc.localeCompare("id_g_personal") || idc.localeCompare("id_s_pers_nomb") || idc.localeCompare("id_sum_mat") ||
							idc.localeCompare("id_licencias") || idc.localeCompare("id_alimentacion") || idc.localeCompare("id_hosp") || idc.localeCompare("id_pareos") ||
							idc.localeCompare("id_transporte") || idc.localeCompare("id_seg_estud") || idc.localeCompare("id_gastosviaje") || idc.localeCompare("id_cap_docente"))){
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
		}
		else{
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
			/*if(idc.localeCompare("id_h_profesionales_ejec") || idc.localeCompare("id_g_personal_ejec") || idc.localeCompare("id_s_pers_nomb_ejec") || idc.localeCompare("id_sum_mat_ejec") ||
							idc.localeCompare("id_licencias_ejec") || idc.localeCompare("id_alimentacion_ejec") || idc.localeCompare("id_hosp_ejec") || idc.localeCompare("id_pareos_ejec") ||
							idc.localeCompare("id_transporte_ejec") || idc.localeCompare("id_seg_estud_ejec") || idc.localeCompare("id_gastosviaje_ejec") || idc.localeCompare("id_cap_docente_ejec")){
				
			}*/	
		}					
	});
	
	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------
	//----------------------------------------------------------------------------------------------------------------------------------
	
	//SUELDO, SALARIOS  Y DEMAS REMUNERACIONES
	$("#gd_ssrem_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_gd_unif_salarial").value;
			var v2 = document.getElementById("id_gd_h_extras").value;
			var v3 = document.getElementById("id_gd_bonificaciones").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gd_suel_sal_rem").value = res;
		}else{
			console.log('ejec');
			var ac = document.getElementById("id_ing_capital_ejec").value;
			var v1 = document.getElementById("id_gd_unif_salarial_ejec").value;
			var v2 = document.getElementById("id_gd_h_extras_ejec").value;
			var v3 = document.getElementById("id_gd_bonificaciones_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gd_suel_sal_rem_ejec").value = res;
		}					
	});
	
	//BENEFICIOS SOCIALES, INDEMNIZACIONES Y OTRAS REMUNERACIONES
	$("#gd_bsirem_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_gd_dec_ter_sueldo").value;
			var v2 = document.getElementById("id_gd_dec_cua_sueldo").value;
			var v3 = document.getElementById("id_gd_f_reserva").value;
			var v4 = document.getElementById("id_gd_vacaciones").value;
			var res = suma_valores(v1,v2,v3,v4);
			document.getElementById("id_gd_ben_iden_rem").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_gd_dec_ter_sueldo_ejec").value;
			var v2 = document.getElementById("id_gd_dec_cua_sueldo_ejec").value;
			var v3 = document.getElementById("id_gd_f_reserva_ejec").value;
			var v4 = document.getElementById("id_gd_vacaciones_ejec").value;
			var res = suma_valores(v1,v2,v3,v4);
			document.getElementById("id_gd_ben_iden_rem_ejec").value = res;
		}					
	});

	//APORTE A LA SEGURIDAD SOCIAL 
	$("#gd_aport_ss_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_gd_aport_patronal").value;
			var v2 = document.getElementById("id_gd_ccc_1").value;
			var v3 = document.getElementById("id_gd_ss_tiempo_parcial").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gd_ap_seg_soc").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_gd_aport_patronal_ejec").value;
			var v2 = document.getElementById("id_gd_ccc_1_ejec").value;
			var v3 = document.getElementById("id_gd_ss_tiempo_parcial_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gd_ap_seg_soc_ejec").value = res;
		}					
	});

	//GASTOS DE PERSONAL CON RELACION DE DEPENDENCIA - GASTOS DEDUCIBLES
	$("#gast_deduc_total_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_gd_suel_sal_rem") || idc.localeCompare("id_gd_ben_iden_rem") || idc.localeCompare("id_gd_ap_seg_soc"))){
			var v1 = document.getElementById("id_gd_suel_sal_rem").value;
			var v2 = document.getElementById("id_gd_ben_iden_rem").value;
			var v3 = document.getElementById("id_gd_ap_seg_soc").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gd_gast_pers").value = res;
		}
		else{
			var v1 = document.getElementById("id_gd_suel_sal_rem_ejec").value;
			var v2 = document.getElementById("id_gd_ben_iden_rem_ejec").value;
			var v3 = document.getElementById("id_gd_ap_seg_soc_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gd_gast_pers_ejec").value = res;
			/*if(idc.localeCompare("id_gd_suel_sal_rem_ejec") || idc.localeCompare("id_gd_ben_iden_rem_ejec") || idc.localeCompare("id_gd_ap_seg_soc_ejec")){
				
			}*/		
		}					
	});	

	//HONORARIOS
	$("#gd_hon_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_gd_h_prof_dietas").value;
			var v2 = document.getElementById("id_serv_ocasionales").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_honorarios").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_gd_h_prof_dietas_ejec").value;
			var v2 = document.getElementById("id_serv_ocasionales_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_honorarios_ejec").value = res;
		}					
	});

	//GASTOS EN SERVICIOS ADMINISTRATIVOS
	$("#gast_sad_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
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
		}else{
			console.log('ejec');
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
		}					
	});

	//MANTENIMIENTO Y REPARACIONES
	$("#mrep_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_man_rep_generales").value;
			var v2 = document.getElementById("id_man_rep_equipos").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_mant_rep").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_man_rep_generales_ejec").value;
			var v2 = document.getElementById("id_man_rep_equipos_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_mant_rep_ejec").value = res;
		}					
	});

	//PROVISIONES
	$("#prov_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_p_jubil_patr").value;
			var v2 = document.getElementById("id_p_desahucio").value;
			var v3 = document.getElementById("id_desp_intepestivo").value;
			var v4 = document.getElementById("id_prov_cuent_incobrables").value;
			var v5 = document.getElementById("id_prov_det_activos").value;
			var v6 = document.getElementById("id_prov_otras").value;
			var res = suma_valores(v1,v2,v3,v4,v5,v6);
			document.getElementById("id_prov").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_p_jubil_patr_ejec").value;
			var v2 = document.getElementById("id_p_desahucio_ejec").value;
			var v3 = document.getElementById("id_desp_intepestivo_ejec").value;
			var v4 = document.getElementById("id_prov_cuent_incobrables_ejec").value;
			var v5 = document.getElementById("id_prov_det_activos_ejec").value;
			var v6 = document.getElementById("id_prov_otras_ejec").value;
			var res = suma_valores(v1,v2,v3,v4,v5,v6);
			document.getElementById("id_prov_ejec").value = res;
		}					
	});
	
	//ALQUILER DE EQUIPOS
	$("#alq_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_alq_equipos").value;
			var res = suma_valores(v1);
			document.getElementById("id_alq_eqpos").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_alq_equipos_ejec").value;
			var res = suma_valores(v1);
			document.getElementById("id_alq_eqpos_ejec").value = res;
		}					
	});
	
	//SUMINISTROS Y MATERIALES
	$("#sm_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_sum_oficina").value;
			var v2 = document.getElementById("id_sum_limpieza").value;
			var v3 = document.getElementById("id_gd_copias").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gd_sum_mat").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_sum_oficina_ejec").value;
			var v2 = document.getElementById("id_sum_limpieza_ejec").value;
			var v3 = document.getElementById("id_gd_copias_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gd_sum_mat_ejec").value = res;
		}					
	});

	//GASTOS DE JARDINERIA Y ORNAMENTACION
	$("#gast_jar_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_mat_jardineria").value;
			var v2 = document.getElementById("id_serv_jardineria").value;
			var v3 = document.getElementById("id_alim_tortugas").value;
			var v4 = document.getElementById("id_med_tortugas").value;
			var res = suma_valores(v1,v2,v3,v4);
			document.getElementById("id_gas_jar_orn").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_mat_jardineria_ejec").value;
			var v2 = document.getElementById("id_serv_jardineria_ejec").value;
			var v3 = document.getElementById("id_alim_tortugas_ejec").value;
			var v4 = document.getElementById("id_med_tortugas_ejec").value;
			var res = suma_valores(v1,v2,v3,v4);
			document.getElementById("id_gas_jar_orn_ejec").value = res;
		}					
	});

	//PROMOCION Y PUBLICIDAD
	$("#pro_pub_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_mat_publicitario").value;
			var v2 = document.getElementById("id_pub_impresos").value;
			var v3 = document.getElementById("id_pub_digitales").value;
			var v4 = document.getElementById("id_cong_even_fer").value;
			var res = suma_valores(v1,v2,v3,v4);
			document.getElementById("id_prom_pub").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_mat_publicitario_ejec").value;
			var v2 = document.getElementById("id_pub_impresos_ejec").value;
			var v3 = document.getElementById("id_pub_digitales_ejec").value;
			var v4 = document.getElementById("id_cong_even_fer_ejec").value;
			var res = suma_valores(v1,v2,v3,v4);
			document.getElementById("id_prom_pub_ejec").value = res;
		}					
	});

	//GASTOS DE MARKETING
	$("#g_mark_total_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_prom_pub") || idc.localeCompare("id_com_ventas"))){
			var v1 = document.getElementById("id_prom_pub").value;
			var v2 = document.getElementById("id_com_ventas").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_gast_mark").value = res;
		}
		else{
			var v1 = document.getElementById("id_prom_pub_ejec").value;
			var v2 = document.getElementById("id_com_ventas_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_gast_mark_ejec").value = res;
			/*if(idc.localeCompare("id_prom_pub_ejec") || idc.localeCompare("id_com_ventas_ejec")){
				
			}*/		
		}					
	});	

	//GASTOS DE ACREDITACION
	$("#g_acred_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_aacsb").value;
			var v2 = document.getElementById("id_gac_pmi").value;
			var v3 = document.getElementById("id_iso").value;
			var v4 = document.getElementById("id_amba").value;
			var res = suma_valores(v1,v2,v3,v4);		
			document.getElementById("id_gast_acred").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_aacsb_ejec").value;
			var v2 = document.getElementById("id_gac_pmi_ejec").value;
			var v3 = document.getElementById("id_iso_ejec").value;
			var v4 = document.getElementById("id_amba_ejec").value;
			var res = suma_valores(v1,v2,v3,v4);
			document.getElementById("id_gast_acred_ejec").value = res;
		}					
	});

	//PASAJES NACIONALES
	$("#gdrep_pnac_total :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_gdrep_p_nacionales").value;
			var v2 = document.getElementById("id_gdrep_seb_nacionales").value;
			var v3 = document.getElementById("id_gdrep_seguro_nacionales").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gd_pnacional").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_gdrep_p_nacionales_ejec").value;
			var v2 = document.getElementById("id_gdrep_seb_nacionales_ejec").value;
			var v3 = document.getElementById("id_gdrep_seguro_nacionales_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gd_pnacional_ejec").value = res;
		}					
	});

	//PASAJES INTERNACIONALES
	$("#gdrep_pint_total :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_gdrep_p_internacionales").value;
			var v2 = document.getElementById("id_gdrep_seb_internacionales").value;
			var v3 = document.getElementById("id_gdrep_seguro_internacionales").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gd_pinternacional").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_gdrep_p_internacionales_ejec").value;
			var v2 = document.getElementById("id_gdrep_seb_internacionales_ejec").value;
			var v3 = document.getElementById("id_gdrep_seguro_internacionales_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gd_pinternacional_ejec").value = res;
		}					
	});
	
	//PASAJES AEREOS
	$("#gd_pareos_total_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_gd_pnacional") || idc.localeCompare("id_gd_pinternacional"))){
			var v1 = document.getElementById("id_gd_pnacional").value;
			var v2 = document.getElementById("id_gd_pinternacional").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_gd_pareos").value = res;
		}
		else{
			var v1 = document.getElementById("id_gd_pnacional_ejec").value;
			var v2 = document.getElementById("id_gd_pinternacional_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_gd_pareos_ejec").value = res;
			/*if(idc.localeCompare("id_gd_pnacional_ejec") || idc.localeCompare("id_gd_pinternacional_ejec")){
				
			}*/		
		}					
	});	

	//GASTOS DE VIAJE
	$("#gd_gviaje_total_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_gdrep_v_nacionales") || idc.localeCompare("id_gdrep_v_internacionales") || idc.localeCompare("id_gd_pareos"))){
			var v1 = document.getElementById("id_gdrep_v_nacionales").value;
			var v2 = document.getElementById("id_gdrep_v_internacionales").value;
			var v3 = document.getElementById("id_gd_pareos").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gas_viaje").value = res;
		}
		else{
			var v1 = document.getElementById("id_gdrep_v_nacionales_ejec").value;
			var v2 = document.getElementById("id_gdrep_v_internacionales_ejec").value;
			var v3 = document.getElementById("id_gd_pareos_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gas_viaje_ejec").value = res;
			/*if(idc.localeCompare("id_gdrep_v_nacionales_ejec") || idc.localeCompare("id_gdrep_v_internacionales_ejec") || idc.localeCompare("id_gd_pareos_ejec")){
				
			}*/		
		}					
	});	

	//GASTOS DE REPRESENTACION
	$("#gast_rep_total_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_ing_corrientes") || idc.localeCompare("id_ing_financiamiento") || idc.localeCompare("id_ing_capital"))){
			var v1 = document.getElementById("id_gdrep_hospedaje").value;
			var v2 = document.getElementById("id_gas_viaje").value;
			var v3 = document.getElementById("id_conv_eventos").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gas_repre").value = res;
		}
		else{
			var v1 = document.getElementById("id_gdrep_hospedaje_ejec").value;
			var v2 = document.getElementById("id_gas_viaje_ejec").value;
			var v3 = document.getElementById("id_conv_eventos_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gas_repre_ejec").value = res;
			/*if(idc.localeCompare("id_ing_corrientes_ejec") || idc.localeCompare("id_ing_financiamiento_ejec") || idc.localeCompare("id_ing_capital_ejec")){
				
			}*/		
		}					
	});	

	//GASTOS DE VIAJE - GASTOS DE INVESTIGACION
	$("#gv_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_gdinv_v_nacionales").value;
			var v2 = document.getElementById("id_gdinv_v_internacionales").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_inv_gas_viaje").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_gdinv_v_nacionales_ejec").value;
			var v2 = document.getElementById("id_gdinv_v_internacionales_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_inv_gas_viaje_ejec").value = res;
		}					
	});

	//PASAJES NACIONALES - GASTOS DE INVESTIGACION
	$("#gbinv_pnac_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_gdinv_p_nacionales").value;
			var v2 = document.getElementById("id_gdinv_seb_nacionales").value;
			var v3 = document.getElementById("id_gdinv_seguro_nacionales").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gdinv_pnacional").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_gdinv_p_nacionales_ejec").value;
			var v2 = document.getElementById("id_gdinv_seb_nacionales_ejec").value;
			var v3 = document.getElementById("id_gdinv_seguro_nacionales_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gdinv_pnacional_ejec").value = res;
		}					
	});

	//PASAJES INTERNACIONALES - GASTOS DE INVESTIGACION 
	$("#gbinv_pint_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_gdinv_p_internacionales").value;
			var v2 = document.getElementById("id_gdinv_seb_internacionales").value;
			var v3 = document.getElementById("id_gdinv_seguro_internacionales").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gdinv_pinternacional").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_gdinv_p_internacionales_ejec").value;
			var v2 = document.getElementById("id_gdinv_seb_internacionales_ejec").value;
			var v3 = document.getElementById("id_gdinv_seguro_internacionales_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gdinv_pinternacional_ejec").value = res;
		}					
	});

	//PASAJES AEREOS - GASTOS DE INVESTIGACION
	$("#gdinv_pareos_total_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_gdinv_pnacional") || idc.localeCompare("id_gdinv_pinternacional"))){
			var v1 = document.getElementById("id_gdinv_pnacional").value;
			var v2 = document.getElementById("id_gdinv_pinternacional").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_gdinv_paereos").value = res;
		}
		else{
			var v1 = document.getElementById("id_gdinv_pnacional_ejec").value;
			var v2 = document.getElementById("id_gdinv_pinternacional_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_gdinv_paereos_ejec").value = res;
			/*if(idc.localeCompare("id_gdinv_pnacional_ejec") || idc.localeCompare("id_gdinv_pinternacional_ejec")){
				
			}*/		
		}					
	});	

	//GASTOS DE INVESTIGACION
	$("#gastos_inves_total_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_gdinv_capacitacion") || idc.localeCompare("id_inv_gas_viaje") || idc.localeCompare("id_gdinv_paereos") || idc.localeCompare("id_gd_honorarios")
			|| idc.localeCompare("id_gd_alimentacion") || idc.localeCompare("id_gd_hospedaje") || idc.localeCompare("id_gd_susc_memb")
			|| idc.localeCompare("id_publicaciones") || idc.localeCompare("id_conv_even_proy"))){
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
		}
		else{
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
			/*if(idc.localeCompare("id_gdinv_capacitacion_ejec") || idc.localeCompare("id_inv_gas_viaje_ejec") || idc.localeCompare("id_gdinv_paereos_ejec") || idc.localeCompare("id_gd_honorarios_ejec")
			|| idc.localeCompare("id_gd_alimentacion_ejec") || idc.localeCompare("id_gd_hospedaje_ejec") || idc.localeCompare("id_gd_susc_memb_ejec")
			|| idc.localeCompare("id_publicaciones_ejec") || idc.localeCompare("id_conv_even_proy_ejec")){
				
			}*/		
		}					
	});	

	//GASTOS DE INTERES
	$("#gas_int_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_i_banc_local").value;
			var v2 = document.getElementById("id_i_pag_local").value;
			var v3 = document.getElementById("id_i_pag_no_local").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gast_interes").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_i_banc_local_ejec").value;
			var v2 = document.getElementById("id_i_pag_local_ejec").value;
			var v3 = document.getElementById("id_i_pag_no_local_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gast_interes_ejec").value = res;
		}					
	});
	
	//GASTOS DE COMISIONES BANCARIAS
	$("#gas_com_ban_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_com_bancarias").value;
			var v2 = document.getElementById("id_com_tarj_cred").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_gas_com_ban").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_com_bancarias_ejec").value;
			var v2 = document.getElementById("id_com_tarj_cred_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_gas_com_ban_ejec").value = res;
		}					
	});

	//GASTOS POR IMPUESTO
	$("#gas_imp_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_iva").value;
			var v2 = document.getElementById("id_isd").value;
			var v3 = document.getElementById("id_ice").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gas_impu").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_iva_ejec").value;
			var v2 = document.getElementById("id_isd_ejec").value;
			var v3 = document.getElementById("id_ice_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gas_impu_ejec").value = res;
		}					
	});

	//GASTOS DE DEPRECIACION
	$("#gas_depre_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_d_propiedades").value;
			var v2 = document.getElementById("id_d_revaluo_prop").value;
			var v3 = document.getElementById("id_d_prop_inversion").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gas_depre").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_d_propiedades_ejec").value;
			var v2 = document.getElementById("id_d_revaluo_prop_ejec").value;
			var v3 = document.getElementById("id_d_prop_inversion_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_gas_depre_ejec").value = res;
		}					
	});

	//SERVICIOS PUBLICOS
	$("#serv_pub_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_agua").value;
			var v2 = document.getElementById("id_luz").value;
			var v3 = document.getElementById("id_fono").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_serv_pub").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_agua_ejec").value;
			var v2 = document.getElementById("id_luz_ejec").value;
			var v3 = document.getElementById("id_fono_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_serv_pub_ejec").value = res;
		}					
	});

	//APORTES INSTITUCIONALES
	$("#ap_inst_total_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			var v1 = document.getElementById("id_ap_espol").value;
			var v2 = document.getElementById("id_ap_fundespol").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_aport_inst").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_ap_espol_ejec").value;
			var v2 = document.getElementById("id_ap_fundespol_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_aport_inst_ejec").value = res;
		}					
	});

	//GASTOS DEDUCIBLES
	$("#gast_deduc_total_total_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_gd_gast_pers") || idc.localeCompare("id_honorarios") || idc.localeCompare("id_gas_ser_admin") || idc.localeCompare("id_mant_rep")
			|| idc.localeCompare("id_mat_ferreteria") || idc.localeCompare("id_prov") || idc.localeCompare("id_alq_eqpos")
			|| idc.localeCompare("id_gd_sum_mat") || idc.localeCompare("id_gd_transporte") || idc.localeCompare("id_seg_reaseg")
			|| idc.localeCompare("id_gas_jar_orn") || idc.localeCompare("id_gast_mark") || idc.localeCompare("id_gast_acred")
			|| idc.localeCompare("id_gas_repre") || idc.localeCompare("id_gdinv") || idc.localeCompare("id_gast_interes")
			|| idc.localeCompare("id_gas_com_ban") || idc.localeCompare("id_imp_cont") || idc.localeCompare("id_serv_pub")
			|| idc.localeCompare("id_gas_depre") || idc.localeCompare("id_g_amortizacion") || idc.localeCompare("id_gd_susc_memb")
			|| idc.localeCompare("id_aport_inst") || idc.localeCompare("id_pago_otros"))){
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
		}
		else{
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
		}					
	});

	//TOTAL DE COSTOS Y GASTOS DEDUCIBLES
	$("#cos_gas_deduc_total_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_costos_deducibles") || idc.localeCompare("id_gdeducibles"))){
			var v1 = document.getElementById("id_costos_deducibles").value;
			var v2 = document.getElementById("id_gdeducibles").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_total_gastos").value = res;
		}
		else{
			var v1 = document.getElementById("id_costos_deducibles_ejec").value;
			var v2 = document.getElementById("id_gdeducibles_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_total_gastos_ejec").value = res;
		}					
	});

	//RESULTADOS
	$("#resultado_total_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_total_ingresos") || idc.localeCompare("id_total_gastos"))){
			var v1 = document.getElementById("id_total_ingresos").value;
			var v2 = document.getElementById("id_total_gastos").value;
			if(v1 == ""){
				v1 = 0.0;
			}
			if(v2 == ""){
				v2 = 0.0;
			}
			var res = v1-v2;
			document.getElementById("id_resultados").value = res;
		}
		else{
			var v1 = document.getElementById("id_total_ingresos_ejec").value;
			var v2 = document.getElementById("id_total_gastos_ejec").value;
			if(v1 == ""){
				v1 = 0.0;
			}
			if(v2 == ""){
				v2 = 0.0;
			}
			var res = v1-v2;
			document.getElementById("id_resultados_ejec").value = res;
		}					
	});
});