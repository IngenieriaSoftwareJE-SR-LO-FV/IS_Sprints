from django.shortcuts import render, redirect
from .forms import NotaCreditoForm
from .models import NotaCredito

# Create your views here.
def index(request):
	return render(request, "procesos_especiales/procesos_especiales_index.html")

def cambio_participante_index(request):
	return render(request, "procesos_especiales/procesos_especiales_index.html")

def devolucion_nuevo(request):
	if(request.method == "POST"):
		form = NotaCreditoForm(request.POST)
		if(form.is_valid()):
			form.save()
			return redirect("procesos_especiales_index")
	else:
		form = NotaCreditoForm()
	return render(request, "procesos_especiales/procesos_especiales_nota_credito_nuevo.html", {"form":form})

def cambio_evento_index(request):
	return render(request, "procesos_especiales/procesos_especiales_index.html")
