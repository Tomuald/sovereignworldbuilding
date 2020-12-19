# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.shortcuts import get_object_or_404

from Campaign.forms import CampaignModelForm, ChapterModelForm, QuestModelForm, QuestEncounterModelForm, QuestEncounterLootModelForm

from Campaign.models import Campaign, Chapter, Quest, QuestEncounter, QuestEncounterLoot
from Project.models import Project
from World.models import Universe, Region, Area, City, Location, NPC
from Dungeon.models import Room
from ItemList.models import Item, Itemlist

from Campaign import decorators

##################
###   #VIEWS   ###
##################

@login_required
@decorators.campaign_in_user_library
def campaign_detail(request, in_project, title):
	project = Project.objects.get(id=in_project)
	campaigns = project.campaign_set.all()
	campaign = get_object_or_404(campaigns, title=title)

	chapters = campaign.chapter_set.all()

	context = {
		'campaign': campaign,
		'chapters': chapters,
	}

	return render(request, "campaign_detail.html", context)

@login_required
@decorators.campaign_in_user_library
def campaign_index(request, in_project, title):
	project = Project.objects.get(id=in_project)
	campaigns = project.campaign_set.all()
	campaign = get_object_or_404(campaigns, title=title)

	chapters = campaign.chapter_set.all()
	quests = project.quest_set.all()
	encounters = project.questencounter_set.all()

	context = {
		'campaign': campaign,
		'chapters': chapters,
		'quests': quests,
		'encounters': encounters,
	}

	return render(request, "campaign_index.html", context)

@login_required
@decorators.chapter_in_user_library
def chapter_detail(request, in_project, title):
	project = Project.objects.get(id=in_project)
	chapters = project.chapter_set.all()
	chapter = get_object_or_404(chapters, title=title)
	main_quests = chapter.quest_set.filter(quest_type='mq')
	side_quests = chapter.quest_set.filter(quest_type='sq')

	preceded_by = chapters.filter(chapter_num=chapter.chapter_num - 1)
	followed_by = chapters.filter(chapter_num=chapter.chapter_num + 1)

	context = {
		'chapter': chapter,
		'main_quests': main_quests,
		'side_quests': side_quests,
		'preceded_by': preceded_by,
		'followed_by': followed_by,
	}

	return render(request, "chapter_detail.html", context)

@login_required
@decorators.quest_in_user_library
def quest_detail(request, in_project, title):
	project = Project.objects.get(id=in_project)
	quests = project.quest_set.all()
	quest = get_object_or_404(quests, title=title)
	preceded_by = quests.filter(
			in_chapter=quest.in_chapter
				).filter(quest_type=quest.quest_type
					).filter(quest_num=quest.quest_num - 1
			)
	followed_by = quests.filter(
			in_chapter=quest.in_chapter
				).filter(quest_type=quest.quest_type
					).filter(quest_num=quest.quest_num + 1
			)

	context = {
		'quest': quest,
		'preceded_by': preceded_by,
		'followed_by': followed_by,
	}

	return render(request, "quest_detail.html", context)

@login_required
@decorators.questencounter_in_user_library
def questencounter_detail(request, in_project, title):
	project = Project.objects.get(id=in_project)
	questencounters = project.questencounter_set.all()
	questencounter = get_object_or_404(questencounters, title=title)

	context = {
		'questencounter': questencounter,
	}

	return render(request, 'questencounter_detail.html', context)

##################
###   #FORMS   ###
##################

@login_required
@decorators.create_campaign_in_user_library
def campaign_create(request, in_project):
	in_project = Project.objects.get(id=in_project)
	universes = in_project.universe_set.all()
	campaigns = in_project.campaign_set.all()
	campaign = Campaign()

	form = CampaignModelForm(campaigns, universes, request.POST or None, initial={'in_project': in_project}, instance=campaign)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('campaign-detail',
						args=[
							str(campaign.in_project.id),
							str(campaign.title)
					]))
	return render(request, 'campaign_form.html', {'form': form})

@login_required
@decorators.campaign_in_user_library
def campaign_update(request, in_project, title):
	in_project = Project.objects.get(id=in_project)
	universes = in_project.universe_set.all()
	campaigns = in_project.campaign_set.all()
	campaign = get_object_or_404(campaigns, title=title)

	form = CampaignModelForm(campaigns, universes, request.POST or None, instance=campaign)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('campaign-detail',
						args=[
							str(campaign.in_project.id),
							str(campaign.title)])
					)
	return render(request, 'campaign_form.html', {'form': form})

@login_required
@decorators.campaign_in_user_library
def campaign_delete(request, in_project, title):
	project = Project.objects.get(id=in_project)
	campaigns = project.campaign_set.all()
	campaign = get_object_or_404(campaigns, title=title)

	if request.method == 'POST':
		campaign.delete()
		return HttpResponseRedirect(
				reverse('project-detail',
					args=[
						campaign.in_project.id
				]))

	return render(request, "campaign_confirm_delete.html", context={'campaign': campaign})

@login_required
@decorators.create_chapter_in_user_library
def chapter_create(request, in_project, in_campaign):
	chapter = Chapter()

	project = Project.objects.get(id=in_project)
	campaign = project.campaign_set.get(title=in_campaign)
	chapters = project.chapter_set.all()
	regions = project.region_set.all()
	npcs = project.npc_set.all()

	form = ChapterModelForm(chapters,
							regions,
							npcs,
							request.POST or None,
							initial={
								'in_project': project, 'in_campaign': campaign
							},
							instance=chapter)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('chapter-detail',
						args=[
							str(project.id),
							str(chapter.title)
					]))
	return render(request, 'chapter_form.html', {'form': form})

@login_required
@decorators.chapter_in_user_library
def chapter_update(request, in_project, title):
	project = Project.objects.get(id=in_project)
	regions = project.region_set.all()
	npcs = project.npc_set.all()
	chapters = project.chapter_set.all()

	chapter = get_object_or_404(chapters, title=title)

	form = ChapterModelForm(chapters,
							regions,
							npcs,
							request.POST or None,
							instance=chapter)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('chapter-detail',
						args=[
							str(chapter.in_project.id),
							str(chapter.title),])
					)
	return render(request, 'chapter_form.html', {'form': form})

@login_required
@decorators.chapter_in_user_library
def chapter_delete(request, in_project, title):
	project = Project.objects.get(id=in_project)
	chapters = project.chapter_set.all()

	chapter = get_object_or_404(chapters, title=title)

	if request.method == 'POST':
		chapter.delete()
		return HttpResponseRedirect(
				reverse('campaign-detail',
					args=[
						str(chapter.in_project.id),
						str(chapter.in_campaign.title)
				]))

	return render(request, "chapter_confirm_delete.html", context={'chapter': chapter})

@login_required
@decorators.create_quest_in_user_library
def quest_create(request, in_project, in_chapter):
	in_project = Project.objects.get(id=in_project)
	in_chapter = in_project.chapter_set.get(title=in_chapter)
	areas = in_project.area_set.filter(in_region__in=in_chapter.regions.all())
	cities = in_project.city_set.filter(in_region__in=in_chapter.regions.all())
	npcs = in_project.npc_set.all()
	quests = in_project.quest_set.all()

	quest = Quest()

	form = QuestModelForm(areas,
						  cities,
						  npcs,
						  quests,
						  request.POST or None,
						  initial={'in_chapter': in_chapter, 'in_project': in_project},
						  instance=quest
						)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('quest-detail',
						args=[
							str(quest.in_project.id),
							str(quest.title)
					]))

	return render(request, 'quest_form.html', {'form': form})

@login_required
@decorators.quest_in_user_library
def quest_update(request, in_project, title):
	in_project = Project.objects.get(id=in_project)

	npcs = in_project.npc_set.all()
	quests = in_project.quest_set.all()

	quest = get_object_or_404(quests, title=title)
	in_chapter = quest.in_chapter

	areas = in_project.area_set.filter(in_region__in=in_chapter.regions.all())
	cities = in_project.city_set.filter(in_region__in=in_chapter.regions.all())

	form = QuestModelForm(areas,
						  cities,
						  npcs,
						  quests,
						  request.POST or None,
						  instance=quest
						)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('quest-detail',
						args=[
							str(quest.in_project.id),
							str(quest.title)])
					)

	return render(request, 'quest_form.html', {'form': form})

@login_required
@decorators.quest_in_user_library
def quest_delete(request, in_project, title):
	project = Project.objects.get(id=in_project)
	quests = project.quest_set.all()
	quest = get_object_or_404(quests, title=title)

	if request.method == 'POST':
		quest.delete()
		return HttpResponseRedirect(
				reverse('chapter-detail',
						args=[
							str(quest.in_project.id), str(quest.in_chapter.title)])
				)

	return render(request, "quest_confirm_delete.html", context={'quest': quest})

@login_required
@decorators.create_questencounter_in_user_library
def questencounter_create(request, in_project, in_quest):
	project = Project.objects.get(id=in_project)
	quest = project.quest_set.get(title=in_quest)
	npcs = project.npc_set.all()
	questencounters = project.questencounter_set.all()

	locations = project.location_set.all()
	locations_a = locations.filter(in_area__in=quest.in_areas.all())
	locations_c = locations.filter(
			in_cityquarter__in_city__in=quest.in_cities.all()
		)

	locations = locations_a | locations_c

	dungeonrooms = project.room_set.filter(
			in_roomset__in_dungeon__in_area__in=quest.in_areas.all()
		)

	questencounter = QuestEncounter()

	form = QuestEncounterModelForm(questencounters,
								   npcs,
								   locations,
								   dungeonrooms,
								   request.POST or None,
								   initial={'in_quest': quest, 'in_project': project},
								   instance=questencounter
								)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('questencounter-detail',
						args=[
							str(questencounter.in_project.id),
							str(questencounter.title)
					]))

	return render(request, "questencounter_form.html", {'form': form})

@login_required
@decorators.questencounter_in_user_library
def questencounter_update(request, in_project, title):
	project = Project.objects.get(id=in_project)
	npcs = project.npc_set.all()
	questencounters = project.questencounter_set.all()

	questencounter = get_object_or_404(questencounters, title=title)
	quest = questencounter.in_quest

	locations = project.location_set.all()
	locations_a = locations.filter(in_area__in=quest.in_areas.all())
	locations_c = locations.filter(
			in_cityquarter__in_city__in=quest.in_cities.all()
		)

	locations = locations_a | locations_c

	dungeonrooms = project.room_set.filter(
			in_roomset__in_dungeon__in_area__in=quest.in_areas.all()
		)

	form = QuestEncounterModelForm(questencounters,
								   npcs,
								   locations,
								   dungeonrooms,
								   request.POST or None,
								   instance=questencounter
								)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('questencounter-detail',
						args=[
							questencounter.in_project.id,
							questencounter.title,
						]))
	return render(request, 'questencounter_form.html', {'form': form})

@login_required
@decorators.questencounter_in_user_library
def questencounter_delete(request, in_project, title):
	project = Project.objects.get(id=in_project)
	questencounters = project.questencounter_set.all()
	questencounter = get_object_or_404(questencounters, title=title)

	if request.method == 'POST':
		questencounter.delete()
		return HttpResponseRedirect(
				reverse('quest-detail',
					args=[
						str(questencounter.in_project.id), str(questencounter.in_quest.title)])
				)

	return render(request, "questencounter_confirm_delete.html", context={'questencounter': questencounter})

@login_required
@decorators.create_questencounterloot_in_user_library
def questencounterloot_create(request, in_project, in_questencounter):
	project = Project.objects.get(id=in_project)
	questencounters = project.questencounter_set.all()

	in_questencounter = get_object_or_404(questencounters, title=in_questencounter)
	items = project.item_set.all()

	itemlists = set([item.in_itemlist for item in items])
	questencounterloot = QuestEncounterLoot()

	form = QuestEncounterLootModelForm(request.POST or None, items=items, initial={'in_questencounter': in_questencounter, 'in_project': project}, instance=questencounterloot)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
					reverse('questencounter-detail',
						args=[
							str(project.id),
							str(in_questencounter.title)
					]))

	return render(request, "questencounterloot_form.html", {'form': form, 'itemlists': itemlists})

@login_required
@decorators.questencounterloot_in_user_library
def questencounterloot_delete(request, in_project, pk):
	questencounterloot = get_object_or_404(QuestEncounterLoot, pk=pk)
	questencounter = questencounterloot.in_questencounter

	if request.method == 'POST':
		questencounterloot.delete()
		return HttpResponseRedirect(
				reverse('questencounter-detail',
					args=[
						str(questencounter.in_project.id), str(questencounter.title)])
				)

	return render(request, "questencounterloot_confirm_delete.html", context={'questencounterloot': questencounterloot})
