from django.core.exceptions import PermissionDenied
from World.models import Universe, Region, Area, City, CityQuarter, Location, WorldEncounter, WorldEncounterLoot
from World.models import Empire, Faction, NPC

### Detail and Delete View Decorators ###

# Checks if this universe's project is in the current user's library.
def universe_in_user_library(function):
	def test_universe_in_user_library(request, pk, *args, **kwargs):
		universe = Universe.objects.get(pk=pk)
		project = universe.in_project

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_universe_in_user_library

# Checks if this region's project is in the current user's library.
def region_in_user_library(function):
	def test_region_in_user_library(request, pk, *args, **kwargs):
		region = Region.objects.get(pk=pk)
		project = region.in_universe.in_project

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_region_in_user_library
	
# Checks if this area's project is in the current user's library.
def area_in_user_library(function):
	def test_area_in_user_library(request, pk, *args, **kwargs):
		area = Area.objects.get(pk=pk)
		project = area.in_region.in_universe.in_project

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_area_in_user_library
	
# Checks if this city's project is in the current user's library.
def city_in_user_library(function):
	def test_city_in_user_library(request, pk, *args, **kwargs):
		city = City.objects.get(pk=pk)
		project = city.in_region.in_universe.in_project

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_city_in_user_library
	
# Checks if this cityquarter's project is in the current user's library.
def cityquarter_in_user_library(function):
	def test_cityquarter_in_user_library(request, pk, *args, **kwargs):
		cityquarter = CityQuarter.objects.get(pk=pk)
		project = cityquarter.in_city.in_region.in_universe.in_project

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_cityquarter_in_user_library
	
# Checks if this cityquarter's project is in the current user's library.
def location_in_user_library(function):
	def test_location_in_user_library(request, pk, *args, **kwargs):
		location = Location.objects.get(pk=pk)
		if location.in_area is not None:
			project = location.in_area.in_region.in_universe.in_project
		elif location.in_cityquarter is not None:
			project = location.in_cityquarter.in_city.in_region.in_universe.in_project
		else:
			return False

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_location_in_user_library
	
# Checks if this worldencounter's project is in the current user's library.
def worldencounter_in_user_library(function):
	def test_worldencounter_in_user_library(request, pk, *args, **kwargs):
		worldencounter = WorldEncounter.objects.get(pk=pk)
		
		if worldencounter.in_location is not None:
			if worldencounter.in_location.in_area is not None:
				project = worldencounter.in_location.in_area.in_region.in_universe.in_project
			elif worldencounter.in_location.in_cityquarter is not None:
				project = worldencounter.in_location.in_cityquarter.in_city.in_region.in_universe.in_project
			else:
				return False
		elif worldencounter.in_dungeon_room is not None:
			project = worldencounter.in_dungeon_room.in_roomset.in_dungeon.in_area.in_region.in_universe.in_project
		else:
			return False

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_worldencounter_in_user_library

# Checks if this worldencounterloot's project is in the current user's library.
def worldencounterloot_in_user_library(function):
	def test_worldencounterloot_in_user_library(request, pk, *args, **kwargs):
		worldencounterloot = WorldEncounterLoot.objects.get(pk=pk)
		
		if worldencounterloot.in_worldencounter.in_location is not None:
			if worldencounterloot.in_worldencounter.in_location.in_area is not None:
				project = worldencounterloot.in_worldencounter.in_location.in_area.in_region.in_universe.in_project
			elif worldencounterloot.in_worldencounter.in_location.in_cityquarter is not None:
				project = worldencounterloot.in_worldencounter.in_location.in_cityquarter.in_city.in_region.in_universe.in_project
			else:
				return False
		elif worldencounterloot.in_worldencounter.in_dungeon_room is not None:
			project = worldencounterloot.in_worldencounter.in_dungeon_room.in_roomset.in_dungeon.in_area.in_region.in_universe.in_project
		else:
			return False

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_worldencounterloot_in_user_library
	
# Checks if this empire's project is in the current user's library.
def empire_in_user_library(function):
	def test_empire_in_user_library(request, pk, *args, **kwargs):
		empire = Empire.objects.get(pk=pk)
		project = empire.in_universe.in_project

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_empire_in_user_library
	
# Checks if this faction's project is in the current user's library.
def faction_in_user_library(function):
	def test_faction_in_user_library(request, pk, *args, **kwargs):
		faction = Faction.objects.get(pk=pk)
		project = faction.in_universe.in_project

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_faction_in_user_library
	
# Checks if this npc's project is in the current user's library.
def npc_in_user_library(function):
	def test_npc_in_user_library(request, pk, *args, **kwargs):
		npc = NPC.objects.get(pk=pk)
		project = npc.in_universe.in_project

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_npc_in_user_library
	


