from django.core.exceptions import PermissionDenied
from Dungeon.models import Dungeon, Roomset, Room

# Checks if this dungeon's project is in the current user's library.
def dungeon_in_user_library(function):
	def test_dungeon_in_user_library(request, pk, *args, **kwargs):
		dungeon = Dungeon.objects.get(pk=pk)
		project = dungeon.in_area.in_region.in_universe.in_project

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_dungeon_in_user_library

# Checks if this roomset's project is in the current user's library.
def roomset_in_user_library(function):
	def test_roomset_in_user_library(request, pk, *args, **kwargs):
		roomset = Roomset.objects.get(pk=pk)
		project = roomset.in_dungeon.in_area.in_region.in_universe.in_project

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_roomset_in_user_library
	
# Checks if this room's project is in the current user's library.
def room_in_user_library(function):
	def test_room_in_user_library(request, pk, *args, **kwargs):
		room = Room.objects.get(pk=pk)
		project = room.in_roomset.in_dungeon.in_area.in_region.in_universe.in_project

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_room_in_user_library
