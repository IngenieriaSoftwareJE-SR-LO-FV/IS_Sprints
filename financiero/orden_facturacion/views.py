from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import OrdenFacturacion, Persona_Natural, Juridica
from .forms import OrdenFacturacionForm
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect
# Create your views here.


class OrdenFacturacionCreate(CreateView):
    model=OrdenFacturacion
    form_class=OrdenFacturacionForm
    template_name='orden_facturacion_nuevo.html'
    success_url=reverse_lazy('orden_facturacion')
    def post(self, request,*args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


def load_personas(request):
    persona = request.GET.get("persona")
    identificacion=[]
    razon_nombre=[]
    if persona=="p_natural":
        personas=Persona_Natural.objects.all()
        identificacion=render_to_string("dropdown_natural_ci.html",{"personas":personas})
        razon_nombre=render_to_string("dropdown_natural_nombres.html",{"personas":personas})
    elif persona=="p_juridica":
        personas=Juridica.objects.all()
        identificacion=render_to_string("dropdown_juridica_ruc.html",{"personas":personas})
        razon_nombre=render_to_string("dropdown_juridica_razon.html",{"personas":personas})    
    return JsonResponse({'ruc_ci': identificacion, 'razon_nombre': razon_nombre})
    