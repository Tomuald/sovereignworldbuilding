# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from itertools import chain

from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory

from World.forms import UniverseModelForm, RegionModelForm, AreaModelForm, CityModelForm, CityQuarterModelForm, LocationModelForm, LocationLootModelForm, WorldEncounterModelForm, WorldEncounterLootModelForm, EmpireModelForm, FactionModelForm, NPCModelForm

from World.models import Universe, Region, Area, City, CityDemographics, CityQuarter, Location, LocationLoot, WorldEncounter, WorldEncounterLoot, Empire, Faction, NPC
from Project.models import Project
from Pantheon.models import Pantheon, God
from Dungeon.models import Dungeon, Room
from ItemList.models import Item

from World import decorators

##################
###   #VIEWS   ###
##################

@login_required
@decorators.universe_in_user_library
def universe_detail(request, pk):
	universe = Universe.objects.get(pk=pk)
	empires = Empire.objects.filter(in_universe=universe.id)
	regions = Region.objects.filter(in_universe=universe.id)
	factions = Faction.objects.filter(in_universe=universe.id)
	unaligned_npcs = NPC.objects.filter(in_universe=universe.id).filter(in_faction__isnull=True)
	pantheons = Pantheon.objects.filter(in_universe=universe.id)
	
	context = {
		'universe': universe,
		'empires': empires,
		'regions': regions,
		'factions': factions,
		'unaligned_npcs': unaligned_npcs,
		'pantheons': pantheons,
	}
	
	return render(request, "SovereignWebsite/universe_detail.html", context)

@login_required
@decorators.universe_in_user_library
def universe_index(request, pk):
	universe = Universe.objects.get(pk=pk)
	
	regions = Region.objects.filter(in_universe=universe.id)
	areas = Area.objects.filter(in_region__in_universe=universe.id)
	locations = Location.objects.filter(in_area__in_region__in_universe=universe.id)
	dungeons = Dungeon.objects.filter(in_area__in_region__in_universe=universe.id)
	empires = Empire.objects.filter(in_universe=universe.id)
	factions = Faction.objects.filter(in_universe=universe.id)
	npcs = NPC.objects.filter(in_universe=universe.id)
	pantheons = Pantheon.objects.filter(in_universe=universe.id)
	gods = God.objects.filter(in_pantheon__in_universe=universe.id)
	
	context = {
		'universe': universe,
		'regions': regions,
		'areas': areas,
		'locations': locations,
		'dungeons': dungeons,
		'empires': empires,
		'factions': factions,
		'npcs': npcs,
		'pantheons': pantheons,
		'gods': gods,
	}
	
	return render(request, "SovereignWebsite/universe_index.html", context=context)

@login_required
@decorators.region_in_user_library
def region_detail(request, pk):
	region = Region.objects.get(pk=pk)
	
	context = {
		'region': region,
	}
	
	return render(request, 'SovereignWebsite/region_detail.html', context)

@login_required
@decorators.area_in_user_library
def area_detail(request, pk):
	area = Area.objects.get(pk=pk)
	npcs = NPC.objects.filter(location__in_area=area.id).distinct()
	
	context = {
		'area': area,
		'npcs': npcs,
	}
	
	return render(request, 'SovereignWebsite/area_detail.html', context)

@login_required
@decorators.city_in_user_library
def city_detail(request, pk):
	city = City.objects.get(pk=pk)
	city_quarters = CityQuarter.objects.filter(in_city=city)
	
	context = {
		'city': city,
		'city_quarters': city_quarters,
	}
	
	return render(request, 'SovereignWebsite/city_detail.html', context)

@login_required
@decorators.cityquarter_in_user_library
def cityquarter_detail(request, pk):
	cityquarter = CityQuarter.objects.get(pk=pk)
	
	context = {
		'cityquarter': cityquarter,
	}
	
	return render(request, 'SovereignWebsite/cityquarter_detail.html', context)

@login_required	
@decorators.location_in_user_library
def location_detail(request, pk):
	location = Location.objects.get(pk=pk)
	
	context = {
		'location': location,
	}
	
	return render(request, 'SovereignWebsite/location_detail.html', context)

@login_required
@decorators.worldencounter_in_user_library
def worldencounter_detail(request, pk):
	worldencounter = WorldEncounter.objects.get(pk=pk)
	
	context = {
		'worldencounter': worldencounter,
	}
	
	return render(request, "SovereignWebsite/worldencounter_detail.html", context)

@login_required
@decorators.empire_in_user_library
def empire_detail(request, pk):
	empire = Empire.objects.get(pk=pk)
	
	context = {
		'empire': empire,
	}
	
	return render(request, "SovereignWebsite/empire_detail.html", context)

@login_required	
@decorators.faction_in_user_library
def faction_detail(request, pk):
	faction = Faction.objects.get(pk=pk)
	
	context = {
		'faction': faction,
	}
	
	return render(request, 'SovereignWebsite/faction_detail.html', context)

@login_required
@decorators.npc_in_user_library
def npc_detail(request, pk):
	npc = NPC.objects.get(pk=pk)
	locations = Location.objects.filter(NPCs__id=npc.id)
	
	context = {
		'npc': npc,
		'locations': locations,
	}
	
	return render(request, 'SovereignWebsite/npc_detail.html', context)
	
##################
###   #FORMS   ###
##################

@login_required
def universe_create(request, in_project, pk=None):
	in_project = Project.objects.get(id=in_project)
	
	if pk:
		universe = get_object_or_404(Universe, pk=pk)
	else:
		universe = Universe()
	
	form = UniverseModelForm(request.POST or None, initial={'in_project': in_project}, instance=universe)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('universe-detail', args=[str(universe.id)]))
	
	return render(request, 'SovereignWebsite/universe_form.html', {'form': form})

@login_required
@decorators.universe_in_user_library
def universe_delete(request, pk):
	universe = get_object_or_404(Universe, pk=pk)
	
	if request.method == 'POST':
		universe.delete()
		return HttpResponseRedirect(reverse('project-detail', args=[str(universe.in_project.id)]))
	
	return render(request, "SovereignWebsite/universe_confirm_delete.html", context={'universe': universe})

@login_required
def region_create(request, in_universe, pk=None):
	in_universe = Universe.objects.get(id=in_universe)
	universe_set = Universe.objects.filter(id=in_universe.id)
	
	if pk:
		region = get_object_or_404(Region, pk=pk)
	else:
		region = Region()
	
	form = RegionModelForm(universe_set,
						   request.POST or None,
						   initial={'in_universe': in_universe},
						   instance=region
						)
						
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('region-detail', args=[str(region.id)]))
		
	return render(request, 'SovereignWebsite/region_form.html', {'form': form})

@login_required	
@decorators.region_in_user_library
def region_delete(request, pk):
	region = get_object_or_404(Region, pk=pk)
	
	if request.method == 'POST':
		region.delete()
		return HttpResponseRedirect(reverse('universe-detail', args=[str(region.in_universe.id)]))
	
	return render(request, "SovereignWebsite/region_confirm_delete.html", context={'region': region})

@login_required	
def empire_create(request, in_universe, pk=None):
	in_universe = Universe.objects.get(id=in_universe)
	regions = Region.objects.filter(in_universe=in_universe.id)
	universe_set = Universe.objects.filter(id=in_universe.id)
	faiths = God.objects.filter(in_pantheon__in_universe=in_universe.id)
	
	if pk:
		empire = get_object_or_404(Empire, pk=pk)
	else:
		empire = Empire()
	
	form = EmpireModelForm(regions,
						   universe_set,
						   faiths,
						   request.POST or None,
						   initial={'in_universe': in_universe},
						   instance=empire
						)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('empire-detail', args=[str(empire.id)]))
	
	return render(request, 'SovereignWebsite/empire_form.html', {'form': form})

@login_required
@decorators.empire_in_user_library
def empire_delete(request, pk):
	empire = get_object_or_404(Empire, pk=pk)
	
	if request.method == 'POST':
		empire.delete()
		return HttpResponseRedirect(reverse('universe-detail', args=[str(empire.in_universe.id)]))
	
	return render(request, "SovereignWebsite/empire_confirm_delete.html", context={'empire': empire})

@login_required
def area_create(request, in_region, pk=None):
	in_region = Region.objects.get(id=in_region)
	regions = Region.objects.filter(in_universe=in_region.in_universe)
	factions = Faction.objects.filter(in_universe=in_region.in_universe)
	
	if pk:
		area = get_object_or_404(Area, pk=pk)
	else:
		area = Area()
	
	form = AreaModelForm(regions,
						 factions,
						 request.POST or None,
						 initial={'in_region': in_region},
						 instance=area
						)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('area-detail', args=[str(area.id)]))
	
	return render(request, 'SovereignWebsite/area_form.html', {'form': form, 'in_region': in_region})

@login_required
@decorators.area_in_user_library
def area_delete(request, pk):
	area = get_object_or_404(Area, pk=pk)
	
	if request.method == 'POST':
		area.delete()
		return HttpResponseRedirect(reverse('region-detail', args=[str(area.in_region.id)]))
	
	return render(request, "SovereignWebsite/area_confirm_delete.html", context={'area': area})

@login_required	
def city_create(request, in_region, pk=None):
	in_region = Region.objects.get(id=in_region)
	regions = Region.objects.filter(in_universe=in_region.in_universe)
	
	if pk:
		city = get_object_or_404(City, pk=pk)
	else:
		city = City()
	
	form = CityModelForm(regions, request.POST or None, initial={'in_region': in_region}, instance=city)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('city-detail', args=[str(city.id)]))
	
	return render(request, 'SovereignWebsite/city_form.html', {'form': form, 'in_region': in_region})

@login_required	
@decorators.city_in_user_library
def city_delete(request, pk):
	city = get_object_or_404(City, pk=pk)
	
	if request.method == 'POST':
		city.delete()
		return HttpResponseRedirect(reverse('region-detail', args=[str(city.in_region.id)]))
	
	return render(request, "SovereignWebsite/city_confirm_delete.html", context={'city': city})

@login_required	
def cityquarter_create(request, in_city, pk=None):
	in_city = City.objects.get(id=in_city)
	cities = City.objects.filter(in_region=in_city.in_region)
	factions = Faction.objects.filter(in_universe=in_city.in_region.in_universe)
	
	if pk:
		cityquarter = get_object_or_404(CityQuarter, pk=pk)
	else:
		cityquarter = CityQuarter()
	
	form = CityQuarterModelForm(cities,
								factions,
								request.POST or None,
								initial={'in_city': in_city},
								instance=cityquarter
							)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('cityquarter-detail', args=[str(cityquarter.id)]))
	
	return render(request, 'SovereignWebsite/cityquarter_form.html', {'form': form, 'in_city': in_city})

@login_required
@decorators.cityquarter_in_user_library
def cityquarter_delete(request, pk):
	cityquarter = get_object_or_404(CityQuarter, pk=pk)
	
	if request.method == 'POST':
		cityquarter.delete()
		return HttpResponseRedirect(reverse('city-detail', args=[str(cityquarter.in_city.id)]))
	
	return render(request, "SovereignWebsite/cityquarter_confirm_delete.html", context={'cityquarter': cityquarter})

@login_required
def citydemographics_create(request, in_city):
	in_city = City.objects.get(id=in_city)
	CityDemographicsInlineFormSet = inlineformset_factory(City, CityDemographics,
														  fields=('race', 'percent'),
														  can_delete=True
														)
	if request.method == 'POST':
		formset = CityDemographicsInlineFormSet(request.POST, instance=in_city)
		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(reverse('city-detail', args=[str(in_city.id)]))
	else:
		formset = CityDemographicsInlineFormSet(instance=in_city)
	
	return render(request, 'SovereignWebsite/citydemographics_form.html', {'formset': formset})

@login_required
def location_create(request, in_area=None, in_cityquarter=None, pk=None):
	if pk:
		location = get_object_or_404(Location, pk=pk)
	else:
		location = Location()
	
	if in_area:
		in_area = Area.objects.get(id=in_area)
		npcs = NPC.objects.filter(in_universe=in_area.in_region.in_universe)
		exit_points = Location.objects.filter(in_area=in_area).exclude(id=location.id)
		
		form = LocationModelForm(request.POST or None,
								 npcs=npcs,
								 exit_points=exit_points,
								 initial={'in_area': in_area,},
								 instance=location
								)
	
	if in_cityquarter:
		in_cityquarter = CityQuarter.objects.get(id=in_cityquarter)
		npcs = NPC.objects.filter(in_universe=in_cityquarter.in_city.in_region.in_universe)
		exit_points = Location.objects.filter(in_cityquarter=in_cityquarter).exclude(id=location.id)
		
		form = LocationModelForm(request.POST or None,
								 npcs=npcs,
								 exit_points=exit_points,
								 initial={'in_cityquarter': in_cityquarter,},
								 instance=location
								)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('location-detail', args=[str(location.id)]))
		
	return render(request, 'SovereignWebsite/location_form.html', {'form': form})

@login_required
@decorators.location_in_user_library
def location_delete(request, pk):
	location = get_object_or_404(Location, pk=pk)
	
	if request.method == 'POST':
		location.delete()
		if location.in_area:
			return HttpResponseRedirect(reverse('area-detail', args=[str(location.in_area.id)]))
		if location.in_cityquarter:
			return HttpResponseRedirect(reverse('cityquarter-detail', args=[str(location.in_cityquarter.id)]))
	
	return render(request, "SovereignWebsite/location_confirm_delete.html", context={'location': location})

@login_required
def npc_create(request, in_universe, in_faction=None, pk=None):
	in_universe = Universe.objects.get(id=in_universe)
	factions = Faction.objects.filter(in_universe=in_universe.id)
	universe_set = Universe.objects.filter(id=in_universe.id)
	faiths = God.objects.filter(in_pantheon__in_universe=in_universe.id)
	
	if in_faction is not None:
		in_faction = Faction.objects.get(id=in_faction)
	
	if pk:
		npc = get_object_or_404(NPC, pk=pk)
	else:
		npc = NPC()
	
	form = NPCModelForm(factions,
						universe_set,
						faiths,
						request.POST or None,
						initial={'in_universe': in_universe, 'in_faction': in_faction},
						instance=npc,
					)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('npc-detail', args=[str(npc.id)]))
	
	return render(request, 'SovereignWebsite/npc_form.html', {'form': form})

@login_required
@decorators.npc_in_user_library
def npc_delete(request, pk):
	npc = get_object_or_404(NPC, pk=pk)
	
	if request.method == 'POST':
		npc.delete()
		if npc.in_faction:
			return HttpResponseRedirect(reverse('faction-detail', args=[str(npc.in_faction.id)]))
		else:
			return HttpResponseRedirect(reverse('universe-detail', args=[str(npc.in_universe.id)]))
	
	return render(request, "SovereignWebsite/npc_confirm_delete.html", context={'npc': npc})

@login_required
def faction_create(request, in_universe, pk=None):
	in_universe = Universe.objects.get(id=in_universe)
	
	if pk:
		faction = get_object_or_404(Faction, pk=pk)	
	else:
		faction = Faction()
	
	leaders = NPC.objects.filter(in_universe=in_universe).filter(in_faction=faction.id)
	universe_set = Universe.objects.filter(id=in_universe.id)
	faiths = God.objects.filter(in_pantheon__in_universe=in_universe)
	form = FactionModelForm(leaders,
							universe_set,
							faiths,
							request.POST or None,
							initial={'in_universe': in_universe},
							instance=faction
						)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('faction-detail', args=[str(faction.id)]))
	
	return render(request, 'SovereignWebsite/faction_form.html', {'form': form, 'leaders': leaders})

@login_required
@decorators.faction_in_user_library
def faction_delete(request, pk):
	faction = get_object_or_404(Faction, pk=pk)
	
	if request.method == 'POST':
		faction.delete()
		return HttpResponseRedirect(reverse('faction-detail', args=[str(faction.in_universe.id)]))
	
	return render(request, "SovereignWebsite/faction_confirm_delete.html", context={'faction': faction})

@login_required
def locationloot_create(request, in_location):
	locationloot = LocationLoot()
	in_location = Location.objects.get(id=in_location)
	
	form = LocationLootModelForm(request.POST or None, initial={'in_location': in_location}, instance=locationloot)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('location-detail', args=[str(in_location.id)]))
	
	return render(request, 'SovereignWebsite/locationloot_form.html', {'form': form})

@login_required	
def locationloot_delete(request, pk):
	locationloot = LocationLoot.objects.get(pk=pk)
	in_location = locationloot.in_location
	
	if request.method == 'POST':
		locationloot.delete()
		return HttpResponseRedirect(reverse('location-detail', args=[str(in_location.id)]))
	
	return render(request, "SovereignWebsite/locationloot_confirm_delete.html", context={'locationloot': locationloot})

@login_required
def worldencounter_create(request, in_dungeon_room=None, in_location=None, pk=None):
	if pk:
		worldencounter = WorldEncounter.objects.get(pk=pk)
	else:
		worldencounter = WorldEncounter()
	
	if in_dungeon_room is not None:
		in_dungeon_room = Room.objects.get(id=in_dungeon_room)
		npcs = NPC.objects.filter(in_universe=in_dungeon_room.in_roomset.in_dungeon.in_area.in_region.in_universe)
		form = WorldEncounterModelForm(request.POST or None,
								  npcs=npcs,
								  initial={'in_dungeon_room': in_dungeon_room},
								  instance=worldencounter
								)
	if in_location is not None:
		in_location = Location.objects.get(id=in_location)
		if in_location.in_area:
			npcs = NPC.objects.filter(in_universe=in_location.in_area.in_region.in_universe)
		if in_location.in_cityquarter:
			npcs = NPC.objects.filter(in_universe=in_location.in_cityquarter.in_city.in_region.in_universe)
		
		form = WorldEncounterModelForm(request.POST or None,
								  npcs=npcs,
								  initial={'in_location': in_location},
								  instance=worldencounter
								)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('worldencounter-detail', args=[str(worldencounter.id)]))
	
	return render(request, "SovereignWebsite/worldencounter_form.html", {'form': form})

@login_required
@decorators.worldencounter_in_user_library
def worldencounter_delete(request, pk):
	worldencounter = WorldEncounter.objects.get(pk=pk)
	
	if request.method == 'POST':
		worldencounter.delete()
		if worldencounter.in_dungeon_room is not None:
			return HttpResponseRedirect(reverse('room-detail', args=[str(worldencounter.in_dungeon_room.id)]))
		if worldencounter.in_location is not None:
			return HttpResponseRedirect(reverse('location-detail', args=[str(worldencounter.in_location.id)]))
	
	return render(request, "SovereignWebsite/worldencounter_confirm_delete.html", context={'worldencounter': worldencounter})

@login_required
def worldencounterloot_create(request, in_worldencounter, pk=None):
	worldencounterloot = WorldEncounterLoot()
	in_worldencounter = WorldEncounter.objects.get(id=in_worldencounter)
	if in_worldencounter.in_location:
		if in_worldencounter.in_location.in_area:
			items = Item.objects.filter(
				in_itemlist__in_project=in_worldencounter.in_location.in_area.in_region.in_universe.in_project
			)
		if in_worldencounter.in_location.in_cityquarter:
			items = Item.objects.filter(	in_itemlist__in_project=in_worldencounter.in_location.in_cityquarter.in_city.in_region.in_universe.in_project
			)
	
	else:
		items = Item.objects.filter(	in_itemlist__in_project=in_worldencounter.in_dungeon_room.in_roomset.in_dungeon.in_area.in_region.in_universe.in_project
		)
	
	form = WorldEncounterLootModelForm(request.POST or None,
									   items=items,
									   initial={'in_worldencounter': in_worldencounter},
									   instance=worldencounterloot
									)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('worldencounter-detail', args=[str(in_worldencounter.id)]))
			
	return render(request, "SovereignWebsite/worldencounterloot_form.html", {'form': form})

@login_required
@decorators.worldencounterloot_in_user_library
def worldencounterloot_delete(request, pk):
	worldencounterloot = WorldEncounterLoot.objects.get(pk=pk)
	
	if request.method == 'POST':
		worldencounterloot.delete()
		return HttpResponseRedirect(reverse('worldencounter-detail', args=[str(worldencounterloot.in_worldencounter.id)]))
	
	return render(request, "SovereignWebsite/worldencounterloot_confirm_delete.html", {'worldencounterloot': worldencounterloot})
	

