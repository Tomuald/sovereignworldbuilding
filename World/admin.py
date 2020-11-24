# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

###################
## -- inlines -- ##
###################

class NPCInline(admin.TabularInline):
	model = NPC
	extra = 0

class LocationInline(admin.TabularInline):
	model = Location
	extra = 0

class AreaInline(admin.TabularInline):
	model = Area
	extra = 0

class CityQuarterInline(admin.TabularInline):
	model = CityQuarter
	extra = 0

class CityInline(admin.TabularInline):
	model = City
	extra = 0

class LocationLootInline(admin.TabularInline):
	model = LocationLoot
	extra = 0
	
class RegionInline(admin.TabularInline):
	model = Region
	extra = 0

class CityDemographicsInline(admin.TabularInline):
	model = CityDemographics
	extra = 0

class WorldEncounterLootInline(admin.TabularInline):
	model = WorldEncounterLoot
	extra = 0

#########################
## -- admin classes -- ##
#########################

@admin.register(Universe)
class UniverseAdmin(admin.ModelAdmin):
	pass

@admin.register(Empire)
class EmpireAdmin(admin.ModelAdmin):
	filter_horizontal = ['faiths', ]

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
	inlines = [AreaInline, CityInline, ]

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
	inlines = [LocationInline, ]
	filter_horizontal = ['factions', ]
	
	fields = ('name', 'area_type', 'in_project', 'in_region', ('description', 'flavor_text'), 'factions')
	
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	inlines = [CityDemographicsInline, CityQuarterInline, ]

@admin.register(CityQuarter)
class CityQuarterAdmin(admin.ModelAdmin):
	pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	inlines = [LocationLootInline, ]
	filter_horizontal = ['NPCs', 'exit_points']

@admin.register(NPC)
class NPCAdmin(admin.ModelAdmin):
	filter_horizontal = ['faiths', ]

@admin.register(Faction)
class FactionAdmin(admin.ModelAdmin):
	inlines = [NPCInline, ]
	filter_horizontal = ['faiths', 'leaders', ]
	
@admin.register(CityDemographics)
class CityDemographics(admin.ModelAdmin):
	list_display = ['race', 'percent', ]
	
@admin.register(LocationLoot)
class LocationLootAdmin(admin.ModelAdmin):
	pass
	
@admin.register(WorldEncounter)
class WorldEncounterAdmin(admin.ModelAdmin):
	inlines = [WorldEncounterLootInline, ]
	
@admin.register(WorldEncounterLoot)
class WorldEncounterLootAdmin(admin.ModelAdmin):
	pass

