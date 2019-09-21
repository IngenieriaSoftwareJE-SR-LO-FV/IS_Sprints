from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import PropuestaCorporativo
from .forms import PropuestaCorporativoForm
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from ventas.reporte_contacto.models import ReporteContacto
from django.db.models import Q
from dal import autocomplete

# Create your views here.
class ReporteAutocomplete(autocomplete.Select2QuerySetView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        qs = ReporteContacto.objects.all().order_by("empresa")
        if self.q:
            qs = qs.filter(Q(empresa__icontains=self.q) | Q(id__istartswith=self.q))
        return qs

    def has_add_permission(self, request):
        return True

class PropuestaCorporativoCreate(CreateView):
    model=PropuestaCorporativo
    form_class=PropuestaCorporativoForm
    template_name='propuesta_corp_form.html'
    success_url=reverse_lazy('propuesta_corporativa')

    def post(self, request,*args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class PropuestaCorporativoUpdate(UpdateView):
    model=PropuestaCorporativo
    form_class=PropuestaCorporativoForm
    template_name='propuesta_corp_form.html'
    success_url=reverse_lazy('propuesta_corporativa')

    def get_context_data(self, **kwargs):
        context =super(PropuestaCorporativoUpdate, self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        l=[]
        vals=str(self.model.objects.get(cod_propuesta=pk).servicios_incluidos).split(',')
        print(vals)
        for s in self.model.SERVICIOS_CHOICES:
            print(s)
            if s[1] in vals or ' '+s[1] in vals:
                print(s[1])
                l.append(s[0])
        print(l)
        context['checked_servicios_incluidos']=l
        return context


class PropuestaCorporativoDelete(DeleteView):
    model=PropuestaCorporativo
    template_name='propuesta_corp_delete.html'
    form_class=PropuestaCorporativoForm
    success_url=reverse_lazy('propuesta_corporativa')
