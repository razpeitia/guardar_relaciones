from django.shortcuts import render_to_response, redirect, get_object_or_404 
from django.template import RequestContext
from gestor_proyecto.apps.registro.models import InfoBasica, Localizacion, calendario, fechas
from gestor_proyecto.apps.registro.forms import InfoBasicaForm, LocalizacionForm, calendarioForm, FechasFormSet
from datetime import datetime

def addregistro(request):
	if request.method == "POST":
		# print request.POST
		infobasica = InfoBasicaForm(request.POST)
		geopos = LocalizacionForm(request.POST)
		cale = calendarioForm(request.POST)
		formset = FechasFormSet(request.POST, prefix= 'fechas', instance=cale.instance)

		if infobasica.is_valid() and geopos.is_valid() and cale.is_valid() and formset.is_valid():
			# print "valido"
			# print infobasica.cleaned_data
			info = infobasica.save() # Guardo el primer formulario
			# Trabajando con el segundo form 
			cal = cale.save(commit=False)  
			cal.infobasica_id = info.id
			cal.save()
			formset.save()

			geo = geopos.save(commit=False) # creo una instancia del formulario que maneja lo ubucacion
			# print geo.cleaned_data
			geo.infobasica_id = info.id # meto el id del primer formulario al este formulario
			geo.save() # Guardo el formulario
			return redirect('/')
	else:	
		infobasica = InfoBasicaForm()
		geopos = LocalizacionForm()
		calendario = calendarioForm()
		formset = FechasFormSet()
	ctx = {'infobasica': infobasica, 'gp': geopos, 'cale': calendario, 'formset': formset }
	return render_to_response ('registro/index.html', ctx, context_instance=RequestContext(request))