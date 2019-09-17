from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	return render(request, 'perfiles_index.html')
def index_analista(request):
	return render(request, 'base_analista.html')
def index_coordinador(request):
	return render(request, 'base_coordinador.html')