# -*- encoding: utf-8 *
from django.db import models

class InfoBasica(models.Model):
	nombre = models.CharField('Nombre del Proyecto', max_length=100)
	codigo = models.CharField('Código Proyecto', max_length=50)
	entidad = models.CharField('Entidad - Dependencia', max_length=50)
	jefe = models.CharField('Titular - Jefe', max_length=50)
	plan = models.CharField('Plan - Programa', max_length=50)
	eje = models.CharField('Eje rector', max_length=50)
	estrategia = models.CharField('Estrategia', max_length=50)
	compromiso = models.IntegerField('Número de compromiso')
	idea = models.CharField('Idea', max_length=50)
	perfil = models.CharField('Perfil', max_length=50)
	prefactibilidad = models.CharField('Prefactibilidad', max_length=50)
	factibilidad = models.CharField('Factibilidad', max_length=50)
	disenio = models.CharField('Diseño', max_length=50)
	ejecucion = models.CharField('Ejecución', max_length=50)
	pejecutivo = models.CharField('Proyecto Ejecutivo', max_length=50)
	costo_beneficio = models.CharField('Evaluación Costo-Beneficio', max_length=50)
	impacto_ambiental = models.CharField('Manifiesto de Impacto Ambiental', max_length=50)
	situacion_problematica = models.TextField('Situación Actual y Problematica')
	objetivo = models.TextField('Objetivo')
	justificacion = models.TextField('Justificacion')
	descripcion = models.TextField('Descripcion')
	beneficios = models.TextField('Beneficios esperados')
	prioridad = models.CharField('Prioridad para el Estado, Localidad o region', max_length=50)
	estrategico = models.CharField('Estrategico para el estado', max_length=50)
	beneficio_social = models.CharField('De beneficio social', max_length=50)
	numpersonas = models.IntegerField('Numero de personas que demandan')
	numatender = models.IntegerField('Numero que se va a atender')
	descripcion_personas = models.TextField('Descripcion de las personas')
	inversionistas = models.TextField('Inversionistas')
	socios = models.TextField('Socios')
	permisos = models.TextField('Permisos')
	financiamiento = models.TextField('Financiamiento')
	comer = models.TextField('Comercializacion')
	ga = models.TextField('Gestion Administrativa')
	incentivos = models.TextField('Incentivos')
	estudios = models.TextField('Estudios')
	antep = models.TextField('Anteproyecto')
	otros = models.TextField('Otros')
	impacto = models.TextField('Impacto')
	empleo = models.TextField('Empleo')
	arraigo = models.TextField('Arraigo')
	apode = models.TextField('Apoderamiento')
	deecono = models.TextField('Derrama Economica')
	creecono = models.TextField('Crecimiento Economico')
	ecade = models.TextField('Encadenamiento Productivo')
	infra = models.TextField('Desarrollo de Infraestructura p/region')
	otrosprio = models.TextField('Otros')
	
	class Meta:
		db_table = "InfoBasica"

	def __unicode__(self):
		return self.nombre
    
class Localizacion(models.Model):
	# infobasica = models.ForeignKey(InfoBasica)
	infobasica = models.OneToOneField(InfoBasica)
	localidad = models.CharField('Localidad:', max_length=50)
	municipio = models.CharField('Municipio:', max_length=50)
    
	class Meta:
		db_table = "Localizacion"
	
	def __unicode__(self):
		return self.localidad


class calendario(models.Model):
	infobasica = models.OneToOneField(InfoBasica)
	inicio = models.DateField()
	fin = models.DateField()

	class Meta:
		db_table = "Calendario"

class fechas(models.Model):
	cale = models.ForeignKey(calendario)    
	anio_inversion = models.DateTimeField()
	monto_inv = models.IntegerField()
	class Meta:
		db_table = "Fechas"
    


