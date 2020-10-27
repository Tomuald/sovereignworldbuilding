from django.core.exceptions import PermissionDenied
from Project.models import Project

# Checks if this project instance is in the current user's library.
def project_in_user_library(function):
	def test_project_in_user_library(request, pk, *args, **kwargs):
		project = Project.objects.get(pk=pk)

		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_project_in_user_library
