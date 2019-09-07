from django.shortcuts import render, redirect
from .forms import Natural_NuevoForm
from .models import Persona_Natural 
from . import forms
from .filters import NaturalBusquedaFilter

# Create your views here.

def index(request):
    naturales_lista = Persona_Natural.objects.all()
    naturales_filter = NaturalBusquedaFilter(request.GET, queryset=naturales_lista)
    return render(request, 'personas_naturales/natural.html', {'naturales_filter': naturales_filter})


def natural_nuevo(request):
	if(request.method == "POST"):
		form = forms.Natural_NuevoForm(request.POST)
		if(form.is_valid()):
			form.save()
		return redirect("index")
	else:
		form = forms.Natural_NuevoForm()
	return render(request,"personas_naturales/natural_nuevo.html",{"form":form})