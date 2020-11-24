from django.core.exceptions import PermissionDenied
from World.models import Universe, Region, Area, City, CityQuarter, Location, WorldEncounter, WorldEncounterLoot
from World.models import Empire, Faction, NPC
from Project.models import Project

### Detail and Delete View Decorators ###

# Checks if this universe's project is in the current user's library.
def universe_in_user_library(function):
	def test_universe_in_user_library(request, in_project, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_universe_in_user_library

def create_universe_in_user_library(function):
	def test_universe_in_user_library(request, in_project, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_universe_in_user_library


# Checks if this region's project is in the current user's library.
def region_in_user_library(function):
	def test_region_in_user_library(request, in_project, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_region_in_user_library

def create_region_in_user_library(function):
	def test_region_in_user_library(request, in_project, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_region_in_user_library

# Checks if this area's project is in the current user's library.
def area_in_user_library(function):
	def test_area_in_user_library(request, in_project, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_area_in_user_library

def create_area_in_user_library(function):
	def test_area_in_user_library(request, in_project, in_region, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_region, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_area_in_user_library

# Checks if this city's project is in the current user's library.
def city_in_user_library(function):
	def test_city_in_user_library(request, in_project, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_city_in_user_library

def create_city_in_user_library(function):
	def test_city_in_user_library(request, in_project, in_region, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_region, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_city_in_user_library

# Checks if this cityquarter's project is in the current user's library.
def cityquarter_in_user_library(function):
	def test_cityquarter_in_user_library(request, in_project, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_cityquarter_in_user_library

def create_cityquarter_in_user_library(function):
	def test_cityquarter_in_user_library(request, in_project, in_city, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_city, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_cityquarter_in_user_library

# Checks if this location's project is in the current user's library.
def location_in_user_library(function):
	def test_location_in_user_library(request, in_project, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_location_in_user_library

def create_location_in_user_library(function):
	def test_location_in_user_library(request, in_project, in_area, in_cityquarter, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_area, in_cityquarter, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_location_in_user_library

# Checks if this locationloot's project is in the current user's library.
def locationloot_in_user_library(function):
	def test_ll_in_user_library(request, in_project, pk, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, pk, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_ll_in_user_library

# Checks if this worldencounter's project is in the current user's library.
def worldencounter_in_user_library(function):
	def test_worldencounter_in_user_library(request, in_project, title, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, title, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_worldencounter_in_user_library

def create_worldencounter_in_user_library(function):
	def test_worldencounter_in_user_library(request, in_project, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_worldencounter_in_user_library

# Checks if this worldencounterloot's project is in the current user's library.
def worldencounterloot_in_user_library(function):
	def test_wel_in_user_library(request, in_project, pk, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, pk, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_wel_in_user_library

def create_worldencounterloot_in_user_library(function):
	def test_wel_in_user_library(request, in_project, in_worldencounter, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_worldencounter, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_wel_in_user_library

# Checks if this empire's project is in the current user's library.
def empire_in_user_library(function):
	def test_empire_in_user_library(request, in_project, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_empire_in_user_library

def create_empire_in_user_library(function):
	def test_empire_in_user_library(request, in_project, in_universe, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_universe, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_empire_in_user_library

# Checks if this faction's project is in the current user's library.
def faction_in_user_library(function):
	def test_faction_in_user_library(request, in_project, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_faction_in_user_library

def create_faction_in_user_library(function):
	def test_faction_in_user_library(request, in_project, in_universe, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_universe, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_faction_in_user_library

# Checks if this npc's project is in the current user's library.
def npc_in_user_library(function):
	def test_npc_in_user_library(request, in_project, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_npc_in_user_library

def create_npc_in_user_library(function):
	def test_npc_in_user_library(request, in_project, in_universe, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_universe, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_npc_in_user_library

def citydemographics_in_user_library(function):
	def test_demographics_in_user_library(request, in_project, pk, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, pk, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_demographics_in_user_library

def create_citydemographics_in_user_library(function):
	def test_demographics_in_user_library(request, in_project, in_city, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_city, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_demographics_in_user_library
