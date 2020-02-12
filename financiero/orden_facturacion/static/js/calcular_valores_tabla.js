function roundToTwo(num) {
    return +(Math.round(num + "e+2") + "e-2");
}

/**
 * Funcion para sumar columnas de tablas basados en los td de clase sum
 * table_id El identificador de la tabla (id o clase)
 * return Un arreglo de igual tamaño que la cantidad de columnas con los valores sumados en la posicion correspondiente
 */
function sumtr(table_id) {
    var s = [];
    var r = 0;
    $(table_id + " tbody tr").each(function (index) {
        var col = 0;
        $(this).children("td").each(function () {
            if ($(this).is(".sum")) {
                if (s.length < col + 1) s[col] = 0;
                var val = parseFloat($(this).html().replace(',', '.').replace('$', '').replace('%', ''));

                s[col] = s[col] + val;
            } else {
                s[col] = "noCount"; // a flag which tells us we're not counting that column
            }
            col++;
        });
        r++;
    });
    $("#id_n_participantes").val(r);
    return s;
}

$('.select2').trigger('change.select2')

$('#env-sol').click(function (e) {
    e.preventDefault();
    $("#id_estado").val("SLCE");
    $("#form-fact").trigger("submit");
});

if ($('#participantes-table tbody tr').length > 0) {
    $('#env-sol').attr('disabled',false);

    s = sumtr("#participantes-table");
    
    $("#id_subtotal").val(s[3]);
    $("#id_valor_total").val(s[5]);
    $("#id_descuento_total").val((s[3] - s[5]).toFixed(2));
    $("#id_descuento_fact").val(roundToTwo(((s[3] - s[5]) / s[3]) * 100));

    $("#subtotal").val("$ "+s[3].toFixed(2));
    $("#valor_total").val('$ '+s[5].toFixed(2));
    $("#descuento_total").val('$ '+(s[3] - s[5]).toFixed(2));
    $("#descuento_fact").val(roundToTwo(((s[3] - s[5]) / s[3]) * 100)+' %');
}
else {
    $('#env-sol').attr('disabled',true);
    $("#id_subtotal").val(0);
    $("#id_valor_total").val(0);
    $("#id_descuento_total").val(0);
    $("#id_descuento_fact").val(0);
}

