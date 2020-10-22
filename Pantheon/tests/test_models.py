# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from Pantheon.models import Pantheon, God
from World.models import Universe
from Project.models import Project
from accounts.models import CustomUser


class PantheonModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="Test User", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.pantheon = Pantheon.objects.create(name="Test Pantheon", in_universe=universe)
	
	def test_pantheon_get_absolute_url(self):
		self.assertEqual(self.pantheon.get_absolute_url(), reverse('pantheon-detail', args=[str(self.pantheon.id)]))

class GodModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="Test User", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		pantheon = Pantheon.objects.create(name="Test Pantheon", in_universe=universe)
		
		self.god = God.objects.create(name="Test God", in_pantheon=pantheon)

	def test_god_get_absolute_url(self):
		self.assertEqual(self.god.get_absolute_url(), reverse('god-detail', args=[str(self.god.id)]))
		
