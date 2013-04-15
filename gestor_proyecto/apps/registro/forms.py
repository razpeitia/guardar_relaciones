from django.forms import ModelForm
from django import forms
from django.forms.models import inlineformset_factory
from gestor_proyecto.apps.registro.models import InfoBasica, Localizacion, calendario, fechas

class InfoBasicaForm(forms.ModelForm):
    class Meta:
        model = InfoBasica
        widgets = {
        	'nombre' : forms.TextInput(attrs={'class':'input-xxlarge', 'required':''}),
        	'codigo' : forms.TextInput(attrs={'class':'input-xxlarge', 'required':''}),
        	'entidad': forms.TextInput(attrs={'class':'input-xxlarge', 'required':''}),
  
        }


class LocalizacionForm(forms.ModelForm):
    class Meta:
        model = Localizacion
        widgets = {
        	'localidad' : forms.TextInput(attrs={'class':'input-xxlarge', 'required':''}),
        	'municipio' : forms.TextInput(attrs={'class':'input-xxlarge', 'required':''}),
  
        }
        exclude = ('infobasica',)

class calendarioForm(forms.ModelForm):
    class Meta:
        model = calendario
        widgets = {
            'inicio' : forms.TextInput(attrs={ 'type':'date', 'class':'input-medium', 'required':''}),
            'fin' : forms.TextInput(attrs={ 'type':'date', 'class':'input-medium', 'required':''}),
        }
        exclude = ('infobasica',)

FechasFormSet = inlineformset_factory(calendario, fechas, extra=2, can_delete=False)


