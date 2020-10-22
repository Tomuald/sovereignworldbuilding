# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

from Project.models import Project
from accounts.models import CustomUser

class WebpagesTest(TestCase):
	def setUp(self):
		self.client = Client()
	
	# Change test when homepage is created.
	def test_homepage(self):
		response = self.client.get('/')
		
		self.assertEqual(response.status_code, 404)
	
	# 302 is a redirect
	def test_worldbuilder_page_without_login(self):
		response = self.client.get('/worldbuilder/')
		
		self.assertEqual(response.status_code, 302)
	
	# Change test when homepage is created.
	def test_community_tool_page(self):
		response = self.client.get('/thelodge/')
		
		self.assertEqual(response.status_code, 404)
	
	def test_login_page(self):
		response = self.client.get('/accounts/login/')
		
		self.assertEqual(response.status_code, 200)
	
	def test_signup_page(self):
		response = self.client.get('/accounts/signup/')
		
		self.assertEqual(response.status_code, 200)
	
	# 302 is a redirect
	def test_logout_page(self):
		response = self.client.get('/accounts/logout/')
		
		self.assertEqual(response.status_code, 302)

