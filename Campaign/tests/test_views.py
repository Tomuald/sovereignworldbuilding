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
		expected_url = "/accounts/login/?next=/worldbuilder/campaign/%d/" % self.campaign.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_and_campaign_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.campaign.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_detail_view_campaign_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_campaign.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('campaign-delete', args=[str(self.campaign.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/campaign/delete/%d/" % self.campaign.id
		self.assertRedirects(response, expected_url)
		
	def test_delete_view_logged_in_and_campaign_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('campaign-delete', args=[str(self.campaign.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_campaign_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('campaign-delete', args=[str(self.second_campaign.id)]))
		self.assertEqual(response.status_code, 403)
	

class ChapterViewTests(TestCase):
	def setUp(self):
		# Set up first user's chapter
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
		
		self.chapter = Chapter.objects.create(title="Test Chapter", chapter_num=1, in_campaign=campaign)
		
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
												in_campaign=second_campaign
											)
	
	# Detail View Tests
	def test_detail_not_logged_in_redirects(self):
		response = self.client.get(self.chapter.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/campaign/chapter/%d/" % self.chapter.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_viewlogged_in_and_chapter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.chapter.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_detail_view_chapter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_chapter.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('chapter-delete', args=[str(self.chapter.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/chapter/delete/%d/" % self.chapter.id
		self.assertRedirects(response, expected_url)
		
	def test_delete_view_logged_in_and_chapter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('chapter-delete', args=[str(self.chapter.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_chapter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('chapter-delete', args=[str(self.second_chapter.id)]))
		self.assertEqual(response.status_code, 403)
		
class QuestViewTests(TestCase):
	def setUp(self):
		# Set up first user's quest
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
		chapter = Chapter.objects.create(title="Test Chapter", chapter_num=1, in_campaign=campaign)
		
		self.quest = Quest.objects.create(title="Test Quest", quest_num=1, in_chapter=chapter)
		
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
												in_campaign=second_campaign
											)
		self.second_quest = Quest.objects.create(title="Second Test Quest", quest_num=1, in_chapter=second_chapter)
	
	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.quest.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/campaign/quest/%d/" % self.quest.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_and_quest_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.quest.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
	def test_detail_view_quest_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_quest.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('quest-delete', args=[str(self.quest.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/quest/delete/%d/" % self.quest.id
		self.assertRedirects(response, expected_url)
		
	def test_delete_view_logged_in_and_quest_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('quest-delete', args=[str(self.quest.id)]))
		self.assertEqual(response.status_code, 200)
		
	def test_delete_view_quest_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('quest-delete', args=[str(self.second_quest.id)]))
		self.assertEqual(response.status_code, 403)
		
class QuestEncounterDetailViewTests(TestCase):
	def setUp(self):
		# Set up first user's quest encounter
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
		chapter = Chapter.objects.create(title="Test Chapter", chapter_num=1, in_campaign=campaign)
		quest = Quest.objects.create(title="Test Quest", quest_num=1, in_chapter=chapter)
		
		self.questencounter = QuestEncounter.objects.create(title="Test QuestEncounter", in_quest=quest)
		
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
												in_campaign=second_campaign
											)
		second_quest = Quest.objects.create(title="Second Test Quest", quest_num=1, in_chapter=second_chapter)
		self.second_encounter = QuestEncounter.objects.create(title="Second Encounter Test", in_quest=second_quest)
	
	# Detail View Tests
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.questencounter.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/campaign/questencounter/%d/" % self.questencounter.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_and_questencounter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.questencounter.get_absolute_url())
		self.assertEqual(response.status_code, 200)
	
	def test_detail_view_encounter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.second_encounter.get_absolute_url())
		self.assertEqual(response.status_code, 403)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('questencounter-delete', args=[str(self.questencounter.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/questencounter/delete/%d/" % self.questencounter.id
		self.assertRedirects(response, expected_url)
		
	def test_delete_view_logged_in_and_questencounter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('questencounter-delete', args=[str(self.questencounter.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_encounter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('questencounter-delete', args=[str(self.second_encounter.id)]))
		self.assertEqual(response.status_code, 403)
		
class QuestEncounterLootViewTests(TestCase):
	def setUp(self):
		# Set up first user's quest encounter loot.
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		user.user_library.add(project)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
		chapter = Chapter.objects.create(title="Test Chapter", chapter_num=1, in_campaign=campaign)
		quest = Quest.objects.create(title="Test Quest", quest_num=1, in_chapter=chapter)
		questencounter = QuestEncounter.objects.create(title="Test QuestEncounter", in_quest=quest)
		
		itemlist = Itemlist.objects.create(name="Test Itemlist", in_project=project)
		item = Item.objects.create(name="Test Item", in_itemlist=itemlist)
		
		self.questencounterloot = QuestEncounterLoot.objects.create(name=item,
																	quantity=1,
																	in_questencounter=questencounter
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
												in_campaign=second_campaign
											)
		second_quest = Quest.objects.create(title="Second Test Quest", quest_num=1, in_chapter=second_chapter)
		second_questencounter = QuestEncounter.objects.create(title="Second Encounter Test", in_quest=second_quest)
		
		second_itemlist = Itemlist.objects.create(name="Second Test Itemlist", in_project=second_project)
		second_item = Item.objects.create(name="Second Test Item", in_itemlist=second_itemlist)
		
		self.second_questencounterloot = QuestEncounterLoot.objects.create(name=second_item,
																	quantity=1,
																	in_questencounter=second_questencounter
																)
	
	# Delete View Tests
	def test_delete_view_not_logged_in_redirects(self):
		response = self.client.get(reverse('questencounterloot-delete', args=[str(self.questencounterloot.id)]))
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/questencounter/encounterloot/delete/%d/" % self.questencounterloot.id
		self.assertRedirects(response, expected_url)
		
	def test_delete_view_logged_in_and_questencounter_in_user_library_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('questencounterloot-delete', args=[str(self.questencounterloot.id)]))
		self.assertEqual(response.status_code, 200)
	
	def test_delete_view_encounter_not_in_user_library_view_forbidden(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(reverse('questencounterloot-delete', args=[str(self.second_questencounterloot.id)]))
		self.assertEqual(response.status_code, 403)
