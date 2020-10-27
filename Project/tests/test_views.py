# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from Project.models import Project


class ProjectsListViewTests(TestCase):
	def setUp(self):
		self.user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		self.project = Project.objects.create(title="Test Project", created_by=self.user)
		self.user.user_library.add(self.project)
	
	def test_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.project.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(reverse('project-list'))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/"
		self.assertRedirects(response, expected_url)
	
	def test_project_list_ony_contains_user_projects(self):
		# Set up a second user, and have him create a project.
		second_user = CustomUser.objects.create_user(username="TestUser2", password="T3stP4ssword")
		second_project = Project.objects.create(title="Test Project 2", created_by=second_user)
		second_user.user_library.add(second_project)
		
		# Test if there is only one project in the first user's project list.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('project-list'))
		self.assertEqual(len(response.context['projects']), len(self.user.user_library.all()))

class ProjectDetailViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		self.project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(self.project)
	
	def test_logged_in_and_project_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.project.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(self.project.get_absolute_url())
		self.assertEqual(response.status_code, 302)
	
	def test_project_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(second_project.get_absolute_url())
		self.assertEqual(response.status_code, 403)

