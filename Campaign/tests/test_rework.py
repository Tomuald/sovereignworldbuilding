# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from Campaign.models import Campaign, Chapter, Quest, QuestEncounter, QuestEncounterLoot
from accounts.models import CustomUser
from Project.models import Project
from World.models import Universe
from ItemList.models import Itemlist, Item

class CampaignViewTests(TestCase):
	def setUp(self):
		# Set up first user's quest encounter loot.
		self.user = CustomUser.objects.create_user(
				username="TestUser",
				password="T3stP4ssword"
			)
		self.project = Project.objects.create(
				title="Test Project",
				created_by=self.user
			)
		self.user.user_library.add(self.project)
		self.universe = Universe.objects.create(
				name="Test Universe",
				in_project=self.project
			)
		self.campaign = Campaign.objects.create(
				title="Test Campaign",
				in_project=self.project,
				in_universe=self.universe
			)
		self.chapter = Chapter.objects.create(
				title="Test Chapter",
				chapter_num=1,
				in_campaign=self.campaign,
				in_project=self.project
			)
		self.quest = Quest.objects.create(
				title="Test Quest",
				quest_num=1,
				in_chapter=self.chapter,
				in_project=self.project
			)
		self.questencounter = QuestEncounter.objects.create(
					title="Test QuestEncounter",
					in_quest=self.quest,
					in_project=self.project
				)

		self.itemlist = Itemlist.objects.create(
					name="Test Itemlist",
					in_project=self.project
				)
		self.item = Item.objects.create(
					name="Test Item",
					in_itemlist=self.itemlist,
					in_project=self.project
				)

		self.questencounterloot = QuestEncounterLoot.objects.create(
					name=self.item,
					quantity=1,
					in_questencounter=self.questencounter,
					in_project=self.project,
					)

		# Set up second user's quest encounter loot.
		self.second_user = CustomUser.objects.create_user(
				username="SecondTestUser",
				password="T3stP4ssword"
			)
		self.second_project = Project.objects.create(
				title="Second Test Project",
				created_by=self.second_user
			)
		self.second_user.user_library.add(self.second_project)
		self.second_universe = Universe.objects.create(
				name="Second Test Universe",
				in_project=self.second_project
			)
		self.second_campaign = Campaign.objects.create(
					title="Second Test Campaign",
					in_project=self.second_project,
					in_universe=self.second_universe
				)
		self.second_chapter = Chapter.objects.create(
					title="Second Test Chapter",
					chapter_num=1,
					in_campaign=self.second_campaign,
					in_project=self.second_project,
				)
		self.second_quest = Quest.objects.create(
					title="Second Test Quest",
					quest_num=1,
					in_chapter=self.second_chapter,
					in_project=self.second_project
				)
		self.second_questencounter = QuestEncounter.objects.create(
					title="Second Encounter Test",
					in_quest=self.second_quest,
					in_project=self.second_project
				)

		self.second_itemlist = Itemlist.objects.create(
					name="Second Test Itemlist",
					in_project=self.second_project
				)
		self.second_item = Item.objects.create(
					name="Second Test Item",
					in_itemlist=self.second_itemlist,
					in_project=self.second_project
				)

		self.second_questencounterloot = QuestEncounterLoot.objects.create(
					name=self.second_item,
					quantity=1,
					in_questencounter=self.second_questencounter,
					in_project=self.second_project,
					)

	# Campaign Detail View Tests
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

	# Campaign Delete View Tests
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

	# Campaign Index View
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

	# Chapter Detail View Tests
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

	# Chapter Delete View Tests
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

	# Quest Detail View Tests
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

	# Quest Delete View Tests
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

	# Quest Encounter Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.questencounter.get_absolute_url())
		self.assertEqual(response.status_code, 302)

	def test_detail_view_logged_in_and_questencounter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.questencounter.get_absolute_url())
		self.assertEqual(response.status_code, 200)

	def test_detail_view_encounter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_questencounter.get_absolute_url())
		self.assertEqual(response.status_code, 403)

	# Quest Encounter Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(
			reverse('questencounter-delete',
				args=[
					str(self.second_questencounter.in_project.id),
					str(self.second_questencounter.title)])
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
						str(self.second_questencounter.in_project.id),
						str(self.second_questencounter.title)])
				)
		self.assertEqual(response.status_code, 403)

	# Quest Encounter Loot Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(
			reverse('questencounterloot-delete',
					args=[
						str(self.second_questencounterloot.in_project.id),
						str(self.second_questencounterloot.id)])
			)
		self.assertEqual(response.status_code, 302)

	def test_delete_view_logged_in_and_questencounter_in_user_library_renders(self):
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
