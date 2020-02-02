
$('.select2').select2({
  language: "es",
  minimunInputLength: 2,
  minimunResultsForSearch: -1
});

function load_data(url) {
  var url = $('#form-fact').attr("data-persona-url");
  var persona = $("#id_tipo_cliente").val();

    var url = url
    $.ajax({
      url: url,
      success: function (data) {
        $("#id_participante").html(data.personas)
        $('#id_participante').val($('#rc').val());
        $('#select2-id_participante-container').text($('#rc').val());
      }
    });
    $('#field-participante').show();
    
    
};




load_data();

$('#id_participante').on('change', function () {
  clean_eventos()
})
function clean_eventos(){
  var url = $('#form-fact').attr("data-evento-url");

    var url = url
    $.ajax({
      url: url,
      data: {
        pk :$("#id_participante").val()
      } ,
      success: function (data) {
        $("#id_evento_origen").html(data.eventos)
        $('#id_evento_origen').val($('#rc').val());
        $('#select2-id_evento_origen-container').text($('#rc').val());
      }
    });
  var url = $('#form-fact').attr("data-evento-url");

    var url = url
    $.ajax({
      url: url,
      data: {
        pk :$("#id_participante").val(),
        exclude:"true"
      } ,
      success: function (data) {
        $("#id_evento_destino").html(data.eventos)
        $('#id_evento_destino').val($('#rc').val());
        $('#select2-id_evento_destino-container').text($('#rc').val());
      }
    });
  
}
$(document).on('change','.select2-participantes',function(){
  var clickedselect=$(this).val();
  var id=$(this).attr('id');
  $('.select2-participantes').each(function(e){
    if($(this).attr('id')!=id){
      if($(this).val()==clickedselect){
        $(this).val("None").trigger('change');
        clean_eventos();
      }
    }
  });
});


