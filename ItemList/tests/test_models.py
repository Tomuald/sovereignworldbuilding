# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from ItemList.models import Itemlist, Item
from Project.models import Project
from accounts.models import CustomUser

class ItemlistModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		self.itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=project)
	
	def test_itemlist_get_absolute_url(self):
		self.assertEqual(self.itemlist.get_absolute_url(), reverse('itemlist-detail', args=[str(self.itemlist.id)]))
		
class ItemModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=project)
		self.item = Item.objects.create(name="Test Item", in_itemlist=itemlist)
	
	def test_item_get_absolute_url(self):
		self.assertEqual(self.item.get_absolute_url(), reverse('item-detail', args=[str(self.item.id)]))
