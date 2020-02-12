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
			var ac = document.getElementById("id_ing_corrientes").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_ing_corrientes").value = parseFloat(ac) + parseFloat((e.target).value);
		}else{
			console.log('ejec');
			var ac = document.getElementById("id_ing_corrientes_ejec").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_ing_corrientes_ejec").value = parseFloat(ac) + parseFloat((e.target).value);
		}					
	});

	//INGRESOS DE FINANCIAMIENO
	$("#ing_financiamiento_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var ac = document.getElementById("id_ing_financiamiento").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_ing_financiamiento").value = parseFloat(ac) + parseFloat((e.target).value);
		}else{
			console.log('ejec');
			var ac = document.getElementById("id_ing_financiamiento_ejec").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_ing_financiamiento_ejec").value = parseFloat(ac) + parseFloat((e.target).value);
		}					
	});

	//INGRESOS DE CAPITAL
	$("#ing_capital_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var ac = document.getElementById("id_ing_capital").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_ing_capital").value = parseFloat(ac) + parseFloat((e.target).value);
		}else{
			console.log('ejec');
			var ac = document.getElementById("id_ing_capital_ejec").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_ing_capital_ejec").value = parseFloat(ac) + parseFloat((e.target).value);
		}					
	});

	// ------------------------------------------------------------------------------------------------------------------------
	// ---------------------------------------------------- PENDIENTE ---------------------------------------------------------
	//TOTAL INGRESOS AÑO
	$("#total_ingresos_div :input").change(function(e){
		var idc = e.target.id;
		if(idc.localeCompare("id_ing_corrientes") || idc.localeCompare("id_ing_financiamiento") || idc.localeCompare("id_ing_capital")){
			var ac = document.getElementById("id_total_ingresos").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_total_ingresos").value = parseFloat(ac) + parseFloat((e.target).value);
		}
		else{
			if(idc.localeCompare("id_ing_corrientes_ejec") || idc.localeCompare("id_ing_financiamiento_ejec") || idc.localeCompare("id_ing_capital_ejec")){
				var ac = document.getElementById("id_total_ingresos_ejec").value;
				if(ac==""){
					ac = 0.0;
				}
				document.getElementById("id_total_ingresos_ejec").value = parseFloat(ac) + parseFloat((e.target).value);
			}		
		}					
	});	
	// ------------------------------------------------------------------------------------------------------------------------
	// ------------------------------------------------------------------------------------------------------------------------

	// ------------------------------------------------------------------------------------------------------------------------
	// ---------------------------------------------------- PENDIENTE ---------------------------------------------------------
	//GASTOS CORRIENTES
	$("#total_g_corrientes_div :input").change(function(e){
		var idc = e.target.id;
		if(idc.localeCompare("id_g_personal") || idc.localeCompare("id_bs_consumo") || idc.localeCompare("id_otros_gastos_corr") || idc.localeCompare("id_transf_corrientes")){
			var ac = document.getElementById("id_total_g_corrientes").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_total_g_corrientes").value = parseFloat(ac) + parseFloat((e.target).value);
		}
		else{
			if(idc.localeCompare("id_g_personal_ejec") || idc.localeCompare("id_bs_consumo_ejec") || idc.localeCompare("id_otros_gastos_corr_ejec") || idc.localeCompare("id_transf_corrientes_ejec")){
				var ac = document.getElementById("id_total_g_corrientes_ejec").value;
				if(ac==""){
					ac = 0.0;
				}
			}
			document.getElementById("id_total_g_corrientes_ejec").value = parseFloat(ac) + parseFloat((e.target).value);
		}					
	});	
	// ------------------------------------------------------------------------------------------------------------------------
	// ------------------------------------------------------------------------------------------------------------------------

	//GASTOS EN PERSONAL
	$("#g_personal_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var ac = document.getElementById("id_g_personal").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_g_personal").value = parseFloat(ac) + parseFloat((e.target).value);
		}else{
			console.log('ejec');
			var ac = document.getElementById("id_g_personal_ejec").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_g_personal_ejec").value = parseFloat(ac) + parseFloat((e.target).value);
		}					
	});

	//BIENES Y SERVICIOS DE CONSUMO
	$("#bs_consumo_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var ac = document.getElementById("id_bs_consumo").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_bs_consumo").value = parseFloat(ac) + parseFloat((e.target).value);
		}else{
			console.log('ejec');
			var ac = document.getElementById("id_bs_consumo_ejec").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_bs_consumo_ejec").value = parseFloat(ac) + parseFloat((e.target).value);
		}					
	});

	//OTROS GASTOS CORRIENTES
	$("#otros_gastos_corr_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var ac = document.getElementById("id_otros_gastos_corr").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_otros_gastos_corr").value = parseFloat(ac) + parseFloat((e.target).value);
		}else{
			console.log('ejec');
			var ac = document.getElementById("id_otros_gastos_corr_ejec").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_otros_gastos_corr_ejec").value = parseFloat(ac) + parseFloat((e.target).value);
		}					
	});

	//TRANSF. CORRIENTES: APORTACIONES DE ACUERDO A LINEAMIENTOS
	$("#transf_corrientes_div :input").change(function(e){
		var cn = e.target.className;
		if(cn.includes('plan')){
			console.log("plan");
			var ac = document.getElementById("id_transf_corrientes").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_transf_corrientes").value = parseFloat(ac) + parseFloat((e.target).value);
		}else{
			console.log('ejec');
			var ac = document.getElementById("id_transf_corrientes_ejec").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_transf_corrientes_ejec").value = parseFloat(ac) + parseFloat((e.target).value);
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
			var ac = document.getElementById("id_act_fijos").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_act_fijos").value = parseFloat(ac) + parseFloat((e.target).value);
			// Como gastos de capital consiste en el valor de activos fijos, aqui mismo actualizo el valor de gastos de capital
			document.getElementById("id_g_capital").value = document.getElementById("id_act_fijos").value;
		}else{
			console.log('ejec');
			var ac = document.getElementById("id_act_fijos_ejec").value;
			if(ac==""){
				ac = 0.0;
			}
			document.getElementById("id_act_fijos_ejec").value = parseFloat(ac) + parseFloat((e.target).value);
			// Como gastos de capital consiste en el valor de activos fijos, aqui mismo actualizo el valor de gastos de capital
			document.getElementById("id_g_capital_ejec").value = document.getElementById("id_act_fijos_ejec").value;
		}					
	});

	// ------------------------------------------------------------------------------------------------------------------------
	// ---------------------------------------------------- PENDIENTE ---------------------------------------------------------
	//TOTAL GASTOS AÑO
	document.getElementById("id_g_capital").onchange = function(){
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
	};
	// ------------------------------------------------------------------------------------------------------------------------
	// ------------------------------------------------------------------------------------------------------------------------
});

