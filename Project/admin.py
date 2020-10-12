# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Project
from Campaign.models import Campaign
from World.models import Universe
from ItemList.models import Itemlist

class CampaignInline(admin.TabularInline):
	model = Campaign
	extra = 0

class UniverseInline(admin.TabularInline):
	model = Universe
	extra = 0
	
class ItemlistInline(admin.TabularInline):
	model = Itemlist
	extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	inlines = [CampaignInline, UniverseInline, ItemlistInline, ]
