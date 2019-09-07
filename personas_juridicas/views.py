from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Juridica
from . import forms

from django.core.paginator import Paginator
# Create your views here.
def index(request):
	juridicas_list = Juridica.objects.all().order_by("id")

	filter = forms.JuridicaFilter(request.GET, queryset=juridicas_list )
	#form = forms.JuridicaForm()
	paginator = Paginator(filter.qs, 30) 

	page = request.GET.get('page')
	juridicas = paginator.get_page(page)
	return render(request, 'personas_juridicas/index.html', {'juridicas': juridicas, "filter":filter})
	#items_per_page=10;
	#elements = (Juridica.objects.order_by("id")[(page-1)*items_per_page:items_per_page*page])
	#return render(request,"personas_juridicas/index.html", {"page":page,"elements":elements})
	
def load_ciudades(request):
	d={'Guayas': ['Guayaquil', 'Durán', 'Milagro', 'Daule', 'Samborondó', 'Velasco Ibarra', 
	'El Triunfo', 'Playas', 'Balzar', 'Naranjito', 'Naranjal', 'Pedro Carbo', 'Yaguachi',
	 'Lomas de Sargentillo', 'Salitre', 'Balao', 'Santa Lucía', 'Palestina', 
	 'Alfredo Baquerizo Moreno (Jujan)', 'Nobol', 'Simón Bolívar', 
	 'Cnel. Marcelino Maridueña', 'Colimes', 'Gral. Antonio Elizalde (Bucay)'
	 , 'Isidro Ayora'], 'Pichincha': ['Quito', 'Sangolquí', 'Cayambe', 'Machachi', 
	 'Tabacundo', 'Pedro Vicente Maldonado', 'San Miguel de Los Bancos', 'Puerto Quito'], 
	 'Azuay': ['Cuenca', 'Gualaceo', 'Paute', 'Santa Isabel', 'Camilo Ponce Enríquez', 
	 'Chordeleg', 'Girón', 'Sígsig', 'San Fernando', 'Nabón', 'Guachapala', 'Pucará', 'Oña',
	  'Sevilla de Oro', 'El Pan'], 'Santo Domingo de los Tsáchilas': ['Santo Domingo', 
	  'La Concordia'], 'El Oro': ['Machala', 'Pasaje', 'Santa Rosa', 'Huaquillas', 
	  'El Guabo', 'Arenillas', 'Piñas', 'Zaruma', 'Portovelo', 'Balsas', 'Marcabelí', 
	  'Paccha', 'La Victoria', 'Chilla'], 'Manabí': ['Manta', 'Portoviejo', 'Chone', 
	  'El Carmen', 'Montecristi', 'Jipijapa', 'Pedernales', 'Bahía de Caráquez', 'Calceta', 
	  'Jaramijó', 'Tosagua', 'Puerto López', 'San Vicente', 'Santa Ana', 'Rocafuerte', 
	  'Pajá', 'Flavio', 'Jama', 'Junín', 'Pichincha', 'Sucre', 'Olmedo'], 
	  'Loja': ['Loja', 'Catamayo', 'Cariamanga', 'Macará', 'Catacocha', 'Alamor', 
	  'Celica', 'Saraguro', 'Zapotillo', 'Pindal', 'Amaluza', 'Gonzanamá', 'Chaguarpamba', 
	  'Sozoranga', 'Quilanga', 'Olmedo'], 'Tungurahua': ['Ambato', 'Baños de Agua Santa', 
	  'Pelileo', 'Píllaro', 'Quero', 'Cevallos', 'Patate', 'Tisaleo', 'Mocha'], 
	  'Esmeraldas': ['Esmeraldas', 'Quinindé', 'San Lorenzo', 'Atacames', 'Muisne', 
	  'Valdez (Limones)', 'Rioverde'], 'Los Ríos': ['Quevedo', 'Babahoyo', 'Buena Fe', 
	  'Ventanas', 'Vinces', 'Valencia', 'Montalvo', 'Mocache', 'Puebloviejo', 'Palenque',
	   'Catarama', 'Baba', 'Quinsaloma'], 'Chimborazo': ['Riobamba', 'Cumandá', 'Guano', 
	   'Alausí', 'Chambo', 'Chunchi', 'Pallatanga', 'Guamote', 'Villa La Unión (Cajabamba)', 
	   'Penipe'], 'Imbabura': ['Ibarra', 'Otavalo', 'Atuntaqui', 'Cotacachi', 'Pimampiro',
	    'Urcuquí'], 'Santa Elena': ['La Libertad', 'Santa Elena', 'Salinas'],
	     'Cotopaxi': ['Latacunga', 'La Maná', 'Salcedo', 'Pujilí', 'Saquisilí', 'Sigchos',
	     'El Corazón'], 'Carchi': ['Tulcá', 'San Gabriel', 'El Ángel', 'Huaca', 'Mira', 
	     'Bolívar'], 'Sucumbíos': ['Nueva Loja', 'Shushufindi',
	      'Puerto El Carmen de Putumayo', 'El Dorado de Cascales', 'Lumbaqui', 'Tarapoa', 
	      'La Bonita'], 'Orellana': ['Puerto Francisco de Orellana', 'La Joya de los Sachas',
	       'Loreto', 'Nuevo Rocafuerte', 'Tiputini'], 'Cañar': ['La Troncal', 'Azogues',
	        'Cañar', 'Biblián', 'El Tambo', 'Suscal', 'Déleg'], 'Pastaza': ['Puyo', 
	        'Santa Clara', 'Arajuno', 'Mera'], 'Bolívar': ['Guaranda', 'San Miguel', 'Caluma', 
	        'Echendí', 'Chimbo', 'Chillanes', 'Las Naves'], 'Napo': ['Tena', 'Archidona', 
	        'El Chaco', 'Baeza', 'Carlos Julio Arosemena Tola'], 'Morona Santiago': ['Macas',
	         'Sucúa', 'Gualaquiza', 'Gral. Leonidas Plaza Gutiérrez (Limón)', 'Palora',
	          'Santiago de Méndez', 'Logroño', 'San Juan Bosco', 'Santiago', 'Taisha',
	           'Huamboya', 'Pablo Sexto'], 'Zamora Chinchipe': ['Zamora', 'Yantzaza',
	           'Zumba', 'El Pangui', 'Zumbi', 'Palanda', 'Guayzimi', 'Yacuambi', 'Paquisha'],
	            'Galápagos': ['Puerto Ayora', 'Puerto Baquerizo Moreno', 'Puerto Villamil']}
	provincia = request.GET.get("provincia")
	return render(request,"personas_juridicas/dropdown_ciudades.html",{"ciudades":d[provincia]})

def juridicas_view(request):
	if(request.method == "POST"):
		form = forms.JuridicaForm(request.POST)
		if(form.is_valid()):
			form.save()
		return redirect("index")
	else:
		form = forms.JuridicaForm()
	return render(request,"personas_juridicas/forma.html", {"form":form})