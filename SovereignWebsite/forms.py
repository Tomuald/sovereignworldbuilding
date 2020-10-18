from django import forms

from tinymce.widgets import TinyMCE

from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Submit, Row
from crispy_forms.bootstrap import InlineCheckboxes

from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory

from World.models import Universe, Region, NPC, Faction, Area, City, CityQuarter, Empire, Location, LocationLoot, WorldEncounter, WorldEncounterLoot
from Campaign.models import Campaign, Chapter, Quest, QuestEncounter, QuestEncounterLoot
from Pantheon.models import Pantheon, God
from Dungeon.models import Dungeon, Roomset, Room, RoomLoot
from ItemList.models import Itemlist, Item
from Project.models import Project

##############################
### --- #PROJECT FORMS --- ###
##############################

class ProjectModelForm(ModelForm):
	class Meta:
		model = Project
		fields = '__all__'
		
	def __init__(self, *args, **kwargs):
		super(ProjectModelForm, self).__init__(*args, **kwargs)
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('title'),
			Field('game_system'),
			Field('created_by', type="hidden"))

############################	
### --- #WORLD FORMS --- ###
############################

class UniverseModelForm(ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={'relative_urls': False}), required=False)
	
	class Meta:
		model = Universe
		fields = '__all__'
	
	def __init__(self, *args, **kwargs):
		super(UniverseModelForm, self).__init__(*args, **kwargs)
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
        	Field('name'),
        	Field('description'),
        	Field('in_project', type="hidden"),
        )

class EmpireModelForm(ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows':30}, mce_attrs={'relative_urls': False}), required=False)
	
	class Meta:
		model = Empire
		fields = '__all__'
		
	def __init__(self, regions, universe_set, faiths, *args, **kwargs):
		super(EmpireModelForm, self).__init__(*args, **kwargs)
		self.fields['regions'].queryset = regions
		self.fields['in_universe'].queryset = universe_set
		self.fields['faiths'].queryset = faiths
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('name'),
			Field('description'),
			InlineCheckboxes('regions'),
			InlineCheckboxes('faiths'),
			Field('in_universe', type="hidden"),
		)

class RegionModelForm(ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={'relative_urls': False}), required=False)
	
	class Meta:
		model = Region
		fields = '__all__'
	
	def __init__(self, universe_set, *args, **kwargs):
		super(RegionModelForm, self).__init__(*args, **kwargs)
		self.fields['in_universe'].queryset = universe_set
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('name'),
			Field('landscape'),
			Field('biome'),
			Field('description'),
			Field('in_universe', type="hidden"),
		)

class AreaModelForm(ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30},
												 mce_attrs={'relative_urls': False}),
												 required=False)

	class Meta:
		model = Area
		fields = '__all__'

	def __init__(self, regions, factions, *args, **kwargs):
		super(AreaModelForm, self).__init__(*args, **kwargs)
		self.fields['in_region'].queryset = regions
		self.fields['factions'].queryset = factions
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('name'),
			Field('landscape'),
			Field('area_type'),
			Field('description'),
			Field('flavor_text'),
			InlineCheckboxes('factions'),
			Field('in_region', type="hidden"),
		)

class CityModelForm(ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={'relative_urls': False}), required=False)
	
	class Meta:
		model = City
		fields = '__all__'
	
	def __init__(self, regions, *args, **kwargs):
		super(CityModelForm, self).__init__(*args, **kwargs)
		self.fields['in_region'].queryset = regions
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('name'),
			Field('landscape'),
			Field('population'),
			Field('description'),
			Field('flavor_text'),
			Field('in_region', type="hidden"),
		)

class CityQuarterModelForm(ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={'relative_urls': False}), required=False)
	
	class Meta:
		model = CityQuarter
		fields = '__all__'
	
	def __init__(self, cities, factions, *args, **kwargs):
		super(CityQuarterModelForm, self).__init__(*args, **kwargs)
		self.fields['in_city'].queryset = cities
		self.fields['factions'].queryset = factions
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('name'),
			Field('description'),
			Field('flavor_text'),
			InlineCheckboxes('factions'),
			Field('in_city', type="hidden"),			
		)

class LocationModelForm(ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={'relative_urls': False}), required=False)
	
	class Meta:
		model = Location
		fields = '__all__'
		
	def __init__(self, *args, **kwargs):
		self.npcs = kwargs.pop('npcs')
		self.exit_points = kwargs.pop('exit_points')
		super(LocationModelForm, self).__init__(*args, **kwargs)
		self.fields['NPCs'].queryset = self.npcs
		self.fields['exit_points'].queryset = self.exit_points
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('name'),
			Field('landscape'),
			Field('location_type'),
			Field('description'),
			Field('flavor_text'),
			InlineCheckboxes('NPCs'),
			InlineCheckboxes('exit_points'),
			Field('in_area', type="hidden"),
			Field('in_cityquarter', type="hidden"),
		)

class LocationLootModelForm(ModelForm):
	class Meta:
		model = LocationLoot
		fields = '__all__'
		
	def __init__(self, *args, **kwargs):
		super(LocationLootModelForm, self).__init__(*args, **kwargs)
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Row(
				Field('name', wrapper_class="col-md-6"),
				Field('quantity', wrapper_class="col-md-6"),
				Field('in_location', type="hidden"),
			)
		)

class NPCModelForm(ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={'relative_urls': False}), required=False)
	

	class Meta:
		model = NPC
		fields = '__all__'

	def __init__(self, factions, universe_set, faiths, *args, **kwargs):
		super(NPCModelForm, self).__init__(*args, **kwargs)
		self.fields['in_faction'].queryset = factions
		self.fields['in_universe'].queryset = universe_set
		self.fields['faiths'].queryset = faiths
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('name'),
			Field('portrait'),
			Field('in_faction'),
			Field('alignment'),
			Field('description'),
			InlineCheckboxes('faiths'),
			Field('in_universe', type="hidden"),
		)
        
class FactionModelForm(ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={'relative_urls': False}), required=False)
	
	class Meta:
		model = Faction
		fields = '__all__'

	def __init__(self, leaders, universe_set, faiths, *args, **kwargs):
		super(FactionModelForm, self).__init__(*args, **kwargs)
		self.fields['leaders'].queryset = leaders
		self.fields['in_universe'].queryset = universe_set
		self.fields['faiths'].queryset = faiths
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('name'),
			Field('faction_role'),
			Field('alignment'),
			Field('description'),
			InlineCheckboxes('leaders'),
			InlineCheckboxes('faiths'),
			Field('in_universe', type="hidden"),
		)

		
class WorldEncounterModelForm(ModelForm):
	summary = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={'relative_urls': False}), required=False)
	
	class Meta:
		model = WorldEncounter
		fields = '__all__'
	
	def __init__(self, *args, **kwargs):
		self.npcs = kwargs.pop('npcs')
		super(WorldEncounterModelForm, self).__init__(*args, **kwargs)
		self.fields['involved_npcs'].queryset = self.npcs
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('title'),
			Field('encounter_num'),
			Field('encounter_type'),
			Field('dramatic_question'),
			Field('summary'),
			Field('flavor_text'),
			InlineCheckboxes('involved_npcs'),
			Field('in_location', type="hidden"),
			Field('in_dungeon_room', type="hidden"),
		)

class WorldEncounterLootModelForm(ModelForm):
	class Meta:
		model = WorldEncounterLoot
		fields = '__all__'
		
	def __init__(self, *args, **kwargs):
		self.items = kwargs.pop('items')
		super(WorldEncounterLootModelForm, self).__init__(*args, **kwargs)
		self.fields['name'].queryset = self.items
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Row(
				Field('name', wrapper_class="col-md-6"),
				Field('quantity', wrapper_class="col-md-6"),
				Field('in_worldencounter', type="hidden"),
			)
		)

##############################	
### --- #DUNGEON FORMS --- ###
##############################

class DungeonModelForm(ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30},
												 mce_attrs={'relative_urls': False}),
												 required=False
											)
	class Meta:
		model = Dungeon
		fields = '__all__'
	
	def __init__(self, areas, *args, **kwargs):
		super(DungeonModelForm, self).__init__(*args, **kwargs)
		self.fields['in_area'].queryset = areas
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('title'),
			Field('landscape'),
			Field('description'),
			Field('in_area', type="hidden"),
		)

class RoomsetModelForm(ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30},
												 mce_attrs={'relative_urls': False}),
												 required=False
											)
	class Meta:
		model = Roomset
		fields = '__all__'
	
	def __init__(self, dungeons, *args, **kwargs):
		super(RoomsetModelForm, self).__init__(*args, **kwargs)
		self.fields['in_dungeon'].queryset = dungeons
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('name'),
			Field('description'),
			Field('in_dungeon', type="hidden"),
		)

class RoomModelForm(ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30},
												 mce_attrs={'relative_urls': False}),
												 required=False
											)

	class Meta:
		model = Room
		fields = '__all__'
	
	def __init__(self, rooms, connected_to, *args, **kwargs):
		super(RoomModelForm, self).__init__(*args, **kwargs)
		self.fields['exits'].initial = connected_to
		self.initial['exits'] = [room.pk for room in connected_to]
		self.fields['exits'].queryset = rooms
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('name'),
			Field('room_number'),
			Field('description'),
			Field('flavor_text'),
			InlineCheckboxes('exits'),
			Field('in_roomset', type="hidden"),
		)
		
class RoomLootModelForm(ModelForm):
	class Meta:
		model = RoomLoot
		fields = '__all__'
	
	def __init__(self, *args, **kwargs):
		self.items = kwargs.pop('items')
		super(RoomLootModelForm, self).__init__(*args, **kwargs)
		self.fields['name'].queryset = self.items
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Row(
				Field('name', wrapper_class="col-md-6"),
				Field('quantity', wrapper_class="col-md-6"),
				Field('in_room', type="hidden")
			)
		)

###############################	
### --- #CAMPAIGN FORMS --- ###
###############################

class CampaignModelForm(ModelForm):
	overview = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={'relative_urls': False}), required=False)
	
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
			Field('overview'),
			Field('in_project', type="hidden"),
		)
		
class ChapterModelForm(ModelForm):
	summary = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={'relative_urls': False}), required=False)
	
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
			Field('summary'),
			InlineCheckboxes('regions'),
			InlineCheckboxes('involved_npcs'),
			Field('in_campaign', type="hidden"),
		)
		
class QuestModelForm(ModelForm):
	summary = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={'relative_urls': False}), required=False)
	
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
			Field('summary'),
			InlineCheckboxes('involved_npcs'),
			Field('in_chapter', type="hidden")
		)
		
class QuestEncounterModelForm(ModelForm):
	summary = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={'relative_urls': False}), required=False)
	
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
			Field('summary'),
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

###############################	
### --- #PANTHEON FORMS --- ###
###############################

class PantheonModelForm(ModelForm):
	background = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30},
												mce_attrs={'relative_urls': False}), required=False)
												
	class Meta:
		model = Pantheon
		fields = '__all__'
		
	def __init__(self, universe_set, *args, **kwargs):
		super(PantheonModelForm, self).__init__(*args, **kwargs)
		self.fields['in_universe'].queryset = universe_set
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('name'),
			Field('background'),
			Field('in_universe', type="hidden"),
		)
		
class GodModelForm(ModelForm):
	background = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30},
												mce_attrs={'relative_urls': False}), required=False)
												
	class Meta:
		model = God
		fields = '__all__'
		
	def __init__(self, pantheons, *args, **kwargs):
		super(GodModelForm, self).__init__(*args, **kwargs)
		self.fields['in_pantheon'].queryset = pantheons
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('name'),
			Field('alternative_names'),
			Field('alignment'),
			Field('background'),
			Field('in_pantheon', type="hidden"),
		)
		
###############################	
### --- #ITEMLIST FORMS --- ###
###############################

class ItemlistModelForm(ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30},
												 mce_attrs={'relative_urls': False}), required=False
											)
	class Meta:
		model = Itemlist
		fields = '__all__'
		
	def __init__(self, *args, **kwargs):
		super(ItemlistModelForm, self).__init__(*args, **kwargs)
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('name'),
			Field('description'),
			Field('in_project', type="hidden"),
		)
		
class ItemModelForm(ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30},
												 mce_attrs={'relative_urls': False}), required=False
											)
	
	def clean_name(self):
		data = self.cleaned_data['name']
		itemlist = Itemlist.objects.get(name=self.in_itemlist.name)
		for item in itemlist.item_set.all():
			if item.name == data:
				msg = "%s is already in %s" % (data, self.in_itemlist.name)
				raise forms.ValidationError(msg)
				
		return data
	
	class Meta:
		model = Item
		fields = '__all__'
	
	def __init__(self, in_itemlist, *args, **kwargs):
		super(ItemModelForm, self).__init__(*args, **kwargs)
		self.in_itemlist = in_itemlist
		
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))
		
		self.helper.layout = Layout(
			Field('name'),
			Field('item_type'),
			Field('item_cost'),
			Field('description'),
			Field('in_itemlist', type="hidden"),
		)
