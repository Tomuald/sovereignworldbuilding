# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from World.models import Universe, Region, Area, City, CityQuarter, Area, Location, WorldEncounter
from World.models import Empire, Faction, NPC
from accounts.models import CustomUser
from Project.models import Project
from Dungeon.models import Dungeon, Roomset, Room

class UniverseDetailViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		
		self.universe = Universe.objects.create(name="Test Universe", in_project=project)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(self.universe.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/%d/" % self.universe.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_universe_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.universe.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_universe_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(second_universe.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
class UniverseDeleteViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		
		self.universe = Universe.objects.create(name="Test Universe", in_project=project)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(reverse('universe-delete', args=[str(self.universe.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/delete/%d/" % self.universe.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_universe_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('universe-delete', args=[str(self.universe.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_universe_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('universe-delete', args=[str(second_universe.id)]))
		self.assertEqual(response.status_code, 403)
		
class RegionDetailViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.region = Region.objects.create(name="Test Region", in_universe=universe)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(self.region.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/region/%d/" % self.region.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_region_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.region.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
	def test_region_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(second_region.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
class RegionDeleteViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.region = Region.objects.create(name="Test Region", in_universe=universe)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(reverse('region-delete', args=[str(self.region.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/region/delete/%d/" % self.region.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_region_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('region-delete', args=[str(self.region.id)]))
		self.assertEqual(response.status_code, 200)
		
	def test_delete_region_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('region-delete', args=[str(second_region.id)]))
		self.assertEqual(response.status_code, 403)
		
class AreaDetailViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		
		self.area = Area.objects.create(name="Test Area", in_region=region)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.area.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/area/%d/" % self.area.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_area_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.area.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
	def test_area_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_area = Area.objects.create(name="Second Test Area", in_region=second_region)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(second_area.get_absolute_url())
		self.assertEqual(response.status_code, 403)

class AreaDeleteViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		
		self.area = Area.objects.create(name="Test Area", in_region=region)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('area-delete', args=[str(self.area.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/area/delete/%d/" % self.area.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_area_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('area-delete', args=[str(self.area.id)]))
		self.assertEqual(response.status_code, 200)
		
	def test_area_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_area = Area.objects.create(name="Second Test Area", in_region=second_region)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('area-delete', args=[str(second_area.id)]))
		self.assertEqual(response.status_code, 403)
		
class CityDetailViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		
		self.city = City.objects.create(name="Test City", in_region=region)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(self.city.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/city/%d/" % self.city.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_city_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.city.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
	def test_city_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_city = City.objects.create(name="Second Test City", in_region=second_region)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(second_city.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
class CityDeleteViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		
		self.city = City.objects.create(name="Test City", in_region=region)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(reverse('city-delete', args=[str(self.city.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/city/delete/%d/" % self.city.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_city_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('city-delete', args=[str(self.city.id)]))
		self.assertEqual(response.status_code, 200)
		
	def test_city_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_city = City.objects.create(name="Second Test City", in_region=second_region)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('city-delete', args=[str(second_city.id)]))
		self.assertEqual(response.status_code, 403)
		
class CityQuarterDetailViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		city = City.objects.create(name="Test City", in_region=region)
		
		self.cityquarter = CityQuarter.objects.create(name="Test CityQuarter", in_city=city)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.cityquarter.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/cityquarter/%d/" % self.cityquarter.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_cityquarter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.cityquarter.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
	def test_cityquarter_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_city = City.objects.create(name="Second Test City", in_region=second_region)
		second_cityquarter = CityQuarter.objects.create(name="Second Test CQ", in_city=second_city)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(second_cityquarter.get_absolute_url())
		self.assertEqual(response.status_code, 403)

class CityQuarterDeleteViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		region = Region.objects.create(name="Test Region", in_universe=universe)
		city = City.objects.create(name="Test City", in_region=region)
		
		self.cityquarter = CityQuarter.objects.create(name="Test CityQuarter", in_city=city)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('cityquarter-delete', args=[str(self.cityquarter.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/cityquarter/delete/%d/" % self.cityquarter.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_cityquarter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('cityquarter-delete', args=[str(self.cityquarter.id)]))
		self.assertEqual(response.status_code, 200)
		
	def test_cityquarter_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_city = City.objects.create(name="Second Test City", in_region=second_region)
		second_cityquarter = CityQuarter.objects.create(name="Second Test CQ", in_city=second_city)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('cityquarter-delete', args=[str(second_cityquarter.id)]))
		self.assertEqual(response.status_code, 403)
		
class LocationDetailViewTests(TestCase):
	def setUp(self):
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
	
	def test_not_logged_in_redirects(self):
		# Test for an Area Location
		response = self.client.get(self.area_location.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/location/%d/" % self.area_location.id
		self.assertRedirects(response, expected_url)
		
		# Test for an CityQuarter Location
		response = self.client.get(self.cq_location.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/location/%d/" % self.cq_location.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_location_in_user_library_renders(self):
		# Test for Area Location.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.area_location.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
		# Test for CityQuarter Location.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.cq_location.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_location_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_area = Area.objects.create(name="Second Test Area", in_region=second_region)
		area_loc = Location.objects.create(name="Second Test Location", in_area=second_area)
		second_city = City.objects.create(name="Second Test City", in_region=second_region)
		second_cityquarter = CityQuarter.objects.create(name="Second Test CQ", in_city=second_city)
		cq_loc = Location.objects.create(name="Second Test Location", in_cityquarter=second_cityquarter)
		
		# Test for Area Location.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(area_loc.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
		# Test for CityQuarter Location
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(cq_loc.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
class LocationDeleteViewTests(TestCase):
	def setUp(self):
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
	
	def test_not_logged_in_redirects(self):
		# Test for an Area Location
		response = self.client.get(reverse('location-delete', args=[str(self.area_location.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/location/delete/%d/" % self.area_location.id
		self.assertRedirects(response, expected_url)
		
		# Test for an CityQuarter Location
		response = self.client.get(reverse('location-delete', args=[str(self.cq_location.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/location/delete/%d/" % self.cq_location.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_location_in_user_library_renders(self):
		# Test for Area Location.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('location-delete', args=[str(self.area_location.id)]))
		self.assertEqual(response.status_code, 200)
		
		# Test for CityQuarter Location.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('location-delete', args=[str(self.cq_location.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_location_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_area = Area.objects.create(name="Second Test Area", in_region=second_region)
		area_loc = Location.objects.create(name="Second Test Location", in_area=second_area)
		second_city = City.objects.create(name="Second Test City", in_region=second_region)
		second_cityquarter = CityQuarter.objects.create(name="Second Test CQ", in_city=second_city)
		cq_loc = Location.objects.create(name="Second Test Location", in_cityquarter=second_cityquarter)
		
		# Test for Area Location.
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('location-delete', args=[str(area_loc.id)]))
		self.assertEqual(response.status_code, 403)
		
		# Test for CityQuarter Location
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('location-delete', args=[str(cq_loc.id)]))
		self.assertEqual(response.status_code, 403)
		
		
class EmpireDetailViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.empire = Empire.objects.create(name="Test Empire", in_universe=universe)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(self.empire.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/empire/%d/" % self.empire.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_empire_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.empire.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_empire_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_empire = Empire.objects.create(name="Second Test Empire", in_universe=second_universe)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(second_empire.get_absolute_url())
		self.assertEqual(response.status_code, 403)

class EmpireDeleteViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.empire = Empire.objects.create(name="Test Empire", in_universe=universe)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(reverse('empire-delete', args=[str(self.empire.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/empire/delete/%d/" % self.empire.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_empire_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('empire-delete', args=[str(self.empire.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_empire_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_empire = Empire.objects.create(name="Second Test Empire", in_universe=second_universe)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('empire-delete', args=[str(second_empire.id)]))
		self.assertEqual(response.status_code, 403)
		
class FactionDetailViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.faction = Faction.objects.create(name="Test Faction", in_universe=universe)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(self.faction.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/faction/%d/" % self.faction.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_faction_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.faction.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_faction_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_faction = Faction.objects.create(name="Second Test Faction", in_universe=second_universe)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(second_faction.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
class FactionDeleteViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.faction = Faction.objects.create(name="Test Faction", in_universe=universe)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(reverse('faction-delete', args=[str(self.faction.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/faction/delete/%d/" % self.faction.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_faction_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('faction-delete', args=[str(self.faction.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_faction_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_faction = Faction.objects.create(name="Second Test Faction", in_universe=second_universe)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('faction-delete', args=[str(second_faction.id)]))
		self.assertEqual(response.status_code, 403)
		
class NPCDetailViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.npc = NPC.objects.create(name="Test NPC", in_universe=universe)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(self.npc.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/npc/%d/" % self.npc.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_npc_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.npc.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_npc_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_npc = NPC.objects.create(name="Second Test NPC", in_universe=second_universe)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(second_npc.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
class NPCDeleteViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.npc = NPC.objects.create(name="Test NPC", in_universe=universe)
	
	def test_not_logged_in_redirects(self):
		response = self.client.get(reverse('npc-delete', args=[str(self.npc.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/npc/delete/%d/" % self.npc.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_npc_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('npc-delete', args=[str(self.npc.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_npc_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_npc = NPC.objects.create(name="Second Test NPC", in_universe=second_universe)
		
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('npc-delete', args=[str(second_npc.id)]))
		self.assertEqual(response.status_code, 403)
		
class WorldEncounterDetailViewTests(TestCase):
	def setUp(self):
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
	
	def test_not_logged_in_redirects(self):
	# Test for WorldEncounter in Location
		response = self.client.get(self.loc_worldencounter.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/worldencounter/%d/" % self.loc_worldencounter.id
		self.assertRedirects(response, expected_url)
		
		# Test for a WorldEncounter in a Dungeon Room
		response = self.client.get(self.room_worldencounter.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/universe/worldencounter/%d/" % self.room_worldencounter.id
		self.assertRedirects(response, expected_url)
		
	def test_logged_in_and_encounter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		
		# Test for WorldEncounter in Location
		response = self.client.get(self.loc_worldencounter.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
		# Test for a WorldEncounter in a Dungeon Room
		response = self.client.get(self.room_worldencounter.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
	def test_worldencounter_not_in_user_library_view_forbidden(self):
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_region = Region.objects.create(name="Second Test Region", in_universe=second_universe)
		second_area = Area.objects.create(name="Second Test Area", in_region=second_region)
		area_loc = Location.objects.create(name="Second Test Location", in_area=second_area)
		area_loc_wencounter = WorldEncounter.objects.create(title="Second WEncounter", in_location=area_loc)
		
		second_dungeon = Dungeon.objects.create(title="Second Test Dungeon", in_area=second_area)
		second_rs = Roomset.objects.create(name="Second Test Roomset", in_dungeon=second_dungeon)
		second_room = Room.objects.create(name="Second Test Room", room_number=1, in_roomset=second_rs)
		room_wencounter = WorldEncounter.objects.create(title="SecondRoomEncounter", in_dungeon_room=second_room)
		
		second_city = City.objects.create(name="Second Test City", in_region=second_region)
		second_cityquarter = CityQuarter.objects.create(name="Second Test CQ", in_city=second_city)
		cq_loc = Location.objects.create(name="Second Test Location", in_cityquarter=second_cityquarter)
		cq_loc_wencounter = WorldEncounter.objects.create(title="Second CQEncounter", in_location=cq_loc)
		
		# Test for WorldEncounter in an Area Location
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(area_loc_wencounter.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
		# Test for WorldEncounter in CityQuarter Location
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(cq_loc_wencounter.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
		# Test for WorldEncounter in a Dungeon Room
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(room_wencounter.get_absolute_url())
		self.assertEqual(response.status_code, 403)
		
