# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from Dungeon.models import Dungeon, Roomset, Room, RoomLoot
from accounts.models import CustomUser
from Project.models import Project
from World.models import Universe, Region, Area
from ItemList.models import Itemlist, Item

class DungeonViewTests(TestCase):
	def setUp(self):
		# Set up first user's dungeon
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe, in_project=project)
		area = Area.objects.create(name="Test Area", in_region=region, in_project=project)

		self.dungeon = Dungeon.objects.create(title="Test Dungeon", in_area=area, in_project=project)

		# Set up second user's dungeon
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe, in_project=second_project)
		second_area = Area.objects.create(name="Second Test Area", in_region=second_region, in_project=second_project)
		self.second_dungeon = Dungeon.objects.create(title="Second Test Dungeon", in_area=second_area, in_project=second_project)

	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.dungeon.get_absolute_url())
		self.assertEqual(response.status_code, 302)

	def test_detail_view_logged_in_and_dungeon_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.dungeon.get_absolute_url())
		self.assertEqual(response.status_code, 200)

	def test_detail_view_dungeon_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_dungeon.get_absolute_url())
		self.assertEqual(response.status_code, 403)

	# Create and Update View Tests
	def test_create_view_dungeon_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('dungeon-create',
					args=[
						self.second_dungeon.in_project.id,
						self.second_dungeon.in_area.name
					])
		)
		self.assertEqual(response.status_code, 403)

	def test_update_view_dungeon_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('dungeon-update',
					args=[
						self.second_dungeon.in_project.id,
						self.second_dungeon.title
					])
		)
		self.assertEqual(response.status_code, 403)

	def test_update_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('dungeon-update',
					args=[
						self.dungeon.in_project.id,
						'bogus title'
					])
		)
		self.assertEqual(response.status_code, 404)

	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(
				reverse('dungeon-delete',
					args=[
						str(self.dungeon.in_project.id),
						str(self.dungeon.title)])
				)
		self.assertEqual(response.status_code, 302)

	def test_delete_view_logged_in_and_dungeon_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('dungeon-delete',
					args=[
						str(self.dungeon.in_project.id),
						str(self.dungeon.title)])
				)
		self.assertEqual(response.status_code, 200)

	def test_delete_view_dungeon_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('dungeon-delete',
					args=[
						str(self.second_dungeon.in_project.id),
						str(self.second_dungeon.title)])
				)
		self.assertEqual(response.status_code, 403)

	def test_delete_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('dungeon-delete',
					args=[
						self.dungeon.in_project.id,
						'bogus title'
					])
		)
		self.assertEqual(response.status_code, 404)

class RoomsetViewTests(TestCase):
	def setUp(self):
		# Set up first user's roomset
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe, in_project=project)
		area = Area.objects.create(name="Test Area", in_region=region, in_project=project)
		dungeon = Dungeon.objects.create(title="Test Dungeon", in_area=area, in_project=project)

		self.roomset = Roomset.objects.create(name="Test Roomset", in_dungeon=dungeon, in_project=project)

		# Set up second user's roomset
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe, in_project=second_project)
		second_area = Area.objects.create(name="Second Test Area", in_region=second_region, in_project=second_project)
		second_dungeon = Dungeon.objects.create(title="Second Test Dungeon", in_area=second_area, in_project=second_project)
		self.second_roomset = Roomset.objects.create(name="Second Test Roomset", in_dungeon=second_dungeon, in_project=second_project)

	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.roomset.get_absolute_url())
		self.assertEqual(response.status_code, 302)

	def test_detail_view_logged_in_and_roomset_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.roomset.get_absolute_url())
		self.assertEqual(response.status_code, 200)

	def test_detail_view_roomset_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_roomset.get_absolute_url())
		self.assertEqual(response.status_code, 403)

	# Create and Update View Tests
	def test_create_view_roomset_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('roomset-create',
					args=[
						self.second_roomset.in_project.id,
						self.second_roomset.in_dungeon.title
					]))
		self.assertEqual(response.status_code, 403)

	def test_update_view_roomset_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('roomset-update',
					args=[
						self.second_roomset.in_project.id,
						self.second_roomset.name
					]))
		self.assertEqual(response.status_code, 403)

	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(
				reverse('roomset-delete',
					args=[
						str(self.roomset.in_project.id),
						str(self.roomset.name)])
				)
		self.assertEqual(response.status_code, 302)

	def test_delete_view_logged_in_and_roomset_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('roomset-delete',
					args=[
						str(self.roomset.in_project.id),
						str(self.roomset.name)])
				)
		self.assertEqual(response.status_code, 200)

	def test_delete_view_roomset_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('roomset-delete',
					args=[
						str(self.second_roomset.in_project.id),
						str(self.second_roomset.name)])
				)
		self.assertEqual(response.status_code, 403)

class RoomViewTests(TestCase):
	def setUp(self):
		# Set up first user's room
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe, in_project=project)
		area = Area.objects.create(name="Test Area", in_region=region, in_project=project)
		dungeon = Dungeon.objects.create(title="Test Dungeon", in_area=area, in_project=project)
		roomset = Roomset.objects.create(name="Test Roomset", in_dungeon=dungeon, in_project=project)

		self.room = Room.objects.create(name="Test Room", room_number=1, in_roomset=roomset, in_project=project)

		# Set up second user's room
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe, in_project=second_project)
		second_area = Area.objects.create(name="Second Test Area", in_region=second_region, in_project=second_project)
		second_dungeon = Dungeon.objects.create(title="Second Test Dungeon", in_area=second_area, in_project=second_project)
		second_roomset = Roomset.objects.create(name="Second Test Roomset", in_dungeon=second_dungeon, in_project=second_project)
		self.second_room = Room.objects.create(name="Second Test Room", room_number=1, in_roomset=second_roomset, in_project=second_project)

	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.room.get_absolute_url())
		self.assertEqual(response.status_code, 302)

	def test_logged_in_and_roomset_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.room.get_absolute_url())
		self.assertEqual(response.status_code, 200)

	def test_room_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_room.get_absolute_url())
		self.assertEqual(response.status_code, 403)

	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(
				reverse('room-delete',
					args=[
						str(self.room.in_project.id),
						str(self.room.name)])
				)
		self.assertEqual(response.status_code, 302)

	def test_delete_view_logged_in_and_roomset_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('room-delete',
					args=[
						str(self.room.in_project.id),
						str(self.room.name)])
				)
		self.assertEqual(response.status_code, 200)

	def test_delete_view_room_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('room-delete',
					args=[
						str(self.second_room.in_project.id),
						str(self.second_room.name)])
				)
		self.assertEqual(response.status_code, 403)

class RoomlootViewTests(TestCase):
	def setUp(self):
		# Set up first user's roomloot
		user = CustomUser.objects.create_user(
				username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(
				name="Test Universe", in_project=project)
		region = Region.objects.create(
				name="Test Region",
				in_universe=universe,
				in_project=project
				)
		area = Area.objects.create(
				name="Test Area",
				in_region=region,
				in_project=project
				)
		dungeon = Dungeon.objects.create(
				title="Test Dungeon",
				in_area=area,
				in_project=project,
				)
		roomset = Roomset.objects.create(
				name="Test Roomset",
				in_dungeon=dungeon,
				in_project=project
				)
		itemlist = Itemlist.objects.create(
				name="Test ItemList",
				in_project=project
				)
		item = Item.objects.create(
				name="Test Item",
				in_itemlist=itemlist,
				in_project=project
				)

		room = Room.objects.create(
				name="Test Room",
				room_number=1,
				in_roomset=roomset,
				in_project=project
				)
		self.roomloot = RoomLoot.objects.create(
				name=item,
				quantity=1,
				in_project=project,
				in_room=room
			)

		# Set up second user's roomloot
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(
				title="Second Test Project",
				created_by=second_user
				)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(
				name="Second Test Universe",
				in_project=second_project)
		second_region = Region.objects.create(
				name="Second Test Region",
				in_universe=second_universe,
				in_project=second_project
				)
		second_area = Area.objects.create(
				name="Second Test Area",
				in_region=second_region,
				in_project=second_project,
				)
		second_dungeon = Dungeon.objects.create(
				title="Second Test Dungeon",
				in_area=second_area,
				in_project=second_project
				)
		second_roomset = Roomset.objects.create(
				name="Second Test Roomset",
				in_dungeon=second_dungeon,
				in_project=second_project
				)
		second_room = Room.objects.create(
				name="Second Test Room",
				room_number=1,
				in_roomset=second_roomset,
				in_project=second_project)
		self.second_roomloot = RoomLoot.objects.create(
				name=item,
				quantity=1,
				in_project=second_project,
				in_room=second_room
			)

	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(
				reverse('roomloot-delete',
					args=[
						str(self.roomloot.in_project.id),
						str(self.roomloot.id)])
				)
		self.assertEqual(response.status_code, 302)

	def test_delete_view_logged_in_and_roomset_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('roomloot-delete',
					args=[
						str(self.roomloot.in_project.id),
						str(self.roomloot.id)])
				)
		self.assertEqual(response.status_code, 200)

	def test_delete_view_roomloot_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('roomloot-delete',
					args=[
						str(self.second_roomloot.in_project.id),
						str(self.second_roomloot.id)])
				)
		self.assertEqual(response.status_code, 403)
