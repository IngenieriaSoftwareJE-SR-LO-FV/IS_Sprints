from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrdenPagoForm
from .models import OrdenPago 
from . import forms
from .filters import OrdenPagoFilter
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
	ordPago_lista = OrdenPago.objects.all()
	ordPago_filter = OrdenPagoFilter(request.GET, queryset=ordPago_lista)
	return render(request, "orden_pago/ordenpago_list.html", {"ordenes_pago":ordPago_lista, "filter":ordPago_filter})
