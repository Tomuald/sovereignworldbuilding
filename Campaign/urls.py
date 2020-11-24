from django.urls import path

from Campaign.views import campaign_detail, campaign_index, campaign_create, campaign_update, campaign_delete
from Campaign.views import chapter_detail, chapter_create, chapter_update, chapter_delete
from Campaign.views import quest_detail, quest_create, quest_update, quest_delete
from Campaign.views import questencounter_detail, questencounter_create, questencounter_update, questencounter_delete
from Campaign.views import questencounterloot_create, questencounterloot_delete

urlpatterns = []

# Detail Views
urlpatterns = [
	path('<int:in_project>/c/<str:title>/index/', campaign_index, name="campaign-index"),
	path('<int:in_project>/c/<str:title>/', campaign_detail, name="campaign-detail"),
	path('<int:in_project>/ch/<str:title>/', chapter_detail, name="chapter-detail"),
	path('<int:in_project>/q/<str:title>/', quest_detail, name="quest-detail"),
	path('<int:in_project>/qe/<str:title>/', questencounter_detail, name="questencounter-detail"),
]

# Create, Update and Delete Views
urlpatterns += [
	# Campaigns
	path('<int:in_project>/c/create/new/', campaign_create, name="campaign-create"),
	path('<int:in_project>/c/<str:title>/update/', campaign_update, name="campaign-update"),
	path('<int:in_project>/c/<str:title>/delete/', campaign_delete, name="campaign-delete"),

	# Chapters
	path('<int:in_project>/c/<str:in_campaign>/ch/create/new/', chapter_create, name="chapter-create"),
	path('<int:in_project>/ch/<str:title>/update/', chapter_update, name="chapter-update"),
	path('<int:in_project>/ch/<str:title>/delete/', chapter_delete, name="chapter-delete"),

	# Quests
	path('<int:in_project>/ch/<str:in_chapter>/q/create/new/', quest_create, name="quest-create"),
	path('<int:in_project>/q/<str:title>/update/', quest_update, name="quest-update"),
	path('<int:in_project>/q/<str:title>/delete/', quest_delete, name="quest-delete"),

	# Quest Encounters
	path('<int:in_project>/q/<str:in_quest>/qe/create/new/', questencounter_create, name="questencounter-create"),
	path('<int:in_project>/qe/<str:title>/update/', questencounter_update, name="questencounter-update"),
	path('<int:in_project>/qe/<str:title>/delete/', questencounter_delete, name="questencounter-delete"),

	# Quest Encounter Loot
	path('<int:in_project>/qe/<str:in_questencounter>/qel/create/new/', questencounterloot_create, name="questencounterloot-create"),
	path('<int:in_project>/qel/<int:pk>/delete/', questencounterloot_delete, name="questencounterloot-delete"),
]
