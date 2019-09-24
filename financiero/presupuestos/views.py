from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse

from .models import *

from . import forms
from dal import autocomplete

from django.core.paginator import Paginator

class AulaAutocomplete(autocomplete.Select2QuerySetView):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def get_queryset(self):
		qs = Aula.objects.all().order_by("nombre")

		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)
		return qs

		
	def has_add_permission(self, request):
		return True
class EmpresaAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		qs = Juridica.objects.all().order_by("nombre")

		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)

		return qs
	def has_add_permission(self, request):
		return True


def index_presupuestos(request):
	presupuestos_list = PresupuestoEvento.objects.all().order_by("id")

	filter = forms.PresupuestoEventoFilter(request.GET, queryset=presupuestos_list )
	paginator = Paginator(filter.qs, 30) 

	page = request.GET.get('page')
	presupuestos = paginator.get_page(page)
	return render(request, 'presupuestos/index.html', {'presupuestos': presupuestos, "filter":filter})

	

def presupuestos_nuevo(request):
	if(request.method == "POST"):
		form = forms.PresupuestoEventoForm(request.POST)
		if(form.is_valid()):
			form.save()
			return redirect("index_presupuestos")
	else:
		form = forms.PresupuestoEventoForm()
	return render(request,"presupuestos/forma.html", {"form":form})

def presupuestos_editar(request,pk):
	if(request.method == "POST"):
		p = get_object_or_404(PresupuestoEvento, pk=pk)
		form = forms.PresupuestoEventoForm(request.POST,instance=p)
		if(form.is_valid()):
			form.save()
			return redirect("index_presupuestos")
	else:

		p = get_object_or_404(PresupuestoEvento, pk=pk)
		form = forms.PresupuestoEventoForm(instance=p,initial={'fecha': p.fecha})
		#form.fields["fecha"].value=None
	return render(request, 'presupuestos/forma.html', {'form': form})