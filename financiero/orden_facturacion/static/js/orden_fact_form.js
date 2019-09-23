$('.select2').select2();

function load_data(url, persona) {
  var url = $('#form-fact').attr("data-persona-url");
  var persona = $("#id_tipo_cliente").val();
  if (persona != "") {
    var url = url
    $.ajax({
      url: url,
      data: {
        'persona': persona
      },
      success: function (data) {
        $("#id_ruc_ci").html(data.ruc_ci)
        $("#id_razon_nombres").html(data.razon_nombre)
      }
    });
    $('#field-razon').show();
    $('#field-ruc-ci').show();

    if (persona == "p_natural") {
      $('#ruc_ci').text('CI');
      $('#ra_nom').text('Nombre');
    }
    else if (persona == "p_juridica") {
      $('#ruc_ci').text('RUC');
      $('#ra_nom').text('Razón Social');
    }
  }
  else{
    $('#field-razon').hide();
    $('#field-ruc-ci').hide();
  }
};

function autocomplete(from, to){
  if(from.val()!=""){
    $('#'+to).val($('#'+to+" option[name='"+from.val()+"']").val());
    $('#select2-'+to+'-container').text($('#'+to).val());
  }
  else{
    $('#'+to).val("");
    $('#select2-'+to+'-container').text("---------");
  }
}



load_data();

$("#id_tipo_cliente").on("change", load_data);

$('#id_razon_nombres').on('change',function(){
  autocomplete($(this), 'id_ruc_ci');
})

$('#id_ruc_ci').on('change',function(){
  autocomplete($(this), 'id_razon_nombres');
})

