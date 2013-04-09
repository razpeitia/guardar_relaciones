from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('gestor_proyecto.apps.registro.views',
	url(r'^$', 'addregistro', name = 'addregistro'),
)
