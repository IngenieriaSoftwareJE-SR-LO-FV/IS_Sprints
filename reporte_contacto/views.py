from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import ReporteContacto, Capacitacion
from .forms import ReporteContactoForm, CapacitacionForm, AsesoriaForm

def index(request):
    return render(request,"reporte_list.html")

class ReporteContactoList(ListView):
    model=ReporteContacto
    template_name='reporte_list.html'
    ordering = ['id']

class ReporteContactoCreate(CreateView):
    model=ReporteContacto
    template_name= 'reporte_form.html'
    form_class=ReporteContactoForm
    second_form_class=CapacitacionForm
    success_url='/reporte_contacto'

    def get_context_data(self, **kwargs):
        context =super(ReporteContactoCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2']=self.second_form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object =self.get_object
        form=self.form_class(request.POST)
        form2=self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            capacitacion=form2.save(commit=False)
            capacitacion.reporte=form.save()
            capacitacion.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class ReporteContactoUpdate(UpdateView):
    model=ReporteContacto
    second_model=Capacitacion
    template_name='reporte_form.html'
    form_class=ReporteContactoForm
    second_form_class=CapacitacionForm
    success_url='/reporte_contacto'

    def get_context_data(self, **kwargs):
        context =super(ReporteContactoUpdate, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        capacitacion=self.second_model.objects.get(id=pk)
        reporte=self.model.objects.get(id=capacitacion.reporte_id)
        if 'form' not in context:   
            context['form']=self.form_class(instance=reporte)
        if 'form2' not in context:
            context['form2']=self.second_form_class(instance=capacitacion)
        context['id']=pk
        return context
    def post(self, request, *args, **kwargs):
        self.object =self.get_object
        id_capacitacion=kwargs['pk']
        capacitacion=self.second_model.objects.get(id=id_capacitacion)
        reporte =self.model.objects.get(id=capacitacion.reporte_id)
        form=self.form_class(request.POST, instance=reporte)
        form2=self.second_form_class(request.POST, instance=capacitacion)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class ReporteContactoDelete(DeleteView):
    model=ReporteContacto
    template_name='reporte_delete.html'
    success_url='/reporte_contacto'
