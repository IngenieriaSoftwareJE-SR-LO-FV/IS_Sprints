$(document).ready(function(){
	//INGRESOS CORRIENTES
	document.getElementById("id_ing_corrientes").onclick = function(){
		var v1 = document.getElementById("id_vb_serv_tecnicos_espec").value;
		var v2 = document.getElementById("id_vb_curs_sem_maes").value;
		var v3 = document.getElementById("id_td_prov_gobcen").value;
		var v4 = document.getElementById("id_td_prov_entdesc").value;
		var v5 = document.getElementById("id_td_prov_entpub").value;
		var v6 = document.getElementById("id_td_prov_gobaut").value;
		var v7 = document.getElementById("id_otros_ingCorr").value;
		document.getElementById("id_ing_corrientes").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7);
	};
	document.getElementById("id_ing_corrientes_ejec").onclick = function(){
		var v1 = document.getElementById("id_vb_serv_tecnicos_espec_ejec").value;
		var v2 = document.getElementById("id_vb_curs_sem_maes_ejec").value;
		var v3 = document.getElementById("id_td_prov_gobcen_ejec").value;
		var v4 = document.getElementById("id_td_prov_entdesc_ejec").value;
		var v5 = document.getElementById("id_td_prov_entpub_ejec").value;
		var v6 = document.getElementById("id_td_prov_gobaut_ejec").value;
		var v7 = document.getElementById("id_otros_ingCorr_ejec").value;
		document.getElementById("id_ing_corrientes_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7);
	};

	//INGRESOS DE FINANCIAMIENTO
	document.getElementById("id_ing_financiamiento").onclick = function(){
		var v1 = document.getElementById("id_fondo_autogest").value;
		var v2 = document.getElementById("id_cta_x_cobrar").value;
		document.getElementById("id_ing_financiamiento").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_ing_financiamiento_ejec").onclick = function(){
		var v1 = document.getElementById("id_fondo_autogest_ejec").value;
		var v2 = document.getElementById("id_cta_x_cobrar_ejec").value;
		document.getElementById("id_ing_financiamiento_ejec").value = parseFloat(v1)+parseFloat(v2);
	};

	//INGRESOS DE CAPITAL
	document.getElementById("id_ing_capital").onclick = function(){
		var v1 = document.getElementById("id_td_cap_prov_gobcen").value;
		var v2 = document.getElementById("id_td_cap_prov_entdesc").value;
		var v3 = document.getElementById("id_td_cap_prov_entpub").value;
		var v4 = document.getElementById("id_td_cap_prov_gobaut").value;
		var v5 = document.getElementById("id_don_cap_ext").value;
		document.getElementById("id_ing_capital").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5);
	};
	document.getElementById("id_ing_capital_ejec").onclick = function(){
		var v1 = document.getElementById("id_td_cap_prov_gobcen_ejec").value;
		var v2 = document.getElementById("id_td_cap_prov_entdesc_ejec").value;
		var v3 = document.getElementById("id_td_cap_prov_entpub_ejec").value;
		var v4 = document.getElementById("id_td_cap_prov_gobaut_ejec").value;
		var v5 = document.getElementById("id_don_cap_ext_ejec").value;
		document.getElementById("id_ing_capital_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5);
	};

	//TOTAL INGRESOS AÑO
	document.getElementById("id_total_ingresos").onclick = function(){
		var v1 = document.getElementById("id_ing_corrientes").value;
		var v2 = document.getElementById("id_ing_financiamiento").value;
		var v3 = document.getElementById("id_ing_capital").value;
		document.getElementById("id_total_ingresos").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_total_ingresos_ejec").onclick = function(){
		var v1 = document.getElementById("id_ing_corrientes_ejec").value;
		var v2 = document.getElementById("id_ing_financiamiento_ejec").value;
		var v3 = document.getElementById("id_ing_capital_ejec").value;
		document.getElementById("id_total_ingresos_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//GASTOS CORRIENTES
	document.getElementById("id_total_g_corrientes").onclick = function(){
		var v1 = document.getElementById("id_g_personal").value;
		var v2 = document.getElementById("id_bs_consumo").value;
		var v3 = document.getElementById("id_otros_gastos_corr").value;
		var v4 = document.getElementById("id_transf_corrientes").value;
		document.getElementById("id_total_g_corrientes").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4);
	};
	document.getElementById("id_total_g_corrientes_ejec").onclick = function(){
		var v1 = document.getElementById("id_g_personal_ejec").value;
		var v2 = document.getElementById("id_bs_consumo_ejec").value;
		var v3 = document.getElementById("id_otros_gastos_corr_ejec").value;
		var v4 = document.getElementById("id_transf_corrientes_ejec").value;
		document.getElementById("id_total_g_corrientes_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4);
	};

	//GASTOS EN PERSONAL
	document.getElementById("id_g_personal").onclick = function(){
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
		document.getElementById("id_g_personal").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7)+parseFloat(v8)+parseFloat(v9)+parseFloat(v10)+parseFloat(v11)+parseFloat(v12)+parseFloat(v13)+parseFloat(v14)+parseFloat(v15);
	};
	document.getElementById("id_g_personal_ejec").onclick = function(){
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
		document.getElementById("id_g_personal_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7)+parseFloat(v8)+parseFloat(v9)+parseFloat(v10)+parseFloat(v11)+parseFloat(v12)+parseFloat(v13)+parseFloat(v14)+parseFloat(v15);
	};

	//BIENES Y SERVICIOS DE CONSUMO
	document.getElementById("id_bs_consumo").onclick = function(){
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
		document.getElementById("id_bs_consumo").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7)+parseFloat(v8)+parseFloat(v9)+parseFloat(v10)+parseFloat(v11)+parseFloat(v12)+parseFloat(v13)+parseFloat(v14)+parseFloat(v15)+parseFloat(v16)+parseFloat(v17)+parseFloat(v18)+parseFloat(v19)+parseFloat(v20)+parseFloat(v21)+parseFloat(v22)+parseFloat(v23)+parseFloat(v24)+parseFloat(v25)+parseFloat(v26)+parseFloat(v27)+parseFloat(v28)+parseFloat(v29)+parseFloat(v30)+parseFloat(v31)+parseFloat(v32)+parseFloat(v33)+parseFloat(v34)+parseFloat(v35)+parseFloat(v36)+parseFloat(v35)+parseFloat(v38)+parseFloat(v39)+parseFloat(v40)+parseFloat(v41)+parseFloat(v42)+parseFloat(v43)+parseFloat(v44)+parseFloat(v45)+parseFloat(v46)+parseFloat(v47)+parseFloat(v48);
	};
	document.getElementById("id_bs_consumo_ejec").onclick = function(){
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
		document.getElementById("id_bs_consumo_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7)+parseFloat(v8)+parseFloat(v9)+parseFloat(v10)+parseFloat(v11)+parseFloat(v12)+parseFloat(v13)+parseFloat(v14)+parseFloat(v15)+parseFloat(v16)+parseFloat(v17)+parseFloat(v18)+parseFloat(v19)+parseFloat(v20)+parseFloat(v21)+parseFloat(v22)+parseFloat(v23)+parseFloat(v24)+parseFloat(v25)+parseFloat(v26)+parseFloat(v27)+parseFloat(v28)+parseFloat(v29)+parseFloat(v30)+parseFloat(v31)+parseFloat(v32)+parseFloat(v33)+parseFloat(v34)+parseFloat(v35)+parseFloat(v36)+parseFloat(v35)+parseFloat(v38)+parseFloat(v39)+parseFloat(v40)+parseFloat(v41)+parseFloat(v42)+parseFloat(v43)+parseFloat(v44)+parseFloat(v45)+parseFloat(v46)+parseFloat(v47)+parseFloat(v48);
	};

	//OTROS GASTOS CORRIENTES
	document.getElementById("id_otros_gastos_corr").onclick = function(){
		var v1 = document.getElementById("id_iva").value;
		var v2 = document.getElementById("id_tasas").value;
		var v3 = document.getElementById("id_otros_imp").value;
		var v4 = document.getElementById("id_seguros").value;
		var v5 = document.getElementById("id_comisiones_banc").value;
		var v6 = document.getElementById("id_devoluciones").value;
		var v7 = document.getElementById("id_otros_gastos_fin").value;
		document.getElementById("id_otros_gastos_corr").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7);
	};
	document.getElementById("id_otros_gastos_corr_ejec").onclick = function(){
		var v1 = document.getElementById("id_iva_ejec").value;
		var v2 = document.getElementById("id_tasas_ejec").value;
		var v3 = document.getElementById("id_otros_imp_ejec").value;
		var v4 = document.getElementById("id_seguros_ejec").value;
		var v5 = document.getElementById("id_comisiones_banc_ejec").value;
		var v6 = document.getElementById("id_devoluciones_ejec").value;
		var v7 = document.getElementById("id_otros_gastos_fin_ejec").value;
		document.getElementById("id_otros_gastos_corr_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7);
	};

	//TRANSF. CORRIENTES: APORTACIONES DE ACUERDO A LINEAMIENTOS
	document.getElementById("id_transf_corrientes").onclick = function(){
		var v1 = document.getElementById("id_espoltech_ep").value;
		var v2 = document.getElementById("id_part_espol").value;
		var v3 = document.getElementById("id_part_unidad").value;
		document.getElementById("id_transf_corrientes").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};
	document.getElementById("id_transf_corrientes_ejec").onclick = function(){
		var v1 = document.getElementById("id_espoltech_ep_ejec").value;
		var v2 = document.getElementById("id_part_espol_ejec").value;
		var v3 = document.getElementById("id_part_unidad_ejec").value;
		document.getElementById("id_transf_corrientes_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3);
	};

	//GASTOS DE CAPITAL
	document.getElementById("id_g_capital").onclick = function(){
		var v1 = document.getElementById("id_act_fijos").value;
		document.getElementById("id_g_capital").value = parseFloat(v1);
	};
	document.getElementById("id_g_capital_ejec").onclick = function(){
		var v1 = document.getElementById("id_act_fijos_ejec").value;
		document.getElementById("id_g_capital_ejec").value = parseFloat(v1);
	};

	//ACTIVOS FIJOS
	document.getElementById("id_act_fijos").onclick = function(){
		var v1 = document.getElementById("id_mobiliarios").value;
		var v2 = document.getElementById("id_maquinaria_equipos").value;
		var v3 = document.getElementById("id_vehiculos").value;
		var v4 = document.getElementById("id_herramientas_84").value;
		var v5 = document.getElementById("id_equipos_sist_paq_84").value;
		var v6 = document.getElementById("id_bienes_artisticos").value;
		var v7 = document.getElementById("id_libros_84").value;
		var v8 = document.getElementById("id_partes_repuestos_84").value;
		document.getElementById("id_act_fijos").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7);
	};
	document.getElementById("id_act_fijos_ejec").onclick = function(){
		var v1 = document.getElementById("id_mobiliarios_ejec").value;
		var v2 = document.getElementById("id_maquinaria_equipos_ejec").value;
		var v3 = document.getElementById("id_vehiculos_ejec").value;
		var v4 = document.getElementById("id_herramientas_84_ejec").value;
		var v5 = document.getElementById("id_equipos_sist_paq_84_ejec").value;
		var v6 = document.getElementById("id_bienes_artisticos_ejec").value;
		var v7 = document.getElementById("id_libros_84_ejec").value;
		var v8 = document.getElementById("id_partes_repuestos_84_ejec").value;
		document.getElementById("id_act_fijos_ejec").value = parseFloat(v1)+parseFloat(v2)+parseFloat(v3)+parseFloat(v4)+parseFloat(v5)+parseFloat(v6)+parseFloat(v7);
	};

	//TOTAL GASTOS AÑO
	document.getElementById("id_total_gastos").onclick = function(){
		var v1 = document.getElementById("id_g_capital").value;
		var v2 = document.getElementById("id_total_g_corrientes").value;
		document.getElementById("id_total_gastos").value = parseFloat(v1)+parseFloat(v2);
	};
	document.getElementById("id_total_gastos_ejec").onclick = function(){
		var v1 = document.getElementById("id_g_capital_ejec").value;
		var v2 = document.getElementById("id_total_g_corrientes_ejec").value;
		document.getElementById("id_total_gastos_ejec").value = parseFloat(v1)+parseFloat(v2);
	};
});

