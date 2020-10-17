# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required

from .forms import NPCModelForm, FactionModelForm, AreaModelForm, CityModelForm, EmpireModelForm, LocationModelForm, CampaignModelForm, ChapterModelForm, QuestModelForm, UniverseModelForm, CityQuarterModelForm, RegionModelForm, PantheonModelForm, GodModelForm, DungeonModelForm, RoomsetModelForm, RoomModelForm, ItemlistModelForm, ItemModelForm, ProjectModelForm

from .forms import QuestEncounterModelForm, QuestEncounterLootModelForm, WorldEncounterModelForm, WorldEncounterLootModelForm, LocationLootModelForm, RoomLootModelForm

from Campaign.models import * 
from Dungeon.models import Dungeon, Roomset, Room, RoomLoot
from Pantheon.models import Pantheon, God
from World.models import *
from ItemList.models import Itemlist, Item
from Project.models import Project
from accounts.models import CustomUser

@login_required
def project_list(request):
	user = CustomUser.objects.get(username=request.user.username)
	projects = user.user_library.all()
	
	context = {
		'projects': projects,
	}
	
	return render(request, "SovereignWebsite/project_list.html", context=context)

@login_required
def project_detail(request, pk):
	project = get_object_or_404(Project, pk=pk)
	
	campaigns = Campaign.objects.filter(in_project=project.id)
	universes = Universe.objects.filter(in_project=project.id)
	itemlists = Itemlist.objects.filter(in_project=project.id)
	
	context = {
		'project': project,
		'campaigns': campaigns,
		'universes': universes,
		'itemlists': itemlists,
	}
	
	return render(request, 'SovereignWebsite/project_detail.html', context=context)


	
###################
# -- #CAMPAIGN -- #
###################

@login_required
def campaign_detail(request, pk):
	campaign = Campaign.objects.get(pk=pk)
	chapters = Chapter.objects.filter(in_campaign=campaign.id)
	
	context = {
		'campaign': campaign,
		'chapters': chapters,
	}
	
	return render(request, "SovereignWebsite/campaign_detail.html", context) 
	
@login_required
def chapter_detail(request, pk):
	chapter = Chapter.objects.get(pk=pk)
	main_quests = Quest.objects.filter(in_chapter=pk, quest_type='mq')
	side_quests = Quest.objects.filter(in_chapter=pk, quest_type='sq')
	
	preceded_by = Chapter.objects.filter(chapter_num=chapter.chapter_num - 1,
											in_campaign=chapter.in_campaign
										)
	followed_by = Chapter.objects.filter(chapter_num=chapter.chapter_num + 1,
											in_campaign=chapter.in_campaign
										)
	
	context = {
		'chapter': chapter,
		'main_quests': main_quests,
		'side_quests': side_quests,
		'preceded_by': preceded_by,
		'followed_by': followed_by,
	}
	
	return render(request, "SovereignWebsite/chapter_detail.html", context)

@login_required	
def quest_detail(request, pk):
	quest = Quest.objects.get(pk=pk)
	preceded_by = Quest.objects.filter(quest_num=quest.quest_num - 1,
									   in_chapter=quest.in_chapter,
									   quest_type=quest.quest_type
									)
	followed_by = Quest.objects.filter(quest_num=quest.quest_num + 1,
									   in_chapter=quest.in_chapter,
									   quest_type=quest.quest_type
									)
	
	context = {
		'quest': quest,
		'preceded_by': preceded_by,
		'followed_by': followed_by,
	}
	
	return render(request, "SovereignWebsite/quest_detail.html", context)

@login_required	
def campaign_index(request, pk):
	campaign = Campaign.objects.get(pk=pk)
	
	chapters = Chapter.objects.filter(in_campaign=campaign.id)
	quests = Quest.objects.filter(in_chapter__in_campaign=campaign.id)
	encounters = QuestEncounter.objects.filter(in_quest__in_chapter__in_campaign=campaign.id)
	
	context = {
		'campaign': campaign,
		'chapters': chapters,
		'quests': quests,
		'encounters': encounters,
	}
	
	return render(request, "SovereignWebsite/campaign_index.html", context)

@login_required	
def questencounter_detail(request, pk):
	questencounter = QuestEncounter.objects.get(pk=pk)
	
	context = {
		'questencounter': questencounter,
	}
	
	return render(request, 'SovereignWebsite/questencounter_detail.html', context)
	
################
# -- #WORLD -- #
################

@login_required
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
def empire_detail(request, pk):
	empire = Empire.objects.get(pk=pk)
	
	context = {
		'empire': empire,
	}
	
	return render(request, "SovereignWebsite/empire_detail.html", context)

@login_required
def region_detail(request, pk):
	region = Region.objects.get(pk=pk)
	
	context = {
		'region': region,
	}
	
	return render(request, 'SovereignWebsite/region_detail.html', context)
@login_required	
def area_detail(request, pk):
	area = Area.objects.get(pk=pk)
	npcs = NPC.objects.filter(location__in_area=area.id).distinct()
	
	context = {
		'area': area,
		'npcs': npcs,
	}
	
	return render(request, 'SovereignWebsite/area_detail.html', context)

@login_required
def city_detail(request, pk):
	city = City.objects.get(pk=pk)
	city_quarters = CityQuarter.objects.filter(in_city=city)
	
	context = {
		'city': city,
		'city_quarters': city_quarters,
	}
	
	return render(request, 'SovereignWebsite/city_detail.html', context)

@login_required	
def cityquarter_detail(request, pk):
	cityquarter = CityQuarter.objects.get(pk=pk)
	
	context = {
		'cityquarter': cityquarter,
	}
	
	return render(request, 'SovereignWebsite/cityquarter_detail.html', context)

@login_required	
def location_detail(request, pk):
	location = Location.objects.get(pk=pk)
	
	context = {
		'location': location,
	}
	
	return render(request, 'SovereignWebsite/location_detail.html', context)
@login_required	
def worldencounter_detail(request, pk):
	worldencounter = WorldEncounter.objects.get(pk=pk)
	
	context = {
		'worldencounter': worldencounter,
	}
	
	return render(request, "SovereignWebsite/worldencounter_detail.html", context)

@login_required	
def faction_detail(request, pk):
	faction = Faction.objects.get(pk=pk)
	
	context = {
		'faction': faction,
	}
	
	return render(request, 'SovereignWebsite/faction_detail.html', context)

@login_required	
def npc_detail(request, pk):
	npc = NPC.objects.get(pk=pk)
	locations = Location.objects.filter(NPCs__id=npc.id)
	
	context = {
		'npc': npc,
		'locations': locations,
	}
	
	return render(request, 'SovereignWebsite/npc_detail.html', context)
	
##################
# -- #DUNGEON -- #
##################

@login_required
def dungeon_detail(request, pk):
	dungeon = Dungeon.objects.get(pk=pk)
	
	context = {
		'dungeon': dungeon,
	}
	
	return render(request, 'SovereignWebsite/dungeon_detail.html', context)

@login_required
def roomset_detail(request, pk):
	roomset = Roomset.objects.get(pk=pk)
	
	context = {'roomset': roomset}
	
	return render(request, 'SovereignWebsite/roomset_detail.html', context)

@login_required	
def room_detail(request, pk):
	room = Room.objects.get(pk=pk)
	
	context = {
		'room': room,
	}
	
	return render(request, 'SovereignWebsite/room_detail.html', context)
	
################
# -- #ITEMS -- #
################

@login_required
def itemlist_detail(request, pk):
	itemlist = Itemlist.objects.get(pk=pk)
	
	context = {'itemlist': itemlist}
	
	return render(request, 'SovereignWebsite/itemlist_detail.html', context)

@login_required
def item_detail(request, pk):
	item = Item.objects.get(pk=pk)
	
	context = {'item': item}
	
	return render(request, 'SovereignWebsite/item_detail.html', context)
	
####################
# -- #PANTHEONS -- #
####################

@login_required
def pantheon_detail(request, pk):
	pantheon = Pantheon.objects.get(pk=pk)
	
	context = {'pantheon': pantheon}
	
	return render(request, "SovereignWebsite/pantheon_detail.html", context)

@login_required
def god_detail(request, pk):
	god = God.objects.get(pk=pk)
	worshipped_by_npcs = NPC.objects.filter(faiths=god)
	worshipped_by_factions = Faction.objects.filter(faiths=god)
	
	context = {
		'god': god,
		'worshipped_by_npcs': worshipped_by_npcs,
		'worshipped_by_factions': worshipped_by_factions,
	}
	
	return render(request, "SovereignWebsite/god_detail.html", context)

################
# -- #FORMS -- #
################	

@login_required
def project_create(request, pk=None):
	user = CustomUser.objects.get(username=request.user.username)
	
	if pk:
		project = get_object_or_404(Project, pk=pk)
	else:
		project = Project()
	
	form = ProjectModelForm(request.POST or None, initial={'created_by': user}, instance=project)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			user.user_library.add(project)
			user.save()
			return HttpResponseRedirect(reverse('project-detail', args=[str(project.id)]))
	
	return render(request, "SovereignWebsite/project_form.html", {'form': form})

@login_required
def project_delete(request, pk):
	project = get_object_or_404(Project, pk=pk)
	user = CustomUser.objects.get(username=request.user.username)
	
	if request.method == 'POST':
		user.user_library.remove(project)
		user.save()
		project.delete()
		return HttpResponseRedirect(reverse('project-list'))
	
	return render(request, "SovereignWebsite/project_confirm_delete.html", context={'project': project})

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
def area_delete(request, pk):
	area = get_object_or_404(Area, pk=pk)
	
	if request.method == 'POST':
		area.delete()
		return HttpResponseRedirect(reverse('region-detail', args=[str(area.in_region.id)]))
	
	return render(request, "SovereignWebsite/area_confirm_delete.html", context={'area': area})

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
def cityquarter_delete(request, pk):
	cityquarter = get_object_or_404(CityQuarter, pk=pk)
	
	if request.method == 'POST':
		cityquarter.delete()
		return HttpResponseRedirect(reverse('city-detail', args=[str(cityquarter.in_city.id)]))
	
	return render(request, "SovereignWebsite/cityquarter_confirm_delete.html", context={'cityquarter': cityquarter})

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
def city_delete(request, pk):
	city = get_object_or_404(City, pk=pk)
	
	if request.method == 'POST':
		city.delete()
		return HttpResponseRedirect(reverse('region-detail', args=[str(city.in_region.id)]))
	
	return render(request, "SovereignWebsite/city_confirm_delete.html", context={'city': city})

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
		
		form = LocationModelForm(in_area,
								 request.POST or None,
								 npcs=npcs,
								 initial={'in_area': in_area,},
								 instance=location
								)
	
	if in_cityquarter:
		in_cityquarter = CityQuarter.objects.get(id=in_cityquarter)
		npcs = NPC.objects.filter(in_universe=in_cityquarter.in_city.in_region.in_universe)
		
		form = LocationModelForm(in_area,
								 request.POST or None,
								 npcs=npcs,
								 initial={'in_cityquarter': in_cityquarter,},
								 instance=location
								)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('location-detail', args=[str(location.id)]))
		
	return render(request, 'SovereignWebsite/location_form.html', {'form': form})

@login_required
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
def worldencounter_delete(request, pk, in_dungeon_room=None, in_location=None):
	worldencounter = WorldEncounter.objects.get(pk=pk)
	
	if request.method == 'POST':
		worldencounter.delete()
		if in_dungeon_room is not None:
			return HttpResponseRedirect(reverse('room-detail', args=[str(in_dungeon_room)]))
		if in_location is not None:
			return HttpResponseRedirect(reverse('location-detail', args=[str(in_location)]))
	
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
			items = Item.objects.filter(
				in_itemlist__in_project=in_worldencounter.in_location.in_cityquarter.in_city.in_region.in_universe.in_project
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
def worldencounterloot_delete(request, pk):
	worldencounterloot = WorldEncounterLoot.objects.get(pk=pk)
	
	if request.method == 'POST':
		worldencounterloot.delete()
		return HttpResponseRedirect(reverse('worldencounter-detail', args=[str(worldencounterloot.in_worldencounter.id)]))
	
	return render(request, "SovereignWebsite/worldencounterloot_confirm_delete.html", {'worldencounterloot': worldencounterloot})
	
################################
### -- #DUNGEON FORMVIEWS -- ###
################################

@login_required
def dungeon_create(request, in_area, pk=None):
	in_area = Area.objects.get(id=in_area)
	areas = Area.objects.filter(in_region=in_area.in_region)
	
	if pk:
		dungeon = get_object_or_404(Dungeon, pk=pk)
	else:
		dungeon = Dungeon()
		
	form = DungeonModelForm(areas,
							request.POST or None,
							initial={'in_area': in_area},
							instance=dungeon
						)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('dungeon-detail', args=[str(dungeon.id)]))
	
	return render(request, 'SovereignWebsite/dungeon_form.html', {'form': form})

@login_required	
def dungeon_delete(request, pk):
	dungeon = get_object_or_404(Dungeon, pk=pk)
	
	if request.method == 'POST':
		dungeon.delete()
		return HttpResponseRedirect(reverse('area-detail', args=[str(dungeon.in_area.id)]))
	
	return render(request, "SovereignWebsite/dungeon_confirm_delete.html", context={'dungeon': dungeon})

@login_required
def roomset_create(request, in_dungeon, pk=None):
	in_dungeon = Dungeon.objects.get(id=in_dungeon)
	dungeons = Dungeon.objects.filter(id=in_dungeon.id)
	
	if pk:
		roomset = get_object_or_404(Roomset, pk=pk)
	else:
		roomset = Roomset()
	
	form = RoomsetModelForm(dungeons, request.POST or None, initial={'in_dungeon': in_dungeon}, instance=roomset)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('roomset-detail', args=[str(roomset.id)]))
	
	return render(request, 'SovereignWebsite/roomset_form.html', {'form': form})

@login_required
def roomset_delete(request, pk):
	roomset = get_object_or_404(Roomset, pk=pk)
	
	if request.method == 'POST':
		roomset.delete()
		return HttpResponseRedirect(reverse('dungeon-detail', args=[str(roomset.in_dungeon.id)]))
	
	return render(request, "SovereignWebsite/roomset_confirm_delete.html", context={'roomset': roomset})

@login_required	
def room_create(request, in_roomset, pk=None):
	in_roomset = Roomset.objects.get(id=in_roomset)
	roomsets = Roomset.objects.filter(in_dungeon=in_roomset.in_dungeon)
	
	if pk:
		room = get_object_or_404(Room, pk=pk)
	else:
		room = Room()
	
	rooms = Room.objects.filter(in_roomset=in_roomset.id).exclude(id=room.id)
	
	form = RoomModelForm(rooms,
						 roomsets,
						 request.POST or None,
						 initial={'in_roomset': in_roomset},
						 instance=room
						)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('room-detail', args=[str(room.id)]))
	
	return render(request, 'SovereignWebsite/room_form.html', {'form': form})

@login_required
def room_delete(request, pk):
	room = get_object_or_404(Room, pk=pk)
	
	if request.method == 'POST':
		room.delete()
		return HttpResponseRedirect(reverse('roomset-detail', args=[str(room.in_roomset.id)]))
	
	return render(request, "SovereignWebsite/room_confirm_delete.html", context={'room': room})

@login_required
def roomloot_create(request, in_room):
	in_room = Room.objects.get(id=in_room)
	items = Item.objects.filter(
		in_itemlist__in_project=in_room.in_roomset.in_dungeon.in_area.in_region.in_universe.in_project
	)
	
	roomloot = RoomLoot()
	
	form = RoomLootModelForm(request.POST or None, items=items, initial={'in_room': in_room}, instance=roomloot)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('room-detail', args=[str(in_room.id)]))
	
	return render(request, 'SovereignWebsite/roomloot_form.html', {'form': form})

@login_required	
def roomloot_delete(request, pk):
	roomloot = RoomLoot.objects.get(pk=pk)
	
	if request.method == 'POST':
		roomloot.delete()
		return HttpResponseRedirect(reverse('room-detail', args=[str(roomloot.in_room.id)]))
	
	return render(request, "SovereignWebsite/roomloot_confirm_delete.html", context={'roomloot': roomloot})

#################################
### -- #CAMPAIGN FORMVIEWS -- ###
#################################

@login_required
def campaign_create(request, in_project, pk=None):
	in_project = Project.objects.get(id=in_project)
	universes = Universe.objects.filter(in_project=in_project.id)

	if pk:
		campaign = get_object_or_404(Campaign, pk=pk)
	else:
		campaign = Campaign()
	
	form = CampaignModelForm(request.POST or None,
							 initial={'in_project': in_project},
							 instance=campaign,
							 universes=universes,
							)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('campaign-detail', args=[str(campaign.id)]))
	
	return render(request, 'SovereignWebsite/campaign_form.html', {'form': form})

@login_required
def campaign_delete(request, pk):
	campaign = get_object_or_404(Campaign, pk=pk)
	
	if request.method == 'POST':
		campaign.delete()
		return HttpResponseRedirect(reverse('myshelf'))
	
	return render(request, "SovereignWebsite/campaign_confirm_delete.html", context={'campaign': campaign})

@login_required
def chapter_create(request, in_campaign, pk=None):
	in_campaign = Campaign.objects.get(id=in_campaign)
	campaigns = Campaign.objects.filter(in_project=in_campaign.in_project.id)
	regions = Region.objects.filter(in_universe=in_campaign.in_universe.id)
	npcs = NPC.objects.filter(in_universe=in_campaign.in_universe.id)
	
	if pk:
		chapter = get_object_or_404(Chapter, pk=pk)
	else:
		chapter = Chapter()
	
	form = ChapterModelForm(campaigns,
							regions,
							npcs,
							request.POST or None,
							initial={'in_campaign': in_campaign},
							instance=chapter
						)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('chapter-detail', args=[str(chapter.id)]))	
	
	return render(request, 'SovereignWebsite/chapter_form.html', {'form': form, 'in_campaign': in_campaign})

@login_required
def chapter_delete(request, pk):
	chapter = get_object_or_404(Chapter, pk=pk)
	
	if request.method == 'POST':
		chapter.delete()
		return HttpResponseRedirect(reverse('campaign-detail', args=[str(chapter.in_campaign.id)]))
	
	return render(request, "SovereignWebsite/chapter_confirm_delete.html", context={'chapter': chapter})

@login_required
def quest_create(request, in_chapter, pk=None):
	in_chapter = Chapter.objects.get(id=in_chapter)
	chapters = Chapter.objects.filter(in_campaign=in_chapter.in_campaign.id)
	areas = Area.objects.filter(in_region__in_universe__in_project=in_chapter.in_campaign.in_project)
	cities = City.objects.filter(in_region__in_universe__in_project=in_chapter.in_campaign.in_project)
	npcs = NPC.objects.filter(in_universe=in_chapter.in_campaign.in_universe)
	
	if pk:
		quest = get_object_or_404(Quest, pk=pk)
	else:
		quest = Quest()
	
	form = QuestModelForm(chapters,
						  areas,
						  cities,
						  npcs,
						  request.POST or None,
						  initial={'in_chapter': in_chapter},
						  instance=quest
						)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('quest-detail', args=[str(quest.id)]))
	
	return render(request, 'SovereignWebsite/quest_form.html', {'form': form, 'in_chapter': in_chapter})

@login_required	
def quest_delete(request, pk):
	quest = get_object_or_404(Quest, pk=pk)
	
	if request.method == 'POST':
		quest.delete()
		return HttpResponseRedirect(reverse('chapter-detail', args=[str(quest.in_chapter.id)]))
	
	return render(request, "SovereignWebsite/quest_confirm_delete.html", context={'quest': quest})

@login_required	
def questencounter_create(request, in_quest, pk=None):
	quest = Quest.objects.get(id=in_quest)
	npcs = NPC.objects.filter(in_universe__in_project=quest.in_chapter.in_campaign.in_project)
	locations = Location.objects.filter(in_area=quest.in_area)
	dungeonrooms = Room.objects.filter(in_roomset__in_dungeon__in_area=quest.in_area)
	
	if pk:
		questencounter = QuestEncounter.objects.get(pk=pk)
	else:
		questencounter = QuestEncounter()
	
	form = QuestEncounterModelForm(request.POST or None,
								   npcs=npcs,
								   locations=locations,
								   dungeonrooms=dungeonrooms,
								   initial={'in_quest': in_quest},
								   instance=questencounter
								)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('questencounter-detail', args=[str(questencounter.id)]))
	
	return render(request, "SovereignWebsite/questencounter_form.html", {'form': form})

@login_required
def questencounter_delete(request, pk):
	questencounter = get_object_or_404(QuestEncounter, pk=pk)
	
	if request.method == 'POST':
		questencounter.delete()
		return HttpResponseRedirect(reverse('quest-detail', args=[str(questencounter.in_quest.id)]))
	
	return render(request, "SovereignWebsite/questencounter_confirm_delete.html", context={'questencounter': questencounter})

@login_required
def questencounterloot_create(request, in_questencounter):
	questencounterloot = QuestEncounterLoot()
	in_questencounter = QuestEncounter.objects.get(id=in_questencounter)
	items = Item.objects.filter(in_itemlist__in_project=in_questencounter.in_quest.in_chapter.in_campaign.in_project)
	
	form = QuestEncounterLootModelForm(request.POST or None, items=items, initial={'in_questencounter': in_questencounter}, instance=questencounterloot)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('questencounter-detail', args=[str(in_questencounter.id)]))
	
	return render(request, "SovereignWebsite/questencounterloot_form.html", {'form': form})

@login_required	
def questencounterloot_delete(request, pk):
	questencounterloot = get_object_or_404(QuestEncounterLoot, pk=pk)
	questencounter = questencounterloot.in_questencounter
	
	if request.method == 'POST':
		questencounterloot.delete()
		return HttpResponseRedirect(reverse('questencounter-detail', args=[str(questencounter.id)]))
	
	return render(request, "SovereignWebsite/questencounterloot_confirm_delete.html", context={'questencounterloot': questencounterloot})
	

#################################
### -- #PANTHEON FORMVIEWS -- ###
#################################

@login_required
def pantheon_create(request, in_universe, pk=None):
	in_universe = Universe.objects.get(id=in_universe)
	universe_set = Universe.objects.filter(id=in_universe.id)
	
	if pk:
		pantheon = get_object_or_404(Pantheon, pk=pk)
	else:
		pantheon = Pantheon()
	
	form = PantheonModelForm(universe_set,
							 request.POST or None,
							 initial={'in_universe': in_universe},
							 instance=pantheon
							)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('pantheon-detail', args=[str(pantheon.id)]))
		
	return render(request, 'SovereignWebsite/pantheon_form.html', {'form': form})

@login_required	
def pantheon_delete(request, pk):
	pantheon = get_object_or_404(Pantheon, pk=pk)
	
	if request.method == 'POST':
		pantheon.delete()
		return HttpResponseRedirect(reverse('universe-detail', args=[str(pantheon.in_universe.id)]))
	
	return render(request, "SovereignWebsite/pantheon_confirm_delete.html", context={'pantheon': pantheon})

@login_required	
def god_create(request, in_pantheon, pk=None):
	in_pantheon = Pantheon.objects.get(id=in_pantheon)
	pantheons = Pantheon.objects.filter(in_universe=in_pantheon.in_universe)
	
	if pk:
		god = get_object_or_404(God, pk=pk)
	else:
		god = God()
	
	form = GodModelForm(pantheons,
						request.POST or None,
						initial={'in_pantheon': in_pantheon},
						instance=god
					)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('god-detail', args=[str(god.id)]))
	
	return render(request, 'SovereignWebsite/god_form.html', {'form': form})

@login_required	
def god_delete(request, pk):
	god = get_object_or_404(God, pk=pk)
	
	if request.method == 'POST':
		god.delete()
		return HttpResponseRedirect(reverse('pantheon-detail', args=[str(god.in_pantheon.id)]))
	
	return render(request, "SovereignWebsite/god_confirm_delete.html", context={'god': god})
	
#################################
### -- #ITEMLIST FORMVIEWS -- ###
#################################

@login_required
def itemlist_create(request, in_project, pk=None):
	in_project = Project.objects.get(id=in_project)
	
	if pk:
		itemlist = Itemlist.objects.get(pk=pk)
	else:
		itemlist = Itemlist()
	
	form = ItemlistModelForm(request.POST or None, initial={'in_project': in_project}, instance=itemlist)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('itemlist-detail', args=[str(itemlist.id)]))
		
	return render(request, 'SovereignWebsite/itemlist_form.html', {'form': form})

@login_required	
def itemlist_delete(request, pk):
	itemlist = get_object_or_404(Itemlist, pk=pk)
	
	if request.method == 'POST':
		itemlist.delete()
		return HttpResponseRedirect(reverse('project-detail', args=[str(itemlist.in_project.id)]))
	
	return render(request, "SovereignWebsite/itemlist_confirm_delete.html", context={'itemlist': itemlist})

@login_required	
def item_create(request, in_itemlist, pk=None):
	in_itemlist = Itemlist.objects.get(id=in_itemlist)
	
	if pk:
		item = get_object_or_404(Item, pk=pk)
	else:
		item = Item()
	
	form = ItemModelForm(in_itemlist, request.POST or None, initial={'in_itemlist': in_itemlist}, instance=item)
	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('item-detail', args=[str(item.id)]))
	
	return render(request, 'SovereignWebsite/item_form.html', {'form': form})

@login_required	
def item_delete(request, pk):
	item = get_object_or_404(Item, pk=pk)
	
	if request.method == 'POST':
		item.delete()
		return HttpResponseRedirect(reverse('itemlist-detail', args=[str(item.in_itemlist.id)]))
	
	return render(request, "SovereignWebsite/item_confirm_delete.html", context={'item': item})
