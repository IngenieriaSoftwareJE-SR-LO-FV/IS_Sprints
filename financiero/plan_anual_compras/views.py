from django.shortcuts import render, redirect, get_object_or_404
from .models import PlanAnualCompras, Partida
from .forms import PlanAnualComprasForm, PartidaForm
from .filters import PlanAnualComprasFilter
from datetime import date
from django.http import HttpResponseRedirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
	pac_lista = PlanAnualCompras.objects.all()
	pac_filter = PlanAnualComprasFilter(request.GET, queryset=pac_lista)
	return render(request, "plan_anual_compras/pac_list.html", {"pac_lista":pac_lista, "filter":pac_filter})


class PACCreate(CreateView):
	model = PlanAnualCompras
	template_name = 'plan_anual_compras/pac_nuevo.html'
	form_class = PlanAnualComprasForm
	success_url = '/financiero/plan_anual_compras/editar'

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			if(form['nombre'].data==''):
				form.instance.nombre = 'Plan Anual de Compras - '+form['año'].data
			pac = form.save()
			return HttpResponseRedirect(self.get_success_url()+'/'+str(pac.pk))
		else:
			return self.render_to_response(self.get_context_data(form=form))


class PACUpdate(UpdateView):
	model = PlanAnualCompras
	second_model = Partida
	template_name = 'plan_anual_compras/pac_editar.html'
	form_class = PlanAnualComprasForm
	success_url = reverse_lazy('pac_index')
	def get_context_data(self, **kwargs):
		context = super(PACUpdate, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		partidas = self.second_model.objects.filter(pac_id=pk)
		context['partidas'] = partidas
		context['pac_id'] = pk
		return context


def PACDelete(request, pk=None):
	if(request.method == "POST"):
		p = get_object_or_404(PlanAnualCompras, pk=pk);
		p.delete()
		return redirect("pac_index")
	else:
		pk = request.GET.get('pk')
		p = get_object_or_404(PlanAnualCompras, pk=pk);
		return render(request, 'plan_anual_compras/pac_eliminar.html', {'object': p})


class PartidaCreate(CreateView):
	model = Partida
	form_class = PartidaForm
	template_name='plan_anual_compras/partida_nuevo.html'
	success_url='/financiero/plan_anual_compras/editar'

	def get_context_data(self, **kwargs):
		context = super(PartidaCreate,self).get_context_data(**kwargs)
		pk=self.kwargs.get('pk',0)
		context['pac_id']=pk
		return context

	def post(self, request,*args,**kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			pac_id=kwargs['pk']
			p = form.save(commit=False)
			p.pac_id = pac_id
			p.save()
			return HttpResponseRedirect(self.get_success_url()+'/'+str(pac_id))
		else:
			return self.render_to_response(self.get_context_data(form=form))


class PartidaUpdate(UpdateView):
	model = Partida
	form_class = PartidaForm
	template_name = 'plan_anual_compras/partida_nuevo.html'
	success_url = '/financiero/plan_anual_compras/editar'

	def get_context_data(self, **kwargs):
		context = super(PartidaUpdate,self).get_context_data(**kwargs)
		fk=self.kwargs.get('fk',0)
		context['pace_id']=fk
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		pac_id = kwargs['fk']
		pk = kwargs['pk']
		partida = self.model.objects.get(id=pk)
		form = self.form_class(request.POST, instance=partida)
		if form.is_valid():
			p=form.save(commit=False)
			p.pac_id = pac_id
			p.save()
			return HttpResponseRedirect(self.get_success_url()+'/'+str(pac_id))
		else:
			return self.render_to_response(self.get_context_data(form=form))


class PartidaDelete(DeleteView):
	model = Partida
	form_class = PartidaForm
	template_name = 'plan_anual_compras/partida_eliminar.html'
	success_url = '/financiero/plan_anual_compras/editar'

	def get_context_data(self, **kwargs):
		context = super(PartidaDelete,self).get_context_data(**kwargs)
		fk = self.kwargs.get('fk',0)
		context['pac_id'] = fk
		return context

	def post(self, request, *args, **kwargs):
		pac_id = kwargs['fk']
		self.object=self.get_object()
		self.object.delete()
		return HttpResponseRedirect(self.get_success_url()+'/'+str(pac_id))


