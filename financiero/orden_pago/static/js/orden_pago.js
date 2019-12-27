$('.select2').select2({
  language: "es",
  minimunInputLength: 2,
  minimunResultsForSearch: -1,
});

function load_data() {
  var url = $('#ordenPagoForm').attr("data-proveedor-url");
  var tipo = $("#id_tipo_proveedor").val();
  if (tipo != "") {
    $.ajax({
      url: url,
      data: {
        'tipo': tipo
      },
      success: function (data) {
        $("#id_proveedor").html(data.pro)
        $('#id_proveedor').val($('#rn').val());
        $('#select2-id_proveedor-container').text($('#rn').val());
      }
    });
    $('#field-proveedor').show();

    if (tipo == "Natural") {
      $('#id_proveedor').text('Nombre');
    }
    else if (tipo == "Jurídica") {
      $('#id_proveedor').text('Razón Social');
    }
  }
  else {
    $('#field-proveedor').hide();
  }
};

function autocomplete(from, to) {
  if (from.val() != "") {
    $('#' + to).val($('#' + to + " option[name='" + from.val() + "']").val());
    $('#select2-' + to + '-container').text($('#' + to).val());
  }
  else {
    $('#' + to).val("");
    $('#select2-' + to + '-container').text("---------");
  }
}




load_data();

$("#id_tipo_proveedor").on("change", load_data);

$('#id_razon_nombres').on('change', function () {
  autocomplete($(this), 'id_proveedor');
})


function close_form(e){
    var modal = document.getElementById("myModal");
      modal.style.display = "block";
    modal.style.display = "none";
  }