# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from Pantheon.models import Pantheon, God
from Project.models import Project
from World.models import Universe

class PantheonViewTests(TestCase):
	def setUp(self):
		# Set up first user's pantheon
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		self.pantheon = Pantheon.objects.create(name="Test Pantheon", in_universe=universe)
		
		# Set up second user's pantheon
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		self.second_pantheon = Pantheon.objects.create(name="Second Test Pantheon", in_universe=second_universe)
		
	# Detail View Tests
	def test_detail_view_logged_in_and_pantheon_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.pantheon.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.pantheon.get_absolute_url())
		self.assertEqual(response.status_code, 302)
	
	def test_detail_view_pantheon_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_pantheon.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_logged_in_and_pantheon_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('pantheon-delete', args=[str(self.pantheon.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('pantheon-delete', args=[str(self.pantheon.id)]))
		self.assertEqual(response.status_code, 302)
	
	def test_delete_view_pantheon_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('pantheon-delete', args=[str(self.second_pantheon.id)]))
		self.assertEqual(response.status_code, 403)

class GodViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		pantheon = Pantheon.objects.create(name="Test Pantheon", in_universe=universe)
		self.god = God.objects.create(name="Test God", in_pantheon=pantheon)
		
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_pantheon = Pantheon.objects.create(name="Second Test Pantheon", in_universe=second_universe)
		self.second_god = God.objects.create(name="Second Test God", in_pantheon=second_pantheon)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.god.get_absolute_url())
		self.assertEqual(response.status_code, 302)
	
	def test_detail_view_logged_in_and_god_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.god.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_detail_view_pantheon_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_god.get_absolute_url())
		self.assertEqual(response.status_code, 403)

	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('god-delete', args=[str(self.god.id)]))
		self.assertEqual(response.status_code, 302)
	
	def test_delete_view_logged_in_and_god_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('god-delete', args=[str(self.god.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_pantheon_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('god-delete', args=[str(self.second_god.id)]))
		self.assertEqual(response.status_code, 403)		
