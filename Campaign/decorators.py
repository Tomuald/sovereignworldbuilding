from django.core.exceptions import PermissionDenied
from Campaign.models import Campaign, Chapter, Quest, QuestEncounter

# Checks if this campaign's project is in the current user's library.
def campaign_in_user_library(function):
	def test_campaign_in_user_library(request, pk, *args, **kwargs):
		campaign = Campaign.objects.get(pk=pk)
		project = campaign.in_project
		
		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_campaign_in_user_library
	
# Checks if this chapter's project is in the current user's library.
def chapter_in_user_library(function):
	def test_chapter_in_user_library(request, pk, *args, **kwargs):
		chapter = Chapter.objects.get(pk=pk)
		project = chapter.in_campaign.in_project
		
		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_chapter_in_user_library
	
# Checks if this quest's project is in the current user's library.
def quest_in_user_library(function):
	def test_quest_in_user_library(request, pk, *args, **kwargs):
		quest = Quest.objects.get(pk=pk)
		project = quest.in_chapter.in_campaign.in_project
		
		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_quest_in_user_library
	
# Checks if this questencounter's project is in the current user's library.
def questencounter_in_user_library(function):
	def test_questencounter_in_user_library(request, pk, *args, **kwargs):
		questencounter = QuestEncounter.objects.get(pk=pk)
		project = questencounter.in_quest.in_chapter.in_campaign.in_project
		
		if project in request.user.user_library.all():
			return function(request, pk, *args, **kwargs)
		else:
			raise PermissionDenied
	
	return test_questencounter_in_user_library
