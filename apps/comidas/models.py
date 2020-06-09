# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class menuentrada(models.Model):
	id_menuentrada	=	models.AutoField(primary_key=True)
	nombre	=	models.CharField(max_length=50)
	observacion	=	models.TextField("Observación", max_length=70)
	importe	=	models.DecimalField("Importe $", max_digits=3, decimal_places=2)

	def __unicode__(self):
		return (self.nombre)

class menuprincipal(models.Model):
	id_menuprincipal	=	models.AutoField(primary_key=True)
	nombre	=	models.CharField(max_length=50)
	observacion	=	models.TextField("Observación", max_length=70)
	importe =	models.DecimalField("Importe $", max_digits=3, decimal_places=2)

	def __unicode__(self):
		return (self.nombre)

class menuespecial(models.Model):
	id_menuespecial	=	models.AutoField(primary_key=True)
	nombre	=	models.CharField(max_length=50)
	observacion	=	models.TextField("Observación", max_length=70)
	importe =	models.DecimalField("Importe $", max_digits=3, decimal_places=2)

	def __unicode__(self):
		return (self.nombre)

# Create your models here.
