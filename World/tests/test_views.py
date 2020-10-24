# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from World.models import Universe, Region, Area, City, CityQuarter, Area, Location, WorldEncounter
from World.models import Empire, Faction, NPC
from accounts.models import CustomUser
from Project.models import Project
from Dungeon.models import Dungeon, Roomset, Room

class UniverseViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		
		self.universe = Universe.objects.create(name="Test Universe", in_project=project)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.universe.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/%d/" % self.universe.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.universe.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
class RegionViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.region = Region.objects.create(name="Test Region", in_universe=universe)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.region.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/region/%d/" % self.region.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.region.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
class AreaViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		
		self.area = Area.objects.create(name="Test Area", in_region=region)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.area.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/area/%d/" % self.area.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.area.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
class CityViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		
		self.city = City.objects.create(name="Test City", in_region=region)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.city.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/city/%d/" % self.city.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.city.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
class CityQuarterViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		city = City.objects.create(name="Test City", in_region=region)
		
		self.cityquarter = CityQuarter.objects.create(name="Test CityQuarter", in_city=city)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.cityquarter.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/cityquarter/%d/" % self.cityquarter.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.cityquarter.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
class LocationViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		area = Area.objects.create(name="Test Area", in_region=region)
		city = City.objects.create(name="Test City", in_region=region)
		cityquarter = CityQuarter.objects.create(name="Test CityQuarter", in_city=city)
		
		self.area_location = Location.objects.create(name="Test AreaLoc", in_area=area)
		self.cq_location = Location.objects.create(name="Test CQLoc", in_cityquarter=cityquarter)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.area_location.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/location/%d/" % self.area_location.id
		self.assertRedirects(response, expected_url)
		
		response = self.client.get(self.cq_location.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/location/%d/" % self.cq_location.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.area_location.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.cq_location.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
class EmpireViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.empire = Empire.objects.create(name="Test Empire", in_universe=universe)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.empire.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/empire/%d/" % self.empire.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.empire.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
class FactionViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.faction = Faction.objects.create(name="Test Faction", in_universe=universe)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.faction.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/faction/%d/" % self.faction.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.faction.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
class NPCViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.npc = NPC.objects.create(name="Test NPC", in_universe=universe)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.npc.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/npc/%d/" % self.npc.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.npc.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
class WorldEncounterViewTests(TestCase):
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
		
		self.loc_worldencounter = WorldEncounter.objects.create(title="", in_location=location)
		self.room_worldencounter = WorldEncounter.objects.create(title="", in_dungeon_room=room)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.loc_worldencounter.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/worldencounter/%d/" % self.loc_worldencounter.id
		self.assertRedirects(response, expected_url)
		
		response = self.client.get(self.room_worldencounter.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/worldencounter/%d/" % self.room_worldencounter.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.loc_worldencounter.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
		response = self.client.get(self.room_worldencounter.get_absolute_url())
		self.assertEqual(response.status_code, 200)
