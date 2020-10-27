from django.core.exceptions import PermissionDenied
from Pantheon.models import Pantheon, God

# Checks if this pantheon's project in the current user's library.
def pantheon_in_user_library(function):
	def test_pantheon_in_user_library(request, pk, *args, **kwargs):
		pantheon = Pantheon.objects.get(pk=pk)
		project = pantheon.in_universe.in_project
		
		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_pantheon_in_user_library

# Checks if this god's project in is the current user's library.
def god_in_user_library(function):
	def test_god_in_user_library(request, pk, *args, **kwargs):
		god = God.objects.get(pk=pk)
		project = god.in_pantheon.in_universe.in_project
		
		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_god_in_user_library
