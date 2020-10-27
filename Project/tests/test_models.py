# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from Project.models import Project

from Project.forms import ProjectModelForm

class ProjectModelTest(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		
		self.project = Project.objects.create(title="Test Project", created_by=user)
	
	def test_project_get_absolute_url(self):
		self.assertEqual(self.project.get_absolute_url(), reverse('project-detail', args=[str(self.project.id)]))

