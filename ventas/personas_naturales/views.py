from django.shortcuts import render, redirect
from .forms import Natural_NuevoForm
from .models import Persona_Natural 
from . import forms
from .filters import NaturalBusquedaFilter
from django.core.paginator import Paginator
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    naturales_lista = Persona_Natural.objects.all()
    naturales_filter = NaturalBusquedaFilter(request.GET, queryset=naturales_lista)
    paginator = Paginator(naturales_filter.qs, 30) 
    page = request.GET.get('page')
    naturales = paginator.get_page(page)
    return render(request, 'personas_naturales/natural.html', {'naturales_filter': naturales_filter,"naturales":naturales})

def natural_nuevo_t(request):
	if(request.method == "POST"):
		form = forms.Natural_NuevoForm(request.POST)
		print(request.POST)
		if(form.is_valid()):
			form.save()
			return redirect("natural_lista")
		return render(request,"personas_naturales/natural_nuevo.html", {"form":form})
	return redirect("natural_lista")

def natural_nuevo(request):
	if(request.method == "POST"):
		form = forms.Natural_NuevoForm(request.POST)
		if(form.is_valid()):
			vacios = 0
			for f in form.fields:
				if(form[f].data==""):
					vacios=vacios+1
			return render(request, "personas_naturales/natural_confirmacion.html", {"form":form, "vacios":vacios})
	else:
		form = forms.Natural_NuevoForm()
	return render(request,"personas_naturales/natural_nuevo.html", {"form":form})

class NaturalUpdate(UpdateView):
	model = Persona_Natural
	form_class = Natural_NuevoForm
	template_name = 'personas_naturales/natural_nuevo.html'
	success_url = reverse_lazy('natural_lista')

class NaturalDelete(DeleteView):
	model = Persona_Natural
	template_name = 'personas_naturales/natural_eliminar.html'
	form_class = Natural_NuevoForm
	success_url = reverse_lazy('natural_lista')
