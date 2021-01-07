from Project.models import Project
from django.shortcuts import get_object_or_404

import re

def clean_urls(string, new_project):
    pattern = r"/worldbuilder/p/[0-9]+/"
    new_url = '/worldbuilder/p/%d/' % new_project
    clean = re.sub(pattern, new_url, string)

    return clean

def save_project(user, project):
    old_project = get_object_or_404(Project, id=project.id)
    itemlists = old_project.itemlist_set.all()
    universes = old_project.universe_set.all()
    pantheons = old_project.pantheon_set.all()
    gods = old_project.god_set.all()
    campaigns = old_project.campaign_set.all()
    regions = old_project.region_set.all()
    empires = old_project.empire_set.all()
    factions = old_project.faction_set.all()
    npcs = old_project.npc_set.all()
    chapters = old_project.chapter_set.all()
    areas = old_project.area_set.all()
    cities = old_project.city_set.all()
    demographics = old_project.citydemographics_set.all()
    cityquarters = old_project.cityquarter_set.all()
    quests = old_project.quest_set.all()
    locations = old_project.location_set.all()
    locationloot = old_project.locationloot_set.all()
    dungeons = old_project.dungeon_set.all()
    roomsets = old_project.roomset_set.all()
    dungeon_rooms = old_project.room_set.all()
    roomloot = old_project.roomloot_set.all()
    worldencounters = old_project.worldencounter_set.all()
    worldencounterloot = old_project.worldencounterloot_set.all()
    questencounters = old_project.questencounter_set.all()
    questencounterloot = old_project.questencounterloot_set.all()

    project.pk = None
    project.save()
    user.user_library.add(project)
    user.save()

    for itemlist in itemlists:
        save_itemlist(itemlist, project)

    for universe in universes:
        save_universe(universe, project)

    for pantheon in pantheons:
        save_pantheon(pantheon, project)

    for god in gods:
        save_god(god, project)

    for campaign in campaigns:
        save_campaign(campaign, project)

    for region in regions:
        save_region(region, project)

    for empire in empires:
       save_empire(empire, project)

    for faction in factions:
        save_faction(faction, project)

    for npc in npcs:
        save_npc(npc, project)

    for chapter in chapters:
        save_chapter(chapter, project)

    for area in areas:
        save_area(area, project)

    for city in cities:
        save_city(city, project)

    for demographic in demographics:
        save_citydemographics(demographic, project)

    for quarter in cityquarters:
        save_cityquarter(quarter, project)

    for quest in quests:
        save_quest(quest, project)

    # Populate a list that stores a tuple (location, [exit_points]),
    # this needs to be done because an unsaved location cannot be added
    # as an exit_point.
    location_exits = []
    for location in locations:
        location_exits.append((location, location.exit_points.all()))
        save_location(location, project)

    for loot in locationloot:
        save_locationloot(loot, project)

    for exit in location_exits:
        save_location_exits(exit, project)

    for dungeon in dungeons:
        save_dungeon(dungeon, project)

    for roomset in roomsets:
        save_roomset(roomset, project)

    room_exits = []
    for room in dungeon_rooms:
        room_exits.append((room, room.exits.all()))
        save_room(room, project)

    for loot in roomloot:
        save_roomloot(loot, project)

    for exit in room_exits:
        save_room_exits(exit, project)

    for encounter in worldencounters:
        save_worldencounter(encounter, project)

    for loot in worldencounterloot:
        save_worldencounterloot(loot, project)

    for encounter in questencounters:
        save_questencounter(encounter, project)

    for loot in questencounterloot:
        save_questencounterloot(loot, project)

def save_full_universe(universe, project):
    old_project = universe.in_project

    pantheons = old_project.pantheon_set.all()
    gods = old_project.god_set.all()
    regions = old_project.region_set.all()
    empires = old_project.empire_set.all()
    factions = old_project.faction_set.all()
    npcs = old_project.npc_set.all()
    areas = old_project.area_set.all()
    cities = old_project.city_set.all()
    demographics = old_project.citydemographics_set.all()
    cityquarters = old_project.cityquarter_set.all()
    locations = old_project.location_set.all()
    locationloot = old_project.locationloot_set.all()
    dungeons = old_project.dungeon_set.all()
    roomsets = old_project.roomset_set.all()
    dungeon_rooms = old_project.room_set.all()
    roomloot = old_project.roomloot_set.all()
    worldencounters = old_project.worldencounter_set.all()
    worldencounterloot = old_project.worldencounterloot_set.all()

    universe.pk = None
    universe.in_project = project
    universe.description = clean_urls(universe.description, project.id)
    universe.save()

    for pantheon in pantheons:
        save_pantheon(pantheon, project)

    for god in gods:
        save_god(god, project)

    for region in regions:
        save_region(region, project)

    for empire in empires:
       save_empire(empire, project)

    for faction in factions:
        save_faction(faction, project)

    for npc in npcs:
        save_npc(npc, project)

    for area in areas:
        save_area(area, project)

    for city in cities:
        save_city(city, project)

    for demographic in demographics:
        save_citydemographics(demographic, project)

    for quarter in cityquarters:
        save_cityquarter(quarter, project)

    # Populate a list that stores a tuple (location, [exit_points]),
    # this needs to be done because an unsaved location cannot be added
    # as an exit_point.
    location_exits = []
    for location in locations:
        location_exits.append((location, location.exit_points.all()))
        save_location(location, project)

    for loot in locationloot:
        save_locationloot(loot, project)

    for exit in location_exits:
        save_location_exits(exit, project)

    for dungeon in dungeons:
        save_dungeon(dungeon, project)

    for roomset in roomsets:
        save_roomset(roomset, project)

    room_exits = []
    for room in dungeon_rooms:
        room_exits.append((room, room.exits.all()))
        save_room(room, project)

    for loot in roomloot:
        save_roomloot(loot, project)

    for exit in room_exits:
        save_room_exits(exit, project)

    for encounter in worldencounters:
        save_worldencounter(encounter, project)

    for loot in worldencounterloot:
        save_worldencounterloot(loot, project)

def save_location_exits(exit, new_project):
    l = get_object_or_404(new_project.location_set, name=exit[0])

    if len(exit[1]) > 0:
        for ex in exit[1]:
            e = get_object_or_404(new_project.location_set, name=ex)
            l.exit_points.add(e)
    else:
        pass

def save_itemlist(itemlist, new_project):
    items = itemlist.item_set.all()

    itemlist.pk = None
    itemlist.in_project = new_project
    itemlist.description = clean_urls(
            itemlist.description,
            new_project.id
        )
    itemlist.save()

    for item in items:
        save_item(item, itemlist, new_project)

def save_item(item, to_itemlist, new_project):
    item.pk = None
    item.in_project = new_project
    item.in_itemlist = to_itemlist
    item.description = clean_urls(
            item.description,
            new_project.id
        )
    item.save()

def save_universe(universe, new_project):
    universe.pk = None
    universe.in_project = new_project
    universe.description = clean_urls(
            universe.description,
            new_project.id
        )
    universe.save()

def save_campaign(campaign, new_project):
    campaign.pk = None
    campaign.in_project = new_project
    campaign.in_universe = get_object_or_404(
            new_project.universe_set, name=campaign.in_universe
        )
    campaign.overview = clean_urls(
            campaign.overview,
            new_project.id
        )
    campaign.save()

def save_region(region, new_project):
    region.pk = None
    region.in_project = new_project
    region.in_universe = get_object_or_404(
            new_project.universe_set, name=region.in_universe
        )
    region.description = clean_urls(
            region.description,
            new_project.id
        )
    region.save()

def save_empire(empire, new_project):
    regions = empire.regions.all()
    faiths = empire.faiths.all()

    empire.pk = None
    empire.in_project = new_project
    empire.in_universe = get_object_or_404(
            new_project.universe_set, name=empire.in_universe
        )
    empire.description = clean_urls(empire.description, new_project.id)
    empire.save()

    for region in regions:
        r = get_object_or_404(new_project.region_set, name=region)
        empire.regions.add(r)

    for faith in faiths:
        god = get_object_or_404(new_project.god_set, name=faith)
        empire.faiths.add(god)

def save_pantheon(pantheon, new_project):
    pantheon.pk = None
    pantheon.in_project = new_project
    pantheon.in_universe = get_object_or_404(
            new_project.universe_set, name=pantheon.in_universe
        )
    pantheon.background = clean_urls(pantheon.background, new_project.id)
    pantheon.save()

def save_god(god, new_project):
    god.pk = None
    god.in_project = new_project
    god.in_pantheon = get_object_or_404(
            new_project.pantheon_set, name=god.in_pantheon
        )
    god.background = clean_urls(god.background, new_project.id)
    god.save()

def save_faction(faction, new_project):
    faiths = faction.faiths.all()

    faction.pk = None
    faction.in_project = new_project
    faction.in_universe = get_object_or_404(
            new_project.universe_set, name=faction.in_universe
        )
    faction.description = clean_urls(faction.description, new_project.id)
    faction.save()

    for faith in faiths:
        god = get_object_or_404(new_project.god_set, name=faith)
        faction.faiths.add(god)

def save_npc(npc, new_project):
    faiths = npc.faiths.all()

    npc.pk = None
    npc.in_project = new_project
    npc.in_universe = get_object_or_404(
            new_project.universe_set, name=npc.in_universe
        )
    if npc.in_faction:
        npc.in_faction = get_object_or_404(
                new_project.faction_set, name=npc.in_faction
            )
    if npc.leader_of:
        npc.leader_of = get_object_or_404(
                new_project.faction_set, name=npc.leader_of
            )
    npc.description = clean_urls(npc.description, new_project.id)
    npc.save()

    for faith in faiths:
        god = get_object_or_404(new_project.god_set, name=faith)
        npc.faiths.add(god)


def save_chapter(chapter, new_project):
    npcs = chapter.involved_npcs.all()
    regions = chapter.regions.all()

    chapter.pk = None
    chapter.in_project = new_project
    chapter.in_campaign = get_object_or_404(
            new_project.campaign_set, title=chapter.in_campaign
        )
    chapter.summary = clean_urls(chapter.summary, new_project.id)
    chapter.save()

    for npc in npcs:
        n = get_object_or_404(new_project.npc_set, name=npc)
        chapter.involved_npcs.add(n)
    for region in regions:
        r = get_object_or_404(new_project.region_set, name=region)
        chapter.regions.add(r)

def save_area(area, new_project):
    factions = area.factions.all()

    area.pk = None
    area.in_project = new_project
    area.in_region = get_object_or_404(
            new_project.region_set, name=area.in_region
        )
    area.description = clean_urls(area.description, new_project.id)
    area.save()

    for faction in factions:
        f = get_object_or_404(new_project.faction_set, name=faction)
        area.factions.add(f)

def save_city(city, new_project):
    city.pk = None
    city.in_project = new_project
    city.in_region = get_object_or_404(
            new_project.region_set, name=city.in_region
        )
    city.description = clean_urls(city.description, new_project.id)
    city.save()

def save_citydemographics(demographic, new_project):
    demographic.pk = None
    demographic.in_project = new_project
    demographic.in_city = get_object_or_404(
            new_project.city_set, name=demographic.in_city
        )
    demographic.save()

def save_cityquarter(quarter, new_project):
    factions = quarter.factions.all()

    quarter.pk = None
    quarter.in_project = new_project
    quarter.in_city = get_object_or_404(
            new_project.city_set, name=quarter.in_city
        )
    quarter.description = clean_urls(quarter.description, new_project.id)
    quarter.save()

    for faction in factions:
        f = get_object_or_404(new_project.faction_set, name=faction)
        quarter.factions.add(f)

def save_quest(quest, new_project):
    areas = quest.in_areas.all()
    cities = quest.in_cities.all()
    npcs = quest.involved_npcs.all()

    quest.pk = None
    quest.in_project = new_project
    quest.in_chapter = get_object_or_404(
            new_project.chapter_set, title=quest.in_chapter
        )
    quest.summary = clean_urls(quest.summary, new_project.id)
    quest.save()

    for area in areas:
        a = get_object_or_404(
                new_project.area_set, name=area
            )
        quest.in_areas.add(a)

    for city in cities:
        c = get_object_or_404(
                new_project.city_set, name=city
            )
        quest.in_cities.add(c)

    for npc in npcs:
        n = get_object_or_404(
                new_project.npc_set, name=npc
            )
        quest.involved_npcs.add(n)

def save_location(location, new_project):
    npcs = location.NPCs.all()
    exits = location.exit_points.all()

    location.pk = None
    location.in_project = new_project
    if location.in_area:
        location.in_area = get_object_or_404(
                new_project.area_set, name=location.in_area
            )
    if location.in_cityquarter:
        location.in_cityquarter = get_object_or_404(
                new_project.cityquarter_set, name=location.in_cityquarter
            )
    location.description = clean_urls(location.description, new_project.id)
    location.save()

    for npc in npcs:
        n = get_object_or_404(new_project.npc_set, name=npc)
        location.NPCs.add(n)

def save_locationloot(loot, new_project):
    loot.pk = None
    loot.name = get_object_or_404(new_project.item_set, name=loot.name)
    loot.in_project = new_project
    loot.in_location = get_object_or_404(
            new_project.location_set, name=loot.in_location
        )
    loot.save()

def save_dungeon(dungeon, new_project):
    dungeon.pk = None
    dungeon.in_project = new_project
    dungeon.in_area = get_object_or_404(
            new_project.area_set, name=dungeon.in_area
        )
    dungeon.description = clean_urls(dungeon.description, new_project.id)
    dungeon.save()

def save_roomset(roomset, new_project):
    roomset.pk = None
    roomset.in_project = new_project
    roomset.in_dungeon = get_object_or_404(
            new_project.dungeon_set, title=roomset.in_dungeon
        )
    roomset.description = clean_urls(roomset.description, new_project.id)
    roomset.save()

def save_room(room, new_project):
    room.pk = None
    room.in_project = new_project
    room.in_roomset = get_object_or_404(
            new_project.roomset_set, name=room.in_roomset
        )
    room.description = clean_urls(room.description, new_project.id)
    room.save()

def save_roomloot(loot, new_project):
    loot.pk = None
    loot.name = get_object_or_404(new_project.item_set, name=loot.name)
    loot.in_project = new_project
    loot.in_room = get_object_or_404(new_project.room_set, name=loot.in_room)
    loot.save()

def save_room_exits(exit, new_project):
    ro = get_object_or_404(new_project.room_set, name=exit[0])

    if len(exit[1]) > 0:
        for ex in exit[1]:
            e = get_object_or_404(new_project.room_set, name=ex)
            ro.exits.add(e)
    else:
        pass

def save_worldencounter(encounter, new_project):
    npcs = encounter.involved_npcs.all()

    encounter.pk = None
    encounter.in_project = new_project
    if encounter.in_location:
        encounter.in_location = get_object_or_404(
                new_project.location_set, name=encounter.in_location
            )
    if encounter.in_dungeon_room:
        encounter.in_dungeon_room = get_object_or_404(
                new_project.room_set, name=encounter.in_dungeon_room
            )
    encounter.summary = clean_urls(encounter.summary, new_project.id)
    encounter.save()

    for npc in npcs:
        n = get_object_or_404(new_project.npc_set, name=npc)
        encounter.involved_npcs.add(n)

def save_worldencounterloot(loot, new_project):
    loot.pk = None
    loot.name = get_object_or_404(new_project.item_set, name=loot.name)
    loot.in_project = new_project
    loot.in_worldencounter = get_object_or_404(
            new_project.worldencounter_set, title=loot.in_worldencounter
        )
    loot.save()

def save_questencounter(encounter, new_project):
    npcs = encounter.involved_npcs.all()

    encounter.pk = None
    encounter.in_project = new_project
    encounter.in_quest = get_object_or_404(
            new_project.quest_set, title=encounter.in_quest
        )
    if encounter.in_location:
        encounter.in_location = get_object_or_404(
                new_project.location_set, name=encounter.in_location
            )
    if encounter.in_dungeon_room:
        encounter.in_dungeon_room = get_object_or_404(
                new_project.room_set, name=encounter.in_dungeon_room
            )
    encounter.summary = clean_urls(encounter.summary, new_project.id)
    encounter.save()

    for npc in npcs:
        n = get_object_or_404(new_project.npc_set, name=npc)
        encounter.involved_npcs.add(n)


def save_questencounterloot(loot, new_project):
    loot.pk = None
    loot.name = get_object_or_404(new_project.item_set, name=loot.name)
    loot.in_project = new_project
    loot.in_questencounter = get_object_or_404(
            new_project.questencounter_set, title=loot.in_questencounter
        )
    loot.save()
