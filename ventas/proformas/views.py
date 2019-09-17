from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProformaForm
from .models import Proforma
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
# Create your views here.


def proforma_view(request):
	if request.method == "POST":
		form=ProformaForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
		return redirect("proforma_lista")
	else:
		form=ProformaForm()
	return render(request, 'proforma_form.html', {'form':form})

class ProformaUpdate(UpdateView):
    model=Proforma
    form_class=ProformaForm
    template_name='proforma_form.html'
    success_url=reverse_lazy('proforma_lista')


class ProformaDelete(DeleteView):
    model=Proforma
    template_name='proforma_delete.html'
    form_class=ProformaForm
    success_url=reverse_lazy('proforma_lista')
