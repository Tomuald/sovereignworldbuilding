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
		self.assertEqual(self.universe.get_absolute_url(),
						 reverse('universe-detail', args=[self.universe.in_project.id, self.universe.name])
					)
					
	def test_universe_get_absolute_url(self):
		self.assertEqual(self.universe.get_absolute_index_url(),
						 reverse('universe-index', args=[self.universe.in_project.id, self.universe.name])
					)

class RegionModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.region = Region.objects.create(name="Test Region", in_universe=universe, in_project=project)
	
	def test_region_get_absolute_url(self):
		self.assertEqual(self.region.get_absolute_url(),
						 reverse('region-detail', args=[self.region.in_project.id, self.region.name])
					)
		
class AreaModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe, in_project=project)
		
		self.area = Area.objects.create(name="Test Area", in_region=region, in_project=project)
	
	def test_area_get_absolute_url(self):
		self.assertEqual(self.area.get_absolute_url(), reverse('area-detail',
																args=[self.area.in_project.id, self.area.name])
															)

class CityModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe, in_project=project)
		
		self.city = City.objects.create(name="Test city", in_region=region, in_project=project)
	
	def test_city_get_absolute_url(self):
		self.assertEqual(self.city.get_absolute_url(), reverse('city-detail', args=[self.city.in_project.id, self.city.name]))
		
class CityQuarterModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe, in_project=project)
		city = City.objects.create(name="Test city", in_region=region, in_project=project)
		
		self.cityquarter = CityQuarter.objects.create(name="Test CityQuarter", in_city=city, in_project=project)
	
	def test_cityquarter_get_absolute_url(self):
		self.assertEqual(self.cityquarter.get_absolute_url(),
						 reverse('cityquarter-detail',
						 		  args=[self.cityquarter.in_project.id, self.cityquarter.name]
						 	)
					)
		
class LocationModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe, in_project=project)
		area = Area.objects.create(name="Test Area", in_region=region, in_project=project)
		city = City.objects.create(name="Test City", in_region=region, in_project=project)
		cityquarter = CityQuarter.objects.create(name="Test CityQuarter", in_city=city, in_project=project)
		
		self.area_location = Location.objects.create(name="Test Area Location", in_area=area, in_project=project)
		self.city_location = Location.objects.create(name="Test City Location", in_cityquarter=cityquarter, in_project=project)
	
	def test_location_get_absolute_url(self):
		self.assertEqual(self.area_location.get_absolute_url(),
						 reverse('location-detail', args=[self.area_location.in_project.id, self.area_location.name])
					)
		self.assertEqual(self.city_location.get_absolute_url(),
						 reverse('location-detail', args=[self.city_location.in_project.id, self.city_location.name])
					)
					
class WorldEncounterModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe, in_project=project)
		area = Area.objects.create(name="Test Area", in_region=region, in_project=project)
		location = Location.objects.create(name="Test Location", in_area=area, in_project=project)
		
		dungeon = Dungeon.objects.create(title="Test Dungeon", in_area=area, in_project=project)
		roomset = Roomset.objects.create(name="Test Roomset", in_dungeon=dungeon, in_project=project)
		room = Room.objects.create(name="Test Room", room_number=1, in_roomset=roomset, in_project=project)
		
		self.loc_worldencounter = WorldEncounter.objects.create(title="Test WorldEncounter", in_location=location, in_project=project)
		self.room_worldencounter = WorldEncounter.objects.create(title="Test WorldEncounter", in_dungeon_room=room, in_project=project)
	
	def test_worldencounter_get_absolute_url(self):
		self.assertEqual(self.loc_worldencounter.get_absolute_url(),
						 reverse('worldencounter-detail', args=[self.loc_worldencounter.in_project.id, self.loc_worldencounter.title])
					)
		self.assertEqual(self.room_worldencounter.get_absolute_url(),
						 reverse('worldencounter-detail', args=[self.room_worldencounter.in_project.id, self.room_worldencounter.title])
					)

					
class EmpireModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.empire = Empire.objects.create(name="Test Empire", in_universe=universe, in_project=project)
	
	def test_empire_get_absolute_url(self):
		self.assertEqual(self.empire.get_absolute_url(), reverse('empire-detail', args=[self.empire.in_project.id, self.empire.name]))
		
class FactionModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.faction = Faction.objects.create(name="Test Faction", in_universe=universe, in_project=project)
	
	def test_faction_get_absolute_url(self):
		self.assertEqual(self.faction.get_absolute_url(), reverse('faction-detail', args=[self.faction.in_project.id, self.faction.name]))
		
class NPCModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.npc = NPC.objects.create(name="Test NPC", in_universe=universe, in_project=project)
	
	def test_npc_get_absolute_url(self):
		self.assertEqual(self.npc.get_absolute_url(), reverse('npc-detail', args=[self.npc.in_project.id, self.npc.name]))			
