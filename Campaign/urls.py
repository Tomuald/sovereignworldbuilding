from django.urls import path

from Campaign.views import campaign_detail, campaign_index, campaign_create, campaign_delete
from Campaign.views import chapter_detail, chapter_create, chapter_delete
from Campaign.views import quest_detail, quest_create, quest_delete
from Campaign.views import questencounter_detail, questencounter_create, questencounter_delete
from Campaign.views import questencounterloot_create, questencounterloot_delete

urlpatterns = []

# Detail Views
urlpatterns = [
	path('<int:pk>/index/', campaign_index, name="campaign-index"),
	path('<int:pk>/', campaign_detail, name="campaign-detail"),
	path('chapter/<int:pk>/', chapter_detail, name="chapter-detail"),
	path('quest/<int:pk>/', quest_detail, name="quest-detail"),
	path('questencounter/<int:pk>/', questencounter_detail, name="questencounter-detail"),
]

# Create, Update and Delete Views
urlpatterns += [
	# Campaigns
	path('<int:in_project>/create/campaign/', campaign_create, name="campaign-create"),
	path('<int:in_project>/update/campaign/<int:pk>/', campaign_create, name="campaign-update"),
	path('delete/<int:pk>/', campaign_delete, name="campaign-delete"),
	
	# Chapters
	path('<int:in_campaign>/create/chapter/', chapter_create, name="chapter-create"),
	path('<int:in_campaign>/update/chapter/<int:pk>/', chapter_create, name="chapter-update"),
	path('chapter/delete/<int:pk>/', chapter_delete, name="chapter-delete"),
	
	# Quests
	path('chapter/<int:in_chapter>/create/quest/', quest_create, name="quest-create"),
	path('chapter/<int:in_chapter>/update/quest/<int:pk>', quest_create, name="quest-update"),
	path('quest/delete/<int:pk>/', quest_delete, name="quest-delete"),
	
	# Quest Encounters
	path('quest/<int:in_quest>/encounter/create/', questencounter_create, name="questencounter-create"),
	path('quest/<int:in_quest>/encounter/update/<int:pk>/', questencounter_create, name="questencounter-update"),
	path('questencounter/delete/<int:pk>/', questencounter_delete, name="questencounter-delete"),
	
	# Quest Encounter Loot
	path('questencounter/<int:in_questencounter>/encounterloot/create/', questencounterloot_create, name="questencounterloot-create"),
	path('questencounter/encounterloot/delete/<int:pk>/', questencounterloot_delete, name="questencounterloot-delete"),
]
