# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from ItemList.models import Itemlist, Item
from Project.models import Project
from accounts.models import CustomUser 

class ItemlistViewTests(TestCase):
	def setUp(self):
		# Set up first user's itemlist
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		self.itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=project)
		
		# Set up second user's itemlist
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		self.second_itemlist = Itemlist.objects.create(name="Second Test Itemlist", in_project=second_project)
	
	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.itemlist.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = '/accounts/login/?next=/worldbuilder/itemlist/%d/' % self.itemlist.id
		self.assertRedirects(response, expected_url)
	
	def test_detail_view_logged_in_and_itemlist_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.itemlist.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_detail_view_itemlist_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_itemlist.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(self.itemlist.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = '/accounts/login/?next=/worldbuilder/itemlist/%d/' % self.itemlist.id
		self.assertRedirects(response, expected_url)
	
	def test_delete_view_logged_in_and_itemlist_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('itemlist-delete', args=[str(self.itemlist.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_itemlist_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('itemlist-delete', args=[str(self.second_itemlist.id)]))
		self.assertEqual(response.status_code, 403)
		
class ItemViewTests(TestCase):
	def setUp(self):
		# Set up first user's item
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=project)
		self.item = Item.objects.create(name="Test Item", in_itemlist=itemlist)
		
		# Set up second user's item
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_itemlist = Itemlist.objects.create(name="Second Test Itemlist", in_project=second_project)
		self.second_item = Item.objects.create(name="Second Test Item", in_itemlist=second_itemlist)
	
	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.item.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = '/accounts/login/?next=/worldbuilder/itemlist/item/%d/' % self.item.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_and_item_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.item.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_detail_view_item_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_item.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('item-delete', args=[str(self.item.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = '/accounts/login/?next=/worldbuilder/item/delete/%d/' % self.item.id
		self.assertRedirects(response, expected_url)
		
	def test_delete_view_logged_in_and_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('item-delete', args=[str(self.item.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_item_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('item-delete', args=[str(self.second_item.id)]))
		self.assertEqual(response.status_code, 403)
