from django.urls import path

from World.views import universe_detail, universe_index, universe_create, universe_delete
from World.views import region_detail, region_create, region_delete
from World.views import area_detail, area_create, area_delete
from World.views import city_detail, city_create, city_delete
from World.views import cityquarter_detail, cityquarter_create, cityquarter_delete
from World.views import citydemographics_create
from World.views import location_detail, location_create, location_delete
from World.views import locationloot_create, locationloot_delete
from World.views import worldencounter_detail, worldencounter_create, worldencounter_delete
from World.views import worldencounterloot_create, worldencounterloot_delete

from World.views import empire_detail, empire_create, empire_delete
from World.views import faction_detail, faction_create, faction_delete
from World.views import npc_detail, npc_create, npc_delete

urlpatterns = []

# Detail Views
urlpatterns += [
	path('<int:pk>/', universe_detail, name="universe-detail"),
	path('<int:pk>/index/', universe_index, name="universe-index"),
	path('region/<int:pk>/', region_detail, name="region-detail"),
	path('empire/<int:pk>/', empire_detail, name="empire-detail"),
	path('area/<int:pk>/', area_detail, name="area-detail"),
	path('city/<int:pk>/', city_detail, name="city-detail"),
	path('cityquarter/<int:pk>/', cityquarter_detail, name="cityquarter-detail"),
	path('location/<int:pk>/', location_detail, name="location-detail"),
	path('worldencounter/<int:pk>/', worldencounter_detail, name="worldencounter-detail"),
	path('faction/<int:pk>/', faction_detail, name="faction-detail"),
	path('npc/<int:pk>/', npc_detail, name="npc-detail"),
]

# Create, Update and Delete Views
urlpatterns += [
	# Universes
	path('project/<int:in_project>/create/universe/', universe_create, name="universe-create"),
	path('project/<int:in_project>/update/universe/<int:pk>/', universe_create, name="universe-update"),
	path('delete/<int:pk>/', universe_delete, name="universe-delete"),
	
	# Regions
	path('<int:in_universe>/create/region/', region_create, name="region-create"),
	path('<int:in_universe>/update/region/<int:pk>', region_create, name="region-update"),
	path('region/delete/<int:pk>/', region_delete, name="region-delete"),
	
	# Empires
	path('<int:in_universe>/create/empire/', empire_create, name="empire-create"),
	path('<int:in_universe>/update/empire/<int:pk>/', empire_create, name="empire-update"),
	path('empire/delete/<int:pk>/', empire_delete, name="empire-delete"),
	
	# NPCs
	path('<int:in_universe>/create/npc/', npc_create, name="npc-create"),
	path('<int:in_universe>/update/npc/<int:pk>/', npc_create, name="npc-update"),
	path('<int:in_universe>/faction/<int:in_faction>/create/npc/', npc_create, name="npc-create"),
	path('<int:in_universe>/faction/<int:in_faction>/update/npc/<int:pk>/', npc_create, name="npc-update"),
	path('npc/delete/<int:pk>/', npc_delete, name="npc-delete"),
	
	# Factions
	path('<int:in_universe>/create/faction/', faction_create, name="faction-create"),
	path('<int:in_universe>/update/faction/<int:pk>/', faction_create, name="faction-update"),
	path('faction/delete/<int:pk>/', faction_delete, name="faction-delete"),
	
	# Cities
	path('region/<int:in_region>/create/city/', city_create, name="city-create"),
	path('region/<int:in_region>/update/city/<int:pk>/', city_create, name="city-update"),
	path('city/delete/<int:pk>/', city_delete, name="city-delete"),
	
	# Areas
	path('region/<int:in_region>/create/location/', area_create, name="area-create"),
	path('region/<int:in_region>/update/location/<int:pk>/', area_create, name="area-update"),
	path('area/delete/<int:pk>/', area_delete, name="area-delete"),
	
	# City Quarters
	path('region/<int:in_city>/create/cityquarter/', cityquarter_create, name="cityquarter-create"),
	path('region/<int:in_city>/update/cityquarter/<int:pk>/', cityquarter_create, name="cityquarter-update"),
	path('cityquarter/delete/<int:pk>/', cityquarter_delete, name="cityquarter-delete"),
	
	# City Demographics
	path('region/<int:in_city>/create/citydemographics/', citydemographics_create, name="citydemographics-create"),
	
	# Locations
	path('area/<int:in_area>/create/location/', location_create, name="location-create"),
	path('area/<int:in_area>/update/location/<int:pk>/', location_create, name="location-update"),
	path('cityquarter/<int:in_cityquarter>/create/location/', location_create, name="location-create"),
	path('cityquarter/<int:in_cityquarter>/update/location/<int:pk>/', location_create, name="location-update"),
	path('location/delete/<int:pk>/', location_delete, name="location-delete"),
	
	# Location Loot
	path('location/<int:in_location>/loot/create/', locationloot_create, name="locationloot-create"),
	path('locationloot/delete/<int:pk>/', locationloot_delete, name="locationloot-delete"),
	
	# World Encounter
	path('dungeon/room/<int:in_dungeon_room>/worldencounter/create/', worldencounter_create, name="worldencounter-create"),
	path('dungeon/room/<int:in_dungeon_room>/worldencounter/update/<int:pk>/', worldencounter_create, name="worldencounter-update"),
	path('location/<int:in_location>/worldencounter/create/', worldencounter_create, name="worldencounter-create"),
	path('location/<int:in_location>/worldencounter/update/<int:pk>/', worldencounter_create, name="worldencounter-update"),
	path('worldencounter/delete/<int:pk>/', worldencounter_delete, name="worldencounter-delete"),
	
	# World Encounter Loot
	path('encounter/<int:in_worldencounter>/encounterloot/create/', worldencounterloot_create, name="worldencounterloot-create"),
	path('encounter/<int:in_worldencounter>/encounterloot/update/<int:pk>/', worldencounterloot_create, name="worldencounterloot-update"),
	path('worldencounterloot/delete/<int:pk>/', worldencounterloot_delete, name="worldencounterloot-delete"),
]
