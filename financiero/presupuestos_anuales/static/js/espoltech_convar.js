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
	//INGRESOS CORRIENTES
	$("#ing_corrientes_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_vb_serv_tecnicos_espec").value;
			var v2 = document.getElementById("id_vb_curs_sem_maes").value;
			var v3 = document.getElementById("id_td_prov_gobcen").value;
			var v4 = document.getElementById("id_td_prov_entdesc").value;
			var v5 = document.getElementById("id_td_prov_entpub").value;
			var v6 = document.getElementById("id_td_prov_gobaut").value;
			var v7 = document.getElementById("id_otros_ingCorr").value;
			var res = suma_valores(v1,v2,v3,v4,v5,v6,v7);
			document.getElementById("id_ing_corrientes").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_vb_serv_tecnicos_espec_ejec").value;
			var v2 = document.getElementById("id_vb_curs_sem_maes_ejec").value;
			var v3 = document.getElementById("id_td_prov_gobcen_ejec").value;
			var v4 = document.getElementById("id_td_prov_entdesc_ejec").value;
			var v5 = document.getElementById("id_td_prov_entpub_ejec").value;
			var v6 = document.getElementById("id_td_prov_gobaut_ejec").value;
			var v7 = document.getElementById("id_otros_ingCorr_ejec").value;
			var res = suma_valores(v1,v2,v3,v4,v5,v6,v7);
			document.getElementById("id_ing_corrientes_ejec").value = res;
		}					
	});

	//INGRESOS DE FINANCIAMIENO
	$("#ing_financiamiento_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log('plan');
			var v1 = document.getElementById("id_fondo_autogest").value;
			var v2 = document.getElementById("id_cta_x_cobrar").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_ing_financiamiento").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_fondo_autogest_ejec").value;
			var v2 = document.getElementById("id_cta_x_cobrar_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_ing_financiamiento_ejec").value = res;
		}					
	});

	//INGRESOS DE CAPITAL
	$("#ing_capital_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_td_cap_prov_gobcen").value;
			var v2 = document.getElementById("id_td_cap_prov_entdesc").value;
			var v3 = document.getElementById("id_td_cap_prov_entpub").value;
			var v4 = document.getElementById("id_td_cap_prov_gobaut").value;
			var v5 = document.getElementById("id_don_cap_ext").value;
			var res = suma_valores(v1,v2,v3,v4,v5);
			document.getElementById("id_ing_capital").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_td_cap_prov_gobcen_ejec").value;
			var v2 = document.getElementById("id_td_cap_prov_entdesc_ejec").value;
			var v3 = document.getElementById("id_td_cap_prov_entpub_ejec").value;
			var v4 = document.getElementById("id_td_cap_prov_gobaut_ejec").value;
			var v5 = document.getElementById("id_don_cap_ext_ejec").value;
			var res = suma_valores(v1,v2,v3,v4,v5);
			document.getElementById("id_ing_capital_ejec").value = res;
		}					
	});

	// ------------------------------------------------------------------------------------------------------------------------
	// ---------------------------------------------------- PENDIENTE ---------------------------------------------------------
	//TOTAL INGRESOS AÑO
	$("#total_ingresos_div :input").change(function(e){
		var idc = e.target.id;
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_ing_corrientes") || idc.localeCompare("id_ing_financiamiento") || idc.localeCompare("id_ing_capital"))){
			var v1 = document.getElementById("id_ing_corrientes").value;
			var v2 = document.getElementById("id_ing_financiamiento").value;
			var v3 = document.getElementById("id_ing_capital").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_total_ingresos").value = res;
		}
		else{
			var v1 = document.getElementById("id_ing_corrientes_ejec").value;
			var v2 = document.getElementById("id_ing_financiamiento_ejec").value;
			var v3 = document.getElementById("id_ing_capital_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_total_ingresos_ejec").value = res;
		}					
	});	
	// ------------------------------------------------------------------------------------------------------------------------
	// ------------------------------------------------------------------------------------------------------------------------

	//GASTOS EN PERSONAL
	$("#g_personal_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_rem_unificadas").value;
			var v2 = document.getElementById("id_h_ext_supl").value;
			var v3 = document.getElementById("id_encargos").value;
			var v4 = document.getElementById("id_dec_ter_sueldo").value;
			var v5 = document.getElementById("id_dec_cua_sueldo").value;
			var v6 = document.getElementById("id_aporte_patronal").value;
			var v7 = document.getElementById("id_fondo_reserva").value;
			var v8 = document.getElementById("id_comp_desahucio").value;
			var v9 = document.getElementById("id_comp_vacaciones").value;
			var v10 = document.getElementById("id_hp_director").value;
			var v11 = document.getElementById("id_hp_coordinador").value;
			var v12 = document.getElementById("id_hp_expertos").value;
			var v13 = document.getElementById("id_hp_otros").value;
			var v14 = document.getElementById("id_hp_dict_clases").value;
			var v15 = document.getElementById("id_ind_laborales").value;
			var res = suma_valores(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15);
			document.getElementById("id_g_personal").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_rem_unificadas_ejec").value;
			var v2 = document.getElementById("id_h_ext_supl_ejec").value;
			var v3 = document.getElementById("id_encargos_ejec").value;
			var v4 = document.getElementById("id_dec_ter_sueldo_ejec").value;
			var v5 = document.getElementById("id_dec_cua_sueldo_ejec").value;
			var v6 = document.getElementById("id_aporte_patronal_ejec").value;
			var v7 = document.getElementById("id_fondo_reserva_ejec").value;
			var v8 = document.getElementById("id_comp_desahucio_ejec").value;
			var v9 = document.getElementById("id_comp_vacaciones_ejec").value;
			var v10 = document.getElementById("id_hp_director_ejec").value;
			var v11 = document.getElementById("id_hp_coordinador_ejec").value;
			var v12 = document.getElementById("id_hp_expertos_ejec").value;
			var v13 = document.getElementById("id_hp_otros_ejec").value;
			var v14 = document.getElementById("id_hp_dict_clases_ejec").value;
			var v15 = document.getElementById("id_ind_laborales_ejec").value;
			var res = suma_valores(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15);
			document.getElementById("id_g_personal_ejec").value = res;
		}					
	});

	//BIENES Y SERVICIOS DE CONSUMO
	$("#bs_consumo_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_agua").value;
			var v2 = document.getElementById("id_energia_elec").value;
			var v3 = document.getElementById("id_telecomunicaciones").value;
			var v4 = document.getElementById("id_correo").value;
			var v5 = document.getElementById("id_trans_personal").value;
			var v6 = document.getElementById("id_impresion").value;
			var v7 = document.getElementById("id_publicidad").value;
			var v8 = document.getElementById("id_serv_seguridad").value;
			var v9 = document.getElementById("id_serv_aseo").value;
			var v10 = document.getElementById("id_membresias").value;
			var v11 = document.getElementById("id_otros_serv_generales").value;
			var v12 = document.getElementById("id_pasajes_int").value;
			var v13 = document.getElementById("id_pasajes_ext").value;
			var v14 = document.getElementById("id_viaticos_int").value;
			var v15 = document.getElementById("id_viaticos_ext").value;
			var v16 = document.getElementById("id_edificios").value;
			var v17 = document.getElementById("id_gastos_mant_mobil").value;
			var v18 = document.getElementById("id_gastos_mant_equipos").value;
			var v19 = document.getElementById("id_gastos_mant_vehic").value;
			var v20 = document.getElementById("id_gastos_libros").value;
			var v21 = document.getElementById("id_otros_gastos").value;
			var v22 = document.getElementById("id_arr_edificios").value;
			var v23 = document.getElementById("id_arr_mobiliarios").value;
			var v24 = document.getElementById("id_arr_maquinaria").value;
			var v25 = document.getElementById("id_cont_estudios").value;
			var v26 = document.getElementById("id_serv_capacitacion").value;
			var v27 = document.getElementById("id_fiscalizacion").value;
			var v28 = document.getElementById("id_arr_equipos").value;
			var v29 = document.getElementById("id_mant_equipos_info").value;
			var v30 = document.getElementById("id_serv_alimentacion").value;
			var v31 = document.getElementById("id_gastos_vestimenta").value;
			var v32 = document.getElementById("id_combustible").value;
			var v33 = document.getElementById("id_materiales_ofician").value;
			var v34 = document.getElementById("id_materiales_aseo").value;
			var v35 = document.getElementById("id_herramientas_53").value;
			var v36 = document.getElementById("id_mat_impresion").value;
			var v37 = document.getElementById("id_medicinas").value;
			var v38 = document.getElementById("id_mat_laboratorio").value;
			var v39 = document.getElementById("id_mat_construccion").value;
			var v40 = document.getElementById("id_mat_didacticos").value;
			var v41 = document.getElementById("id_respuestos").value;
			var v42 = document.getElementById("id_suministros_agrop").value;
			var v43 = document.getElementById("id_otros_bienes").value;
			var v44 = document.getElementById("id_mobiliarios_bienes").value;
			var v45 = document.getElementById("id_maquinaria_equipos_bienes").value;
			var v46 = document.getElementById("id_equipos_sist_paq_53").value;
			var v47 = document.getElementById("id_libros_53").value;
			var v48 = document.getElementById("id_partes_repuestos_53").value;
			var res = suma_valores(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30,v31,v32,v33,v34,v35,v36,v37,v38,v39,v40,v41,v42,v43,v44,v45,v46,v47,v48);
			document.getElementById("id_bs_consumo").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_agua_ejec").value;
			var v2 = document.getElementById("id_energia_elec_ejec").value;
			var v3 = document.getElementById("id_telecomunicaciones_ejec").value;
			var v4 = document.getElementById("id_correo_ejec").value;
			var v5 = document.getElementById("id_trans_personal_ejec").value;
			var v6 = document.getElementById("id_impresion_ejec").value;
			var v7 = document.getElementById("id_publicidad_ejec").value;
			var v8 = document.getElementById("id_serv_seguridad_ejec").value;
			var v9 = document.getElementById("id_serv_aseo_ejec").value;
			var v10 = document.getElementById("id_membresias_ejec").value;
			var v11 = document.getElementById("id_otros_serv_generales_ejec").value;
			var v12 = document.getElementById("id_pasajes_int_ejec").value;
			var v13 = document.getElementById("id_pasajes_ext_ejec").value;
			var v14 = document.getElementById("id_viaticos_int_ejec").value;
			var v15 = document.getElementById("id_viaticos_ext_ejec").value;
			var v16 = document.getElementById("id_edificios_ejec").value;
			var v17 = document.getElementById("id_gastos_mant_mobil_ejec").value;
			var v18 = document.getElementById("id_gastos_mant_equipos_ejec").value;
			var v19 = document.getElementById("id_gastos_mant_vehic_ejec").value;
			var v20 = document.getElementById("id_gastos_libros_ejec").value;
			var v21 = document.getElementById("id_otros_gastos_ejec").value;
			var v22 = document.getElementById("id_arr_edificios_ejec").value;
			var v23 = document.getElementById("id_arr_mobiliarios_ejec").value;
			var v24 = document.getElementById("id_arr_maquinaria_ejec").value;
			var v25 = document.getElementById("id_cont_estudios_ejec").value;
			var v26 = document.getElementById("id_serv_capacitacion_ejec").value;
			var v27 = document.getElementById("id_fiscalizacion_ejec").value;
			var v28 = document.getElementById("id_arr_equipos_ejec").value;
			var v29 = document.getElementById("id_mant_equipos_info_ejec").value;
			var v30 = document.getElementById("id_serv_alimentacion_ejec").value;
			var v31 = document.getElementById("id_gastos_vestimenta_ejec").value;
			var v32 = document.getElementById("id_combustible_ejec").value;
			var v33 = document.getElementById("id_materiales_ofician_ejec").value;
			var v34 = document.getElementById("id_materiales_aseo_ejec").value;
			var v35 = document.getElementById("id_herramientas_53_ejec").value;
			var v36 = document.getElementById("id_mat_impresion_ejec").value;
			var v37 = document.getElementById("id_medicinas_ejec").value;
			var v38 = document.getElementById("id_mat_laboratorio_ejec").value;
			var v39 = document.getElementById("id_mat_construccion_ejec").value;
			var v40 = document.getElementById("id_mat_didacticos_ejec").value;
			var v41 = document.getElementById("id_respuestos_ejec").value;
			var v42 = document.getElementById("id_suministros_agrop_ejec").value;
			var v43 = document.getElementById("id_otros_bienes_ejec").value;
			var v44 = document.getElementById("id_mobiliarios_bienes_ejec").value;
			var v45 = document.getElementById("id_maquinaria_equipos_bienes_ejec").value;
			var v46 = document.getElementById("id_equipos_sist_paq_53_ejec").value;
			var v47 = document.getElementById("id_libros_53_ejec").value;
			var v48 = document.getElementById("id_partes_repuestos_53_ejec").value;
			var res = suma_valores(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30,v31,v32,v33,v34,v35,v36,v37,v38,v39,v40,v41,v42,v43,v44,v45,v46,v47,v48);
			document.getElementById("id_bs_consumo_ejec").value = res;
		}					
	});

	//OTROS GASTOS CORRIENTES
	$("#otros_gastos_corr_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_iva").value;
			var v2 = document.getElementById("id_tasas").value;
			var v3 = document.getElementById("id_otros_imp").value;
			var v4 = document.getElementById("id_seguros").value;
			var v5 = document.getElementById("id_comisiones_banc").value;
			var v6 = document.getElementById("id_devoluciones").value;
			var v7 = document.getElementById("id_otros_gastos_fin").value;
			var res = suma_valores(v1,v2,v3,v4,v5,v6,v7);
			document.getElementById("id_otros_gastos_corr").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_iva_ejec").value;
			var v2 = document.getElementById("id_tasas_ejec").value;
			var v3 = document.getElementById("id_otros_imp_ejec").value;
			var v4 = document.getElementById("id_seguros_ejec").value;
			var v5 = document.getElementById("id_comisiones_banc_ejec").value;
			var v6 = document.getElementById("id_devoluciones_ejec").value;
			var v7 = document.getElementById("id_otros_gastos_fin_ejec").value;
			var res = suma_valores(v1,v2,v3,v4,v5,v6,v7);
			document.getElementById("id_otros_gastos_corr_ejec").value = res;
		}					
	});

	//TRANSF. CORRIENTES: APORTACIONES DE ACUERDO A LINEAMIENTOS
	$("#transf_corrientes_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_espoltech_ep").value;
			var v2 = document.getElementById("id_part_espol").value;
			var v3 = document.getElementById("id_part_unidad").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_transf_corrientes").value = res;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_espoltech_ep_ejec").value;
			var v2 = document.getElementById("id_part_espol_ejec").value;
			var v3 = document.getElementById("id_part_unidad_ejec").value;
			var res = suma_valores(v1,v2,v3);
			document.getElementById("id_transf_corrientes_ejec").value = res;
		}					
	});

	
	// ------------------------------------------------------------------------------------------------------------------------
	// ---------------------------------------------------- PENDIENTE ---------------------------------------------------------
	//GASTOS DE CAPITAL
	/*document.getElementById("id_g_capital").onclick = function(){
		var v1 = document.getElementById("id_act_fijos").value;
		var res = suma_valores(v1);
		document.getElementById("id_g_capital").value = res;
	};
	document.getElementById("id_g_capital_ejec").onclick = function(){
		var v1 = document.getElementById("id_act_fijos_ejec").value;
		var res = suma_valores(v1);
		document.getElementById("id_g_capital_ejec").value = res;
	};*/
	// ------------------------------------------------------------------------------------------------------------------------
	// ------------------------------------------------------------------------------------------------------------------------

	//ACTIVOS FIJOS
	$("#act_fijos_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var v1 = document.getElementById("id_mobiliarios").value;
			var v2 = document.getElementById("id_maquinaria_equipos").value;
			var v3 = document.getElementById("id_vehiculos").value;
			var v4 = document.getElementById("id_herramientas_84").value;
			var v5 = document.getElementById("id_equipos_sist_paq_84").value;
			var v6 = document.getElementById("id_bienes_artisticos").value;
			var v7 = document.getElementById("id_libros_84").value;
			var v8 = document.getElementById("id_partes_repuestos_84").value;
			var res = suma_valores(v1,v2,v3,v4,v5,v6,v7,v8);
			document.getElementById("id_act_fijos").value = res;
			// Como gastos de capital consiste en el valor de activos fijos, aqui mismo actualizo el valor de gastos de capital
			document.getElementById("id_g_capital").value = document.getElementById("id_act_fijos").value;
		}else{
			console.log('ejec');
			var v1 = document.getElementById("id_mobiliarios_ejec").value;
			var v2 = document.getElementById("id_maquinaria_equipos_ejec").value;
			var v3 = document.getElementById("id_vehiculos_ejec").value;
			var v4 = document.getElementById("id_herramientas_84_ejec").value;
			var v5 = document.getElementById("id_equipos_sist_paq_84_ejec").value;
			var v6 = document.getElementById("id_bienes_artisticos_ejec").value;
			var v7 = document.getElementById("id_libros_84_ejec").value;
			var v8 = document.getElementById("id_partes_repuestos_84_ejec").value;
			var res = suma_valores(v1,v2,v3,v4,v5,v6,v7,v8);
			document.getElementById("id_act_fijos_ejec").value = res;
			// Como gastos de capital consiste en el valor de activos fijos, aqui mismo actualizo el valor de gastos de capital
			document.getElementById("id_g_capital_ejec").value = document.getElementById("id_act_fijos_ejec").value;
		}					
	});

	// ------------------------------------------------------------------------------------------------------------------------
	// ---------------------------------------------------- PENDIENTE ---------------------------------------------------------
	//GASTOS CORRIENTES
	$("#total_g_corrientes_div :input").change(function(e){
		var idc = e.target.id;
		console.log(idc);
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_g_personal") || idc.localeCompare("id_bs_consumo") || idc.localeCompare("id_otros_gastos_corr") || idc.localeCompare("id_transf_corrientes"))){
			var v1 = document.getElementById("id_g_personal").value;
			var v2 = document.getElementById("id_bs_consumo").value;
			var v3 = document.getElementById("id_otros_gastos_corr").value;
			var v4 = document.getElementById("id_transf_corrientes").value;
			var res = suma_valores(v1,v2,v3,v4);
			document.getElementById("id_total_g_corrientes").value = res;
		}
		else{
			var v1 = document.getElementById("id_g_personal_ejec").value;
			var v2 = document.getElementById("id_bs_consumo_ejec").value;
			var v3 = document.getElementById("id_otros_gastos_corr_ejec").value;
			var v4 = document.getElementById("id_transf_corrientes_ejec").value;
			var res = suma_valores(v1,v2,v3,v4);
			document.getElementById("id_total_g_corrientes_ejec").value = res;
			/*if(idc.localeCompare("id_g_personal_ejec") || idc.localeCompare("id_bs_consumo_ejec") || idc.localeCompare("id_otros_gastos_corr_ejec") || idc.localeCompare("id_transf_corrientes_ejec")){
				
			}*/
		}					
	});	
	// ------------------------------------------------------------------------------------------------------------------------
	// ------------------------------------------------------------------------------------------------------------------------

	// ------------------------------------------------------------------------------------------------------------------------
	// ---------------------------------------------------- PENDIENTE ---------------------------------------------------------
	//TOTAL GASTOS AÑO
	$("#total_gastos_total_div :input").change(function(e){
		var idc = e.target.id;
		console.log(idc);
		var cn = e.target.className;
		if(cn.includes('plan') && (idc.localeCompare("id_g_capital") || idc.localeCompare("id_total_g_corrientes"))){
			var v1 = document.getElementById("id_g_capital").value;
			var v2 = document.getElementById("id_total_g_corrientes").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_total_gastos").value = res;
		}
		else{
			var v1 = document.getElementById("id_g_capital_ejec").value;
			var v2 = document.getElementById("id_total_g_corrientes_ejec").value;
			var res = suma_valores(v1,v2);
			document.getElementById("id_total_gastos_ejec").value = res;
		}					
	});	
	/*document.getElementById("id_g_capital").onchange = function(){
		var v1 = document.getElementById("id_g_capital").value;
		var v2 = document.getElementById("id_total_g_corrientes").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_total_gastos").value = res;
	};
	document.getElementById("id_total_g_corrientes").onchange = function(){
		var v1 = document.getElementById("id_g_capital").value;
		var v2 = document.getElementById("id_total_g_corrientes").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_total_gastos").value = res;
	};
	document.getElementById("id_g_capital_ejec").onchange = function(){
		var v1 = document.getElementById("id_g_capital_ejec").value;
		var v2 = document.getElementById("id_total_g_corrientes_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_total_gastos_ejec").value = res;
	};
	document.getElementById("id_total_g_corrientes_ejec").onchange = function(){
		var v1 = document.getElementById("id_g_capital_ejec").value;
		var v2 = document.getElementById("id_total_g_corrientes_ejec").value;
		var res = suma_valores(v1,v2);
		document.getElementById("id_total_gastos_ejec").value = res;
	};*/
	// ------------------------------------------------------------------------------------------------------------------------
	// ------------------------------------------------------------------------------------------------------------------------
});

