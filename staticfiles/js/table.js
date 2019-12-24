$(document).ready(function () {
    $('#dtBasicExample').DataTable({
        "searching": false,
        "ordering": false,
        "language": {
            "lengthMenu": "Mostrar _MENU_ por página",
            //"zeroRecords": "Nothing found - sorry",
            "info": "Mostrando página _PAGE_ de _PAGES_",
            //"infoEmpty": "No records available",
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