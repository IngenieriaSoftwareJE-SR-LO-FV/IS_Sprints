from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Juridica
from .models import Ciudad
from .models import Sector
from .models import TipoEmpresa
from . import forms
from dal import autocomplete

from django.core.paginator import Paginator

class TipoAutocomplete(autocomplete.Select2QuerySetView):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def get_queryset(self):
		qs = TipoEmpresa.objects.all().order_by("nombre")

		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)
		return qs

		
	def has_add_permission(self, request):
		return True
class SectorAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		qs = Sector.objects.all().order_by("nombre")

		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)

		return qs
	def has_add_permission(self, request):
		return True
# Create your views here.
def index_juridicas(request):
	juridicas_list = Juridica.objects.all().order_by("id")

	filter = forms.JuridicaFilter(request.GET, queryset=juridicas_list )
	paginator = Paginator(filter.qs, 30) 

	page = request.GET.get('page')
	juridicas = paginator.get_page(page)
	return render(request, 'personas_juridicas/index.html', {'juridicas': juridicas, "filter":filter})

	
def load_ciudades(request):
	provincia_id = request.GET.get("provincia")
	ciudades = Ciudad.objects.filter(provincia_id=provincia_id).order_by('nombre')
	
	return render(request,"personas_juridicas/dropdown_ciudades.html",{"ciudades":ciudades})

def juridicas_view(request):
	if(request.method == "POST"):
		form = forms.JuridicaForm(request.POST)
		if(form.is_valid()):
			form.save()
		return redirect("index_juridicas")
	else:
		form = forms.JuridicaForm()
	return render(request,"personas_juridicas/forma.html", {"form":form})