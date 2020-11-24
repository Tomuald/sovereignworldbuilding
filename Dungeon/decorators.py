from django.core.exceptions import PermissionDenied
from Dungeon.models import Dungeon, Roomset, Room, RoomLoot
from Project.models import Project

# Checks if this dungeon's project is in the current user's library.
def dungeon_in_user_library(function):
	def test_dungeon_in_user_library(request, in_project, title, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, title, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_dungeon_in_user_library

def create_dungeon_in_user_library(function):
	def test_dungeon_in_user_library(request, in_project, in_area, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_area, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_dungeon_in_user_library

# Checks if this roomset's project is in the current user's library.
def roomset_in_user_library(function):
	def test_roomset_in_user_library(request, in_project, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_roomset_in_user_library

def create_roomset_in_user_library(function):
	def test_roomset_in_user_library(request, in_project, in_dungeon, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_dungeon, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_roomset_in_user_library

# Checks if this room's project is in the current user's library.
def room_in_user_library(function):
	def test_room_in_user_library(request, in_project, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_room_in_user_library

def create_room_in_user_library(function):
	def test_room_in_user_library(request, in_project, in_roomset, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_roomset, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_room_in_user_library

# Checks if this roomloot's project is in the current user's library.
def roomloot_in_user_library(function):
	def test_roomloot_in_user_library(request, in_project, pk, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, pk, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_roomloot_in_user_library

def create_roomloot_in_user_library(function):
	def test_roomloot_in_user_library(request, in_project, in_room, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_room, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_roomloot_in_user_library
