from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import ReporteContacto, Capacitacion, Asesoria
from .forms import ReporteContactoForm, CapacitacionForm, AsesoriaForm

def index(request):
    return render(request,"reporte_list.html")

class ReporteContactoList(ListView):
    model=ReporteContacto
    template_name='reporte_list.html'
    ordering = ['id']

class ReporteContactoCreate(CreateView):
    model=ReporteContacto
    second_model=Capacitacion
    template_name= 'reporte_form.html'
    form_class=ReporteContactoForm
    second_form_class=CapacitacionForm
    third_form_class=AsesoriaForm
    success_url='/reporte_contacto'

    def get_context_data(self, **kwargs):
        context =super(ReporteContactoCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2']=self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3']=self.third_form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object =self.get_object
        form=self.form_class(request.POST)
        form2=self.second_form_class(request.POST)
        form3=self.third_form_class(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            reporte=form.save()
            capacitacion=form2.save(commit=False)
            asesoria=form3.save(commit=False)
            capacitacion.reporte=reporte
            capacitacion.save()
            asesoria.reporte=reporte
            asesoria.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))


class ReporteContactoUpdate(UpdateView):
    model=ReporteContacto
    second_model=Capacitacion
    third_model=Asesoria
    template_name='reporte_form.html'
    form_class=ReporteContactoForm
    second_form_class=CapacitacionForm
    third_form_class=AsesoriaForm
    success_url='/reporte_contacto'

    def get_context_data(self, **kwargs):
        context =super(ReporteContactoUpdate, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        reporte=self.model.objects.get(id=pk)
        capacitacion=self.second_model.objects.get(reporte_id=pk)
        asesoria=self.third_model.objects.get(reporte_id=pk)
        if 'form' not in context:   
            context['form']=self.form_class(instance=reporte)
        if 'form2' not in context:
            context['form2']=self.second_form_class(instance=capacitacion)
        if 'form3' not in context:
            context['form3']=self.third_form_class(instance=asesoria)
        context['id']=pk
        return context

    def post(self, request, *args, **kwargs):
        self.object =self.get_object()
        id_reporte=kwargs['pk']
        reporte =self.model.objects.get(id=id_reporte)
        capacitacion=self.second_model.objects.get(reporte_id=id_reporte)
        print(capacitacion)
        asesoria=self.third_model.objects.get(reporte_id=id_reporte)
        print(asesoria)
        form=self.form_class(request.POST, instance=reporte)
        form2=self.second_form_class(request.POST, instance=capacitacion)
        form3=self.third_form_class(request.POST, instance=asesoria)
        print(form.is_valid(),form2.is_valid(),form3.is_valid())
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            print("SON VALIDAS")
            form.save()
            form2.save()
            form3.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class ReporteContactoDelete(DeleteView):
    model=ReporteContacto
    template_name='reporte_delete.html'
    success_url='/reporte_contacto'
