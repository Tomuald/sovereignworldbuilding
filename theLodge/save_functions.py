# REMEMBER TO CHECK ABOUT UPDATING FOREIGN KEYS. IF NOT, THEY LINK
# TO THE ORIGINAL OBJECT.

import asyncio

def save_itemlist(itemlist, to_project):
    items = itemlist.item_set.all()

    itemlist.pk = None
    itemlist.in_project = to_project
    itemlist.save()

    for item in items:
        save_item(item, itemlist, itemlist.in_project)

def save_item(item, to_itemlist, to_project):
    item.pk = None
    item.in_project = to_project
    item.in_itemlist = to_itemlist
    item.save()

def save_universe(universe, to_project):
    pantheons = universe.pantheon_set.all()
    npcs = universe.npc_set.filter(in_faction__isnull=True)
    regions = universe.region_set.all()
    empires = universe.empire_set.all()

    universe.pk = None
    universe.in_project = to_project
    universe.save()

    for pantheon in pantheons:
        save_pantheon(pantheon, universe, to_project)

    for npc in npcs:
        faiths = npc.faiths.all()
        save_npc(npc, universe, to_project, faiths)

    for region in regions:
        save_region(region, universe, to_project)

    for empire in empires:
        save_empire(empire, universe, to_project)


def save_pantheon(pantheon, to_universe, to_project):
    gods = pantheon.god_set.all()

    pantheon.pk = None
    pantheon.in_universe = to_universe
    pantheon.in_project = to_project
    pantheon.save()

    for god in gods:
        save_god(god, pantheon, to_project)

def save_god(god, to_pantheon, to_project):
    god.pk = None
    god.in_pantheon = to_pantheon
    god.in_project = to_project
    god.save()

def save_npc(npc, to_universe, to_project, faiths):
    npc.pk = None
    npc.in_universe = to_universe
    npc.in_project = to_project
    npc.save()

    for faith in faiths:
        god = npc.in_project.god_set.get(name=faith.name)
        npc.faiths.add(god)

def save_region(region, to_universe, to_project):
    region.pk = None
    region.in_universe = to_universe
    region.in_project = to_project
    region.save()

def save_empire(empire, to_universe, to_project):
    faiths = empire.faiths.all()
    regions = empire.regions.all()

    empire.pk = None
    empire.in_universe = to_universe
    empire.in_project = to_project
    empire.save()

    for faith in faiths:
        god = empire.in_project.god_set.get(name=faith.name)
        empire.faiths.add(god)

    # This fails if regions haven't been imported yet...
    # REMEMBER TO RUN A FUNCTION TO CHANGE URLs!
    for r in regions:
        region = empire.in_project.region_set.get(name=r.name)
        empire.regions.add(region)
