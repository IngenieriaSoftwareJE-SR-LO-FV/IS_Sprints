from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProformaForm
from .models import Proforma
from django.urls import reverse_lazy
from datetime import date
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
# Create your views here.

"""try:
            pre=str(int(self.model.objects.latest('pk').pk+1))
            sec='0'*(4-len(pre))+pre
        except self.model.DoesNotExist:
            sec='0001'
        form.instance.cod_orden_fact=sec+'-'+str(date.today().year)"""

def proforma_view(request):
	if request.method == "POST":
		form=ProformaForm(request.POST,request.FILES)
		if form.is_valid():
			try:
				pre = str(int(Proforma.objects.latest('pk').pk+1))
				sec = '0'*(4-len(pre))+pre
			except Proforma.DoesNotExist:
				sec = '0001'
			form.instance.codigo = 'PROF-CEC-'+sec+'-'+str(date.today().year)
			form.save()
		return redirect("proforma_lista")
	else:
		form=ProformaForm()
	return render(request, 'proforma_form.html', {'form':form})

class ProformaUpdate(UpdateView):
    model=Proforma
    form_class=ProformaForm
    template_name='proforma_editar.html'
    success_url=reverse_lazy('proforma_lista')


class ProformaDelete(DeleteView):
    model=Proforma
    template_name='proforma_delete.html'
    form_class=ProformaForm
    success_url=reverse_lazy('proforma_lista')
