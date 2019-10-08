from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import OrdenFacturacion, Persona_Natural, Juridica
from .forms import OrdenFacturacionForm, OrdenFacturacionUpdateForm, OrdenFacturacionFinalForm
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect
from datetime import date

# Create your views here.


class OrdenFacturacionCreate(CreateView):
    model=OrdenFacturacion
    form_class=OrdenFacturacionForm
    template_name='orden_facturacion_nuevo.html'
    success_url=reverse_lazy('orden_facturacion')

    def form_valid(self, form):
        try:
            pre=str(int(self.model.objects.latest('pk').pk+1))
            sec='0'*(4-len(pre))+pre
        except self.model.DoesNotExist:
            sec='0001'
        form.instance.cod_orden_fact=sec+'-'+str(date.today().year)
        return super().form_valid(form)
    
    def get_success_url(self, **kwargs):         
        return reverse_lazy('orden_facturacion_editar', args = (self.object.id,))

class OrdenFacturacionUpdate(UpdateView):
    model=OrdenFacturacion
    form_class=OrdenFacturacionUpdateForm
    second_form_class=OrdenFacturacionForm
    third_form_class=OrdenFacturacionFinalForm
    template_name='orden_facturacion_editar.html'
    success_url=reverse_lazy('orden_facturacion')

    def get_context_data(self, **kwargs):
        context=super(OrdenFacturacionUpdate,self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        orden=self.model.objects.get(id=pk)
        if 'form' in context:
            if orden.estado=='ACTV':
                context['form']=self.second_form_class(instance=orden)
            elif orden.estado=='FAES':
                context['form']=self.third_form_class(instance=orden)
            else:
                context['form']=self.form_class(instance=orden)
        context['orden_id']=pk
        selected_participantes=[]
        for par in orden.participantes.all():
            selected_participantes.append(par.pk)
        context['selected_participantes']=selected_participantes
        context['num']=list(range(0, orden.participantes.count()))
        return context

class OrdenFacturacionDelete(DeleteView):
    model=OrdenFacturacion
    template_name='orden_facturacion_eliminar.html'
    success_url=reverse_lazy('orden_facturacion')

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        self.object.estado="ANLD"
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

def orden_fact_conf_elim(request):
    orden_id=request.GET.get('pk')
    orden=OrdenFacturacion.objects.get(id=orden_id)
    return render(request,"orden_facturacion_eliminar.html",{"orden":orden})



def cambiar_estado(request, pk):
    orden=OrdenFacturacion.objects.get(id=pk)
    orden.estado='SLCE'
    orden.save()
    return HttpResponseRedirect(reverse_lazy('orden_facturacion'))

def verificar_campos(request):
    return render(request,"orden_facturacion_confirmar.html")



def load_personas(request):
    persona = request.GET.get("persona")
    identificacion=[]
    razon_nombre=[]
    if persona=="Natural":
        personas=Persona_Natural.objects.all()
        identificacion=render_to_string("dropdown_natural_ci.html",{"personas":personas})
        razon_nombre=render_to_string("dropdown_natural_nombres.html",{"personas":personas})
    elif persona=="Jurídica":
        personas=Juridica.objects.all()
        identificacion=render_to_string("dropdown_juridica_ruc.html",{"personas":personas})
        razon_nombre=render_to_string("dropdown_juridica_razon.html",{"personas":personas})    
    return JsonResponse({'ruc_ci': identificacion, 'razon_nombre': razon_nombre})
    