from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import OrdenFacturacion, Persona_Natural, Juridica
from .forms import OrdenFacturacionForm, OrdenFacturacionUpdateForm
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
            sec='00'+str(int(self.model.objects.latest('pk').pk)+1)
        except self.model.DoesNotExist:
            sec='001'
        form.instance.cod_orden_fact=sec+'-'+str(date.today().year)
        return super().form_valid(form)
    

class OrdenFacturacionUpdate(UpdateView):
    model=OrdenFacturacion
    form_class=OrdenFacturacionUpdateForm
    template_name='orden_facturacion_editar.html'
    success_url=reverse_lazy('orden_facturacion')

class OrdenFacturacionDelete(DeleteView):
    model=OrdenFacturacion
    template_name='orden_facturacion_eliminar.html'
    success_url=reverse_lazy('orden_facturacion')

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
    