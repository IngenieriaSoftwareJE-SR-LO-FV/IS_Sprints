$(document).ready(function () {
    $('#dtBasicExample').DataTable({
        "searching": false,
        "ordering": false,
        "language": {
            "lengthMenu": "Mostrar _MENU_ por página",
            "zeroRecords": "Sin datos",
            "info": "Mostrando página _PAGE_ de _PAGES_",
            "infoEmpty": "",
            "search": "Buscar:",
            "paginate": {
                "first": "Primero",
                "last": "Último",
                "next": "Siguiente",
                "previous": "Anterior"
            },
        }
    });

    $('.dataTables_length').addClass('bs-select');
});