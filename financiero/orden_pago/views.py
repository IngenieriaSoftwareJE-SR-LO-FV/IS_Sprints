from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrdenPagoForm, OrdenPagoEditarFinalForm, OrdenPagoEditarThirdForm, OrdenPagoEditarFirstForm, OrdenPagoEditarSecondForm
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
	if (request.GET.get('estado',None)!=None and 'ANLD' in request.GET['estado']):
		ordPago_lista = OrdenPago.objects.all()
	else:
		ordPago_lista = OrdenPago.objects.all().exclude(estado='ANLD')
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
		naturales = Persona_Natural.objects.all().order_by("apellidos")
		proveedor = render_to_string("orden_pago/dropdown_naturales.html", {"proveedor":naturales})
	elif(tipo == "Jurídica"):
		juridicas = Juridica.objects.all().order_by("nombre")
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


def orden_pago_editar(request, pk):
	if(request.method == 'POST'):
		p = get_object_or_404(OrdenPago, pk=pk)
		form = OrdenPagoForm(request.POST, instance=p)
		if(form.is_valid()):
			form.save()
			return redirect('orden_pago_lista')
	else:
		p = get_object_or_404(OrdenPago, pk=pk)
		form = OrdenPagoForm(instance=p)
	return render(request, 'orden_pago/ordenpago_editar_1.html', {'form': form})


def orden_pago_editarAUTR_analista(request, pk):
	if(request.method == 'POST'):
		p = get_object_or_404(OrdenPago, pk=pk)
		form = OrdenPagoEditarSecondForm(request.POST, instance=p)
		if(form.is_valid()):
			form.save()
			return redirect('orden_pago_lista')
	else:
		p = get_object_or_404(OrdenPago, pk=pk)
		form = OrdenPagoEditarSecondForm(instance=p)
	return render(request, 'orden_pago/ordenpago_editar_1.html', {'form': form})


def orden_pago_editarAUTR(request, pk):
	if(request.method == 'POST'):
		p = get_object_or_404(OrdenPago, pk=pk)
		form = OrdenPagoEditarSecondForm(request.POST, instance=p)
		if(form.is_valid()):
			form.save()
			return redirect('pendiente_aprobacion')
	else:
		p = get_object_or_404(OrdenPago, pk=pk)
		form = OrdenPagoEditarSecondForm(instance=p)
	return render(request, 'orden_pago/ordenpago_autorizar.html', {'form': form, "p":p})

def orden_pago_editarPOST_AUTR(request, pk):
	if(request.method == 'POST'):
		p = get_object_or_404(OrdenPago, pk=pk)
		form = OrdenPagoEditarThirdForm(request.POST, request.FILES, instance=p)
		if(form.is_valid()):
			form.save()
			p = get_object_or_404(OrdenPago, pk=pk)
			p.estado = 'PGDO'
			p.save()
			return redirect('orden_pago_lista')
	else:
		p = get_object_or_404(OrdenPago, pk=pk)
		form = OrdenPagoEditarThirdForm(instance=p)
	return render(request, 'orden_pago/ordenpago_editar_2.html', {'form': form})

def orden_pago_editarPGDO(request, pk):
	if(request.method == 'POST'):
		p = get_object_or_404(OrdenPago, pk=pk)
		form = OrdenPagoEditarFinalForm(request.POST, instance=p)
		if(form.is_valid()):
			form.save()
			return redirect('orden_pago_lista')
	else:
		p = get_object_or_404(OrdenPago, pk=pk)
		form = OrdenPagoEditarFinalForm(instance=p)
	return render(request, 'orden_pago/ordenpago_editar_2.html', {'form': form, "p":p})


def orden_pago_enviar(request, pk):
	p = get_object_or_404(OrdenPago, cod_ord_pago=pk)
	p.estado = 'ENVD'
	p.save()
	return redirect('orden_pago_lista')


def orden_pago_autorizar(request, pk):
	p = get_object_or_404(OrdenPago, cod_ord_pago=pk)
	p.estado = 'AUTR'
	p.save()
	return redirect('pendiente_aprobacion')


def orden_pago_anular(request, pk=None):
	if(request.method == "POST"):
		p = get_object_or_404(OrdenPago, pk=pk)
		form = OrdenPagoForm(request.POST,instance=p)
		if(form.is_valid()):
			form.instance.estado = 'ANLD'
			form.save()
		return redirect('orden_pago_lista')
	else:
		pk = request.GET.get('pk')
		p = get_object_or_404(OrdenPago, pk=pk)
		form = OrdenPagoForm(instance=p)
		return render(request, 'orden_pago/ordenpago_anular.html', {'object':p, 'form':form})


