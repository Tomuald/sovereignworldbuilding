# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from itertools import chain

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.forms import inlineformset_factory, formset_factory

from World.forms import UniverseModelForm, RegionModelForm, AreaModelForm, CityModelForm, CityQuarterModelForm, LocationModelForm, LocationLootModelForm, WorldEncounterModelForm, WorldEncounterLootModelForm, EmpireModelForm, FactionModelForm, NPCModelForm, CityDemographicsModelForm

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
def universe_detail(request, in_project, name):
	project = Project.objects.get(id=in_project)
	universe = project.universe_set.get(name=name)
	empires = universe.empire_set.all()
	regions = universe.region_set.all()
	factions = universe.faction_set.all()
	unaligned_npcs = universe.npc_set.filter(in_faction__isnull=True)
	pantheons = universe.pantheon_set.all()

	context = {
		'universe': universe,
		'empires': empires,
		'regions': regions,
		'factions': factions,
		'unaligned_npcs': unaligned_npcs,
		'pantheons': pantheons,
	}

	return render(request, "universe_detail.html", context)

@login_required
@decorators.universe_in_user_library
def universe_index(request, in_project, name):
	project = Project.objects.get(id=in_project)
	universe = project.universe_set.get(name=name)

	regions = universe.region_set.all()
	areas = project.area_set.all()
	locations = project.location_set.all()
	dungeons = project.dungeon_set.all()
	empires = project.empire_set.all()
	factions = project.faction_set.all()
	npcs = project.npc_set.all()
	pantheons = project.pantheon_set.all()
	gods = project.god_set.all()

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

	return render(request, "universe_index.html", context=context)

@login_required
@decorators.region_in_user_library
def region_detail(request, in_project, name):
	project = Project.objects.get(id=in_project)
	regions = project.region_set.all()
	region = get_object_or_404(regions, name=name)

	context = {'region': region}

	return render(request, 'region_detail.html', context)

@login_required
@decorators.area_in_user_library
def area_detail(request, in_project, name):
	project = Project.objects.get(id=in_project)
	areas = project.area_set.all()
	area = get_object_or_404(areas, name=name)
	npcs = project.npc_set.filter(location__in_area=area).distinct()

	context = {
		'area': area,
		'npcs': npcs,
	}

	return render(request, 'area_detail.html', context)

@login_required
@decorators.city_in_user_library
def city_detail(request, in_project, name):
	project = Project.objects.get(id=in_project)
	cities = project.city_set.all()
	city = get_object_or_404(cities, name=name)
	city_quarters = city.cityquarter_set.all()

	context = {
		'city': city,
		'city_quarters': city_quarters,
	}

	return render(request, 'city_detail.html', context)

@login_required
@decorators.cityquarter_in_user_library
def cityquarter_detail(request, in_project, name):
	project = Project.objects.get(id=in_project)
	cityquarters = project.cityquarter_set.all()
	cityquarter = get_object_or_404(cityquarters, name=name)

	context = {'cityquarter': cityquarter}

	return render(request, 'cityquarter_detail.html', context)

@login_required
@decorators.location_in_user_library
def location_detail(request, in_project, name):
	project = Project.objects.get(id=in_project)
	locations = project.location_set.all()
	location = get_object_or_404(locations, name=name)

	context = {'location': location}

	return render(request, 'location_detail.html', context)

@login_required
@decorators.worldencounter_in_user_library
def worldencounter_detail(request, in_project, title):
	project = Project.objects.get(id=in_project)
	worldencounters = project.worldencounter_set.all()
	worldencounter = get_object_or_404(worldencounters, title=title)

	context = {'worldencounter': worldencounter}

	return render(request, "worldencounter_detail.html", context)

@login_required
@decorators.empire_in_user_library
def empire_detail(request, in_project, name):
	project = Project.objects.get(id=in_project)
	empires = project.empire_set.all()
	empire = get_object_or_404(empires, name=name)

	context = {'empire': empire}

	return render(request, "empire_detail.html", context)

@login_required
@decorators.faction_in_user_library
def faction_detail(request, in_project, name):
	project = Project.objects.get(id=in_project)
	factions = project.faction_set.all()
	faction = get_object_or_404(factions, name=name)

	context = {'faction': faction}

	return render(request, 'faction_detail.html', context)

@login_required
@decorators.npc_in_user_library
def npc_detail(request, in_project, name):
	project = Project.objects.get(id=in_project)
	npcs = project.npc_set.all()
	npc = get_object_or_404(npcs, name=name)
	locations = project.location_set.filter(NPCs__id=npc.id)

	context = {
		'npc': npc,
		'locations': locations,
	}

	return render(request, 'npc_detail.html', context)

##################
###   #FORMS   ###
##################

@login_required
@decorators.create_universe_in_user_library
def universe_create(request, in_project):
	in_project = Project.objects.get(id=in_project)
	universes = in_project.universe_set.all()

	universe = Universe()

	form = UniverseModelForm(universes, request.POST or None, initial={'in_project': in_project}, instance=universe)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('universe-detail',
						args=[
							str(universe.in_project.id),
							str(universe.name)
						]))

	return render(request, 'universe_form.html', {'form': form})

@login_required
@decorators.universe_in_user_library
def universe_update(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	universes = in_project.universe_set.all()

	universe = get_object_or_404(universes, name=name)

	form = UniverseModelForm(universes, request.POST or None, initial={'in_project': in_project}, instance=universe)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('universe-detail',
						args=[
							str(universe.in_project.id),
							str(universe.name)
						]))

	return render(request, 'universe_form.html', {'form': form})

@login_required
@decorators.universe_in_user_library
def universe_delete(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	universes = in_project.universe_set.all()

	universe = get_object_or_404(universes, name=name)

	if request.method == 'POST':
		universe.delete()
		return HttpResponseRedirect(
				reverse('project-detail',
					args=[
						str(universe.in_project.id)
					]))

	return render(request, "universe_confirm_delete.html", context={'universe': universe})

@login_required
@decorators.create_region_in_user_library
def region_create(request, in_project, in_universe):
	in_project = Project.objects.get(id=in_project)
	regions = in_project.region_set.all()
	universes = in_project.universe_set.all()
	in_universe = get_object_or_404(universes, name=in_universe)

	region = Region()

	form = RegionModelForm(regions,
						   request.POST or None,
						   initial={'in_universe': in_universe, 'in_project': in_project},
						   instance=region
						)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('region-detail',
						args=[
							str(region.in_project.id),
							str(region.name)
					]))

	return render(request, 'region_form.html', {'form': form})

@login_required
@decorators.region_in_user_library
def region_update(request, in_project, name):
		in_project = Project.objects.get(id=in_project)
		regions = in_project.region_set.all()
		region = get_object_or_404(regions, name=name)

		in_universe = region.in_universe

		form = RegionModelForm(regions,
							   request.POST or None,
							   instance=region
							)

		if request.method == 'POST':
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(
						reverse('region-detail',
							args=[
								str(region.in_project.id),
								str(region.name)]))

		return render(request, 'region_form.html', {'form': form})

@login_required
@decorators.region_in_user_library
def region_delete(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	regions = in_project.region_set.all()
	region = get_object_or_404(regions, name=name)

	if request.method == 'POST':
		region.delete()
		return HttpResponseRedirect(
				reverse('universe-detail',
					args=[
						str(region.in_project.id),
						str(region.in_universe.name)])
				)

	return render(request, "region_confirm_delete.html", context={'region': region})

@login_required
@decorators.create_area_in_user_library
def area_create(request, in_project, in_region):
	in_project = Project.objects.get(id=in_project)
	regions = in_project.region_set.all()
	in_region = get_object_or_404(regions, name=in_region)
	factions = in_project.faction_set.all()
	areas = in_project.area_set.all()

	area = Area()

	form = AreaModelForm(areas,
						 factions,
						 request.POST or None,
						 initial={'in_region': in_region, 'in_project': in_project},
						 instance=area
						)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('area-detail',
						args=[
							str(area.in_project.id),
							str(area.name)
					]))

	return render(request, 'area_form.html', {'form': form})

@login_required
@decorators.area_in_user_library
def area_update(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	factions = in_project.faction_set.all()
	areas = in_project.area_set.all()

	area = get_object_or_404(areas, name=name)

	form = AreaModelForm(areas,
						 factions,
						 request.POST or None,
						 instance=area
						)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('area-detail',
						args=[
							str(area.in_project.id),
							str(area.name)
					]))

	return render(request, 'area_form.html', {'form': form})

@login_required
@decorators.area_in_user_library
def area_delete(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	areas = in_project.area_set.all()

	area = get_object_or_404(areas, name=name)

	if request.method == 'POST':
		area.delete()
		return HttpResponseRedirect(
				reverse('region-detail',
					args=[
						str(area.in_project.id),
						str(area.in_region.name)])
				)

	return render(request, "area_confirm_delete.html", context={'area': area})

@login_required
@decorators.create_city_in_user_library
def city_create(request, in_project, in_region):
	in_project = Project.objects.get(id=in_project)
	regions = in_project.region_set.all()
	in_region = get_object_or_404(regions, name=in_region)
	cities = in_project.city_set.all()

	city = City()

	form = CityModelForm(cities, request.POST or None, initial={'in_region': in_region, 'in_project': in_project}, instance=city)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('city-detail',
						args=[
							str(city.in_project.id),
							str(city.name)
					]))

	return render(request, 'city_form.html', {'form': form})

@login_required
@decorators.city_in_user_library
def city_update(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	cities = City.objects.filter(in_project=in_project)
	city = get_object_or_404(cities, name=name)

	form = CityModelForm(cities, request.POST or None, instance=city)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('city-detail',
						args=[
							str(city.in_project.id),
							str(city.name)
					]))

	return render(request, 'city_form.html', {'form': form})

@login_required
@decorators.city_in_user_library
def city_delete(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	cities = City.objects.filter(in_project=in_project)
	city = get_object_or_404(cities, name=name)

	if request.method == 'POST':
		city.delete()
		return HttpResponseRedirect(
				reverse('region-detail',
					args=[
						str(city.in_project.id),
						str(city.in_region.name)])
				)
	return render(request, "city_confirm_delete.html", context={'city': city})

@login_required
@decorators.create_cityquarter_in_user_library
def cityquarter_create(request, in_project, in_city):
	in_project = Project.objects.get(id=in_project)
	cities = in_project.city_set.all()
	in_city = get_object_or_404(cities, name=in_city)
	factions = in_project.faction_set.all()
	cityquarters = in_project.cityquarter_set.all()

	cityquarter = CityQuarter()

	form = CityQuarterModelForm(cityquarters,
								factions,
								request.POST or None,
								initial={'in_city': in_city, 'in_project': in_project},
								instance=cityquarter
							)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('cityquarter-detail',
						args=[
							str(cityquarter.in_project.id),
							str(cityquarter.name)
					]))

	return render(request, 'cityquarter_form.html', {'form': form})

@login_required
@decorators.cityquarter_in_user_library
def cityquarter_update(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	factions = in_project.faction_set.all()
	cityquarters = in_project.cityquarter_set.all()
	cityquarter = get_object_or_404(cityquarters, name=name)

	form = CityQuarterModelForm(cityquarters,
								factions,
								request.POST or None,
								instance=cityquarter
							)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('cityquarter-detail',
						args=[
							str(cityquarter.in_project.id),
							str(cityquarter.name)
					]))

	return render(request, 'cityquarter_form.html', {'form': form})

@login_required
@decorators.cityquarter_in_user_library
def cityquarter_delete(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	cityquarters = in_project.cityquarter_set.all()
	cityquarter = get_object_or_404(cityquarters, name=name)

	if request.method == 'POST':
		cityquarter.delete()
		return HttpResponseRedirect(
				reverse('city-detail',
					args=[
						str(cityquarter.in_project.id),
						str(cityquarter.in_city.name)])
				)

	return render(request, "cityquarter_confirm_delete.html", context={'cityquarter': cityquarter})

@login_required
@decorators.create_citydemographics_in_user_library
def citydemographics_create(request, in_project, in_city):
	in_project = Project.objects.get(id=in_project)
	cities = in_project.city_set.all()
	in_city = get_object_or_404(cities, name=in_city)

	citydemographics = CityDemographics()

	form = CityDemographicsModelForm(request.POST or None, initial={'in_project': in_project, 'in_city': in_city}, instance=citydemographics)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('city-detail',
						args=[
							str(citydemographics.in_project.id),
							str(citydemographics.in_city.name),
						]))

	return render(request, 'citydemographics_form.html', {'form': form})

@login_required
@decorators.citydemographics_in_user_library
def citydemographics_delete(request, in_project, pk):
	in_project = Project.objects.get(id=in_project)
	citydemography = in_project.citydemographics_set.all()
	citydemographics = get_object_or_404(citydemography, pk=pk)

	if request.method == 'POST':
		citydemographics.delete()
		return HttpResponseRedirect(
				reverse('city-detail',
					args=[
						str(citydemographics.in_project.id),
						str(citydemographics.in_city.name),
					]))
	return render(request, "citydemographics_confirm_delete.html", context={'citydemographics': citydemographics})

@login_required
def location_create(request, in_project, in_area=None, in_cityquarter=None):
	in_project = Project.objects.get(id=in_project)
	locations = in_project.location_set.all()
	npcs = in_project.npc_set.all()

	location = Location()

	if in_area:
		areas = in_project.area_set.all()
		in_area = get_object_or_404(areas, name=in_area)
		exit_points = locations.filter(in_area=in_area).exclude(id=location.id)

	if in_cityquarter:
		cityquarters = in_project.cityquarter_set.all()
		in_cityquarter = get_object_or_404(cityquarters, name=in_cityquarter)
		exit_points = locations.filter(
				in_cityquarter=in_cityquarter
					).exclude(id=location.id)

	form = LocationModelForm(locations,
							 npcs,
							 exit_points,
							 request.POST or None,
							 initial={'in_area': in_area, 'in_project': in_project, 'in_cityquarter': in_cityquarter},
							 instance=location
							)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('location-detail',
						args=[
							str(location.in_project.id),
							str(location.name)
					]))

	return render(request, 'location_form.html', {'form': form})

@login_required
@decorators.location_in_user_library
def location_update(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	locations = in_project.location_set.all()
	npcs = in_project.npc_set.all()

	location = get_object_or_404(locations, name=name)

	if location.in_area:
		in_area = location.in_area
		exit_points = locations.filter(in_area=in_area).exclude(id=location.id)

	if location.in_cityquarter:
		in_cityquarter = location.in_cityquarter
		exit_points = locations.filter(
				in_cityquarter=in_cityquarter
					).exclude(id=location.id)

	form = LocationModelForm(locations,
							 npcs,
							 exit_points,
							 request.POST or None,
							 instance=location
							)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('location-detail',
						args=[
							str(location.in_project.id),
							str(location.name)
					]))

	return render(request, 'location_form.html', {'form': form})

@login_required
@decorators.location_in_user_library
def location_delete(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	locations = in_project.location_set.all()

	location = get_object_or_404(locations, name=name)

	if request.method == 'POST':
		location.delete()
		if location.in_area:
			return HttpResponseRedirect(
					reverse('area-detail',
						args=[
							str(location.in_project.id),
							str(location.in_area.name)])
					)
		if location.in_cityquarter:
			return HttpResponseRedirect(
					reverse('cityquarter-detail',
						args=[
							str(location.in_project.id),
							str(location.in_cityquarter.name)]))

	return render(request, "location_confirm_delete.html", context={'location': location})

@login_required
@decorators.create_empire_in_user_library
def empire_create(request, in_project, in_universe):
	in_project = Project.objects.get(id=in_project)
	in_universe = in_project.universe_set.get(name=in_universe)
	regions = in_project.region_set.all()
	faiths = in_project.god_set.all()
	empires = in_project.empire_set.all()

	empire = Empire()

	form = EmpireModelForm(empires,
						   regions,
						   faiths,
						   request.POST or None,
						   initial={'in_universe': in_universe, 'in_project': in_project},
						   instance=empire
						)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('empire-detail',
						args=[
							str(empire.in_project.id),
							str(empire.name)
					]))

	return render(request, 'empire_form.html', {'form': form})

@login_required
@decorators.empire_in_user_library
def empire_update(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	regions = in_project.region_set.all()
	faiths = in_project.god_set.all()
	empires = in_project.empire_set.all()

	empire = get_object_or_404(empires, name=name)

	form = EmpireModelForm(empires,
						   regions,
						   faiths,
						   request.POST or None,
						   instance=empire
						)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('empire-detail',
						args=[
							str(empire.in_project.id),
							str(empire.name)
					]))

	return render(request, 'empire_form.html', {'form': form})

@login_required
@decorators.empire_in_user_library
def empire_delete(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	empires = in_project.empire_set.all()

	empire = get_object_or_404(empires, name=name)

	if request.method == 'POST':
		empire.delete()
		return HttpResponseRedirect(
				reverse('universe-detail',
					args=[
						str(empire.in_project.id),
						str(empire.in_universe.name)])
				)

	return render(request, "empire_confirm_delete.html", context={'empire': empire})

@login_required
@decorators.create_faction_in_user_library
def faction_create(request, in_project, in_universe):
	in_project = Project.objects.get(id=in_project)
	in_universe = in_project.universe_set.get(name=in_universe)

	faction = Faction()

	leaders = in_project.npc_set.filter(in_faction=faction.id)
	faiths = in_project.god_set.all()
	factions = in_project.faction_set.all()

	form = FactionModelForm(leaders,
							factions,
							faiths,
							request.POST or None,
							initial={'in_project': in_project, 'in_universe': in_universe},
							instance=faction
						)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('faction-detail',
						args=[
							str(faction.in_project.id),
							str(faction.name)
					]))

	return render(request, 'faction_form.html', {'form': form})

@login_required
@decorators.faction_in_user_library
def faction_update(request, in_project, name):
	in_project = Project.objects.get(id=in_project)

	faiths = in_project.god_set.all()
	factions = in_project.faction_set.all()

	faction = get_object_or_404(factions, name=name)

	leaders = in_project.npc_set.filter(in_faction=faction.id)

	form = FactionModelForm(leaders,
							factions,
							faiths,
							request.POST or None,
							instance=faction
						)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('faction-detail',
						args=[
							str(faction.in_project.id),
							str(faction.name)
					]))

	return render(request, 'faction_form.html', {'form': form})

@login_required
@decorators.faction_in_user_library
def faction_delete(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	factions = in_project.faction_set.all()

	faction = get_object_or_404(factions, name=name)

	if request.method == 'POST':
		faction.delete()
		return HttpResponseRedirect(
				reverse('universe-detail',
					args=[
						str(faction.in_project.id),
						str(faction.in_universe.name)])
				)

	return render(request, "faction_confirm_delete.html", context={'faction': faction})

@login_required
@decorators.create_npc_in_user_library
def npc_create(request, in_project, in_universe, in_faction=None):
	in_project = Project.objects.get(id=in_project)
	in_universe = in_project.universe_set.get(name=in_universe)
	factions = in_project.faction_set.all()
	faiths = in_project.god_set.all()
	npcs = in_project.npc_set.all()

	if in_faction is not None:
		in_faction = get_object_or_404(factions, name=in_faction)

	npc = NPC()

	form = NPCModelForm(factions,
						npcs,
						faiths,
						request.POST or None,
						initial={'in_project': in_project, 'in_universe': in_universe, 'in_faction': in_faction},
						instance=npc,
					)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('npc-detail',
						args=[
							str(npc.in_project.id),
							str(npc.name)
					]))

	return render(request, 'npc_form.html', {'form': form})

@login_required
@decorators.npc_in_user_library
def npc_update(request, in_project, name, in_faction=None):
	in_project = Project.objects.get(id=in_project)
	faiths = in_project.god_set.all()
	factions = in_project.faction_set.all()
	npcs = in_project.npc_set.all()

	npc = get_object_or_404(npcs, name=name)

	if in_faction is not None:
		in_faction = get_object_or_404(factions, name=in_faction)

	form = NPCModelForm(factions,
						npcs,
						faiths,
						request.POST or None,
						instance=npc,
					)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('npc-detail',
						args=[
							str(npc.in_project.id),
							str(npc.name)
					]))

	return render(request, 'npc_form.html', {'form': form})

@login_required
@decorators.npc_in_user_library
def npc_delete(request, in_project, name):
	in_project = Project.objects.get(id=in_project)
	npcs = in_project.npc_set.all()

	npc = get_object_or_404(npcs, name=name)

	if request.method == 'POST':
		npc.delete()
		if npc.in_faction:
			return HttpResponseRedirect(
					reverse('faction-detail',
						args=[
							str(npc.in_project.id),
							str(npc.in_faction.name)])
					)
		else:
			return HttpResponseRedirect(
					reverse('universe-detail',
							args=[
								str(npc.in_project.id),
								str(npc.in_universe.name)])
					)
	return render(request, "npc_confirm_delete.html", context={'npc': npc})

@login_required
def locationloot_create(request, in_project, in_location):
	in_project = Project.objects.get(id=in_project)
	locations = in_project.location_set.all()
	in_location = get_object_or_404(locations, name=in_location)
	items = in_project.item_set.all()

	locationloot = LocationLoot()

	form = LocationLootModelForm(items, request.POST or None, initial={'in_project': in_project, 'in_location': in_location}, instance=locationloot)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('location-detail',
						args=[
							str(locationloot.in_project.id),
							str(locationloot.in_location.name)
					]))

	return render(request, 'locationloot_form.html', {'form': form})

@login_required
@decorators.locationloot_in_user_library
def locationloot_delete(request, in_project, pk):
	in_project = Project.objects.get(id=in_project)
	locationloots = in_project.locationloot_set.all()
	locationloot = get_object_or_404(locationloots, pk=pk)
	in_location = locationloot.in_location

	if request.method == 'POST':
		locationloot.delete()
		return HttpResponseRedirect(
				reverse('location-detail',
					args=[
						str(locationloot.in_project.id),
						str(in_location.name)])
				)
	return render(request, "locationloot_confirm_delete.html", context={'locationloot': locationloot})

@login_required
@decorators.create_worldencounter_in_user_library
def worldencounter_create(request, in_project, in_dungeon_room=None, in_location=None):
	in_project = Project.objects.get(id=in_project)
	npcs = in_project.npc_set.all()
	worldencounters = in_project.worldencounter_set.all()

	worldencounter = WorldEncounter()

	if in_dungeon_room:
		rooms = in_project.room_set.all()
		in_dungeon_room = get_object_or_404(rooms, name=in_dungeon_room)
	if in_location:
		locations = in_project.location_set.all()
		in_location = get_object_or_404(locations, name=in_location)

	form = WorldEncounterModelForm(npcs,
								   worldencounters,
								   request.POST or None,
							  	   initial={'in_project': in_project, 'in_location': in_location, 'in_dungeon_room': in_dungeon_room},
							  	   instance=worldencounter
							)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('worldencounter-detail',
						args=[
							str(worldencounter.in_project.id),
							str(worldencounter.title)
					]))

	return render(request, "worldencounter_form.html", {'form': form})

@login_required
@decorators.worldencounter_in_user_library
def worldencounter_update(request, in_project, title):
	in_project = Project.objects.get(id=in_project)
	npcs = in_project.npc_set.all()
	worldencounters = in_project.worldencounter_set.all()

	worldencounter = get_object_or_404(worldencounters, title=title)

	if worldencounter.in_dungeon_room:
		in_dungeon_room = worldencounter.in_dungeon_room
	if worldencounter.in_location:
		in_location = worldencounter.in_location

	form = WorldEncounterModelForm(npcs,
								   worldencounters,
								   request.POST or None,
							  	   instance=worldencounter
							)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('worldencounter-detail',
						args=[
							str(worldencounter.in_project.id),
							str(worldencounter.title)
					]))

	return render(request, "worldencounter_form.html", {'form': form})

@login_required
@decorators.worldencounter_in_user_library
def worldencounter_delete(request, in_project, title):
	in_project = Project.objects.get(id=in_project)
	worldencounters = in_project.worldencounter_set.all()
	worldencounter = get_object_or_404(worldencounters, title=title)

	if request.method == 'POST':
		worldencounter.delete()
		if worldencounter.in_dungeon_room is not None:
			return HttpResponseRedirect(
					reverse('room-detail',
						args=[
							str(worldencounter.in_project.id),
							str(worldencounter.in_dungeon_room.name)
					]))
		if worldencounter.in_location is not None:
			return HttpResponseRedirect(
					reverse('location-detail',
						args=[
							str(worldencounter.in_project.id),
							str(worldencounter.in_location.name)
					]))
	return render(request, "worldencounter_confirm_delete.html", context={'worldencounter': worldencounter})

@login_required
@decorators.create_worldencounterloot_in_user_library
def worldencounterloot_create(request, in_project, in_worldencounter):
	in_project = Project.objects.get(id=in_project)
	worldencounters = in_project.worldencounter_set.all()
	in_worldencounter = get_object_or_404(
			worldencounters, title=in_worldencounter)
	items = in_project.item_set.all()

	worldencounterloot = WorldEncounterLoot()


	form = WorldEncounterLootModelForm(items,
									   request.POST or None,
									   initial={'in_project': in_project, 'in_worldencounter': in_worldencounter},
									   instance=worldencounterloot
									)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('worldencounter-detail',
						args=[
							str(worldencounterloot.in_project.id),
							str(worldencounterloot.in_worldencounter.title)
					]))

	return render(request, "worldencounterloot_form.html", {'form': form})

@login_required
@decorators.worldencounterloot_in_user_library
def worldencounterloot_delete(request, in_project, pk):
	in_project = Project.objects.get(id=in_project)
	worldencounterloots = in_project.worldencounterloot_set.all()

	worldencounterloot = get_object_or_404(worldencounterloots, pk=pk)

	if request.method == 'POST':
		worldencounterloot.delete()
		return HttpResponseRedirect(
				reverse('worldencounter-detail',
					args=[
						str(worldencounterloot.in_project.id),
						str(worldencounterloot.in_worldencounter.title)]))

	return render(request, "worldencounterloot_confirm_delete.html", {'worldencounterloot': worldencounterloot})
