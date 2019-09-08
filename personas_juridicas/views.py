from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Juridica
from .models import Ciudad
from . import forms

from django.core.paginator import Paginator
# Create your views here.
def index_juridicas(request):
	juridicas_list = Juridica.objects.all().order_by("id")

	filter = forms.JuridicaFilter(request.GET, queryset=juridicas_list )
	#form = forms.JuridicaForm()
	paginator = Paginator(filter.qs, 30) 

	page = request.GET.get('page')
	juridicas = paginator.get_page(page)
	return render(request, 'personas_juridicas/index.html', {'juridicas': juridicas, "filter":filter})
	#items_per_page=10;
	#elements = (Juridica.objects.order_by("id")[(page-1)*items_per_page:items_per_page*page])
	#return render(request,"personas_juridicas/index.html", {"page":page,"elements":elements})
	
def load_ciudades(request):
	provincia_id = request.GET.get("provincia")
	ciudades = Ciudad.objects.filter(provincia_id=provincia_id).order_by('nombre')
	
	return render(request,"personas_juridicas/dropdown_ciudades.html",{"ciudades":ciudades})

def juridicas_view(request):
	if(request.method == "POST"):
		form = forms.JuridicaForm(request.POST)
		if(form.is_valid()):
			form.save()
			return redirect("url index")
	else:
		form = forms.JuridicaForm()
	return render(request,"personas_juridicas/forma.html", {"form":form})