# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from ItemList.models import Item
from World.models import Area
from Project.models import Project

class Dungeon(models.Model):
	"""A dungeon is a collection of rooms of varying sizes. These rooms form
	Roomsets which are connected by Passageways. Roomsets are designed for
	encounters, while passageways represent a break in player interaction.
	Dungeons are basically well-defined locations."""

	title = models.CharField(max_length=125)
	landscape = models.URLField(max_length=255, blank=True, null=True, help_text="Provide a URL to an image file.")
	in_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
	in_area = models.ForeignKey(Area, on_delete=models.CASCADE)

	description = models.TextField(blank=True, null=True)


	def get_absolute_url(self):
		return reverse('dungeon-detail', args=[str(self.in_project.id), str(self.title)])

	def __str__(self):
		return self.title

class Roomset(models.Model):
	"""A Roomset is a series of adjacent rooms that share an aesthetic theme.
	Typically, a dungeon will have a few Roomsets, represented by levels of a
	dungeon, or different locales. These roomsets are interconnected by
	passageways linking room-to-room. Roomsets have maps."""

	name = models.CharField(max_length=75)
	in_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
	in_dungeon = models.ForeignKey(Dungeon, on_delete=models.CASCADE)

	description = models.TextField(blank=True, null=True)
	# map = 'path/to/file'

	def get_absolute_url(self):
		return reverse('roomset-detail', args=[str(self.in_project.id), str(self.name)])

	def __str__(self):
		return self.name

class Room(models.Model):
	"""A room typically contains grid-based encounters. This is the layer with
	which the players will interact, and therefore has flavor text."""

	name = models.CharField(max_length=75)
	room_number = models.IntegerField()
	in_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
	in_roomset = models.ForeignKey(Roomset, on_delete=models.CASCADE)
	exits = models.ManyToManyField('Room', blank=True)

	description = models.TextField(blank=True, null=True)

	flavor_text = models.TextField(blank=True, null=True)

	class Meta:
		ordering = ['in_roomset', 'room_number', ]

	def get_absolute_url(self):
		return reverse('room-detail', args=[str(self.in_project.id), str(self.name)])

	def __str__(self):
		return self.name

class RoomLoot(models.Model):
	name = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	in_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
	in_room = models.ForeignKey(Room, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Room Loot"

	def __str__(self):
		return self.name.name
