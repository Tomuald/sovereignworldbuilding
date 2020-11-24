# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from Project.models import Project

class Itemlist(models.Model):
	name = models.CharField(max_length=255)
	in_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
	description = models.TextField(blank=True, null=True)

	def get_absolute_url(self):
		return reverse('itemlist-detail', args=[str(self.in_project.id), str(self.name)])

	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=125)
	in_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
	in_itemlist = models.ForeignKey(Itemlist, on_delete=models.CASCADE)

	item_type = models.CharField(max_length=255)
	item_cost = models.CharField(max_length=255)

	description = models.TextField(blank=True, null=True)

	class Meta:
		ordering = ['name', ]

	def get_absolute_url(self):
		return reverse('item-detail', args=[str(self.in_project.id), str(self.in_itemlist.name), str(self.name)])

	def __str__(self):
		return self.name
