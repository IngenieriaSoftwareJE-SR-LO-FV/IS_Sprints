from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	return render(request, 'financiero/base_financiero.html')
def index_analista(request):
	return render(request, 'financiero/base_analista.html')
def index_coordinador(request):
	return render(request, 'financiero/base_coordinador.html')