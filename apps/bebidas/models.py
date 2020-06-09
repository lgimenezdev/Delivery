# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class gaseosa(models.Model):
	id_gaseosa		=	models.AutoField(primary_key=True)
	nombre			=	models.CharField("Nombre", max_length=20)
	marca 			=	models.CharField("Marca", max_length=10)
	presentacion	=	models.CharField(max_length=20, choices=[
	('500cc', '500 CC'),
	('1L', '1 Litro'),
	('1,5Lts', '1,5 Litros'),
	('2Lts', '2 Litros'),
	('2,25Lts', '2,25 Litros'),
	],
	)

	def __str__(self):
		gase="%s %s"%(self.nombre,self.presentacion)
		return gase

class aguamineral(models.Model):
	id_aguamineral	=	models.AutoField(primary_key=True)
	nombre			=	models.CharField("Nombre", max_length=20)
	marca 			=	models.CharField("Marca", max_length=10)
	presentacion	=	models.CharField(max_length=20, choices=[
	('500cc', '500 CC'),
	('1L', '1 Litro'),
	('1,5Lts', '1,5 Litros'),
	('2Lts', '2 Litros'),
	('2,25Lts', '2,25 Litros'),
	],
	)

	def __str__(self):
		aguamin="%s %s"%(self.nombre,self.presentacion)
		return aguamin

class aguasaborizada(models.Model):
	id_aguasaborizada	=	models.AutoField(primary_key=True)
	nombre				=	models.CharField("Nombre", max_length=20)
	marca 				=	models.CharField("Marca", max_length=10)
	presentacion		=	models.CharField(max_length=20, choices=[
	('500cc', '500 CC'),
	('1L', '1 Litro'),
	('1,5Lts', '1,5 Litros'),
	('2Lts', '2 Litros'),
	('2,25Lts', '2,25 Litros'),
	],
	)

	def __str__(self):
		aguasabor="%s %s"%(self.nombre,self.presentacion)
		return aguasabor
# Create your models here.
