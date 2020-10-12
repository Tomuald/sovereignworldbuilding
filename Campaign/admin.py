# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

#################
# -- inlines -- #
#################

class QuestInline(admin.TabularInline):
	model = Quest
	exclude = ['involved_npcs']
	extra = 0
	
class QuestEncounterInline(admin.TabularInline):
	model = QuestEncounter
	extra = 0

class QuestEncounterLootInline(admin.TabularInline):
	model = QuestEncounterLoot
	extra = 0

#######################
# -- admin classes -- #
#######################

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
	pass
	
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
	inlines = [QuestInline, ]
	filter_horizontal = ('involved_npcs', 'regions', )

@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
	filter_horizontal = ('involved_npcs', )
	inlines = [QuestEncounterInline, ]

	
@admin.register(QuestEncounter)
class QuestEncounterAdmin(admin.ModelAdmin):
	inlines = [QuestEncounterLootInline, ]
	filter_horizontal = ('involved_npcs', )

@admin.register(QuestEncounterLoot)
class QuestEncounterLootAdmin(admin.ModelAdmin):
	pass
	

