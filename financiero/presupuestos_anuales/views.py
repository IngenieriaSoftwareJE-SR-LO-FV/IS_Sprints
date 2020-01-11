from django.shortcuts import render, redirect, get_object_or_404
from .forms import EspoltechForm, FundespolForm
from .models import Espoltech, Fundespol
from .filters import EspoltechFilter, FundespolFilter
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from datetime import date
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

def index(request):
	presupuesto_lista = Espoltech.objects.all()
	presupuesto_filter = EspoltechFilter(request.GET, queryset=presupuesto_lista)
	presupuesto_lista_f = Fundespol.objects.all()
	presupuesto_filter_f = FundespolFilter(request.GET, queryset=presupuesto_lista_f)
	return render(request, "presupuestos_anuales/presupuestos_anuales_list.html", {"presupuestos_an":presupuesto_lista, "filter":presupuesto_filter, "presupuesto_an_f":presupuesto_lista_f, "filter_f":presupuesto_filter_f})



# FUNCIONES DE CREAR NUEVO
def presupuestos_anuales_nuevo(request):
	if(request.method == 'POST'):
		form = EspoltechForm(request.POST)
		if(form.is_valid()):
			form.save()
			return redirect("presupuesto_anual_lista")
	else:
		form = EspoltechForm()
	return render(request, "presupuestos_anuales/espoltech_nuevo.html", {"form":form})

def presupuestos_anuales_nuevo_fundespol(request):
	if(request.method == 'POST'):
		form = FundespolForm(request.POST)
		if(form.is_valid()):
			form.save()
			return redirect("presupuesto_anual_lista")
	else:
		form = FundespolForm()
	return render(request, "presupuestos_anuales/fundespol_nuevo.html", {"form":form})



# FUNCIONES DE EDITAR
def presupuesto_anual_editar(request, pk):
	if(request.method == 'POST'):
		p = get_object_or_404(Espoltech, pk=pk)
		form = EspoltechForm(request.POST, instance=p)
		if(form.is_valid()):
			form.save()
			return redirect("presupuesto_anual_lista")
	else:
		p = get_object_or_404(Espoltech, pk=pk)
		form = EspoltechForm(instance=p)
	return render(request, "presupuestos_anuales/espoltech_editar.html", {'form': form, 'p':p})

def presupuesto_anual_editar_fundespol(request, pk):
	if(request.method == 'POST'):
		p = get_object_or_404(Fundespol, pk=pk)
		form = FundespolForm(request.POST, instance=p)
		if(form.is_valid()):
			form.save()
			return redirect("presupuesto_anual_lista")
	else:
		p = get_object_or_404(Fundespol, pk=pk)
		form = FundespolForm(instance=p)
	return render(request, "presupuestos_anuales/fundespol_editar.html", {'form': form, 'p':p})



# FUNCIONES DE EDITAR UNA VEZ ENVIADA LA SOLICITUD DE APROBACION
def presupuesto_anual_editarAUTR(request, pk):
	if(request.method == 'POST'):
		p = get_object_or_404(Espoltech, pk=pk)
		form = EspoltechForm(request.POST, instance=p)
		if(form.is_valid()):
			form.save()
			return redirect("pendiente_aprobacion")
	else:
		p = get_object_or_404(Espoltech, pk=pk)
		form = EspoltechForm(instance=p)
	return render(request, "presupuestos_anuales/espoltech_aprobar.html", {'form': form, 'p':p})

def presupuesto_anual_editarAUTR_fundespol(request, pk):
	if(request.method == 'POST'):
		p = get_object_or_404(Fundespol, pk=pk)
		form = FundespolForm(request.POST, instance=p)
		if(form.is_valid()):
			form.save()
			return redirect("pendiente_aprobacion")
	else:
		p = get_object_or_404(Fundespol, pk=pk)
		form = FundespolForm(instance=p)
	return render(request, "presupuestos_anuales/fundespol_aprobar.html", {'form': form, 'p':p})



# FUNCIONES DE ENVIAR SOLICITUD
def presupuesto_anual_enviar(request, pk):
	p = get_object_or_404(Espoltech, pk=pk)
	p.estado = 'ENVD'
	p.save()
	return redirect('presupuesto_anual_lista')

def presupuesto_anual_enviar_fundespol(request, pk):
	p = get_object_or_404(Fundespol, pk=pk)
	p.estado = 'ENVD'
	p.save()
	return redirect('presupuesto_anual_lista')



# FUNCIONES DE AUTORIZAR PRESUPUESTO
def presupuesto_anual_autorizar(request, pk):
	p = get_object_or_404(Espoltech, pk=pk)
	p.estado = 'AUTR'
	p.save()
	return redirect('pendiente_aprobacion')

def presupuesto_anual_autorizar_fundespol(request, pk):
	p = get_object_or_404(Fundespol, pk=pk)
	p.estado = 'AUTR'
	p.save()
	return redirect('pendiente_aprobacion')



# FUNCIONES DE ANULAR PRESUPUESTO
def presupuesto_anual_anular(request, pk=None):
	if(request.method == "POST"):
		p = get_object_or_404(Espoltech, pk=pk)
		form = EspoltechForm(request.POST, instance=p)
		if(form.is_valid()):
			form.instance.estado = 'ANLD'
			form.save()
		return redirect('presupuesto_anual_lista')
	else:
		pk = request.GET.get('pk')
		p = get_object_or_404(Espoltech, pk=pk)
		form = EspoltechForm(instance=p)
		return render(request, 'presupuestos_anuales/presupuestos_anuales_anular.html', {'object':p, 'form':form})

def presupuesto_anual_anular_fundespol(request, pk=None):
	if(request.method == "POST"):
		p = get_object_or_404(Fundespol, pk=pk)
		form = FundespolForm(request.POST, instance=p)
		if(form.is_valid()):
			form.instance.estado = 'ANLD'
			form.save()
		return redirect('presupuesto_anual_lista')
	else:
		pk = request.GET.get('pk')
		p = get_object_or_404(Fundespol, pk=pk)
		form = FundespolForm(instance=p)
		return render(request, 'presupuestos_anuales/presupuestos_anuales_anular.html', {'object':p, 'form':form})

