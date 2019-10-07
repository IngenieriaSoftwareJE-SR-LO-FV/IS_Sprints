from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import OrdenIngreso
from .forms import OrdenIngresoForm
from django.urls import reverse_lazy
# Create your views here.

"""class OrdenIngresoCreate(CreateView):
    model=OrdenIngreso
    form_class=OrdenIngresoForm
    template_name='ordenIngreso_form.html'
    success_url=reverse_lazy('ordenIngreso')

    def post(self, request,*args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))"""


class OrdenIngresoCreate(CreateView):
    model=OrdenIngreso
    form_class=OrdenIngresoForm
    template_name='ordenIngreso_form.html'
    success_url=reverse_lazy('ordenIngreso')

    def form_valid(self, form):
        try:
            pre=str(int(self.model.objects.latest('pk').pk+1))
            sec='0'*(4-len(pre))+pre
        except self.model.DoesNotExist:
            sec='0001'
        form.instance.cod_orden_ing=sec+'-'+str(date.today().year)
        return super().form_valid(form)
    
    def get_success_url(self, **kwargs):         
            return reverse_lazy('orden_facturacion_editar', args = (self.object.id,))