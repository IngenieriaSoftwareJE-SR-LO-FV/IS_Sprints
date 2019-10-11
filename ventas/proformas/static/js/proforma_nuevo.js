
window.onload = function() {
    var e = document.getElementById("seleccion");
	var text = e.options[e.selectedIndex].text;	
	console.log(text)
	document.getElementById("id_codigo").readOnly=true;

	if (text!="Aceptada"){
		document.getElementById("id_fechaRespuesta").disabled=true;
		document.getElementById("id_montoAceptado").disabled=true;
		document.getElementById("id_montoEjecutado").disabled=true;
		document.getElementById("id_montoPorEjecutarse").disabled=true;
	}
	else{
		document.getElementById("id_fechaRespuesta").disabled=false;
		document.getElementById("id_montoAceptado").disabled=false;
		document.getElementById("id_montoEjecutado").disabled=false;
		document.getElementById("id_montoPorEjecutarse").disabled=false;

	}
};

function run(){
	var e = document.getElementById("seleccion");
	var text = e.options[e.selectedIndex].text;	
	console.log(text)
	document.getElementById("id_codigo").readOnly=true;

	if (text!="Aceptada"){
		document.getElementById("id_fechaRespuesta").disabled=true;
		document.getElementById("id_montoAceptado").disabled=true;
		document.getElementById("id_montoEjecutado").disabled=true;
		document.getElementById("id_montoPorEjecutarse").disabled=true;
	}
	else{
		document.getElementById("id_fechaRespuesta").disabled=false;
		document.getElementById("id_montoAceptado").disabled=false;
		document.getElementById("id_montoEjecutado").disabled=false;
		document.getElementById("id_montoPorEjecutarse").disabled=false;
	}
}	
