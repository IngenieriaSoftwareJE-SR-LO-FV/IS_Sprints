from django.shortcuts import render, redirect, get_object_or_404
from .forms import EspoltechForm, FundespolForm
from .models import Espoltech, Fundespol
from .filters import EspoltechFilter
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from datetime import date
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

def index(request):
	presupuesto_lista = Espoltech.objects.all()
	presupuesto_filter = EspoltechFilter(request.GET, queryset=presupuesto_lista)
	return render(request, "presupuestos_anuales/presupuestos_anuales_list.html", {"presupuestos_an":presupuesto_lista, "filter":presupuesto_filter})


def presupuestos_anuales_nuevo(request):
	if(request.method == 'POST'):
		form = EspoltechForm(request.POST)
		if(form.is_valid()):
			form.save()
			return redirect("presupuesto_anual_lista")
	else:
		form = EspoltechForm()
	return render(request, "presupuestos_anuales/espoltech_nuevo.html", {"form":form})


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


def presupuesto_anual_enviar(request, pk):
	p = get_object_or_404(Espoltech, pk=pk)
	p.estado = 'ENVD'
	p.save()
	return redirect('presupuesto_anual_lista')


def presupuesto_anual_autorizar(request, pk):
	p = get_object_or_404(Espoltech, pk=pk)
	p.estado = 'AUTR'
	p.save()
	return redirect('pendiente_aprobacion')
