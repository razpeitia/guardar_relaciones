from django.shortcuts import render_to_response
from django.template import RequestContext
from gestor_proyecto.apps.registro.models import InfoBasica, Localizacion
from gestor_proyecto.apps.registro.forms import InfoBasicaForm, LocalizacionForm

def addregistro(request):
	if request.method == "POST":
		infobasica = InfoBasicaForm(request.POST)
		geopos = LocalizacionForm(request.POST)
		if infobasica.is_valid() and geopos.is_valid():
			info = infobasica.save() # Guardo el primer formulario
			geo = geopos.save(commit=False) # creo una instancia del 2do formulario
			geo.infobasica_id = info.id # meto el id del primer formulario al segundo formulario
			geo.save() # Guardo el 2do formulario
	else:	
		infobasica = InfoBasicaForm()
		geopos = LocalizacionForm()
	ctx = {'infobasica': infobasica, 'gp': geopos}
	return render_to_response ('registro/index.html', ctx, context_instance=RequestContext(request))