from django.core.exceptions import PermissionDenied
from Campaign.models import Campaign, Chapter, Quest, QuestEncounter, QuestEncounterLoot
from Project.models import Project

# Checks if this campaign's project is in the current user's library.
def campaign_in_user_library(function):
	def test_campaign_in_user_library(request, in_project, title, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, title, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_campaign_in_user_library

def create_campaign_in_user_library(function):
	def test_campaign_in_user_library(request, in_project, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_campaign_in_user_library

# Checks if this chapter's project is in the current user's library.
def chapter_in_user_library(function):
	def test_chapter_in_user_library(request, in_project, title, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, title, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_chapter_in_user_library

def create_chapter_in_user_library(function):
	def test_chapter_in_user_library(request, in_project, in_campaign, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_campaign, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_chapter_in_user_library

# Checks if this quest's project is in the current user's library.
def quest_in_user_library(function):
	def test_quest_in_user_library(request, in_project, title, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, title, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_quest_in_user_library

def create_quest_in_user_library(function):
	def test_quest_in_user_library(request, in_project, in_chapter, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_chapter, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_quest_in_user_library

# Checks if this questencounter's project is in the current user's library.
def questencounter_in_user_library(function):
	def test_questencounter_in_user_library(request, in_project, title, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, title, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_questencounter_in_user_library

def create_questencounter_in_user_library(function):
	def test_questencounter_in_user_library(request, in_project, in_quest, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_quest, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_questencounter_in_user_library

# Checks if this questencounterloot's project is in the current user's library.
def questencounterloot_in_user_library(function):
	def test_questencounterloot_in_user_library(request, in_project, pk, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, pk, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_questencounterloot_in_user_library

def create_questencounterloot_in_user_library(function):
	def test_questencounterloot_in_user_library(request, in_project, in_questencounter, *args, **kwargs):
		project = Project.objects.get(id=in_project)

		if project in request.user.user_library.all():
			return function(request, in_project, in_questencounter, *args, **kwargs)
		else:
			raise PermissionDenied

	return test_questencounterloot_in_user_library
