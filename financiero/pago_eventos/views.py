from django.shortcuts import render
from financiero.orden_facturacion.models import OrdenFacturacion
from .filters import *
from django.core.paginator import Paginator
# Create your views here.

"""def index_pagos(request):
	pagos_list = OrdenFacturacion.objects.all().order_by("id")

	filter = PagoEventosFilter(request.GET, queryset=pagos_list )
	paginator = Paginator(filter.qs, 30) 

	page = request.GET.get('page')
	juridicas = paginator.get_page(page)
	return render(request, 'pago_eventos/pago_eventos.html', {'juridicas': juridicas, "filter":filter})
"""