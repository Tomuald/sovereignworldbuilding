# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from ItemList.models import Itemlist, Item
from Project.models import Project
from accounts.models import CustomUser 

class ItemlistViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		self.itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=project)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.itemlist.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = '/accounts/login/?next=/worldbuilder/itemlist/%d/' % self.itemlist.id
		self.assertRedirects(response, expected_url)
	
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.itemlist.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
class ItemViewTests(TestCase):
	def setUp(self):
		self.user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=self.user)
		self.itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=project)
		self.item = Item.objects.create(name="Test Item", in_itemlist=self.itemlist)
		
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.item.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = '/accounts/login/?next=/worldbuilder/itemlist/item/%d/' % self.item.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.item.get_absolute_url())
		self.assertEqual(response.status_code, 200)
