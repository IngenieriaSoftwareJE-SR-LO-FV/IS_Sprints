
from django.shortcuts import render, redirect
from . import forms
from .models import *
from django.http import JsonResponse, HttpResponseRedirect
from ventas.personas_naturales.models import Persona_Natural
from financiero.orden_facturacion.models import OrdenFacturacionParticipante
from django.template.loader import render_to_string

from django.shortcuts import render, redirect, get_object_or_404
from .forms import NotaCreditoForm
from .models import NotaCredito


# Create your views here.
def index(request):
	nota_credito = NotaCredito.objects.all()
	return render(request, "procesos_especiales/procesos_especiales_index.html", {"nota_credito":nota_credito})

def cambio_participante_index(request):
	return render(request, "procesos_especiales/procesos_especiales_index.html")

def devolucion_nuevo(request):
	if(request.method == "POST"):
		form = NotaCreditoForm(request.POST)
		if(form.is_valid()):
			form.save()
			return redirect("procesos_especiales_index")
	else:
		form = NotaCreditoForm()
	return render(request, "procesos_especiales/procesos_especiales_nota_credito_nuevo.html", {"form":form})

def devolucion_editar(request, pk):
	if(request.method == 'POST'):
		p = get_object_or_404(NotaCredito, pk=pk)
		form = NotaCreditoForm(request.POST, instance=p)
		if(form.is_valid()):
			form.save()
			return redirect("procesos_especiales_index")
	else:
		p = get_object_or_404(NotaCredito, pk=pk)
		form = NotaCreditoForm(instance=p)
	return render(request, "procesos_especiales/procesos_especiales_nota_credito_editar.html", {'form': form})

def cambio_evento_index(request):
	if(request.method == "POST"):
		form = forms.CambiarEventoForm(request.POST)
		print("psot request")
		print(form)
		if(form.is_valid()):
			print("bye")
			form.save()
			return redirect("procesos_especiales_cambio_evento")
	else:
		form = forms.CambiarEventoForm()
	return render(request, "procesos_especiales/procesos_especiales_cambio_evento.html",{"form":form})


def load_eventos_participante(request):
	pk = request.GET.get("pk")
	exclude_pk = request.GET.get("exclude")
	if(exclude_pk!=None):
		eventos = OrdenFacturacionParticipante.objects.exclude(participante=pk)
	else:
	
		eventos = OrdenFacturacionParticipante.objects.filter(participante=pk)
	eventos_res = render_to_string("dropdown_evento.html",{'eventos': eventos})
	return JsonResponse({'eventos': eventos_res})

def load_personas_evento(request):


	personas=Persona_Natural.objects.all()
	personas=render_to_string("dropdown_natural.html",{"personas":personas})

 
	return JsonResponse({'personas': personas})
def confirmar_cambio(request):
	pk = request.GET.get('cedula')

	p = Persona_Natural.objects.get(pk=pk)

	e_o = OrdenFacturacionParticipante.objects.filter(cod_evento=request.GET.get('evento_origen'))[0]
	e_d = OrdenFacturacionParticipante.objects.filter(cod_evento=request.GET.get('evento_destino'))[0]
	print({'object': p,"eo":e_o,"ed":e_d});
	return render(request, 'procesos_especiales/cambio_evento_confirmacion.html', {'object': p,"eo":e_o,"ed":e_d})
def cambio_evento_autorizar(request, pk):
	tmp = CambioEvento.objects.get(pk=pk)
	orden_origen = OrdenFacturacionParticipante.objects.filter(participante=tmp.participante.pk)[0]
	orden_destino = OrdenFacturacionParticipante.objects.filter(cod_evento=tmp.evento_destino)[0]

	
	orden_origen.nombre_evento=orden_destino.nombre_evento
	orden_origen.cod_evento=orden_destino.cod_evento
	orden_origen.descuento=orden_destino.descuento
	orden_origen.valor=orden_destino.valor
	orden_origen.save()
	tmp.estado = "ACPF";
	tmp.save()
	return HttpResponseRedirect("/financiero/perfiles/pendiente_aprobacion/")

def cambio_evento_anular(request, pk):
	tmp = CambioEvento.objects.get(pk=pk)
	tmp.estado = "ANLD";
	tmp.save()
	return HttpResponseRedirect("/financiero/perfiles/pendiente_aprobacion/")