from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import OrdenIngreso
from .forms import OrdenIngresoForm, OrdenIngresoUpdateForm, OrdenIngresoPrintForm
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
        try:
            datos = OrdenFacturacion.objects.get(pk=self.kwargs.get('pk'))
            
            if(datos!=None):
                initial["ruc_ci"]=datos.ruc_ci
                initial["orden_facturacion"] = datos.id
                initial["tipo_cliente"]="Natural"
        except:
            pass
        return initial
    def form_valid(self, form):
        try:
            pre=str(int(self.model.objects.latest('pk').pk+1))
            sec='0'*(4-len(pre))+pre
        except self.model.DoesNotExist:
            sec='0001'
        form.instance.cod_orden_ing=sec+'-'+str(date.today().year)
        return super().form_valid(form)
    def post(self, request,*args,**kwargs):
        self.object =self.get_object
        form=self.form_class(request.POST)
        if form.is_valid():
            obj=(form.instance.orden_facturacion)
            obj.valor_pendiente-=form.instance.valor;
            if(obj.valor_pendiente==0):
                obj.estado='CNCL'
            obj.save()
            form.save()
           
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
    def get_success_url(self, **kwargs):         
            return reverse_lazy('ordenIngreso')


class OrdenIngresoUpdate(UpdateView):
    model=OrdenIngreso
    form_class=OrdenIngresoUpdateForm
    template_name='ordenIngreso_editar.html'
    success_url=reverse_lazy('ordenIngreso')

class OrdenIngresoPrint(UpdateView):
    model=OrdenIngreso
    form_class=OrdenIngresoPrintForm
    template_name='ordenIngreso_print.html'
    success_url=reverse_lazy('ordenIngreso')

class OrdenIngresoDelete(DeleteView):
    model=OrdenIngreso
    template_name='ordenIngreso_eliminar.html'
    success_url=reverse_lazy('ordenIngreso')

def orden_ing_conf_elim(request):
    orden_id=request.GET.get('pk')
    orden=OrdenIngreso.objects.get(id=orden_id)
    return render(request,"ordenIngreso_eliminar.html",{"ordenIngreso":orden})