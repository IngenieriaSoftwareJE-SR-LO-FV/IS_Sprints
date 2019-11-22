from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrdenPagoForm
from .models import OrdenPago, Centro_Costos, Egresos
from ventas.personas_naturales.models import Persona_Natural
from ventas.personas_juridicas.models import Juridica
from .filters import OrdenPagoFilter
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from datetime import date
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

def index(request):
	ordPago_lista = OrdenPago.objects.all()
	ordPago_filter = OrdenPagoFilter(request.GET, queryset=ordPago_lista)
	return render(request, "orden_pago/ordenpago_list.html", {"ordenes_pago":ordPago_lista, "filter":ordPago_filter})


def load_egresos(request):
	centroc_id = request.GET.get("centroc")
	egresos = Egresos.objects.filter(centroc_id=centroc_id).order_by("nombre")
	return render(request, "orden_pago/dropdown_egresos.html", {"egresos":egresos})


def load_proveedor(request):
	tipo = request.GET.get("tipo")
	proveedor = []
	if(tipo == "Natural"):
		naturales = Persona_Natural.objects.all()
		proveedor = render_to_string("orden_pago/dropdown_naturales.html", {"proveedor":naturales})
	elif(tipo == "Jurídica"):
		juridicas = Juridica.objects.all()
		proveedor = render_to_string("orden_pago/dropdown_juridica.html", {"proveedor":juridicas})
	return JsonResponse({"pro":proveedor})


def orden_pago_nuevo(request):
	if(request.method == "POST"):
		form = OrdenPagoForm(request.POST)
		if(form.is_valid()):
			try:
				pre = str(int(OrdenPago.objects.latest('pk').pk+1))
				sec = '0'*(4-len(pre))+pre
			except OrdenPago.DoesNotExist:
				sec = '0001'
			form.instance.cod_ord_pago = sec+'-'+str(date.today().year)
			form.save()
			return redirect("orden_pago_lista")
	else:
		form = OrdenPagoForm()
	return render(request, "orden_pago/ordenpago_nuevo.html", {"form":form})
