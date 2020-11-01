from django.urls import path

from Dungeon.views import dungeon_detail, dungeon_create, dungeon_delete
from Dungeon.views import roomset_detail, roomset_create, roomset_delete
from Dungeon.views import room_detail, room_create, room_delete
from Dungeon.views import roomloot_create, roomloot_delete

urlpatterns = []

# Detail Views
urlpatterns += [
	path('<int:pk>/', dungeon_detail, name="dungeon-detail"),
	path('roomset/<int:pk>', roomset_detail, name="roomset-detail"),
	path('room/<int:pk>/', room_detail, name="room-detail"),
]

# Create, Update and Delete Views
urlpatterns += [
	# Dungeons
	path('area/<int:in_area>/create/dungeon/', dungeon_create, name="dungeon-create"),
	path('area/<int:in_area>/update/dungeon/<int:pk>/', dungeon_create, name="dungeon-update"),
	path('delete/<int:pk>/', dungeon_delete, name="dungeon-delete"),
	
	# Roomsets
	path('<int:in_dungeon>/create/roomset/', roomset_create, name="roomset-create"),
	path('<int:in_dungeon>/update/roomset/<int:pk>/', roomset_create, name="roomset-update"),
	path('roomset/delete/<int:pk>/', roomset_delete, name="roomset-delete"),
	
	# Rooms
	path('roomset/<int:in_roomset>/create/room/', room_create, name="room-create"),
	path('roomset/<int:in_roomset>/create/room/<int:pk>/', room_create, name="room-update"),
	path('room/delete/<int:pk>/', room_delete, name="room-delete"),
	
	# Room Loot
	path('room/<int:in_room>/loot/create/', roomloot_create, name="roomloot-create"),
	path('roomloot/delete/<int:pk>/', roomloot_delete, name="roomloot-delete"),
]
