from django.shortcuts import render
from django.views.generic import CreateView
from .models import OrdenFacturacion, Persona_Natural, Juridica
from .forms import OrdenFacturacionForm
# Create your views here.


class OrdenFacturacionCreate(CreateView):
    model=OrdenFacturacion
    form_class=OrdenFacturacionForm
    template_name='orden_facturacion_nuevo.html'

def load_personas(request):
    return render(request,"dropdown_personas_id.html",{"personas":get_personas(request)})

def get_personas(request):
    persona = request.GET.get("persona")
    if persona=="p_natural":
        personas=Persona_Natural.objects.all()
    elif persona=="p_juridica":
        personas=Juridica.objects.all()
    else:
        personas=[]
    return personas
    