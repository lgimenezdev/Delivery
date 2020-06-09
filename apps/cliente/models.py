# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#-------Creación del Modelo Cliente-------
class cliente(models.Model):
	id_cliente 	= models.AutoField(primary_key=True)
	nombreyapellido	=	models.CharField(max_length=30)
	direccion	=	models.CharField(max_length=50)
	localidad	=	models.CharField(max_length=30)
	telefono	=	models.CharField(max_length=13)
	email 	=	models.EmailField(max_length=20, blank=True)
#-------Retorna el nombre ----------
	def __unicode__(self):
		cliente="%s %s"%(self.id_cliente,self.nombreyapellido)
		return cliente
