from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Field
from crispy_forms.bootstrap import InlineCheckboxes

from Campaign.models import Campaign, Chapter, Quest, QuestEncounter, QuestEncounterLoot
from Project.models import Project



###############################
### --- #CAMPAIGN FORMS --- ###
###############################

class CampaignModelForm(ModelForm):
	class Meta:
		model = Campaign
		fields = '__all__'

	def clean_title(self):
		data = self.cleaned_data['title']
		if not self.instance.title == data:
			if self.campaigns.filter(title=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, campaigns, universes, *args, **kwargs):
		self.campaigns = campaigns
		super(CampaignModelForm, self).__init__(*args, **kwargs)
		self.fields['in_universe'].queryset = universes

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

	def clean_title(self):
		data = self.cleaned_data['title']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.title == data:
			if self.chapters.filter(title=data).exists():
				msg = "%s already exists in %s" % (data, self.campaign.title)
				raise forms.ValidationError(msg)
		return data

	def __init__(self, chapters, regions, npcs, *args, **kwargs):
		super(ChapterModelForm, self).__init__(*args, **kwargs)
		self.chapters = chapters
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
			Field('in_project', type="hidden"),
			Field('in_campaign', type="hidden"),
		)

class QuestModelForm(ModelForm):
	class Meta:
		model = Quest
		fields = '__all__'

	def clean_title(self):
		data = self.cleaned_data['title']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.title == data:
			if self.quests.filter(title=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, areas, cities, npcs, quests, *args, **kwargs):
		super(QuestModelForm, self).__init__(*args, **kwargs)
		self.quests = quests
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
			Field('in_project', type="hidden"),
			Field('in_chapter', type="hidden"),
		)

class QuestEncounterModelForm(ModelForm):
	class Meta:
		model = QuestEncounter
		fields = '__all__'

	def clean_title(self):
		data = self.cleaned_data['title']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.title == data:
			if self.questencounters.filter(title=data).exists():
				msg = "%s already in project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, questencounters, npcs, locations, dungeonrooms, *args, **kwargs):
		super(QuestEncounterModelForm, self).__init__(*args, **kwargs)
		self.questencounters = questencounters
		self.fields['involved_npcs'].queryset = npcs
		self.fields['in_location'].queryset = locations
		self.fields['in_dungeon_room'].queryset = dungeonrooms

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
			Field('in_project', type="hidden"),
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
				Field('in_project', type="hidden"),
				Field('in_questencounter', type="hidden"),
			)
		)
