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
		self.user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		self.user.save()
		
		self.project = Project()
		self.project.title = "Test Project"
		self.project.created_by = self.user
		self.project.save()
	
	def test_project_get_absolute_url(self):
		self.assertEqual(self.project.get_absolute_url(), reverse('project-detail', args=[str(self.project.id)]))
		
class UserProjectsListViewTest(TestCase):
	def setUp(self):
		self.user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		self.project = Project.objects.create(title="Test Project", created_by=self.user)
		self.project.save()
		self.user.user_library.add(self.project)
		self.user.save()
	
	def test_logged_in_can_view(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('project-list'))
		self.assertEqual(response.status_code, 200)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(reverse('project-list'))
		self.assertEqual(response.status_code, 302)
	
	def test_project_list_ony_contains_user_projects(self):
		# Set up a second user, and have him create a project.
		second_user = CustomUser.objects.create_user(username="TestUser2", password="T3stP4ssword")
		second_project = Project.objects.create(title="Test Project 2", created_by=second_user)
		second_project.save()
		second_user.user_library.add(second_project)
		second_user.save()
		
		# Test if there is only one project in the first user's project list.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('project-list'))
		self.assertEqual(len(response.context['projects']), len(self.user.user_library.all()))
