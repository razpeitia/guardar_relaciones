from django.forms import ModelForm
from django import forms
from gestor_proyecto.apps.registro.models import InfoBasica, Localizacion

class InfoBasicaForm(forms.ModelForm):
    class Meta:
        model = InfoBasica

class LocalizacionForm(forms.ModelForm):
    class Meta:
        model = Localizacion
        exclude = {'infobasica',}
    