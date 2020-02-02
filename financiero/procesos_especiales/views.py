from django.shortcuts import render, redirect, get_object_or_404
from .forms import NotaCreditoForm
from .models import NotaCredito

# Create your views here.
def index(request):
	nota_credito = NotaCredito.objects.all()
	return render(request, "procesos_especiales/procesos_especiales_index.html", {"nota_credito":nota_credito})

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

def devolucion_editar(request, pk):
	if(request.method == 'POST'):
		p = get_object_or_404(NotaCredito, pk=pk)
		form = NotaCreditoForm(request.POST, instance=p)
		if(form.is_valid()):
			form.save()
			return redirect("procesos_especiales_index")
	else:
		p = get_object_or_404(NotaCredito, pk=pk)
		form = NotaCreditoForm(instance=p)
	return render(request, "procesos_especiales/procesos_especiales_nota_credito_editar.html", {'form': form})

def cambio_evento_index(request):
	return render(request, "procesos_especiales/procesos_especiales_index.html")
