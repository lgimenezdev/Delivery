# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rudelivery.apps.comidas.models import menuentrada, menuprincipal, menuespecial

admin.site.register(menuentrada)
admin.site.register(menuprincipal)
admin.site.register(menuespecial)

# Register your models here.
