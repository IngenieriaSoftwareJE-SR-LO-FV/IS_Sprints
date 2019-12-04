from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import OrdenIngreso
from .forms import OrdenIngresoForm, OrdenIngresoUpdateForm
from django.urls import reverse_lazy
from datetime import date
from financiero.orden_facturacion.models import OrdenFacturacion
# Create your views here.



class OrdenIngresoCreate(CreateView):
    model=OrdenIngreso
    form_class=OrdenIngresoForm
    template_name='ordenIngreso_form.html'
    success_url=reverse_lazy('ordenIngreso')
    def get_initial(self):
        initial = super(OrdenIngresoCreate, self).get_initial()
        # Copy the dictionary so we don't accidentally change a mutable dict
        initial = initial.copy()
        
        datos = OrdenFacturacion.objects.get(pk=self.kwargs.get('pk'))
        if(datos!=None):
            initial["ruc_ci"]="123"
            initial["tipo_cliente"]="Jurídica"
       # etc...
        return initial
    def form_valid(self, form):
        try:
            pre=str(int(self.model.objects.latest('pk').pk+1))
            sec='0'*(4-len(pre))+pre
        except self.model.DoesNotExist:
            sec='0001'
        form.instance.cod_orden_ing=sec+'-'+str(date.today().year)
        return super().form_valid(form)
    
    def get_success_url(self, **kwargs):         
            return reverse_lazy('ordenIngreso')


class OrdenIngresoUpdate(UpdateView):
    model=OrdenIngreso
    form_class=OrdenIngresoUpdateForm
    template_name='ordenIngreso_editar.html'
    success_url=reverse_lazy('ordenIngreso')

class OrdenIngresoDelete(DeleteView):
    model=OrdenIngreso
    template_name='ordenIngreso_eliminar.html'
    success_url=reverse_lazy('ordenIngreso')

def orden_ing_conf_elim(request):
    orden_id=request.GET.get('pk')
    orden=OrdenIngreso.objects.get(id=orden_id)
    return render(request,"ordenIngreso_eliminar.html",{"ordenIngreso":orden})