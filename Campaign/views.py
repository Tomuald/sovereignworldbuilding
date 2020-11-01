# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

from Campaign.forms import CampaignModelForm, ChapterModelForm, QuestModelForm, QuestEncounterModelForm, QuestEncounterLootModelForm

from Campaign.models import Campaign, Chapter, Quest, QuestEncounter, QuestEncounterLoot
from Project.models import Project
from World.models import Universe, Region, Area, City, Location, NPC
from Dungeon.models import Room
from ItemList.models import Item

from Campaign import decorators


##################
###   #VIEWS   ###
##################

@login_required
@decorators.campaign_in_user_library
def campaign_detail(request, pk):
	campaign = Campaign.objects.get(pk=pk)
	chapters = Chapter.objects.filter(in_campaign=campaign.id)
	
	context = {
		'campaign': campaign,
		'chapters': chapters,
	}
	
	return render(request, "campaign_detail.html", context)
	
@login_required	
@decorators.campaign_in_user_library
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
	
	return render(request, "campaign_index.html", context)
	
@login_required
@decorators.chapter_in_user_library
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
	
	return render(request, "chapter_detail.html", context)
	
@login_required
@decorators.quest_in_user_library
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
	
	return render(request, "quest_detail.html", context)
	
@login_required	
@decorators.questencounter_in_user_library
def questencounter_detail(request, pk):
	questencounter = QuestEncounter.objects.get(pk=pk)
	
	context = {
		'questencounter': questencounter,
	}
	
	return render(request, 'questencounter_detail.html', context)
	
##################
###   #FORMS   ###
##################
	
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
	
	return render(request, 'campaign_form.html', {'form': form})

@login_required
@decorators.campaign_in_user_library
def campaign_delete(request, pk):
	campaign = get_object_or_404(Campaign, pk=pk)
	
	if request.method == 'POST':
		campaign.delete()
		return HttpResponseRedirect(reverse('myshelf'))
	
	return render(request, "campaign_confirm_delete.html", context={'campaign': campaign})
	
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
	
	return render(request, 'chapter_form.html', {'form': form, 'in_campaign': in_campaign})
	
@login_required
@decorators.chapter_in_user_library
def chapter_delete(request, pk):
	chapter = get_object_or_404(Chapter, pk=pk)
	
	if request.method == 'POST':
		chapter.delete()
		return HttpResponseRedirect(reverse('campaign-detail', args=[str(chapter.in_campaign.id)]))
	
	return render(request, "chapter_confirm_delete.html", context={'chapter': chapter})
	
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
	
	return render(request, 'quest_form.html', {'form': form, 'in_chapter': in_chapter})

@login_required
@decorators.quest_in_user_library
def quest_delete(request, pk):
	quest = get_object_or_404(Quest, pk=pk)
	
	if request.method == 'POST':
		quest.delete()
		return HttpResponseRedirect(reverse('chapter-detail', args=[str(quest.in_chapter.id)]))
	
	return render(request, "quest_confirm_delete.html", context={'quest': quest})
	
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
	
	return render(request, "questencounter_form.html", {'form': form})

@login_required
@decorators.questencounter_in_user_library
def questencounter_delete(request, pk):
	questencounter = get_object_or_404(QuestEncounter, pk=pk)
	
	if request.method == 'POST':
		questencounter.delete()
		return HttpResponseRedirect(reverse('quest-detail', args=[str(questencounter.in_quest.id)]))
	
	return render(request, "questencounter_confirm_delete.html", context={'questencounter': questencounter})
	
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
	
	return render(request, "questencounterloot_form.html", {'form': form})

@login_required
@decorators.questencounterloot_in_user_library
def questencounterloot_delete(request, pk):
	questencounterloot = get_object_or_404(QuestEncounterLoot, pk=pk)
	questencounter = questencounterloot.in_questencounter
	
	if request.method == 'POST':
		questencounterloot.delete()
		return HttpResponseRedirect(reverse('questencounter-detail', args=[str(questencounter.id)]))
	
	return render(request, "questencounterloot_confirm_delete.html", context={'questencounterloot': questencounterloot})
