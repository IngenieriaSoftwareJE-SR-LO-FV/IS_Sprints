from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "procesos_especiales/procesos_especiales_index.html")

def cambio_participante_index(request):
	return render(request, "procesos_especiales/procesos_especiales_index.html")

def devolucion_index(request):
	return render(request, "procesos_especiales/procesos_especiales_index.html")

def cambio_evento_index(request):
	return render(request, "procesos_especiales/procesos_especiales_index.html")
