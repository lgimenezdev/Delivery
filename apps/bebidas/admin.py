# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rudelivery.apps.bebidas.models import gaseosa, aguamineral, aguasaborizada

admin.site.register(gaseosa)
admin.site.register(aguamineral)
admin.site.register(aguasaborizada)

# Register your models here.
