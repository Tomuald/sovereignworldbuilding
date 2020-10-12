# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

@admin.register(Dungeon)
class DungeonAdmin(admin.ModelAdmin):
	pass
	
@admin.register(Roomset)
class RoomsetAdmin(admin.ModelAdmin):
	pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
	pass
	
@admin.register(RoomLoot)
class RoomLootAdmin(admin.ModelAdmin):
	pass
