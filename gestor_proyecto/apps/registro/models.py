# -*- encoding: utf-8 *
from django.db import models

class InfoBasica(models.Model):
	nombre = models.CharField('Nombre del Proyecto:', max_length=100)
	codigo = models.CharField('Código Proyecto:', max_length=50)
	entidad = models.CharField('Entidad - Dependencia:', max_length=50)
	jefe = models.CharField('Titular - Jefe:', max_length=50)
	plan = models.CharField('Plan - Programa:', max_length=50)
	eje = models.CharField('Eje rector:', max_length=50)
	estrategia = models.CharField('Estrategia ', max_length=50)
	compromiso = models.IntegerField('Número de compromiso')

	class Meta:
		db_table = "InfoBasica"

	def __unicode__(self):
		return self.nombre
    
class Localizacion(models.Model):
	infobasica = models.ForeignKey(InfoBasica)
	localidad = models.CharField('Localidad:', max_length=50)
	municipio = models.CharField('Municipio:', max_length=50)
    
	class Meta:
		db_table = "Localizacion"
	
	def __unicode__(self):
		return self.localidad
    