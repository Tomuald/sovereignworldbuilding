# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from World.models import Universe, Region, Area, City, CityQuarter, Area, Location, WorldEncounter, WorldEncounterLoot
from World.models import Empire, Faction, NPC
from accounts.models import CustomUser
from Project.models import Project
from Dungeon.models import Dungeon, Roomset, Room

from ItemList.models import Itemlist, Item
# 694+ lines
class UniverseViewTests(TestCase):
	def setUp(self):
		# Set up first user's universe
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		self.universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		# Set up second user's universe
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		self.second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
	
	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.universe.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		
	def test_detail_view_logged_in_universe_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.universe.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_detail_view_universe_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_universe.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('universe-delete', args=[str(self.universe.id)]))
		self.assertEqual(response.status_code, 302)
		
	def test_delete_view_logged_in_universe_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('universe-delete', args=[str(self.universe.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_universe_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('universe-delete', args=[str(self.second_universe.id)]))
		self.assertEqual(response.status_code, 403)
		
class RegionViewTests(TestCase):
	def setUp(self):
		# Set up first user's region
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		self.region = Region.objects.create(name="Test Region", in_universe=universe)
		
		# Set up second user's region
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		self.second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
	
	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.region.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		
	def test_detail_view_logged_in_and_region_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.region.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
	def test_detail_view_region_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_region.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('region-delete', args=[str(self.region.id)]))
		self.assertEqual(response.status_code, 302)
		
	def test_delete_view_logged_in_and_region_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('region-delete', args=[str(self.region.id)]))
		self.assertEqual(response.status_code, 200)
		
	def test_delete_View_region_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('region-delete', args=[str(self.second_region.id)]))
		self.assertEqual(response.status_code, 403)

class AreaViewTests(TestCase):
	def setUp(self):
		# Set up first user's area
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		self.area = Area.objects.create(name="Test Area", in_region=region)
		
		# Set up second user's area
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		self.second_area = Area.objects.create(name="Second Test Area", in_region=second_region)
	
	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.area.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		
	def test_detail_view_logged_in_and_area_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.area.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
	def test_detail_view_area_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_area.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('area-delete', args=[str(self.area.id)]))
		self.assertEqual(response.status_code, 302)
		
	def test_delete_view_logged_in_and_area_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('area-delete', args=[str(self.area.id)]))
		self.assertEqual(response.status_code, 200)
		
	def test_delete_view_area_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('area-delete', args=[str(self.second_area.id)]))
		self.assertEqual(response.status_code, 403)
		
class CityViewTests(TestCase):
	def setUp(self):
		# Set up first user's city
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		self.city = City.objects.create(name="Test City", in_region=region)
		
		# Set up second user's city
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		self.second_city = City.objects.create(name="Second Test City", in_region=second_region)
	
	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.city.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		
	def test_detail_view_logged_in_and_city_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.city.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
	def test_detail_view_city_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_city.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('city-delete', args=[str(self.city.id)]))
		self.assertEqual(response.status_code, 302)
		
	def test_delete_view_logged_in_and_city_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('city-delete', args=[str(self.city.id)]))
		self.assertEqual(response.status_code, 200)
		
	def test_delete_view_city_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('city-delete', args=[str(self.second_city.id)]))
		self.assertEqual(response.status_code, 403)
		
class CityQuarterViewTests(TestCase):
	def setUp(self):
		# Set up first user's cityquarter
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		city = City.objects.create(name="Test City", in_region=region)
		self.cityquarter = CityQuarter.objects.create(name="Test CityQuarter", in_city=city)
		
		# Set up second user's cityquarter
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_city = City.objects.create(name="Second Test City", in_region=second_region)
		self.second_cityquarter = CityQuarter.objects.create(name="Second Test CQ", in_city=second_city)
	
	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.cityquarter.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		
	def test_detail_view_logged_in_and_cityquarter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.cityquarter.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
	def test_detail_view_cityquarter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_cityquarter.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('cityquarter-delete', args=[str(self.cityquarter.id)]))
		self.assertEqual(response.status_code, 302)
		
	def test_delete_view_logged_in_and_cityquarter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('cityquarter-delete', args=[str(self.cityquarter.id)]))
		self.assertEqual(response.status_code, 200)
		
	def test_delete_view_cityquarter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('cityquarter-delete', args=[str(self.second_cityquarter.id)]))
		self.assertEqual(response.status_code, 403)
		
class LocationViewTests(TestCase):
	def setUp(self):
		# Set up first user's locations
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		area = Area.objects.create(name="Test Area", in_region=region)
		city = City.objects.create(name="Test City", in_region=region)
		cityquarter = CityQuarter.objects.create(name="Test CityQuarter", in_city=city)
		self.area_location = Location.objects.create(name="Test AreaLoc", in_area=area)
		self.cq_location = Location.objects.create(name="Test CQLoc", in_cityquarter=cityquarter)
		
		# Set up second user's locations
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_area = Area.objects.create(name="Second Test Area", in_region=second_region)
		second_city = City.objects.create(name="Second Test City", in_region=second_region)
		second_cityquarter = CityQuarter.objects.create(name="Second Test CQ", in_city=second_city)
		self.second_area_loc = Location.objects.create(name="Second Test Location", in_area=second_area)
		self.second_cq_loc = Location.objects.create(name="Second Test Location", in_cityquarter=second_cityquarter)
	
	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		# Test for an Area Location
		response = self.client.get(self.area_location.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		
		# Test for an CityQuarter Location
		response = self.client.get(self.cq_location.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		
	def test_detail_view_logged_in_and_location_in_user_library_renders(self):
		# Test for Area Location.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.area_location.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
		# Test for CityQuarter Location.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.cq_location.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_detail_view_location_not_in_user_library_view_forbidden(self):
		# Test for Area Location.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_area_loc.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
		# Test for CityQuarter Location
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_cq_loc.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		# Test for an Area Location
		response = self.client.get(reverse('location-delete', args=[str(self.area_location.id)]))
		self.assertEqual(response.status_code, 302)
		
		# Test for an CityQuarter Location
		response = self.client.get(reverse('location-delete', args=[str(self.cq_location.id)]))
		self.assertEqual(response.status_code, 302)
		
	def test_delete_view_logged_in_and_location_in_user_library_renders(self):
		# Test for Area Location.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('location-delete', args=[str(self.area_location.id)]))
		self.assertEqual(response.status_code, 200)
		
		# Test for CityQuarter Location.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('location-delete', args=[str(self.cq_location.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_location_not_in_user_library_view_forbidden(self):
		# Test for Area Location.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('location-delete', args=[str(self.second_area_loc.id)]))
		self.assertEqual(response.status_code, 403)
		
		# Test for CityQuarter Location
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('location-delete', args=[str(self.second_cq_loc.id)]))
		self.assertEqual(response.status_code, 403)
		
class EmpireViewTests(TestCase):
	def setUp(self):
		# Set up first user's empire
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		self.empire = Empire.objects.create(name="Test Empire", in_universe=universe)
		
		# Set up second user's empire
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		self.second_empire = Empire.objects.create(name="Second Test Empire", in_universe=second_universe)
	
	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.empire.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		
	def test_detail_view_logged_in_and_empire_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.empire.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_detail_view_empire_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_empire.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('empire-delete', args=[str(self.empire.id)]))
		self.assertEqual(response.status_code, 302)
		
	def test_delete_view_logged_in_and_empire_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('empire-delete', args=[str(self.empire.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_empire_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('empire-delete', args=[str(self.second_empire.id)]))
		self.assertEqual(response.status_code, 403)
		
class FactionViewTests(TestCase):
	def setUp(self):
		# Set up first user's faction
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		self.faction = Faction.objects.create(name="Test Faction", in_universe=universe)
		
		# Set up second user's faction
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		self.second_faction = Faction.objects.create(name="Second Test Faction", in_universe=second_universe)
	
	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.faction.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		
	def test_detail_view_logged_in_and_faction_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.faction.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_detail_view_faction_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_faction.get_absolute_url())
		self.assertEqual(response.status_code, 403)

	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('faction-delete', args=[str(self.faction.id)]))
		self.assertEqual(response.status_code, 302)
		
	def test_delete_view_logged_in_and_faction_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('faction-delete', args=[str(self.faction.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_faction_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('faction-delete', args=[str(self.second_faction.id)]))
		self.assertEqual(response.status_code, 403)
		
class NPCViewTests(TestCase):
	def setUp(self):
		# Set up first user's npc
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		self.npc = NPC.objects.create(name="Test NPC", in_universe=universe)
		
		# Set up second user's npc
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		self.second_npc = NPC.objects.create(name="Second Test NPC", in_universe=second_universe)
	
	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.npc.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		
	def test_detail_view_logged_in_and_npc_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.npc.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_detail_view_npc_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_npc.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('npc-delete', args=[str(self.npc.id)]))
		self.assertEqual(response.status_code, 302)
		
	def test_delete_view_logged_in_and_npc_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('npc-delete', args=[str(self.npc.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_npc_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('npc-delete', args=[str(self.second_npc.id)]))
		self.assertEqual(response.status_code, 403)
		
class WorldEncounterViewTests(TestCase):
	def setUp(self):
		# Set up first user's encounters
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		area = Area.objects.create(name="Test Area", in_region=region)
		location = Location.objects.create(name="Test Location", in_area=area)
		dungeon = Dungeon.objects.create(title="Test Dungeon", in_area=area)
		roomset = Roomset.objects.create(name="Test Roomset", in_dungeon=dungeon)
		room = Room.objects.create(name="Test Room", room_number=1, in_roomset=roomset)
		self.loc_worldencounter = WorldEncounter.objects.create(title="", in_location=location)
		self.room_worldencounter = WorldEncounter.objects.create(title="", in_dungeon_room=room)
		
		city = City.objects.create(name="Test City", in_region=region)
		cityquarter = CityQuarter.objects.create(name="Test CityQuarter", in_city=city)
		cq_location = Location.objects.create(name="Test CQ Location", in_cityquarter=cityquarter)
		self.cq_worldencounter = WorldEncounter.objects.create(title="CQ Test WorldEncounter", in_location=cq_location)
		
		# Set up second user's encounters
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_area = Area.objects.create(name="Second Test Area", in_region=second_region)
		area_loc = Location.objects.create(name="Second Test Location", in_area=second_area)
		self.area_loc_wencounter = WorldEncounter.objects.create(title="Second WEncounter", in_location=area_loc)
		
		second_dungeon = Dungeon.objects.create(title="Second Test Dungeon", in_area=second_area)
		second_rs = Roomset.objects.create(name="Second Test Roomset", in_dungeon=second_dungeon)
		second_room = Room.objects.create(name="Second Test Room", room_number=1, in_roomset=second_rs)
		self.room_wencounter = WorldEncounter.objects.create(
									title="SecondRoomEncounter",
									in_dungeon_room=second_room
								)
		
		second_city = City.objects.create(name="Second Test City", in_region=second_region)
		second_cityquarter = CityQuarter.objects.create(name="Second Test CQ", in_city=second_city)
		cq_loc = Location.objects.create(name="Second Test Location", in_cityquarter=second_cityquarter)
		self.cq_loc_wencounter = WorldEncounter.objects.create(title="Second CQEncounter", in_location=cq_loc)
	
	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		# Test for WorldEncounter in Location
		response = self.client.get(self.loc_worldencounter.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		
		# Test for WorldEncounter in CityQuarter Location
		response = self.client.get(self.cq_worldencounter.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		
		# Test for a WorldEncounter in a Dungeon Room
		response = self.client.get(self.room_worldencounter.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		
	def test_detail_view_logged_in_and_encounter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		
		# Test for WorldEncounter in Location
		response = self.client.get(self.loc_worldencounter.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
		# Test for WorldEncounter in CityQuarter
		response = self.client.get(self.cq_worldencounter.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
		# Test for a WorldEncounter in a Dungeon Room
		response = self.client.get(self.room_worldencounter.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
	def test_detail_view_worldencounter_not_in_user_library_view_forbidden(self):
		# Test for WorldEncounter in an Area Location
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.area_loc_wencounter.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
		# Test for WorldEncounter in CityQuarter Location
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.cq_loc_wencounter.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
		# Test for WorldEncounter in a Dungeon Room
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.room_wencounter.get_absolute_url())
		self.assertEqual(response.status_code, 403)

	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		# Test for WorldEncounter in Location
		response = self.client.get(reverse('worldencounter-delete', args=[str(self.loc_worldencounter.id)]))
		self.assertEqual(response.status_code, 302)
	
		# Test for WorldEncounter in CityQuarter
		response = self.client.get(reverse('worldencounter-delete', args=[str(self.cq_worldencounter.id)]))
		self.assertEqual(response.status_code, 302)
		
		# Test for WorldEncounter in Dungeon Room
		response = self.client.get(reverse('worldencounter-delete', args=[str(self.room_worldencounter.id)]))
		self.assertEqual(response.status_code, 302)
	
	def test_delete_view_logged_in_and_worldencounter_in_user_library_renders(self):
		# Test for WorldEncounter in Location
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('worldencounter-delete', args=[str(self.loc_worldencounter.id)]))
		self.assertEqual(response.status_code, 200)
		
		# Test for WorldEncounter in CityQuarter
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('worldencounter-delete', args=[str(self.cq_worldencounter.id)]))
		self.assertEqual(response.status_code, 200)
		
		# Test for WorldEncounter in Dungeon Room
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('worldencounter-delete', args=[str(self.room_worldencounter.id)]))
		self.assertEqual(response.status_code, 200)
		
	def test_delete_view_not_in_user_library_view_forbidden(self):
		# Test for WorldEncounter in an Area Location
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.area_loc_wencounter.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
		# Test for WorldEncounter in CityQuarter Location
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.cq_loc_wencounter.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
		# Test for WorldEncounter in a Dungeon Room
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.room_wencounter.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
class WorldEncounterLootViewTests(TestCase):
	def setUp(self):
		# Set up first user's worldencounterloot
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		area = Area.objects.create(name="Test Area", in_region=region)
		location = Location.objects.create(name="Test Location", in_area=area)
		worldencounter = WorldEncounter.objects.create(title="Test WorldEncounter", in_location=location)
		
		itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=project)
		item = Item.objects.create(name="Test item", in_itemlist=itemlist)
		
		self.worldencounterloot = WorldEncounterLoot.objects.create(
								name=item, quantity=1, in_worldencounter=worldencounter
							)
		
		# Set up second user's worldencounterloot
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Test Region", in_universe=second_universe)
		second_area = Area.objects.create(name="Test Area", in_region=second_region)
		second_location = Location.objects.create(name="Test Location", in_area=second_area)
		second_worldencounter = WorldEncounter.objects.create(
									title="Test WorldEncounter", in_location=second_location
								)
		
		second_itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=second_project)
		second_item = Item.objects.create(name="Test item", in_itemlist=second_itemlist)
		
		self.second_worldencounterloot = WorldEncounterLoot.objects.create(
								name=item, quantity=1, in_worldencounter=second_worldencounter
							)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('worldencounterloot-delete', args=[str(self.worldencounterloot.id)]))
		self.assertEqual(response.status_code, 302)
	
	def test_delete_view_logged_in_and_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('worldencounterloot-delete', args=[str(self.worldencounterloot.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_worldencounterloot_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
						reverse('worldencounterloot-delete', args=[str(self.second_worldencounterloot.id)])
					)
