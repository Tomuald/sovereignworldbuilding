from django.urls import path

from ItemList.views import itemlist_detail, itemlist_create, itemlist_delete
from ItemList.views import item_detail, item_create, item_delete

urlpatterns = []

# Detail Views
urlpatterns += [
	path('<int:pk>/', itemlist_detail, name="itemlist-detail"),
	path('item/<int:pk>/', item_detail, name="item-detail"),
]

# Create, Update and Delete Views
urlpatterns += [
	# Itemlists
	path('project/<int:in_project>/create/', itemlist_create, name="itemlist-create"),
	path('project/<int:in_project>/update/<int:pk>/', itemlist_create, name="itemlist-update"),
	path('delete/<int:pk>/', itemlist_delete, name="itemlist-delete"),
	
	# Items
	path('<int:in_itemlist>/create/item/', item_create, name="item-create"),
	path('<int:in_itemlist>/update/item/<int:pk>/', item_create, name="item-update"),
	path('item/delete/<int:pk>/', item_delete, name="item-delete"),
]
