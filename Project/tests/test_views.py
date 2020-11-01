# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from Project.models import Project

class ProjectViewTests(TestCase):
	def setUp(self):
		# Set up first user's project
		self.user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		self.project = Project.objects.create(title="Test Project", created_by=self.user)
		self.user.user_library.add(self.project)
		
		# Set up second user's project
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		self.second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(self.second_project)
	
	# List View Tests	
	def test_list_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.project.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_list_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('project-list'))
		self.assertEqual(response.status_code, 302)
	
	def test_project_list_only_contains_user_projects(self):
		# Test if there is only one project in the first user's project list.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('project-list'))
		self.assertEqual(len(response.context['projects']), len(self.user.user_library.all()))
	
	# Detail View Tests
	def test_detail_view_logged_in_and_project_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.project.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.project.get_absolute_url())
		self.assertEqual(response.status_code, 302)
	
	def test_detail_view_project_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_project.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_logged_in_and_project_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('project-delete', args=[str(self.project.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(self.project.get_absolute_url())
		self.assertEqual(response.status_code, 302)
	
	def test_delete_view_project_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('project-delete', args=[str(self.second_project.id)]))
		self.assertEqual(response.status_code, 403)
