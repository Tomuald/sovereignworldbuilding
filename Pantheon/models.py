# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from Project.models import Project

class Pantheon(models.Model):
	name = models.CharField(max_length=125)
	in_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
	in_universe = models.ForeignKey('World.Universe', on_delete=models.CASCADE)

	background = models.TextField(blank=True, null=True)

	def get_absolute_url(self):
		return reverse('pantheon-detail', args=[str(self.in_project.id), str(self.name)])

	class Meta:
		ordering = ['name', ]

	def __str__(self):
		return self.name

class God(models.Model):
	name = models.CharField(max_length=125)
	alternative_names = models.CharField(max_length=255, blank=True, null=True)

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
	in_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
	in_pantheon = models.ForeignKey(Pantheon, on_delete=models.CASCADE)

	background = models.TextField(blank=True, null=True)

	class Meta:
		ordering = ['name', ]

	def get_absolute_url(self):
		return reverse('god-detail', args=[str(self.in_project.id), str(self.name)])

	def __str__(self):
		return self.name
