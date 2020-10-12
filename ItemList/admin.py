# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Item, Itemlist

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	pass

@admin.register(Itemlist)
class ItemlistAdmin(admin.ModelAdmin):
	pass
