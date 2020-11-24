# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class Project(models.Model):
	title = models.CharField(max_length=255)
	created_by = models.ForeignKey("accounts.CustomUser",
			on_delete=models.CASCADE
		)

	game_system = models.CharField(max_length=255,
			help_text="(e.g., Dungeons & Dragons 5th Edition, Shadowrun 20th Anniversary, ...", blank=True, null=True
		)

	def get_absolute_url(self):
		return reverse('project-detail', args=[str(self.id)])

	def __str__(self):
		return self.title
