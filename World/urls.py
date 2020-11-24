from django.urls import path

from World.views import universe_detail, universe_index, universe_create, universe_update, universe_delete
from World.views import region_detail, region_create, region_update, region_delete
from World.views import area_detail, area_create, area_update, area_delete
from World.views import city_detail, city_create, city_update, city_delete
from World.views import cityquarter_detail, cityquarter_create, cityquarter_update, cityquarter_delete
from World.views import citydemographics_create, citydemographics_delete
from World.views import location_detail, location_create, location_update, location_delete
from World.views import locationloot_create, locationloot_delete
from World.views import worldencounter_detail, worldencounter_create, worldencounter_update, worldencounter_delete
from World.views import worldencounterloot_create, worldencounterloot_delete

from World.views import empire_detail, empire_create, empire_update, empire_delete
from World.views import faction_detail, faction_create, faction_update, faction_delete
from World.views import npc_detail, npc_create, npc_update, npc_delete

urlpatterns = []

# Detail Views
urlpatterns += [
	path('<int:in_project>/u/<str:name>/', universe_detail, name="universe-detail"),
	path('<int:in_project>/u/<str:name>/index/', universe_index, name="universe-index"),
	path('<int:in_project>/r/<str:name>/', region_detail, name="region-detail"),
	path('<int:in_project>/a/<str:name>/', area_detail, name="area-detail"),
	path('<int:in_project>/ct/<str:name>/', city_detail, name="city-detail"),
	path('<int:in_project>/cq/<str:name>/', cityquarter_detail, name="cityquarter-detail"),
	path('<int:in_project>/l/<str:name>/', location_detail, name="location-detail"),
	path('<int:in_project>/we/<str:title>/', worldencounter_detail, name="worldencounter-detail"),
	path('<int:in_project>/e/<str:name>/', empire_detail, name="empire-detail"),
	path('<int:in_project>/f/<str:name>/', faction_detail, name="faction-detail"),
	path('<int:in_project>/n/<str:name>/', npc_detail, name="npc-detail"),
]

# Create, Update and Delete Views
urlpatterns += [
	# Universes
	path('<int:in_project>/u/create/new/', universe_create, name="universe-create"),
	path('<int:in_project>/u/<str:name>/update/', universe_update, name="universe-update"),
	path('<int:in_project>/u/<str:name>/delete/', universe_delete, name="universe-delete"),

	# Regions
	path('<int:in_project>/u/<str:in_universe>/r/create/new/', region_create, name="region-create"),
	path('<int:in_project>/r/<str:name>/update/', region_update, name="region-update"),
	path('<int:in_project>/r/<str:name>/delete/', region_delete, name="region-delete"),

	# Areas
	path('<int:in_project>/r/<str:in_region>/a/create/new/', area_create, name="area-create"),
	path('<int:in_project>/a/<str:name>/update/', area_update, name="area-update"),
	path('<int:in_project>/a/<str:name>/delete/', area_delete, name="area-delete"),

	# Cities
	path('<int:in_project>/r/<str:in_region>/ct/create/new/', city_create, name="city-create"),
	path('<int:in_project>/ct/<str:name>/update/', city_update, name="city-update"),
	path('<int:in_project>/ct/<str:name>/delete/', city_delete, name="city-delete"),

	# City Quarters
	path('<int:in_project>/c/<str:in_city>/cq/create/new/', cityquarter_create, name="cityquarter-create"),
	path('<int:in_project>/cq/<str:name>/update/', cityquarter_update, name="cityquarter-update"),
	path('<int:in_project>/cq/<str:name>/delete/', cityquarter_delete, name="cityquarter-delete"),

	# City Demographics
	path('<int:in_project>/ct/<str:in_city>/ctd/create/new/', citydemographics_create, name="citydemographics-create"),
	path('<int:in_project>/ctd/<int:pk>/delete/', citydemographics_delete, name="citydemographics-delete"),

	# Locations
	path('<int:in_project>/a/<str:in_area>/l/create/new/', location_create, name="location-create"),
	path('<int:in_project>/l/<str:name>/update/', location_update, name="location-update"),
	path('<int:in_project>/cq/<str:in_cityquarter>/l/create/new/', location_create, name="location-create"),
	path('<int:in_project>/l/<str:name>/update/', location_update, name="location-update"),
	path('<int:in_project>/l/<str:name>/delete/', location_delete, name="location-delete"),

	# Location Loot
	path('<int:in_project>/l/<str:in_location>/ll/create/new/', locationloot_create, name="locationloot-create"),
	path('<int:in_project>/ll/<int:pk>/delete/', locationloot_delete, name="locationloot-delete"),

	# World Encounter
	path('<int:in_project>/rm/<str:in_dungeon_room>/we/create/new/', worldencounter_create, name="worldencounter-create"),
	path('<int:in_project>/l/<str:in_location>/we/create/new/', worldencounter_create, name="worldencounter-create"),
	path('<int:in_project>/we/<str:title>/update/', worldencounter_update, name="worldencounter-update"),
	path('<int:in_project>/we/<str:title>/delete/', worldencounter_delete, name="worldencounter-delete"),

	# World Encounter Loot
	path('<int:in_project>/we/<str:in_worldencounter>/wel/create/new/', worldencounterloot_create, name="worldencounterloot-create"),
	path('<int:in_project>/wel/<int:pk>/delete/', worldencounterloot_delete, name="worldencounterloot-delete"),

	# Empires
	path('<int:in_project>/u/<str:in_universe>/e/create/new/', empire_create, name="empire-create"),
	path('<int:in_project>/e/<str:name>/update/', empire_update, name="empire-update"),
	path('<int:in_project>/e/<str:name>/delete/', empire_delete, name="empire-delete"),

	# Factions
	path('<int:in_project>/u/<str:in_universe>/f/create/new/', faction_create, name="faction-create"),
	path('<int:in_project>/f/<str:name>/update/', faction_update, name="faction-update"),
	path('<int:in_project>/f/<str:name>/delete/', faction_delete, name="faction-delete"),

	# NPCs
	path('<int:in_project>/u/<str:in_universe>/n/create/new/', npc_create, name="npc-create"),
	path('<int:in_project>/n/<str:name>/update/', npc_update, name="npc-update"),
	path('<int:in_project>/u/<str:in_universe>/f/<str:in_faction>/n/create/new/', npc_create, name="npc-create"),
	path('<int:in_project>/f/<str:in_faction>/n/<str:name>/update/', npc_update, name="npc-update"),
	path('<int:in_project>/n/<str:name>/delete/', npc_delete, name="npc-delete"),
]
