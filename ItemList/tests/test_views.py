# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from ItemList.models import Itemlist, Item
from Project.models import Project
from accounts.models import CustomUser 

class ItemlistDetailViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		self.itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=project)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(self.itemlist.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = '/accounts/login/?next=/worldbuilder/itemlist/%d/' % self.itemlist.id
		self.assertRedirects(response, expected_url)
	
	def test_logged_in_and_itemlist_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.itemlist.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_itemlist_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_itemlist = Itemlist.objects.create(name="Second Test Itemlist", in_project=second_project)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(second_project.get_absolute_url())
		self.assertEqual(response.status_code, 403)

class ItemlistDeleteViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		self.itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=project)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(self.itemlist.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = '/accounts/login/?next=/worldbuilder/itemlist/%d/' % self.itemlist.id
		self.assertRedirects(response, expected_url)
	
	def test_logged_in_and_itemlist_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('itemlist-delete', args=[str(self.itemlist.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_itemlist_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_itemlist = Itemlist.objects.create(name="Second Test Itemlist", in_project=second_project)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('itemlist-delete', args=[str(second_itemlist.id)]))
		self.assertEqual(response.status_code, 403)
		
class ItemDetailViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=project)
		self.item = Item.objects.create(name="Test Item", in_itemlist=itemlist)
		
	def test_not_logged_in_redirects(self):
		response = self.client.get(self.item.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = '/accounts/login/?next=/worldbuilder/itemlist/item/%d/' % self.item.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_item_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.item.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_item_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_itemlist = Itemlist.objects.create(name="Second Test Itemlist", in_project=second_project)
		second_item = Item.objects.create(name="Second Test Item", in_itemlist=second_itemlist)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(second_item.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
class ItemDeleteViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=project)
		self.item = Item.objects.create(name="Test Item", in_itemlist=itemlist)
		
	def test_not_logged_in_redirects(self):
		response = self.client.get(reverse('item-delete', args=[self.item.id]))
		self.assertEqual(response.status_code, 302)
		expected_url = '/accounts/login/?next=/worldbuilder/item/delete/%d/' % self.item.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('item-delete', args=[self.item.id]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_item_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_itemlist = Itemlist.objects.create(name="Second Test Itemlist", in_project=second_project)
		second_item = Item.objects.create(name="Second Test Item", in_itemlist=second_itemlist)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('item-delete', args=[second_item.id]))
		self.assertEqual(response.status_code, 403)
