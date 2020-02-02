from django.shortcuts import render, redirect
from . import forms
from .models import *
from django.http import JsonResponse, HttpResponseRedirect
from ventas.personas_naturales.models import Persona_Natural
from financiero.orden_facturacion.models import OrdenFacturacionParticipante
from django.template.loader import render_to_string
# Create your views here.
def index(request):
	return render(request, "procesos_especiales/procesos_especiales_index.html")

def cambio_participante_index(request):
	return render(request, "procesos_especiales/procesos_especiales_index.html")

def devolucion_index(request):
	return render(request, "procesos_especiales/procesos_especiales_index.html")

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

	e_o = OrdenFacturacionParticipante.objects.get(cod_evento=request.GET.get('evento_origen'))
	e_d = OrdenFacturacionParticipante.objects.get(cod_evento=request.GET.get('evento_destino'))
	print({'object': p,"eo":e_o,"ed":e_d});
	return render(request, 'procesos_especiales/cambio_evento_confirmacion.html', {'object': p,"eo":e_o,"ed":e_d})
def cambio_evento_autorizar(request, pk):
	tmp = CambioEvento.objects.get(pk=pk)
	orden=Persona_Natural.objects.get(pk=tmp.participante.pk)
	orden_destino = OrdenFacturacionParticipante.objects.get(cod_evento=tmp.evento_destino)
	orden.nombre_evento=orden_destino.nombre_evento
	orden.cod_evento=orden_destino.cod_evento
	orden.save()
	tmp.estado = "ACPF";
	tmp.save()
	return HttpResponseRedirect("/financiero/perfiles/pendiente_aprobacion/")

def cambio_evento_anular(request, pk):
	tmp = CambioEvento.objects.get(pk=pk)
	tmp.estado = "ANLD";
	tmp.save()
	return HttpResponseRedirect("/financiero/perfiles/pendiente_aprobacion/")