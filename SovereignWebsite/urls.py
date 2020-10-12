from django.urls import path
from . import views

urlpatterns = []

###########################
### --- #MODEL URLS --- ###
###########################

urlpatterns += [
	# Project
	path('worldbuilder/', views.project_list, name="project-list"),
	path('worldbuilder/project/<int:pk>/', views.project_detail, name="project-detail"),
	
	# Campaign
	path('worldbuilder/campaign/<int:pk>/index/', views.campaign_index, name="campaign-index"),
	path('worldbuilder/campaign/<int:pk>/', views.campaign_detail, name="campaign-detail"),
	path('worldbuilder/campaign/chapter/<int:pk>/', views.chapter_detail, name="chapter-detail"),
	path('worldbuilder/campaign/quest/<int:pk>/', views.quest_detail, name="quest-detail"),
	path('worldbuilder/campaign/questencounter/<int:pk>/', views.questencounter_detail, name="questencounter-detail"),
	
	
	# Universe
	path('worldbuilder/universe/<int:pk>/', views.universe_detail, name="universe-detail"),
	path('worldbulder/universe/<int:pk>/index/', views.universe_index, name="universe-index"),
	path('worldbuilder/universe/region/<int:pk>/', views.region_detail, name="region-detail"),
	path('worldbuilder/universe/empire/<int:pk>/', views.empire_detail, name="empire-detail"),
	path('worldbuilder/universe/area/<int:pk>/', views.area_detail, name="area-detail"),
	path('worldbuilder/universe/city/<int:pk>/', views.city_detail, name="city-detail"),
	path('worldbuilder/universe/cityquarter/<int:pk>', views.cityquarter_detail, name="cityquarter-detail"),
	path('worldbuilder/universe/location/<int:pk>/', views.location_detail, name="location-detail"),
	path('worldbuilder/universe/worldencounter/<int:pk>/', views.worldencounter_detail, name="worldencounter-detail"),
	path('worldbuilder/universe/faction/<int:pk>/', views.faction_detail, name="faction-detail"),
	path('worldbuilder/universe/npc/<int:pk>/', views.npc_detail, name="npc-detail"),
	
	# Dungeons
	path('worldbuilder/universe/dungeon/<int:pk>/', views.dungeon_detail, name="dungeon-detail"),
	path('worldbuilder/universe/dungeon/roomset/<int:pk>', views.roomset_detail, name="roomset-detail"),
	path('worldbuilder/universe/dungeon/room/<int:pk>/', views.room_detail, name="room-detail"),
	
	# Itemlist
	path('worldbuilder/itemlist/<int:pk>/', views.itemlist_detail, name="itemlist-detail"),
	path('worldbuilder/itemlist/item/<int:pk>/', views.item_detail, name="item-detail"),
	
	# Pantheons
	path('worldbuilder/universe/pantheon/<int:pk>/', views.pantheon_detail, name="pantheon-detail"),
	path('worldbuilder/universe/pantheon/god/<int:pk>/', views.god_detail, name="god-detail"),
]

##########################
### --- #FORM URLS --- ###
##########################

# PROJECT FORMS
urlpatterns += [
	path('worldbuilder/project/create/', views.project_create, name="project-create"),
	path('worldbuilder/project/update/<int:pk>/', views.project_create, name="project-update"),
	path('worldbuilder/project/delete/<int:pk>/', views.project_delete, name="project-delete"),
]

# WORLD FORMS
urlpatterns += [
	# Universes
	path('worldbuilder/project/<int:in_project>/create/universe/', views.universe_create, name="universe-create"),
	path('worldbuilder/project/<int:in_project>/update/universe/<int:pk>/', views.universe_create, name="universe-update"),
	path('worldbuilder/delete/universe/<int:pk>/', views.universe_delete, name="universe-delete"),
	
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
	path('worldbuilder/universe/dungeon/room/<int:in_dungeon_room>/worldencounter/delete/<int:pk>/', views.worldencounter_delete, name="worldencounter-delete"),
	path('worldbuilder/universe/location/<int:in_location>/worldencounter/delete/<int:pk>/', views.worldencounter_delete, name="worldencounter-delete"),
	
	# World Encounter Loot
	path('worldbuilder/universe/encounter/<int:in_worldencounter>/encounterloot/create/', views.worldencounterloot_create, name="worldencounterloot-create"),
	path('worldbuilder/universe/encounter/<int:in_worldencounter>/encounterloot/update/<int:pk>/', views.worldencounterloot_create, name="worldencounterloot-update"),
	path('worldbuilder/worldencounterloot/delete/<int:pk>/', views.worldencounterloot_delete, name="worldencounterloot-delete"),
]

urlpatterns += [
	# Dungeons
	path('worldbuilder/area/<int:in_area>/create/dungeon/', views.dungeon_create, name="dungeon-create"),
	path('worldbuilder/area/<int:in_area>/update/dungeon/<int:pk>/', views.dungeon_create, name="dungeon-update"),
	path('worldbuilder/dungeon/delete/<int:pk>/', views.dungeon_delete, name="dungeon-delete"),
	
	# Roomsets
	path('worldbuilder/dungeon/<int:in_dungeon>/create/roomset/', views.roomset_create, name="roomset-create"),
	path('worldbuilder/dungeon/<int:in_dungeon>/update/roomset/<int:pk>/', views.roomset_create, name="roomset-update"),
	path('worldbuilder/roomset/delete/<int:pk>/', views.roomset_delete, name="roomset-delete"),
	
	# Rooms
	path('worldbuilder/dungeon/roomset/<int:in_roomset>/create/room/', views.room_create, name="room-create"),
	path('worldbuilder/dungeon/roomset/<int:in_roomset>/create/room/<int:pk>/', views.room_create, name="room-update"),
	path('worldbuilder/room/delete/<int:pk>/', views.room_delete, name="room-delete"),
	
	# Room Loot
	path('worldbuilder/dungeon/room/<int:in_room>/loot/create/', views.roomloot_create, name="roomloot-create"),
	path('worldbuilder/dungeon/roomloot/delete/<int:pk>/', views.roomloot_delete, name="roomloot-delete"),
]

# CAMPAIGN FORMS

urlpatterns += [
	# Campaigns
	path('worldbuilder/<int:in_project>/create/campaign/', views.campaign_create, name="campaign-create"),
	path('worldbuilder/<int:in_project>/update/campaign/<int:pk>/', views.campaign_create, name="campaign-update"),
	path('worldbuilder/campaign/delete/<int:pk>/', views.campaign_delete, name="campaign-delete"),
	
	# Chapters
	path('worldbuilder/campaign/<int:in_campaign>/create/chapter/', views.chapter_create, name="chapter-create"),
	path('worldbuilder/campaign/<int:in_campaign>/update/chapter/<int:pk>/', views.chapter_create, name="chapter-update"),
	path('worldbuilder/chapter/<int:pk>/', views.chapter_delete, name="chapter-delete"),
	
	# Quests
	path('worldbuilder/chapter/<int:in_chapter>/create/quest/', views.quest_create, name="quest-create"),
	path('worldbuilder/chapter/<int:in_chapter>/update/quest/<int:pk>', views.quest_create, name="quest-update"),
	path('worldbuilder/quest/delete/<int:pk>/', views.quest_delete, name="quest-delete"),
	
	# Quest Encounters
	path('worldbuilder/quest/<int:in_quest>/encounter/create/', views.questencounter_create, name="questencounter-create"),
	path('worldbuilder/quest/<int:in_quest>/encounter/update/<int:pk>/', views.questencounter_create, name="questencounter-update"),
	path('worldbuilder/questencounter/delete/<int:pk>/', views.questencounter_delete, name="questencounter-delete"),
	
	# Quest Encounter Loot
	path('worldbuilder/questencounter/<int:in_questencounter>/encounterloot/create/', views.questencounterloot_create, name="questencounterloot-create"),
	path('worldbuilder/questencounter/encounterloot/delete/<int:pk>/', views.questencounterloot_delete, name="questencounterloot-delete"),
]

# ITEMLIST FORMS

urlpatterns += [
	# Itemlists
	path('worldbuilder/project/<int:in_project>/itemlist/create/', views.itemlist_create, name="itemlist-create"),
	path('worldbuilder/project/<int:in_project>/itemlist/update/<int:pk>/', views.itemlist_create, name="itemlist-update"),
	path('worldbuilder/itemlist/delete/<int:pk>/', views.itemlist_delete, name="itemlist-delete"),
	
	# Items
	path('worldbuilder/itemlist/<int:in_itemlist>/create/item/', views.item_create, name="item-create"),
	path('worldbuilder/itemlist/<int:in_itemlist>/update/item/<int:pk>/', views.item_create, name="item-update"),
	path('worldbuilder/item/delete/<int:pk>/', views.item_delete, name="item-delete"),
]

# PANTHEON FORMS

urlpatterns += [
	# Pantheons
	path('worldbuilder/universe/<int:in_universe>/create/pantheon/', views.pantheon_create, name="pantheon-create"),
	path('worldbuilder/universe/<int:in_universe>/update/pantheon/<int:pk>/', views.pantheon_create, name="pantheon-update"),
	path('worldbuilder/pantheon/delete/<int:pk>/', views.pantheon_delete, name="pantheon-delete"),
	
	# Gods
	path('worldbuilder/universe/pantheon/<int:in_pantheon>/create/god/', views.god_create, name="god-create"),
	path('worldbuilder/universe/pantheon/<int:in_pantheon>/update/god/<int:pk>/', views.god_create, name="god-update"),
	path('worldbuilder/god/delete/<int:pk>/', views.god_delete, name="god-delete"),
]
