# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser

from django.db import models
from Project.models import Project

class CustomUser(AbstractUser):
	user_library = models.ManyToManyField(Project, blank=True)
	
	def __str__(self):
		return self.username
