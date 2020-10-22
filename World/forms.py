from django import forms
from django.forms import ModelForm

from tinymce.widgets import TinyMCE
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Field
from crispy_forms.bootstrap import InlineCheckboxes

from World.models import Universe, Region, Area, City, CityQuarter, Location, LocationLoot, WorldEncounter, WorldEncounterLoot, Empire, Faction, NPC


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
