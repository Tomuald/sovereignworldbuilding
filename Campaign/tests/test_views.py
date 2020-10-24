# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from Campaign.models import Campaign, Chapter, Quest, QuestEncounter
from accounts.models import CustomUser
from Project.models import Project
from World.models import Universe

class CampaignViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.campaign.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/campaign/%d/" % self.campaign.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.campaign.get_absolute_url())
		self.assertEqual(response.status_code, 200)

class ChapterViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
		
		self.chapter = Chapter.objects.create(title="Test Chapter", chapter_num=1, in_campaign=campaign)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.chapter.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/campaign/chapter/%d/" % self.chapter.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.chapter.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
class QuestViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
		chapter = Chapter.objects.create(title="Test Chapter", chapter_num=1, in_campaign=campaign)
		
		self.quest = Quest.objects.create(title="Test Quest", quest_num=1, in_chapter=chapter)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.quest.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/campaign/quest/%d/" % self.quest.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.quest.get_absolute_url())
		self.assertEqual(response.status_code, 200)
		
class QuestEncounterViewTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
		chapter = Chapter.objects.create(title="Test Chapter", chapter_num=1, in_campaign=campaign)
		quest = Quest.objects.create(title="Test Quest", quest_num=1, in_chapter=chapter)
		
		self.questencounter = QuestEncounter.objects.create(title="Test QuestEncounter", in_quest=quest)
	
	def test_detail_view_not_logged_in_redirects(self):
		response = self.client.get(self.questencounter.get_absolute_url())
		self.assertEqual(response.status_code, 302)
		expected_url = "/accounts/login/?next=/worldbuilder/campaign/questencounter/%d/" % self.questencounter.id
		self.assertRedirects(response, expected_url)
		
	def test_detail_view_logged_in_renders(self):
		self.client.login(username="TestUser", password="T3stP4ssword")
		response = self.client.get(self.questencounter.get_absolute_url())
		self.assertEqual(response.status_code, 200)
