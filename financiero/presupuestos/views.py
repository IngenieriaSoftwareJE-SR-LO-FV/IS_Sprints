from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
#from django.core import serializers
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer


from .models import *

from . import forms
from dal import autocomplete

from django.core.paginator import Paginator

class AulaAutocomplete(autocomplete.Select2QuerySetView):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def get_queryset(self):
		qs = Aula.objects.all().order_by("nombre")

		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)
		return qs

		
	def has_add_permission(self, request):
		return True

def index_presupuestos(request):
	presupuestos_list = PresupuestoEvento.objects.all().order_by("id")

	filter = forms.PresupuestoEventoFilter(request.GET, queryset=presupuestos_list )
	paginator = Paginator(filter.qs, 30) 

	page = request.GET.get('page')
	presupuestos = paginator.get_page(page)
	return render(request, 'presupuestos/index.html', {'presupuestos': presupuestos, "filter":filter})

	

def presupuestos_nuevo(request):
	if(request.method == "POST"):
		form = forms.PresupuestoEventoForm(request.POST)
		if(form.is_valid()):
			form.save()
			return redirect("index_presupuestos")
	else:
		form = forms.PresupuestoEventoForm()
		form_tarifario = forms.PresupuestoTarifario()
	return render(request,"presupuestos/forma.html", {"form":form,"form_tarifario":form_tarifario})

def presupuestos_editar(request,pk):
	if(request.method == "POST"):
		p = get_object_or_404(PresupuestoEvento, pk=pk)
		form = forms.PresupuestoEventoForm(request.POST,instance=p)
		if(form.is_valid()):
			form.save()
			return redirect("index_presupuestos")
	else:

		p = get_object_or_404(PresupuestoEvento, pk=pk)
		form = forms.PresupuestoEventoForm(instance=p,initial={'fecha': p.fecha})
		#form.fields["fecha"].value=None
	return render(request, 'presupuestos/forma.html', {'form': form})


def presupuestos_eliminar(request,pk=None):
	if(request.method == "POST"):
		p = get_object_or_404(PresupuestoEvento,pk=pk);
		p.delete()
		return redirect("index_presupuestos")
	else:

	
		pk= request.GET.get('pk')
		p = get_object_or_404(PresupuestoEvento,pk=pk);

		return render(request, 'presupuestos/eliminar.html', {'object': p})

def presupuestos_aprobar(request,pk):
	if(request.method == "POST"):
		p = get_object_or_404(PresupuestoEvento, pk=pk)
		form = forms.PresupuestoEventoForm(request.POST, instance=p)
		if(form.is_valid()):
			form.save()
			return redirect("pendiente_aprobacion")
	else:
		p = get_object_or_404(PresupuestoEvento, pk=pk)
		form = forms.PresupuestoEventoForm(instance=p,initial={'fecha': p.fecha});
	return render(request, 'presupuestos/aprobar.html', {'form': form})


class TarifarioHospedajeAlimentacionDocenteSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = TarifarioHospedajeAlimentacionDocente

class TarifarioDocenteSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = TarifarioDocente

class TarifarioHospedajeAlimentacionPersonalSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = TarifarioHospedajeAlimentacionPersonal

class TarifarioServicioAereoSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = TarifarioServicioAereo

class TarifarioInstalacionSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = TarifarioInstalacion

class TarifarioPlantillaDelPersonalSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = TarifarioPlantillaDelPersonal

class TarifarioMaterialSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = TarifarioMaterial

class TarifarioServicioAlimentacionSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = TarifarioServicioAlimentacion

class TarifarioPrecioSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = TarifarioPrecio

class TarifarioAportacionSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = TarifarioAportacion

class TarifarioProductoSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = TarifarioProducto

class TarifarioProspectoSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = TarifarioProspecto

class TarifarioPublicidadSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = TarifarioPublicidad

class TarifarioOtroSuministroSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = TarifarioOtroSuministro

class TarifarioSerializer(serializers.ModelSerializer):
	docente = TarifarioDocenteSerializer(many=True,read_only=True)
	hospedaje_alimentacion_docente = TarifarioHospedajeAlimentacionDocenteSerializer(many=True,read_only=True)
	hospedaje_alimentacion_personal = TarifarioHospedajeAlimentacionPersonalSerializer(many=True,read_only=True)
	servicios_aereos = TarifarioServicioAereoSerializer(many=True,read_only=True)
	instalaciones = TarifarioInstalacionSerializer(many=True,read_only=True)
	plantilla_del_personal = TarifarioPlantillaDelPersonalSerializer(many=True,read_only=True)
	materiales_del_evento = TarifarioMaterialSerializer(many=True,read_only=True)
	servicio_de_alimentacion = TarifarioServicioAlimentacionSerializer(many=True,read_only=True)
	precios = TarifarioPrecioSerializer(many=True,read_only=True)
	aportaciones = TarifarioAportacionSerializer(many=True,read_only=True)
	productos = TarifarioProductoSerializer(many=True,read_only=True)
	prospecto = TarifarioProspectoSerializer(many=True,read_only=True)
	publicidad = TarifarioPublicidadSerializer(many=True,read_only=True)
	otros_suministros = TarifarioOtroSuministroSerializer(many=True,read_only=True)

	class Meta:
		fields = '__all__'
		model = Tarifario

def load_tarifario(request):
	
	tarifario = Tarifario.objects.get(pk=1)
	data = TarifarioSerializer([tarifario], many=True).data
	return HttpResponse(JSONRenderer().render(data), content_type='application/json');
	#return HttpResponse(serializers.serialize("json", [tarifario]), content_type='application/json')
	