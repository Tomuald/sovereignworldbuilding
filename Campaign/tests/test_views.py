# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from Campaign.models import Campaign, Chapter, Quest, QuestEncounter, QuestEncounterLoot
from accounts.models import CustomUser
from Project.models import Project
from World.models import Universe, Region, NPC, Area, City, Location
from Dungeon.models import Room
from ItemList.models import Itemlist, Item

from Campaign.forms import CampaignModelForm, ChapterModelForm, QuestModelForm, QuestEncounterModelForm

class CampaignViewTests(TestCase):
	def setUp(self):
		# Set up first user's campaign
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)

		self.campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)

		# Set up second user's campaign
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		self.second_campaign = Campaign.objects.create(title="Second Test Campaign",
												  in_project=second_project,
												  in_universe=second_universe
											)

	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.campaign.get_absolute_url())
		self.assertEqual(response.status_code, 302)

	def test_detail_view_logged_in_and_campaign_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.campaign.get_absolute_url())
		self.assertEqual(response.status_code, 200)

	def test_detail_view_campaign_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_campaign.get_absolute_url())
		self.assertEqual(response.status_code, 403)

	def test_detail_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('campaign-detail',
					args=[
						self.campaign.in_project.id,
						'bogus title'])
				)
		self.assertEqual(response.status_code, 404)

	# Form Tests
	def test_campaign_title_already_taken(self):
		in_project = self.campaign.in_project.id
		universes = Universe.objects.filter(in_project=in_project)
		form = CampaignModelForm(in_project,
				data={
					'title': self.campaign.title,
					'in_universe': self.campaign.in_universe,
					'in_project': self.campaign.in_project
				}, universes=universes)
		self.assertFalse(form.is_valid())

	# Create and Update Views
	def test_create_view_initial_data(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.post(
				reverse('campaign-create',
					args=[
						self.campaign.in_project.id,])
				)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(
				response.context['form'].initial['in_project'], self.campaign.in_project.id
			)

	def test_create_view_campaign_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('campaign-create',
					args=[
						self.second_campaign.in_project.id,])
				)
		self.assertEqual(response.status_code, 403)

	def test_update_view_campaign_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('campaign-update',
					args=[
						self.second_campaign.in_project.id,
						self.second_campaign.title])
				)
		self.assertEqual(response.status_code, 403)

	def test_update_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('campaign-update',
					args=[
						self.campaign.in_project.id,
						'bogus title'])
				)
		self.assertEqual(response.status_code, 404)

	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(
				reverse('campaign-delete',
					args=[str(self.campaign.in_project.id),
						  str(self.campaign.title)])
				)
		self.assertEqual(response.status_code, 302)

	def test_delete_view_logged_in_and_campaign_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('campaign-delete',
					args=[str(self.campaign.in_project.id),
						  str(self.campaign.title)])
				)
		self.assertEqual(response.status_code, 200)

	def test_delete_view_campaign_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('campaign-delete', args=[str(self.second_campaign.in_project.id), str(self.second_campaign.title)]))
		self.assertEqual(response.status_code, 403)

	# Campaign Index
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.campaign.get_absolute_index_url())
		self.assertEqual(response.status_code, 302)

	def test_detail_view_logged_in_and_campaign_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.campaign.get_absolute_index_url())
		self.assertEqual(response.status_code, 200)

	def test_detail_view_campaign_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_campaign.get_absolute_index_url())
		self.assertEqual(response.status_code, 403)

	def test_index_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('campaign-index',
					args=[
						self.campaign.in_project.id,
						'bogus title'])
				)
		self.assertEqual(response.status_code, 404)

class ChapterViewTests(TestCase):
	def setUp(self):
		# Set up first user's chapter
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)

		self.chapter = Chapter.objects.create(title="Test Chapter", chapter_num=1, in_campaign=campaign, in_project=project)

		# Set up second user's chapter
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_campaign = Campaign.objects.create(title="Second Test Campaign",
												  in_project=second_project,
												  in_universe=second_universe
											)
		self.second_chapter = Chapter.objects.create(title="Second Test Chapter",
												chapter_num=1,
												in_campaign=second_campaign,
												in_project=second_project
											)

	# Detail View Tests
	def test_detail_not_logged_in_redirects(self):
		response = self.client.get(self.chapter.get_absolute_url())
		self.assertEqual(response.status_code, 302)

	def test_detail_viewlogged_in_and_chapter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.chapter.get_absolute_url())
		self.assertEqual(response.status_code, 200)

	def test_detail_view_chapter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_chapter.get_absolute_url())
		self.assertEqual(response.status_code, 403)

	# Forms Test
	def test_chapter_title_already_taken(self):
		in_project = self.chapter.in_project.id
		in_campaign = self.chapter.in_campaign
		regions = Region.objects.filter(
				in_universe=self.chapter.in_campaign.in_universe)
		npcs = NPC.objects.filter(
				in_universe=self.chapter.in_campaign.in_universe)

		form = ChapterModelForm(in_campaign, regions,
				npcs,
				data={
					'title': self.chapter.title,
					'in_campaign': in_campaign,
					'in_project': in_project
				})
		self.assertFalse(form.is_valid())

	# Create and Update View Tests
	def test_create_view_initial_data(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.post(
				reverse('chapter-create',
					args=[
						str(self.chapter.in_project.id),
						str(self.chapter.in_campaign.title),
					]))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(
				response.context['form'].initial['in_project'], self.chapter.in_project)
		self.assertEqual(
				response.context['form'].initial['in_campaign'], self.chapter.in_campaign)

	def test_update_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('chapter-update',
					args=[
						self.chapter.in_project.id,
						'bogus title'])
				)
		self.assertEqual(response.status_code, 404)

	def test_create_view_chapter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('chapter-create',
					args=[
						self.second_chapter.in_project.id,
						self.second_chapter.in_campaign.title,
					]))
		self.assertEqual(response.status_code, 403)

	def test_update_view_chapter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('chapter-create',
					args=[
						self.second_chapter.in_project.id,
						self.second_chapter.title,
					]))
		self.assertEqual(response.status_code, 403)

	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(
				reverse('chapter-delete',
					args=[str(self.second_chapter.in_project.id),
						  str(self.second_chapter.title)])
				)
		self.assertEqual(response.status_code, 302)

	def test_delete_view_logged_in_and_chapter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('chapter-delete',
					args=[str(self.chapter.in_project.id),
						  str(self.chapter.title)])
				)
		self.assertEqual(response.status_code, 200)

	def test_delete_view_chapter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('chapter-delete',
					args=[str(self.second_chapter.in_project.id),
						  str(self.second_chapter.title)])
				)
		self.assertEqual(response.status_code, 403)

	def test_delete_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('chapter-delete',
					args=[
						self.chapter.in_project.id,
						'bogus title'])
				)
		self.assertEqual(response.status_code, 404)

class QuestViewTests(TestCase):
	def setUp(self):
		# Set up first user's quest
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
		chapter = Chapter.objects.create(title="Test Chapter", chapter_num=1, in_campaign=campaign, in_project=project)

		self.quest = Quest.objects.create(title="Test Quest", quest_num=1, in_chapter=chapter, in_project=project)

		# Set up second user's quest
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_campaign = Campaign.objects.create(title="Second Test Campaign",
												  in_project=second_project,
												  in_universe=second_universe
											)
		second_chapter = Chapter.objects.create(title="Second Test Chapter",
												chapter_num=1,
												in_campaign=second_campaign,
												in_project=second_project,
											)
		self.second_quest = Quest.objects.create(title="Second Test Quest", quest_num=1, in_chapter=second_chapter, in_project=second_project)

	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.quest.get_absolute_url())
		self.assertEqual(response.status_code, 302)

	def test_detail_view_logged_in_and_quest_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.quest.get_absolute_url())
		self.assertEqual(response.status_code, 200)

	def test_detail_view_quest_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_quest.get_absolute_url())
		self.assertEqual(response.status_code, 403)

	# Form Tests
	def test_quest_title_already_taken(self):
		in_project = self.quest.in_project.id
		in_chapter = self.quest.in_chapter
		areas = Area.objects.filter(in_project=in_project)
		cities = City.objects.filter(in_project=in_project)
		npcs = NPC.objects.filter(
				in_universe=in_chapter.in_campaign.in_universe)

		form = QuestModelForm(areas, cities, npcs, in_project,
				data={
					'title': self.quest.title,
					'in_chapter': in_chapter,
					'in_project': in_project
				})
		self.assertFalse(form.is_valid())

	# Create and Update View Tests
	def test_create_view_initial_data(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.post(
				reverse('quest-create',
					args=[
						self.quest.in_project.id,
						self.quest.in_chapter.title
					]))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['form'].initial['in_project'], self.quest.in_project)
		self.assertEqual(response.context['form'].initial['in_chapter'], self.quest.in_chapter)

	def test_update_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('quest-update',
					args=[
						str(self.quest.in_project.id),
						'bogus title'
					]))

		self.assertEqual(response.status_code, 404)

	def test_update_view_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('quest-update',
					args=[
						self.second_quest.in_project.id,
						self.second_quest.id
					]))
		self.assertEqual(response.status_code, 403)

	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(
				reverse('quest-delete',
					args=[
						str(self.quest.in_project.id),
						str(self.quest.title)])
				)
		self.assertEqual(response.status_code, 302)

	def test_delete_view_logged_in_and_quest_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('quest-delete',
					args=[
						str(self.quest.in_project.id),
						str(self.quest.title)])
				)
		self.assertEqual(response.status_code, 200)

	def test_delete_view_quest_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('quest-delete',
						args=[
							str(self.second_quest.in_project.id), str(self.second_quest.title)])
				)
		self.assertEqual(response.status_code, 403)

	def test_delete_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('quest-delete',
					args=[
						self.quest.in_project.id,
						'bogus title'])
				)
		self.assertEqual(response.status_code, 404)

class QuestEncounterViewTests(TestCase):
	def setUp(self):
		# Set up first user's quest encounter
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
		chapter = Chapter.objects.create(title="Test Chapter", chapter_num=1, in_campaign=campaign, in_project=project)
		quest = Quest.objects.create(title="Test Quest", quest_num=1, in_chapter=chapter, in_project=project)

		self.questencounter = QuestEncounter.objects.create(title="Test QuestEncounter", in_quest=quest, in_project=project)

		# Set up second user's quest encounter
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_campaign = Campaign.objects.create(title="Second Test Campaign",
												  in_project=second_project,
												  in_universe=second_universe
											)
		second_chapter = Chapter.objects.create(title="Second Test Chapter",
												chapter_num=1,
												in_campaign=second_campaign,
												in_project=second_project
											)
		second_quest = Quest.objects.create(title="Second Test Quest", quest_num=1, in_chapter=second_chapter, in_project=second_project)
		self.second_encounter = QuestEncounter.objects.create(title="Second Encounter Test", in_quest=second_quest, in_project=second_project)

	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.questencounter.get_absolute_url())
		self.assertEqual(response.status_code, 302)

	def test_detail_view_logged_in_and_questencounter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.questencounter.get_absolute_url())
		self.assertEqual(response.status_code, 200)

	def test_detail_view_encounter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_encounter.get_absolute_url())
		self.assertEqual(response.status_code, 403)

	# Form Tests
	def test_encounter_title_already_taken(self):
		project = self.questencounter.in_project
		in_quest = self.questencounter.in_quest
		locations = Location.objects.filter(in_project=project)
		dungeonrooms = Room.objects.filter(in_project=project)
		npcs = NPC.objects.filter(in_project=project)

		form = QuestEncounterModelForm(project,
				data={
					'title': self.questencounter.title,
					'in_quest': in_quest,
					'in_project': project
				}, npcs=npcs, locations=locations, dungeonrooms=dungeonrooms)
		self.assertFalse(form.is_valid())


	# Create and Update View Tests
	def test_create_view_not_in_user_library_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('questencounter-create',
					args=[
						self.second_encounter.in_project.id,
						self.second_encounter.title
					]))
		self.assertEqual(response.status_code, 403)

	def test_create_view_initial_data(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.post(
				reverse('questencounter-create',
					args=[
						self.questencounter.in_project.id,
						self.questencounter.in_quest.title
					]))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['form'].initial['in_project'], self.questencounter.in_project)
		self.assertEqual(response.context['form'].initial['in_quest'], self.questencounter.in_quest)

	def test_update_view_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('questencounter-update',
					args=[
						self.second_encounter.in_project.id,
						self.second_encounter.title
					]))
		self.assertEqual(response.status_code, 403)

	def test_update_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('questencounter-update',
					args=[
						self.questencounter.in_project.id,
						'bogus title'
					]))
		self.assertEqual(response.status_code, 404)

	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(
			reverse('questencounter-delete',
				args=[
					str(self.second_encounter.in_project.id),
					str(self.second_encounter.title)])
			)
		self.assertEqual(response.status_code, 302)

	def test_delete_view_logged_in_and_encounter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('questencounter-delete',
					args=[
						str(self.questencounter.in_project.id),
						str(self.questencounter.title)])
				)
		self.assertEqual(response.status_code, 200)

	def test_delete_view_encounter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('questencounter-delete',
					args=[
						str(self.second_encounter.in_project.id),
						str(self.second_encounter.title)])
				)
		self.assertEqual(response.status_code, 403)

	def test_delete_view_non_existent_query_raises_404(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
				reverse('questencounter-delete',
					args=[
						str(self.questencounter.in_project.id),
						'bogus title'])
				)
		self.assertEqual(response.status_code, 404)

class QuestEncounterLootViewTests(TestCase):
	def setUp(self):
		# Set up first user's quest encounter loot.
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
		chapter = Chapter.objects.create(title="Test Chapter", chapter_num=1, in_campaign=campaign, in_project=project)
		quest = Quest.objects.create(title="Test Quest", quest_num=1, in_chapter=chapter, in_project=project)
		questencounter = QuestEncounter.objects.create(title="Test QuestEncounter", in_quest=quest, in_project=project)

		itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=project)
		item = Item.objects.create(name="Test Item", in_itemlist=itemlist, in_project=project)

		self.questencounterloot = QuestEncounterLoot.objects.create(name=item,
																	quantity=1,
																	in_questencounter=questencounter,
																	in_project=project,
																)

		# Set up second user's quest encounter loot.
		second_user = CustomUser.objects.create_user(username="SecondTestUser", password="T3stP4ssword")
		second_project = Project.objects.create(title="Second Test Project", created_by=second_user)
		second_user.user_library.add(second_project)
		second_universe = Universe.objects.create(name="Second Test Universe", in_project=second_project)
		second_campaign = Campaign.objects.create(title="Second Test Campaign",
												  in_project=second_project,
												  in_universe=second_universe
											)
		second_chapter = Chapter.objects.create(title="Second Test Chapter",
												chapter_num=1,
												in_campaign=second_campaign,
												in_project=second_project
											)
		second_quest = Quest.objects.create(title="Second Test Quest", quest_num=1, in_chapter=second_chapter, in_project=second_project)
		second_questencounter = QuestEncounter.objects.create(title="Second Encounter Test", in_quest=second_quest, in_project=second_project)

		second_itemlist = Itemlist.objects.create(name="Second Test Itemlist", in_project=second_project)
		second_item = Item.objects.create(name="Second Test Item", in_itemlist=second_itemlist, in_project=second_project)

		self.second_questencounterloot = QuestEncounterLoot.objects.create(
				name=second_item,
				quantity=1,
				in_questencounter=second_questencounter,
				in_project=second_project,
				)

	# Create View Tests
	def test_create_view_initial_data(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.post(
				reverse('questencounterloot-create',
					args=[
						self.questencounterloot.in_project.id,
						self.questencounterloot.in_questencounter.title,
					]))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['form'].initial['in_project'], self.questencounterloot.in_project)
		self.assertEqual(response.context['form'].initial['in_questencounter'], self.questencounterloot.in_questencounter)

	def test_create_view_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.post(
				reverse('questencounterloot-create',
					args=[
						self.second_questencounterloot.in_project.id,
						self.second_questencounterloot.in_questencounter.title,
					]))
		self.assertEqual(response.status_code, 403)

	def test_create_view_not_logged_in_redirects(self):
		response = self.client.get(
				reverse('questencounter-create',
					args=[
						self.questencounterloot.in_project.id,
						self.questencounterloot.in_questencounter.title,
					]))
		self.assertEqual(response.status_code, 302)

	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(
			reverse('questencounterloot-delete',
					args=[
						str(self.second_questencounterloot.in_project.id),
						str(self.second_questencounterloot.id)])
			)
		self.assertEqual(response.status_code, 302)

	def test_delete_view_logged_in_and_encounter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
			reverse('questencounterloot-delete',
					args=[
						str(self.questencounterloot.in_project.id),
						str(self.questencounterloot.id)])
			)
		self.assertEqual(response.status_code, 200)

	def test_delete_view_encounter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(
			reverse('questencounterloot-delete',
					args=[
						str(self.second_questencounterloot.in_project.id),
						str(self.second_questencounterloot.id)])
			)
		self.assertEqual(response.status_code, 403)
