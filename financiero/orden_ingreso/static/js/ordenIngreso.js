
window.onload = function() {
    var e = document.getElementById("seleccion");
	var text = e.options[e.selectedIndex].text;	
	console.log(text);

	if (text!="Tarjeta de Crédito"){
		document.getElementById("id_emisoraTarjeta").required=false;
	}
	else{
		document.getElementById("id_emisoraTarjeta").required=true;

	}
};

function run(){
	var e = document.getElementById("seleccion");
	var text = e.options[e.selectedIndex].text;	
	console.log(text);

	if (text!="Tarjeta de Crédito"){
		document.getElementById("id_emisoraTarjeta").required=false;
		console.log("owo");
	}
	else{
		document.getElementById("id_emisoraTarjeta").required=true;
		console.log("uwu");
	}
}	
