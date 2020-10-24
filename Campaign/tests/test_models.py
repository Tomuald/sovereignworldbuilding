# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from Campaign.models import Campaign, Chapter, Quest, QuestEncounter
from accounts.models import CustomUser
from Project.models import Project
from World.models import Universe

class CampaignModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		
		self.campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
	
	def test_campaign_get_absolute_url(self):
		self.assertEqual(self.campaign.get_absolute_url(), reverse('campaign-detail', args=[str(self.campaign.id)]))
		
class ChapterModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
		
		self.chapter = Chapter.objects.create(title="Test Chapter", chapter_num=1, in_campaign=campaign)
	
	def test_chapter_get_absolute_url(self):
		self.assertEqual(self.chapter.get_absolute_url(), reverse('chapter-detail', args=[str(self.chapter.id)]))

class QuestModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
		chapter = Chapter.objects.create(title="Test Chapter", chapter_num=1, in_campaign=campaign)
		
		self.quest = Quest.objects.create(title="Test Quest", quest_num=1, in_chapter=chapter)
	
	def test_quest_get_absolute_url(self):
		self.assertEqual(self.quest.get_absolute_url(), reverse('quest-detail', args=[str(self.quest.id)]))

class QuestEncounterModelTests(TestCase):
	def setUp(self):
		user = CustomUser.objects.create_user(username="TestUser", password="T3stP4ssword")
		project = Project.objects.create(title="Test Project", created_by=user)
		universe = Universe.objects.create(name="Test Universe", in_project=project)
		campaign = Campaign.objects.create(title="Test Campaign", in_project=project, in_universe=universe)
		chapter = Chapter.objects.create(title="Test Chapter", chapter_num=1, in_campaign=campaign)
		quest = Quest.objects.create(title="Test Quest", quest_num=1, in_chapter=chapter)
		
		self.questencounter = QuestEncounter.objects.create(title="Test QuestEncounter", in_quest=quest)
	
	def test_questencounter_get_absolute_url(self):
		self.assertEqual(self.questencounter.get_absolute_url(),
						 reverse('questencounter-detail', args=[str(self.questencounter.id)])
					)
