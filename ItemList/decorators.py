from django.core.exceptions import PermissionDenied
from ItemList.models import Itemlist, Item
from accounts.models import CustomUser

# Checks if this ItemList is in a project in the current user's library.
def itemlist_in_user_library(function):
	def test_itemlist_in_user_library(request, pk, *args, **kwargs):
		itemlist = Itemlist.objects.get(pk=pk)
		project = itemlist.in_project
		
		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
		
	return test_itemlist_in_user_library
	
# Checks if this item is in a project in the current user's library.
def item_in_user_library(function):
	def test_item_in_user_library(request, pk, *args, **kwargs):
		item = Item.objects.get(pk=pk)
		project = item.in_itemlist.in_project
		
		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_item_in_user_library
