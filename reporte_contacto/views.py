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
    template_name= 'reporte_form.html'
    form_class=ReporteContactoForm
    success_url='/reporte_contacto/editar'
    
    def post(self, request, *args, **kwargs):
        self.object =self.get_object
        form=self.form_class(request.POST)
        if form.is_valid():
            reporte=form.save()
            return HttpResponseRedirect(self.get_success_url()+'/'+str(reporte.id))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ReporteContactoUpdate(UpdateView):
    model=ReporteContacto
    second_model=Capacitacion
    third_model=Asesoria
    template_name='reporte_update.html'
    form_class=ReporteContactoForm
    success_url='/reporte_contacto'

    def get_context_data(self, **kwargs):
        context =super(ReporteContactoUpdate, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        capacitaciones=self.second_model.objects.filter(reporte_id=pk)
        asesorias=self.third_model.objects.filter(reporte_id=pk)
        context['capacitaciones']=capacitaciones
        context['asesorias']=asesorias
        context['reporte_id']=pk
        return context

class ReporteContactoDelete(DeleteView):
    model=ReporteContacto
    template_name='reporte_delete.html'
    success_url='/reporte_contacto'

class CapacitacionCreate(CreateView):
    model=Capacitacion
    form_class=CapacitacionForm
    template_name='capacitacion_form.html'
    success_url='/reporte_contacto/editar'

    def get_context_data(self, **kwargs):
        context=super(CapacitacionCreate,self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        context['reporte_id']=pk
        return context

    def post(self, request,*args,**kwargs):
        self.object =self.get_object
        form=self.form_class(request.POST)
        if form.is_valid():
            reporte_id=kwargs['pk']
            c=form.save(commit=False)
            c.reporte_id=reporte_id
            c.save()
            return HttpResponseRedirect(self.get_success_url()+'/'+str(reporte_id))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class CapacitacionUpdate(UpdateView):
    model=Capacitacion
    form_class=CapacitacionForm
    template_name='capacitacion_form.html'
    success_url='/reporte_contacto/editar'

    def get_context_data(self, **kwargs):
        context=super(CapacitacionUpdate,self).get_context_data(**kwargs)
        fk=self.kwargs.get('fk',0)
        context['reporte_id']=fk
        return context

    def post(self, request, *args, **kwargs):
        self.object=self.get_object
        reporte_id=kwargs['fk']
        pk=kwargs['pk']
        capacitacion=self.model.objects.get(id=pk)
        form=self.form_class(request.POST, instance=capacitacion)
        if form.is_valid():
            c=form.save(commit=False)
            c.reporte_id=reporte_id
            c.save()
            return HttpResponseRedirect(self.get_success_url()+'/'+str(reporte_id))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class CapacitacionDelete(DeleteView):
    model=Capacitacion
    form_class=CapacitacionForm
    template_name='capacitacion_delete.html'
    success_url='/reporte_contacto/editar'

    def get_context_data(self, **kwargs):
        context=super(CapacitacionDelete,self).get_context_data(**kwargs)
        fk=self.kwargs.get('fk',0)
        context['reporte_id']=fk
        return context

    def post(self, request, *args, **kwargs):
        reporte_id=kwargs['fk']
        self.object=self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url()+'/'+str(reporte_id))


class AsesoriaCreate(CreateView):
    model=Asesoria
    form_class=AsesoriaForm
    template_name='asesoria_form.html'
    success_url='/reporte_contacto/editar'

    def get_context_data(self, **kwargs):
        context=super(AsesoriaCreate,self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        context['reporte_id']=pk
        return context

    def post(self, request,*args,**kwargs):
        self.object =self.get_object
        form=self.form_class(request.POST)
        if form.is_valid():
            reporte_id=kwargs['pk']
            a=form.save(commit=False)
            a.reporte_id=reporte_id
            a.save()
            return HttpResponseRedirect(self.get_success_url()+'/'+str(reporte_id))
        else:
            return self.render_to_response(self.get_context_data(form=form))

class AsesoriaUpdate(UpdateView):
    model=Asesoria
    form_class=AsesoriaForm
    template_name='asesoria_form.html'
    success_url='/reporte_contacto/editar'

    def get_context_data(self, **kwargs):
        context=super(AsesoriaUpdate,self).get_context_data(**kwargs)
        fk=self.kwargs.get('fk',0)
        context['reporte_id']=fk
        return context

    def post(self, request, *args, **kwargs):
        self.object=self.get_object
        reporte_id=kwargs['fk']
        pk=kwargs['pk']
        asesoria=self.model.objects.get(id=pk)
        form=self.form_class(request.POST, instance=asesoria)
        if form.is_valid():
            a=form.save(commit=False)
            a.reporte_id=reporte_id
            a.save()
            return HttpResponseRedirect(self.get_success_url()+'/'+str(reporte_id))
        else:
            return self.render_to_response(self.get_context_data(form=form))



class AsesoriaDelete(DeleteView):
    model=Asesoria
    form_class=AsesoriaForm
    template_name='asesoria_delete.html'
    success_url='/reporte_contacto/editar'

    def get_context_data(self, **kwargs):
        context=super(AsesoriaDelete,self).get_context_data(**kwargs)
        fk=self.kwargs.get('fk',0)
        context['reporte_id']=fk
        return context

    def post(self, request, *args, **kwargs):
        reporte_id=kwargs['fk']
        self.object=self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url()+'/'+str(reporte_id))