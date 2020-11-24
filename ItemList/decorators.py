from django.core.exceptions import PermissionDenied
from ItemList.models import Itemlist, Item
from accounts.models import CustomUser
from Project.models import Project

# Checks if this ItemList is in a project in the current user's library.
def itemlist_in_user_library(function):
	def test_itemlist_in_user_library(request, in_project, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_itemlist_in_user_library

def create_itemlist_in_user_library(function):
	def test_itemlist_in_user_library(request, in_project, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_itemlist_in_user_library

# Checks if this item is in a project in the current user's library.
def item_in_user_library(function):
	def test_item_in_user_library(request, in_project, in_itemlist, name, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_itemlist, name, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_item_in_user_library

def create_item_in_user_library(function):
	def test_item_in_user_library(request, in_project, in_itemlist, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_itemlist, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_item_in_user_library
