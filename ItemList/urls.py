from django.urls import path

from ItemList.views import itemlist_detail, itemlist_create, itemlist_update, itemlist_delete
from ItemList.views import item_detail, item_create, item_update, item_delete

urlpatterns = []

# Detail Views
urlpatterns += [
	path('<int:in_project>/il/<str:name>/', itemlist_detail, name="itemlist-detail"),
	path('<int:in_project>/il/<str:in_itemlist>/i/<str:name>/', item_detail, name="item-detail"),
]

# Create, Update and Delete Views
urlpatterns += [
	# Itemlists
	path('<int:in_project>/il/create/new/', itemlist_create, name="itemlist-create"),
	path('<int:in_project>/il/<str:name>/update/', itemlist_update, name="itemlist-update"),
	path('<int:in_project>/il/<str:name>/delete/', itemlist_delete, name="itemlist-delete"),

	# Items
	path('<int:in_project>/il/<str:in_itemlist>/i/create/new/', item_create, name="item-create"),
	path('<int:in_project>/il/<str:in_itemlist>/i/<str:name>/update/', item_update, name="item-update"),
	path('<int:in_project>/il/<str:in_itemlist>/i/<str:name>/delete/', item_delete, name="item-delete"),
]
