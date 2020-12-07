# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from ItemList.models import Item
from World.models import Location, NPC, Region, Area, City
from Dungeon.models import Room
from World.models import Universe
from Project.models import Project

class Campaign(models.Model):
	title = models.CharField(max_length=125)
	in_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
	in_universe = models.ForeignKey(Universe, on_delete=models.SET_NULL, blank=True, null=True)

	overview = models.TextField(blank=True, null=True)

	def get_absolute_url(self):
		return reverse('campaign-detail', args=[str(self.in_project.id), str(self.title)])

	def get_absolute_index_url(self):
		return reverse('campaign-index', args=[str(self.in_project.id), str(self.title)])

	def __str__(self):
		return self.title

class Chapter(models.Model):
	title = models.CharField(max_length=125)
	in_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
	in_campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
	chapter_num = models.IntegerField()

	summary = models.TextField(blank=True, null=True)

	involved_npcs = models.ManyToManyField(NPC, blank=True, related_name="involvednpcs")

	regions = models.ManyToManyField(Region, blank=True)

	class Meta:
		ordering = ['chapter_num', ]

	def get_absolute_url(self):
		return reverse('chapter-detail', args=[str(self.in_project.id), str(self.title)])

	def __str__(self):
		return self.title

class Quest(models.Model):
	title = models.CharField(max_length=255)
	in_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

	QUEST_TYPES = (
		('mq', 'Main Quest'),
		('sq', 'Side Quest'),
	)

	quest_type = models.CharField(max_length=2, choices=QUEST_TYPES)
	quest_num = models.IntegerField()

	in_chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
	in_areas = models.ManyToManyField(Area, blank=True)
	in_cities = models.ManyToManyField(City, blank=True)

	summary = models.TextField(blank=True, null=True)

	involved_npcs = models.ManyToManyField(NPC, blank=True)

	class Meta:
		ordering = ['quest_num', ]

	def get_absolute_url(self):
		return reverse('quest-detail', args=[str(self.in_project.id), str(self.title)])

	def __str__(self):
		return self.title

class QuestEncounter(models.Model):
	title = models.CharField(max_length=125)
	in_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
	in_quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
	encounter_num = models.IntegerField(blank=True, null=True)
	in_location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
	in_dungeon_room = models.ForeignKey(Room, on_delete=models.SET_NULL, blank=True, null=True)

	ENCOUNTER_TYPES = (
		('gbe', 'Grid-based'),
		('totme', 'Theater-of-the-Mind'),
		('lbe', 'Lore-based'),
	)
	encounter_type = models.CharField(max_length=5, choices=ENCOUNTER_TYPES, blank=True, null=True)

	dramatic_question = models.CharField(max_length=255, blank=True, null=True)
	summary = models.TextField(blank=True, null=True)
	flavor_text = models.TextField(max_length=2500, blank=True, null=True)

	involved_npcs = models.ManyToManyField(NPC, blank=True)

	class Meta:
		ordering = ['encounter_num']

	def get_absolute_url(self):
		return reverse('questencounter-detail', args=[str(self.in_project.id), str(self.title)])

	def __str__(self):
		return self.title

class QuestEncounterLoot(models.Model):
	name = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	in_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
	in_questencounter = models.ForeignKey(QuestEncounter, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Quest Encounter Loot"
		order_with_respect_to = 'name'

	def __str__(self):
		return self.name.name
