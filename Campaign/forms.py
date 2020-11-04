from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Field
from crispy_forms.bootstrap import InlineCheckboxes

from Campaign.models import Campaign, Chapter, Quest, QuestEncounter, QuestEncounterLoot

###############################	
### --- #CAMPAIGN FORMS --- ###
###############################

class CampaignModelForm(ModelForm):
	class Meta:
		model = Campaign
		fields = '__all__'
	
	def __init__(self, *args, **kwargs):
		universe = kwargs.pop('universes')
		super(CampaignModelForm, self).__init__(*args, **kwargs)
		self.fields['in_universe'].queryset = universe
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('title'),
			Field('in_universe'),
			Field('overview', id="textarea"),
			Field('in_project', type="hidden"),
		)
		
class ChapterModelForm(ModelForm):	
	class Meta:
		model = Chapter
		fields = '__all__'
	
	def __init__(self, campaigns, regions, npcs, *args, **kwargs):
		super(ChapterModelForm, self).__init__(*args, **kwargs)
		self.fields['in_campaign'].queryset = campaigns
		self.fields['regions'].queryset = regions
		self.fields['involved_npcs'].queryset = npcs
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('title'),
			Field('chapter_num'),
			Field('summary', id="textarea"),
			InlineCheckboxes('regions'),
			InlineCheckboxes('involved_npcs'),
			Field('in_campaign', type="hidden"),
		)
		
class QuestModelForm(ModelForm):	
	class Meta:
		model = Quest
		fields = '__all__'
	
	def __init__(self, chapters, areas, cities, npcs, *args, **kwargs):
		super(QuestModelForm, self).__init__(*args, **kwargs)
		self.fields['in_chapter'].queryset = chapters
		self.fields['in_area'].queryset = areas
		self.fields['in_city'].queryset = cities
		self.fields['involved_npcs'].queryset = npcs
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('title'),
			Field('quest_type'),
			Field('quest_num'),
			Row(
				Field('in_area', wrapper_class="col-md-6"),
				Field('in_city', wrapper_class="col-md-6"),
			),
			Field('summary', id="textarea"),
			InlineCheckboxes('involved_npcs'),
			Field('in_chapter', type="hidden")
		)
		
class QuestEncounterModelForm(ModelForm):
	class Meta:
		model = QuestEncounter
		fields = '__all__'
	
	def __init__(self, *args, **kwargs):
		self.npcs = kwargs.pop('npcs')
		self.locations = kwargs.pop('locations')
		self.dungeonrooms = kwargs.pop('dungeonrooms')
		super(QuestEncounterModelForm, self).__init__(*args, **kwargs)
		self.fields['involved_npcs'].queryset = self.npcs
		self.fields['in_location'].queryset = self.locations
		self.fields['in_dungeon_room'].queryset = self.dungeonrooms
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('title'),
			Field('encounter_type'),
			Field('encounter_num'),
			Row(
				Field('in_location', wrapper_class="col-md-6"),
				Field('in_dungeon_room', wrapper_class="col-md-6"),
			),
			Field('dramatic_question'),
			Field('summary', id="textarea"),
			Field('flavor_text'),
			InlineCheckboxes('involved_npcs'),
			Field('in_quest', type="hidden"),
		)
		
class QuestEncounterLootModelForm(ModelForm):
	class Meta:
		model = QuestEncounterLoot
		fields = '__all__'
	
	def __init__(self, *args, **kwargs):
		self.items = kwargs.pop('items')
		super(QuestEncounterLootModelForm, self).__init__(*args, **kwargs)
		self.fields['name'].queryset = self.items
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		self.helper.layout = Layout(
			Row(
				Field('name', wrapper_class="col-md-6"),
				Field('quantity', wrapper_class="col-md-6"),
				Field('in_questencounter', type="hidden"),
			)
		)
