$(document).ready(function(){
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

	//COSTOS DEL SERVICIO - DEDUCIBLES

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
	
});