# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from Project.models import Project

class Itemlist(models.Model):
	name = models.CharField(max_length=255)
	in_project = models.ForeignKey(Project, on_delete=models.CASCADE)
	description = models.TextField(blank=True, null=True)
	
	def get_absolute_url(self):
		return reverse('itemlist-detail', args=[str(self.id)])
	
	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=125)
	in_itemlist = models.ForeignKey(Itemlist, on_delete=models.CASCADE)
	
	item_type = models.CharField(max_length=255)
	item_cost = models.CharField(max_length=255)
	
	description = models.TextField(blank=True, null=True)
	
	class Meta:
		ordering = ['name', ]
	
	def get_absolute_url(self):
		return reverse('item-detail', args=[str(self.id)])
	
	def __str__(self):
		return self.name
