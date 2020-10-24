# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from World.models import Universe, Region, Area, City, CityQuarter, Location, Empire, Faction, NPC, WorldEncounter
from accounts.models import CustomUser
from Project.models import Project
from Dungeon.models import Dungeon, Roomset, Room

class UniverseModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		
		self.universe = Universe.objects.create(name="Test Universe", in_project=project)
	
	def test_universe_get_absolute_url(self):
		self.assertEqual(self.universe.get_absolute_url(), reverse('universe-detail', args=[self.universe.id]))

class RegionModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.region = Region.objects.create(name="Test Region", in_universe=universe)
	
	def test_region_get_absolute_url(self):
		self.assertEqual(self.region.get_absolute_url(), reverse('region-detail', args=[self.region.id]))
		
class AreaModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		
		self.area = Area.objects.create(name="Test Area", in_region=region)
	
	def test_area_get_absolute_url(self):
		self.assertEqual(self.area.get_absolute_url(), reverse('area-detail', args=[self.area.id]))

class CityModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		
		self.city = City.objects.create(name="Test city", in_region=region)
	
	def test_city_get_absolute_url(self):
		self.assertEqual(self.city.get_absolute_url(), reverse('city-detail', args=[self.city.id]))
		
class CityQuarterModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		city = City.objects.create(name="Test city", in_region=region)
		
		self.cityquarter = CityQuarter.objects.create(name="Test CityQuarter", in_city=city)
	
	def test_cityquarter_get_absolute_url(self):
		self.assertEqual(self.cityquarter.get_absolute_url(),
						 reverse('cityquarter-detail', args=[self.cityquarter.id])
					)
		
class LocationModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		area = Area.objects.create(name="Test Area", in_region=region)
		city = City.objects.create(name="Test City", in_region=region)
		cityquarter = CityQuarter.objects.create(name="Test CityQuarter", in_city=city)
		
		self.area_location = Location.objects.create(name="Test Area Location", in_area=area)
		self.city_location = Location.objects.create(name="Test City Location", in_cityquarter=cityquarter)
	
	def test_location_get_absolute_url(self):
		self.assertEqual(self.area_location.get_absolute_url(),
						 reverse('location-detail', args=[self.area_location.id])
					)
		self.assertEqual(self.city_location.get_absolute_url(),
						 reverse('location-detail', args=[self.city_location.id])
					)
					
class EmpireModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.empire = Empire.objects.create(name="Test Empire", in_universe=universe)
	
	def test_empire_get_absolute_url(self):
		self.assertEqual(self.empire.get_absolute_url(), reverse('empire-detail', args=[self.empire.id]))
		
class FactionModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.faction = Faction.objects.create(name="Test Faction", in_universe=universe)
	
	def test_faction_get_absolute_url(self):
		self.assertEqual(self.faction.get_absolute_url(), reverse('faction-detail', args=[self.faction.id]))
		
class NPCModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.npc = NPC.objects.create(name="Test NPC", in_universe=universe)
	
	def test_npc_get_absolute_url(self):
		self.assertEqual(self.npc.get_absolute_url(), reverse('npc-detail', args=[self.npc.id]))	
		
class WorldEncounterModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		area = Area.objects.create(name="Test Area", in_region=region)
		location = Location.objects.create(name="Test Location", in_area=area)
		
		dungeon = Dungeon.objects.create(title="Test Dungeon", in_area=area)
		roomset = Roomset.objects.create(name="Test Roomset", in_dungeon=dungeon)
		room = Room.objects.create(name="Test Room", room_number=1, in_roomset=roomset)
		
		self.loc_worldencounter = WorldEncounter.objects.create(title="Test WorldEncounter", in_location=location)
		self.room_worldencounter = WorldEncounter.objects.create(title="Test WorldEncounter", in_dungeon_room=room)
	
	def test_worldencounter_get_absolute_url(self):
		self.assertEqual(self.loc_worldencounter.get_absolute_url(),
						 reverse('worldencounter-detail', args=[self.loc_worldencounter.id])
					)
		self.assertEqual(self.room_worldencounter.get_absolute_url(),
						 reverse('worldencounter-detail', args=[self.room_worldencounter.id])
					)
		
