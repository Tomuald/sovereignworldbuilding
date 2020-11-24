from django.core.exceptions import PermissionDenied
from Pantheon.models import Pantheon, God

from Project.models import Project

# Checks if this pantheon's project in the current user's library.
def pantheon_in_user_library(function):
	def test_pantheon_in_user_library(request, in_project, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_pantheon_in_user_library

def create_pantheon_in_user_library(function):
	def test_pantheon_in_user_library(request, in_project, in_universe, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_universe, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_pantheon_in_user_library

# Checks if this god's project in is the current user's library.
def god_in_user_library(function):
	def test_god_in_user_library(request, in_project, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_god_in_user_library

def create_god_in_user_library(function):
	def test_god_in_user_library(request, in_project, in_pantheon, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_pantheon, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_god_in_user_library
