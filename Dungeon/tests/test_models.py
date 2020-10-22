# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from Dungeon.models import Dungeon, Roomset, Room
from accounts.models import CustomUser
from Project.models import Project
from World.models import Universe, Region, Area

class DungeonModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		area = Area.objects.create(name="Test Area", in_region=region)
		self.dungeon = Dungeon.objects.create(title="Test Dungeon", in_area=area)
		
	def test_dungeon_get_absolute_url(self):
		self.assertEqual(self.dungeon.get_absolute_url(), reverse('dungeon-detail', args=[self.dungeon.id]))
		
class RoomsetModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		area = Area.objects.create(name="Test Area", in_region=region)
		dungeon = Dungeon.objects.create(title="Test Dungeon", in_area=area)
		
		self.roomset = Roomset.objects.create(name="Test Roomset", in_dungeon=dungeon)
	
	def test_roomset_get_absolute_url(self):
		self.assertEqual(self.roomset.get_absolute_url(), reverse('roomset-detail', args=[str(self.roomset.id)]))
		
class RoomModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		area = Area.objects.create(name="Test Area", in_region=region)
		dungeon = Dungeon.objects.create(title="Test Dungeon", in_area=area)
		roomset = Roomset.objects.create(name="Test Roomset", in_dungeon=dungeon)
		
		self.room = Room.objects.create(name="Test Room", room_number=1, in_roomset=roomset)
		
	def test_room_get_absolute_url(self):
		self.assertEqual(self.room.get_absolute_url(), reverse('room-detail', args=[str(self.room.id)]))
