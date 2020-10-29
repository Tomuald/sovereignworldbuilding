from django.urls import path
from . import views
from Project.views import project_list, project_detail, project_create, project_delete
from Campaign.views import campaign_detail, campaign_index, campaign_create, campaign_delete
from Campaign.views import chapter_detail, chapter_create, chapter_delete
from Campaign.views import quest_detail, quest_create, quest_delete
from Campaign.views import questencounter_detail, questencounter_create, questencounter_delete
from Campaign.views import questencounterloot_create, questencounterloot_delete

from Dungeon.views import dungeon_detail, dungeon_create, dungeon_delete
from Dungeon.views import roomset_detail, roomset_create, roomset_delete
from Dungeon.views import room_detail, room_create, room_delete
from Dungeon.views import roomloot_create, roomloot_delete

from Pantheon.views import pantheon_detail, pantheon_create, pantheon_delete
from Pantheon.views import god_detail, god_create, god_delete

from ItemList.views import itemlist_detail, itemlist_create, itemlist_delete
from ItemList.views import item_detail, item_create, item_delete

from World import views

urlpatterns = []

###########################
### --- #MODEL URLS --- ###
###########################

urlpatterns += [
	# Project
	path('worldbuilder/', project_list, name="project-list"),
	path('worldbuilder/project/<int:pk>/', project_detail, name="project-detail"),
	
	# Campaign
	path('worldbuilder/campaign/<int:pk>/index/', campaign_index, name="campaign-index"),
	path('worldbuilder/campaign/<int:pk>/', campaign_detail, name="campaign-detail"),
	path('worldbuilder/campaign/chapter/<int:pk>/', chapter_detail, name="chapter-detail"),
	path('worldbuilder/campaign/quest/<int:pk>/', quest_detail, name="quest-detail"),
	path('worldbuilder/campaign/questencounter/<int:pk>/', questencounter_detail, name="questencounter-detail"),
	
	
	# Universe
	path('worldbuilder/universe/<int:pk>/', views.universe_detail, name="universe-detail"),
	path('worldbulder/universe/<int:pk>/index/', views.universe_index, name="universe-index"),
	path('worldbuilder/universe/region/<int:pk>/', views.region_detail, name="region-detail"),
	path('worldbuilder/universe/empire/<int:pk>/', views.empire_detail, name="empire-detail"),
	path('worldbuilder/universe/area/<int:pk>/', views.area_detail, name="area-detail"),
	path('worldbuilder/universe/city/<int:pk>/', views.city_detail, name="city-detail"),
	path('worldbuilder/universe/cityquarter/<int:pk>/', views.cityquarter_detail, name="cityquarter-detail"),
	path('worldbuilder/universe/location/<int:pk>/', views.location_detail, name="location-detail"),
	path('worldbuilder/universe/worldencounter/<int:pk>/', views.worldencounter_detail, name="worldencounter-detail"),
	path('worldbuilder/universe/faction/<int:pk>/', views.faction_detail, name="faction-detail"),
	path('worldbuilder/universe/npc/<int:pk>/', views.npc_detail, name="npc-detail"),
	
	# Dungeons
	path('worldbuilder/universe/dungeon/<int:pk>/', dungeon_detail, name="dungeon-detail"),
	path('worldbuilder/universe/dungeon/roomset/<int:pk>', roomset_detail, name="roomset-detail"),
	path('worldbuilder/universe/dungeon/room/<int:pk>/', room_detail, name="room-detail"),
	
	# Itemlist
	path('worldbuilder/itemlist/<int:pk>/', itemlist_detail, name="itemlist-detail"),
	path('worldbuilder/itemlist/item/<int:pk>/', item_detail, name="item-detail"),
	
	# Pantheons
	path('worldbuilder/universe/pantheon/<int:pk>/', pantheon_detail, name="pantheon-detail"),
	path('worldbuilder/universe/pantheon/god/<int:pk>/', god_detail, name="god-detail"),
]

##########################
### --- #FORM URLS --- ###
##########################

# PROJECT FORMS
urlpatterns += [
	path('worldbuilder/project/create/', project_create, name="project-create"),
	path('worldbuilder/project/update/<int:pk>/', project_create, name="project-update"),
	path('worldbuilder/project/delete/<int:pk>/', project_delete, name="project-delete"),
]

# WORLD FORMS
urlpatterns += [
	# Universes
	path('worldbuilder/project/<int:in_project>/create/universe/', views.universe_create, name="universe-create"),
	path('worldbuilder/project/<int:in_project>/update/universe/<int:pk>/', views.universe_create, name="universe-update"),
	path('worldbuilder/universe/delete/<int:pk>/', views.universe_delete, name="universe-delete"),
	
	# Regions
	path('worldbuilder/universe/<int:in_universe>/create/region/', views.region_create, name="region-create"),
	path('worldbuilder/universe/<int:in_universe>/update/region/<int:pk>', views.region_create, name="region-update"),
	path('worldbuilder/region/delete/<int:pk>/', views.region_delete, name="region-delete"),
	
	# Empires
	path('worldbuilder/universe/<int:in_universe>/create/empire/', views.empire_create, name="empire-create"),
	path('worldbuilder/universe/<int:in_universe>/update/empire/<int:pk>/', views.empire_create, name="empire-update"),
	path('worldbuilder/empire/delete/<int:pk>/', views.empire_delete, name="empire-delete"),
	
	# NPCs
	path('worldbuilder/universe/<int:in_universe>/create/npc/', views.npc_create, name="npc-create"),
	path('worldbuilder/<int:in_universe>/update/npc/<int:pk>/', views.npc_create, name="npc-update"),
	path('worldbuilder/universe/<int:in_universe>/faction/<int:in_faction>/create/npc/', views.npc_create, name="npc-create"),
	path('worldbuilder/universe/<int:in_universe>/faction/<int:in_faction>/update/npc/<int:pk>/', views.npc_create, name="npc-update"),
	path('worldbuilder/npc/delete/<int:pk>/', views.npc_delete, name="npc-delete"),
	
	# Factions
	path('worldbuilder/universe/<int:in_universe>/create/faction/', views.faction_create, name="faction-create"),
	path('worldbuilder/universe/<int:in_universe>/update/faction/<int:pk>/', views.faction_create, name="faction-update"),
	path('worldbuilder/faction/delete/<int:pk>/', views.faction_delete, name="faction-delete"),
	
	# Cities
	path('worldbuilder/region/<int:in_region>/create/city/', views.city_create, name="city-create"),
	path('worldbuilder/region/<int:in_region>/update/city/<int:pk>/', views.city_create, name="city-update"),
	path('worldbuilder/city/delete/<int:pk>/', views.city_delete, name="city-delete"),
	
	# Areas
	path('worldbuilder/region/<int:in_region>/create/location/', views.area_create, name="area-create"),
	path('worldbuilder/region/<int:in_region>/update/location/<int:pk>/', views.area_create, name="area-update"),
	path('worldbuilder/area/delete/<int:pk>/', views.area_delete, name="area-delete"),
	
	# City Quarters
	path('worldbuilder/region/<int:in_city>/create/cityquarter/', views.cityquarter_create, name="cityquarter-create"),
	path('worldbuilder/region/<int:in_city>/update/cityquarter/<int:pk>/', views.cityquarter_create, name="cityquarter-update"),
	path('worldbuilder/cityquarter/delete/<int:pk>/', views.cityquarter_delete, name="cityquarter-delete"),
	
	# City Demographics
	path('worldbuilder/region/<int:in_city>/create/citydemographics/', views.citydemographics_create, name="citydemographics-create"),
	
	# Locations
	path('worldbuilder/area/<int:in_area>/create/location/', views.location_create, name="location-create"),
	path('worldbuilder/area/<int:in_area>/update/location/<int:pk>/', views.location_create, name="location-update"),
	path('worldbuilder/cityquarter/<int:in_cityquarter>/create/location/', views.location_create, name="location-create"),
	path('worldbuilder/cityquarter/<int:in_cityquarter>/update/location/<int:pk>/', views.location_create, name="location-update"),
	path('worldbuilder/location/delete/<int:pk>/', views.location_delete, name="location-delete"),
	
	# Location Loot
	path('worldbuilder/location/<int:in_location>/loot/create/', views.locationloot_create, name="locationloot-create"),
	path('worldbuilder/locationloot/delete/<int:pk>/', views.locationloot_delete, name="locationloot-delete"),
	
	# World Encounter
	path('worldbuilder/universe/dungeon/room/<int:in_dungeon_room>/worldencounter/create/', views.worldencounter_create, name="worldencounter-create"),
	path('worldbuilder/universe/dungeon/room/<int:in_dungeon_room>/worldencounter/update/<int:pk>/', views.worldencounter_create, name="worldencounter-update"),
	path('worldbuilder/universe/location/<int:in_location>/worldencounter/create/', views.worldencounter_create, name="worldencounter-create"),
	path('worldbuilder/universe/location/<int:in_location>/worldencounter/update/<int:pk>/', views.worldencounter_create, name="worldencounter-update"),
	path('worldbuilder/worldencounter/delete/<int:pk>/', views.worldencounter_delete, name="worldencounter-delete"),
	
	# World Encounter Loot
	path('worldbuilder/universe/encounter/<int:in_worldencounter>/encounterloot/create/', views.worldencounterloot_create, name="worldencounterloot-create"),
	path('worldbuilder/universe/encounter/<int:in_worldencounter>/encounterloot/update/<int:pk>/', views.worldencounterloot_create, name="worldencounterloot-update"),
	path('worldbuilder/worldencounterloot/delete/<int:pk>/', views.worldencounterloot_delete, name="worldencounterloot-delete"),
]

urlpatterns += [
	# Dungeons
	path('worldbuilder/area/<int:in_area>/create/dungeon/', dungeon_create, name="dungeon-create"),
	path('worldbuilder/area/<int:in_area>/update/dungeon/<int:pk>/', dungeon_create, name="dungeon-update"),
	path('worldbuilder/dungeon/delete/<int:pk>/', dungeon_delete, name="dungeon-delete"),
	
	# Roomsets
	path('worldbuilder/dungeon/<int:in_dungeon>/create/roomset/', roomset_create, name="roomset-create"),
	path('worldbuilder/dungeon/<int:in_dungeon>/update/roomset/<int:pk>/', roomset_create, name="roomset-update"),
	path('worldbuilder/roomset/delete/<int:pk>/', roomset_delete, name="roomset-delete"),
	
	# Rooms
	path('worldbuilder/dungeon/roomset/<int:in_roomset>/create/room/', room_create, name="room-create"),
	path('worldbuilder/dungeon/roomset/<int:in_roomset>/create/room/<int:pk>/', room_create, name="room-update"),
	path('worldbuilder/room/delete/<int:pk>/', room_delete, name="room-delete"),
	
	# Room Loot
	path('worldbuilder/dungeon/room/<int:in_room>/loot/create/', roomloot_create, name="roomloot-create"),
	path('worldbuilder/dungeon/roomloot/delete/<int:pk>/', roomloot_delete, name="roomloot-delete"),
]

# CAMPAIGN FORMS

urlpatterns += [
	# Campaigns
	path('worldbuilder/<int:in_project>/create/campaign/', campaign_create, name="campaign-create"),
	path('worldbuilder/<int:in_project>/update/campaign/<int:pk>/', campaign_create, name="campaign-update"),
	path('worldbuilder/campaign/delete/<int:pk>/', campaign_delete, name="campaign-delete"),
	
	# Chapters
	path('worldbuilder/campaign/<int:in_campaign>/create/chapter/', chapter_create, name="chapter-create"),
	path('worldbuilder/campaign/<int:in_campaign>/update/chapter/<int:pk>/', chapter_create, name="chapter-update"),
	path('worldbuilder/chapter/delete/<int:pk>/', chapter_delete, name="chapter-delete"),
	
	# Quests
	path('worldbuilder/chapter/<int:in_chapter>/create/quest/', quest_create, name="quest-create"),
	path('worldbuilder/chapter/<int:in_chapter>/update/quest/<int:pk>', quest_create, name="quest-update"),
	path('worldbuilder/quest/delete/<int:pk>/', quest_delete, name="quest-delete"),
	
	# Quest Encounters
	path('worldbuilder/quest/<int:in_quest>/encounter/create/', questencounter_create, name="questencounter-create"),
	path('worldbuilder/quest/<int:in_quest>/encounter/update/<int:pk>/', questencounter_create, name="questencounter-update"),
	path('worldbuilder/questencounter/delete/<int:pk>/', questencounter_delete, name="questencounter-delete"),
	
	# Quest Encounter Loot
	path('worldbuilder/questencounter/<int:in_questencounter>/encounterloot/create/', questencounterloot_create, name="questencounterloot-create"),
	path('worldbuilder/questencounter/encounterloot/delete/<int:pk>/', questencounterloot_delete, name="questencounterloot-delete"),
]

# ITEMLIST FORMS

urlpatterns += [
	# Itemlists
	path('worldbuilder/project/<int:in_project>/itemlist/create/', itemlist_create, name="itemlist-create"),
	path('worldbuilder/project/<int:in_project>/itemlist/update/<int:pk>/', itemlist_create, name="itemlist-update"),
	path('worldbuilder/itemlist/delete/<int:pk>/', itemlist_delete, name="itemlist-delete"),
	
	# Items
	path('worldbuilder/itemlist/<int:in_itemlist>/create/item/', item_create, name="item-create"),
	path('worldbuilder/itemlist/<int:in_itemlist>/update/item/<int:pk>/', item_create, name="item-update"),
	path('worldbuilder/item/delete/<int:pk>/', item_delete, name="item-delete"),
]

# PANTHEON FORMS

urlpatterns += [
	# Pantheons
	path('worldbuilder/universe/<int:in_universe>/create/pantheon/', pantheon_create, name="pantheon-create"),
	path('worldbuilder/universe/<int:in_universe>/update/pantheon/<int:pk>/', pantheon_create, name="pantheon-update"),
	path('worldbuilder/pantheon/delete/<int:pk>/', pantheon_delete, name="pantheon-delete"),
	
	# Gods
	path('worldbuilder/universe/pantheon/<int:in_pantheon>/create/god/', god_create, name="god-create"),
	path('worldbuilder/universe/pantheon/<int:in_pantheon>/update/god/<int:pk>/', god_create, name="god-update"),
	path('worldbuilder/god/delete/<int:pk>/', god_delete, name="god-delete"),
]
