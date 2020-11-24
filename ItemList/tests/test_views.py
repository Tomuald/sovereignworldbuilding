# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from ItemList.models import Itemlist, Item
from Project.models import Project
from accounts.models import CustomUser

from ItemList.forms import ItemlistModelForm, ItemModelForm

class ItemlistViewTests(TestCase):
	def setUp(self):
		# Set up first user's itemlist
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		self.project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(self.project)
		self.itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=self.project)

		# Set up second user's itemlist
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		self.second_itemlist = Itemlist.objects.create(name="Second Test Itemlist", in_project=second_project)

	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.itemlist.get_absolute_url())
		self.assertEqual(response.status_code, 302)

	def test_detail_view_logged_in_and_itemlist_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.itemlist.get_absolute_url())
		self.assertEqual(response.status_code, 200)

	def test_detail_view_itemlist_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_itemlist.get_absolute_url())
		self.assertEqual(response.status_code, 403)

	def test_detail_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('itemlist-detail',
					args=[
						self.project.id,
						'bogus name'])
				)
		self.assertEqual(response.status_code, 404)

	# Form Tests
	def test_create_form_name_already_taken(self):
		in_project = self.project
		form = ItemlistModelForm(in_project,
				data={
					'name': self.itemlist.name,
					'in_project': self.itemlist.in_project
				})
		self.assertFalse(form.is_valid())

	# Create / Update View Tests
	def test_create_view_not_logged_in_redirects(self):
		response = self.client.get(
				reverse('itemlist-create',
					args=[self.itemlist.in_project.id])
				)
		self.assertEqual(response.status_code, 302)

	def test_create_view_itemlist_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('itemlist-create', args=[self.second_itemlist.in_project.id]))
		self.assertEqual(response.status_code, 403)

	def test_update_view_itemlist_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('itemlist-update', args=[self.second_itemlist.in_project.id, self.second_itemlist.id]))
		self.assertEqual(response.status_code, 403)

	def test_create_view_initial_data(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.post(
				reverse('itemlist-create',
					args=[
						self.itemlist.in_project.id,])
				)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(
				response.context['form'].initial['in_project'], self.project
			)

	def test_update_view_initial_data(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('itemlist-update',
					args=[
						self.itemlist.in_project.id,
						self.itemlist.name])
				)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(
				response.context['form'].initial['in_project'], self.project.id
			)

	def test_update_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('itemlist-update',
					args=[
						self.project.id,
						'bogus name'])
				)
		self.assertEqual(response.status_code, 404)

	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(self.itemlist.get_absolute_url())
		self.assertEqual(response.status_code, 302)

	def test_delete_view_logged_in_and_itemlist_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('itemlist-delete', args=[str(self.itemlist.in_project.id), str(self.itemlist.name)]))
		self.assertEqual(response.status_code, 200)

	def test_delete_view_itemlist_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('itemlist-delete', args=[str(self.second_itemlist.in_project.id), str(self.second_itemlist.name)]))
		self.assertEqual(response.status_code, 403)

	def test_delete_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('itemlist-delete',
					args=[
						self.project.id,
						'bogus name'])
				)
		self.assertEqual(response.status_code, 404)

class ItemViewTests(TestCase):
	def setUp(self):
		# Set up first user's item
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		self.project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(self.project)
		itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=self.project)
		self.item = Item.objects.create(name="Test Item", in_itemlist=itemlist, in_project=self.project)

		# Set up second user's item
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_itemlist = Itemlist.objects.create(name="Second Test Itemlist", in_project=second_project)
		self.second_item = Item.objects.create(name="Second Test Item", in_itemlist=second_itemlist, in_project=second_project)

	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.item.get_absolute_url())
		self.assertEqual(response.status_code, 302)

	def test_detail_view_logged_in_and_item_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.item.get_absolute_url())
		self.assertEqual(response.status_code, 200)

	def test_detail_view_item_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_item.get_absolute_url())
		self.assertEqual(response.status_code, 403)

	def test_detail_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('item-detail',
					args=[
						self.project.id,
						self.item.in_itemlist.name,
						'bogus name'])
				)
		self.assertEqual(response.status_code, 404)

	# Form Tests
	def test_create_form_name_already_taken(self):
		in_itemlist = self.item.in_itemlist
		form = ItemModelForm(in_itemlist,
				data={
					'name': self.item.name,
					'item_type': 'type',
					'item_cost': 'cost',
					'in_project': self.item.in_project,
					'in_itemlist': self.item.in_itemlist
				})
		self.assertFalse(form.is_valid())

	# Create and Update View Tests
	def test_create_view_initial_data(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.post(
				reverse('item-create',
					args=[
						self.item.in_project.id,
						self.item.in_itemlist.name,])
				)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(
				response.context['form'].initial['in_project'], self.project
			)
		self.assertEqual(response.context['form'].initial['in_itemlist'], self.item.in_itemlist)

	def test_update_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('item-update',
					args=[
						self.project.id,
						self.item.in_itemlist.name,
						'bogus name'])
				)
		self.assertEqual(response.status_code, 404)

	def test_create_view_item_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('item-create',
					args=[
						self.second_item.in_project.id,
						self.second_item.in_itemlist.name,])
				)
		self.assertEqual(response.status_code, 403)

	def test_update_view_item_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('item-update',
					args=[
						self.second_item.in_project.id,
						self.second_item.in_itemlist.name,
						self.second_item.name])
				)
		self.assertEqual(response.status_code, 403)

	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(
				reverse('item-delete',
					args=[str(self.item.in_project.id),
						  str(self.item.in_itemlist.name),
						  str(self.item.name)])
				)
		self.assertEqual(response.status_code, 302)

	def test_delete_view_logged_in_and_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('item-delete',
					args=[str(self.item.in_project.id),
						  str(self.item.in_itemlist.name),
						  str(self.item.name)])
				)
		self.assertEqual(response.status_code, 200)

	def test_delete_view_item_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('item-delete',
						args=[str(self.second_item.in_project.id),
							  str(self.second_item.in_itemlist.name),
							  str(self.second_item.name)])
				)
		self.assertEqual(response.status_code, 403)
