# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from Dungeon.models import Dungeon, Roomset, Room
from accounts.models import CustomUser
from Project.models import Project
from World.models import Universe, Region, Area

class DungeonViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		area = Area.objects.create(name="Test Area", in_region=region)
		
		self.dungeon = Dungeon.objects.create(title="Test Dungeon", in_area=area)
		
	def test_not_logged_in_redirects(self):
		response = self.client.get(self.dungeon.get_absolute_url())
		self.assertEqual(response.status_code, 302)
	
	def test_logged_in_and_dungeon_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.dungeon.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_dungeon_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_area = Area.objects.create(name="Second Test Area", in_region=second_region)
		second_dungeon = Dungeon.objects.create(title="Second Test Dungeon", in_area=second_area)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(second_dungeon.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
class RoomsetViewTests(TestCase):
	def setUp(self):	
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		area = Area.objects.create(name="Test Area", in_region=region)
		dungeon = Dungeon.objects.create(title="Test Dungeon", in_area=area)
		
		self.roomset = Roomset.objects.create(name="Test Roomset", in_dungeon=dungeon)
		
	def test_not_logged_in_redirects(self):
		response = self.client.get(self.roomset.get_absolute_url())
		self.assertEqual(response.status_code, 302)
	
	def test_logged_in_and_roomset_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.roomset.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_roomset_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_area = Area.objects.create(name="Second Test Area", in_region=second_region)
		second_dungeon = Dungeon.objects.create(title="Second Test Dungeon", in_area=second_area)
		second_roomset = Roomset.objects.create(name="Second Test Roomset", in_dungeon=second_dungeon)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(second_roomset.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
class RoomViewTests(TestCase):
	def setUp(self):	
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		area = Area.objects.create(name="Test Area", in_region=region)
		dungeon = Dungeon.objects.create(title="Test Dungeon", in_area=area)
		roomset = Roomset.objects.create(name="Test Roomset", in_dungeon=dungeon)
		
		self.room = Room.objects.create(name="Test Room", room_number=1, in_roomset=roomset)
		
	def test_not_logged_in_redirects(self):
		response = self.client.get(self.room.get_absolute_url())
		self.assertEqual(response.status_code, 302)
	
	def test_logged_in_and_roomset_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.room.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
	def test_room_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_area = Area.objects.create(name="Second Test Area", in_region=second_region)
		second_dungeon = Dungeon.objects.create(title="Second Test Dungeon", in_area=second_area)
		second_roomset = Roomset.objects.create(name="Second Test Roomset", in_dungeon=second_dungeon)
		second_room = Room.objects.create(name="Second Test Room", room_number=1, in_roomset=second_roomset)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(second_room.get_absolute_url())
		self.assertEqual(response.status_code, 403)
