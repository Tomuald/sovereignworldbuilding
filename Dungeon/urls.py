from django.urls import path

from Dungeon.views import dungeon_detail, dungeon_create, dungeon_update, dungeon_delete
from Dungeon.views import roomset_detail, roomset_create, roomset_update, roomset_delete
from Dungeon.views import room_detail, room_create, room_update, room_delete
from Dungeon.views import roomloot_create, roomloot_delete

urlpatterns = []

# Detail Views
urlpatterns += [
	path('<int:in_project>/d/<str:title>/', dungeon_detail, name="dungeon-detail"),
	path('<int:in_project>/rs/<str:name>/', roomset_detail, name="roomset-detail"),
	path('<int:in_project>/rm/<str:name>/', room_detail, name="room-detail"),
]

# Create, Update and Delete Views
urlpatterns += [
	# Dungeons
	path('<int:in_project>/a/<str:in_area>/d/create/new/', dungeon_create, name="dungeon-create"),
	path('<int:in_project>/d/<str:title>/update/', dungeon_update, name="dungeon-update"),
	path('<int:in_project>/d/<str:title>/delete/', dungeon_delete, name="dungeon-delete"),

	# Roomsets
	path('<int:in_project>/d/<str:in_dungeon>/rs/create/new/', roomset_create, name="roomset-create"),
	path('<int:in_project>/rs/<str:name>/update/', roomset_update, name="roomset-update"),
	path('<int:in_project>/rs/<str:name>/delete/', roomset_delete, name="roomset-delete"),

	# Rooms
	path('<int:in_project>/rs/<str:in_roomset>/rm/create/new/', room_create, name="room-create"),
	path('<int:in_project>/rm/<str:name>/update/', room_update, name="room-update"),
	path('<int:in_project>/rm/<str:name>/delete/', room_delete, name="room-delete"),

	# Room Loot
	path('<int:in_project>/rm/<str:in_room>/rl/create/new/', roomloot_create, name="roomloot-create"),
	path('<int:in_project>/rl/<int:pk>/delete/', roomloot_delete, name="roomloot-delete"),
]
