from django.shortcuts import render, redirect
from financiero.presupuestos.models import PresupuestoEvento

# Create your views here.

def index(request):
	return render(request, 'perfiles_index.html')

def index_analista(request):
	return render(request, 'base_analista.html')

def index_coordinador(request):
	return render(request, 'base_coordinador.html')

def por_aprobar(request):
	presupuestos_ev = PresupuestoEvento.objects.filter(estado=None)
	return render(request, 'por_aprobar.html', {"presupuestos_ev":presupuestos_ev})