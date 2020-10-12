# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

from ItemList.models import Item
from Pantheon.models import God
from Project.models import Project

class Universe(models.Model):
	name = models.CharField(max_length=125)
	in_project = models.OneToOneField(Project, on_delete=models.CASCADE)
	description = HTMLField(blank=True, null=True)
	
	def get_absolute_url(self):
		return reverse('universe-detail', args=[str(self.id)])
		
	def get_absolute_index_url(self):
		return reverse('universe-index', args=[str(self.id)])
	
	def __str__(self):
		return self.name
	

class Empire(models.Model):
	name = models.CharField(max_length=125)
	in_universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
	
	description = HTMLField(blank=True, null=True)
	
	regions = models.ManyToManyField('Region', blank=True)
	
	faiths = models.ManyToManyField(God, blank=True)
	
	def get_absolute_url(self):
		return reverse('empire-detail', args=[str(self.id)])
	
	def __str__(self):
		return self.name

class Region(models.Model):
	name = models.CharField(max_length=125)
	landscape = models.URLField(max_length=255, blank=True, null=True,
					help_text="Provide a URL to an image file. Preferably, to the actual file, and not a link to a search engine.")
	
	in_universe = models.ForeignKey(Universe, on_delete=models.CASCADE, blank=True, null=True)
	
	BIOMES = (
		('Dr', 'Dry'),
		('Tr', 'Tropical'),
		('Te', 'Temperate'),
		('Co', 'Continental'),
		('Po', 'Polar'),
	)
	biome = models.CharField(max_length=2, choices=BIOMES, blank=True, null=True)
	
	description = HTMLField(blank=True, null=True)
	
	def get_absolute_url(self):
		return reverse('region-detail', args=[str(self.id)])
	
	def __str__(self):
		return self.name

class Area(models.Model):
	name = models.CharField(max_length=125)
	landscape = models.URLField(max_length=255, blank=True, null=True,
					help_text="Provide a URL to an image file. Preferably, to the actual file, and not a link to a search engine.")

	area_type = models.CharField(max_length=255, blank=True, null=True)
	
	in_region = models.ForeignKey(Region, on_delete=models.CASCADE)
	
	factions = models.ManyToManyField('Faction', blank=True)
	
	description = HTMLField(blank=True, null=True)
	flavor_text = models.TextField(blank=True, null=True)
	
	def get_absolute_url(self):
		return reverse('area-detail', args=[str(self.id)])
	
	def __str__(self):
		return self.name
	
class City(models.Model):
	name = models.CharField(max_length=125)
	landscape = models.URLField(max_length=255, blank=True, null=True,
					help_text="Provide a URL to an image file. Preferably, to the actual file, and not a link to a search engine.")
	
	in_region = models.ForeignKey(Region, on_delete=models.CASCADE)
	population = models.CharField(max_length=10, blank=True, null=True)

	description = HTMLField(blank=True, null=True)
	flavor_text = models.TextField(blank=True, null=True)
	
	class Meta:
		verbose_name_plural = "Cities"
	
	def get_absolute_url(self):
		return reverse('city-detail', args=[str(self.id)])
	
	def __str__(self):
		return self.name

class CityQuarter(models.Model):
	name = models.CharField(max_length=125)
	in_city = models.ForeignKey(City, on_delete=models.CASCADE)
	
	factions = models.ManyToManyField('Faction', blank=True)
	
	description = HTMLField(blank=True, null=True)
	flavor_text = models.TextField(blank=True, null=True)
	
	class Meta:
		verbose_name_plural = 'City Quarters'
		
	def get_absolute_url(self):
		return reverse('cityquarter-detail', args=[str(self.id)])
		
	def __str__(self):
		return self.name

class Location(models.Model):
	name = models.CharField(max_length=125)
	landscape = models.URLField(max_length=255, blank=True, null=True,
					help_text="URL to an image file. The better the resolution, the longer the loading time.")
	
	location_type = models.CharField(max_length=125, blank=True, null=True)
	
	in_area = models.ForeignKey(Area, on_delete=models.CASCADE, blank=True, null=True)
	in_cityquarter = models.ForeignKey(CityQuarter, on_delete=models.CASCADE, blank=True, null=True)
	
	description = HTMLField(blank=True, null=True)
	flavor_text = models.TextField(blank=True, null=True)
	
	NPCs = models.ManyToManyField('NPC', blank=True)
	
	exit_points = models.ManyToManyField('Location', blank=True)
	
	def get_absolute_url(self):
		return reverse('location-detail', args=[str(self.id)])
	
	def __str__(self):
		return self.name

class LocationLoot(models.Model):
	name = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	in_location = models.ForeignKey(Location, on_delete=models.CASCADE)
	
	class Meta:
		verbose_name_plural = "Location Loot"
	
	def __str__(self):
		return self.name.name
	
class NPC(models.Model):
	name = models.CharField(max_length=125)
	in_universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
	in_faction = models.ForeignKey('Faction', on_delete=models.CASCADE, blank=True, null=True)
	portrait = models.URLField(max_length=255, blank=True, null=True,
				help_text="Provide a URL to an image file. Preferably, to the actual file, and not a link to a search engine.")
	
	ALIGNMENTS = (
		('LG', 'Lawful/Good'),
		('NG', 'Neutral/Good'),
		('CG', 'Chaotic/Good'),
		('LN', 'Lawful/Neutral'),
		('N', 'True Neutral'),
		('CN', 'Chaotic/Neutral'),
		('LE', 'Lawful/Evil'),
		('NE', 'Neutral/Evil'),
		('CE', 'Chaotic/Evil'),
	)
	
	alignment = models.CharField(max_length=2, choices=ALIGNMENTS, blank=True, null=True)
	faiths = models.ManyToManyField(God, blank=True)
	
	description = HTMLField(blank=True, null=True)
	
	def get_absolute_url(self):
		return reverse('npc-detail', args=[str(self.id)])
	
	def __str__(self):
		return self.name

class Faction(models.Model):
	name = models.CharField(max_length=125)
	in_universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
	faction_role = models.CharField(max_length=255, blank=True, null=True)
	
	ALIGNMENTS = (
		('LG', 'Lawful/Good'),
		('NG', 'Neutral/Good'),
		('CG', 'Chaotic/Good'),
		('LN', 'Lawful/Neutral'),
		('N', 'True Neutral'),
		('CN', 'Chaotic/Neutral'),
		('CE', 'Chaotic/Evil'),
		('NE', 'Neutral/Evil'),
		('LE', 'Lawful/Evil'),
	)
	
	alignment = models.CharField(max_length=2, choices=ALIGNMENTS, blank=True, null=True)
	faiths = models.ManyToManyField(God, blank=True)
	
	description = HTMLField(blank=True, null=True)
	leaders = models.ManyToManyField(NPC, blank=True)
	
	def get_absolute_url(self):
		return reverse('faction-detail', args=[str(self.id)])
	
	def __str__(self):
		return self.name
		

class Demographics(models.Model):
	race = models.CharField(max_length=125)
	percent = models.IntegerField()
	
	class Meta:
		abstract = True

class CityDemographics(Demographics):
	in_city = models.ForeignKey(City, on_delete=models.CASCADE)
	
	class Meta:
		ordering = ('-percent', )
		verbose_name_plural = 'City Demographics'
	
	def __str__(self):
		return self.race


class WorldEncounter(models.Model):
	title = models.CharField(max_length=125)
	encounter_num = models.IntegerField(blank=True, null=True)
	
	in_location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
	in_dungeon_room = models.ForeignKey('Dungeon.Room', on_delete=models.CASCADE, blank=True, null=True)
	
	ENCOUNTER_TYPES = (
		('gbe', 'Grid-based'),
		('totme', 'Theater-of-the-Mind'),
		('lbe', 'Lore-based'),
	)
	encounter_type = models.CharField(max_length=5, choices=ENCOUNTER_TYPES, blank=True, null=True)
	
	dramatic_question = models.CharField(max_length=255, blank=True, null=True)
	summary = HTMLField(blank=True, null=True)
	flavor_text = models.TextField(blank=True, null=True)
	
	involved_npcs = models.ManyToManyField(NPC, blank=True)
	
	class Meta:
		ordering = ['encounter_num']
	
	def get_absolute_url(self):
		return reverse('worldencounter-detail', args=[str(self.id)])
	
	def __str__(self):
		return self.title

class WorldEncounterLoot(models.Model):
	name = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	in_worldencounter = models.ForeignKey(WorldEncounter, on_delete=models.CASCADE)
	
	class Meta:
		verbose_name_plural = "World Encounter Loot"
	
	def __str__(self):
		return self.name.name
