from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Juridica
from .models import Ciudad
from .models import Sector
from .models import TipoEmpresa
from . import forms
from dal import autocomplete

from django.core.paginator import Paginator


class EmpresaAutocomplete(autocomplete.Select2QuerySetView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        qs = Juridica.objects.all().order_by("nombre")
        if self.q:
            qs = qs.filter(Q(nombre__icontains=self.q) | Q(ruc__istartswith=self.q))
            #qs = qs.filter(nombre__istartswith=self.q)
        return qs

    def has_add_permission(self, request):
        return True

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
	juridicas_list = Juridica.objects.all().order_by("pk")

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


def juridicas_editar(request,pk):
	if(request.method == "POST"):
		p = get_object_or_404(Juridica, pk=pk)
		form = forms.JuridicaForm(request.POST,instance=p)
		if(form.is_valid()):
			form.save()
			return redirect("index_juridicas")
	else:

		p = get_object_or_404(Juridica, pk=pk)
		form = forms.JuridicaForm(instance=p)
		#form.fields["fecha"].value=None
	return render(request, 'personas_juridicas/editar_forma.html', {'form': form})


def juridicas_eliminar(request,pk=None):
	if(request.method == "POST"):
		p = get_object_or_404(Juridica,pk=pk)
		p.delete()
		return redirect("index_juridicas")
	else:
		pk= request.GET.get('pk')
		if len(pk)<13:
			pk="0"+str(pk)
		p = get_object_or_404(Juridica,pk=pk)
		return render(request, 'personas_juridicas/eliminar.html', {'object': p})