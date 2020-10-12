# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pantheon, God

class GodInline(admin.TabularInline):
	model = God
	extra = 0

@admin.register(Pantheon)
class PantheonAdmin(admin.ModelAdmin):
	inlines = [GodInline, ]
	
@admin.register(God)
class GodAdmin(admin.ModelAdmin):
	pass
