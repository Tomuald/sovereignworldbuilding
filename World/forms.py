from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Field
from crispy_forms.bootstrap import InlineCheckboxes

from World.models import Universe, Region, Area, City, CityDemographics, CityQuarter, Location, LocationLoot, WorldEncounter, WorldEncounterLoot, Empire, Faction, NPC, CityDemographics


class UniverseModelForm(ModelForm):
	class Meta:
		model = Universe
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.universes.filter(name=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, universes, *args, **kwargs):
		super(UniverseModelForm, self).__init__(*args, **kwargs)
		self.universes = universes

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
        	Field('name'),
        	Field('description', id="textarea"),
        	Field('in_project', type="hidden"),
        )

class RegionModelForm(ModelForm):
	class Meta:
		model = Region
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character"
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.regions.filter(name=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, regions, *args, **kwargs):
		super(RegionModelForm, self).__init__(*args, **kwargs)
		self.regions = regions

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('name'),
			Field('landscape'),
			Field('biome'),
			Field('description', id="textarea"),
			Field('in_project', type="hidden"),
			Field('in_universe', type="hidden"),
		)

class AreaModelForm(ModelForm):
	class Meta:
		model = Area
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.areas.filter(name=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, areas, factions, *args, **kwargs):
		super(AreaModelForm, self).__init__(*args, **kwargs)
		self.areas = areas
		self.fields['factions'].queryset = factions

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('name'),
			Field('landscape'),
			Field('area_type'),
			Field('description', id="textarea"),
			Field('flavor_text'),
			InlineCheckboxes('factions'),
			Field('in_project', type="hidden"),
			Field('in_region', type="hidden"),
		)

class CityModelForm(ModelForm):
	class Meta:
		model = City
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.cities.filter(name=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, cities, *args, **kwargs):
		super(CityModelForm, self).__init__(*args, **kwargs)
		self.cities = cities

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('name'),
			Field('landscape'),
			Field('population'),
			Field('description', id="textarea"),
			Field('flavor_text'),
			Field('in_project', type="hidden"),
			Field('in_region', type="hidden"),
		)

class CityQuarterModelForm(ModelForm):
	class Meta:
		model = CityQuarter
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.cityquarters.filter(name=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, cityquarters, factions, *args, **kwargs):
		super(CityQuarterModelForm, self).__init__(*args, **kwargs)
		self.cityquarters = cityquarters
		self.fields['factions'].queryset = factions

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('name'),
			Field('description', id="textarea"),
			Field('flavor_text'),
			InlineCheckboxes('factions'),
			Field('in_project', type="hidden"),
			Field('in_city', type="hidden"),
		)

class LocationModelForm(ModelForm):
	class Meta:
		model = Location
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.locations.filter(name=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, locations, npcs, exit_points, *args, **kwargs):
		super(LocationModelForm, self).__init__(*args, **kwargs)
		self.locations = locations
		self.fields['NPCs'].queryset = npcs
		self.fields['exit_points'].queryset = exit_points

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('name'),
			Field('landscape'),
			Field('location_type'),
			Field('description', id="textarea"),
			Field('flavor_text'),
			InlineCheckboxes('NPCs'),
			InlineCheckboxes('exit_points'),
			Field('in_project', type="hidden"),
			Field('in_area', type="hidden"),
			Field('in_cityquarter', type="hidden"),
		)

class LocationLootModelForm(ModelForm):
	class Meta:
		model = LocationLoot
		fields = '__all__'

	def __init__(self, items, *args, **kwargs):
		super(LocationLootModelForm, self).__init__(*args, **kwargs)
		self.fields['name'].queryset = items

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Row(
				Field('name', wrapper_class="col-md-6"),
				Field('quantity', wrapper_class="col-md-6"),
				Field('in_project', type="hidden"),
				Field('in_location', type="hidden"),
			)
		)

class EmpireModelForm(ModelForm):
	class Meta:
		model = Empire
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.empires.filter(name=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, empires, regions, faiths, *args, **kwargs):
		super(EmpireModelForm, self).__init__(*args, **kwargs)
		self.empires = empires
		self.fields['regions'].queryset = regions
		self.fields['faiths'].queryset = faiths

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('name'),
			Field('description', id="textarea"),
			InlineCheckboxes('regions'),
			InlineCheckboxes('faiths'),
			Field('in_project', type="hidden"),
			Field('in_universe', type="hidden"),
		)

class FactionModelForm(ModelForm):
	class Meta:
		model = Faction
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.factions.filter(name=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, leaders, factions, faiths, *args, **kwargs):
		super(FactionModelForm, self).__init__(*args, **kwargs)
		self.factions = factions
		self.fields['leaders'].queryset = leaders
		self.fields['faiths'].queryset = faiths

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('name'),
			Field('faction_role'),
			Field('alignment'),
			Field('description', id="textarea"),
			InlineCheckboxes('leaders'),
			InlineCheckboxes('faiths'),
			Field('in_project', type="hidden"),
			Field('in_universe', type="hidden"),
		)

class NPCModelForm(ModelForm):
	class Meta:
		model = NPC
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.npcs.filter(name=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, factions, npcs, faiths, *args, **kwargs):
		super(NPCModelForm, self).__init__(*args, **kwargs)
		self.fields['in_faction'].queryset = factions
		self.fields['faiths'].queryset = faiths
		self.npcs = npcs

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('name'),
			Field('portrait'),
			Field('in_faction'),
			Field('alignment'),
			Field('description', id="textarea"),
			InlineCheckboxes('faiths'),
			Field('in_project', type="hidden"),
			Field('in_universe', type="hidden"),
		)

class WorldEncounterModelForm(ModelForm):
	class Meta:
		model = WorldEncounter
		fields = '__all__'

	def clean_title(self):
		data = self.cleaned_data['title']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.title == data:
			if self.worldencounters.filter(title=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, npcs, worldencounters, *args, **kwargs):
		super(WorldEncounterModelForm, self).__init__(*args, **kwargs)
		self.worldencounters = worldencounters
		self.fields['involved_npcs'].queryset = npcs

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('title'),
			Field('encounter_num'),
			Field('encounter_type'),
			Field('dramatic_question'),
			Field('summary', id="textarea"),
			Field('flavor_text'),
			InlineCheckboxes('involved_npcs'),
			Field('in_project', type="hidden"),
			Field('in_location', type="hidden"),
			Field('in_dungeon_room', type="hidden"),
		)

class WorldEncounterLootModelForm(ModelForm):
	class Meta:
		model = WorldEncounterLoot
		fields = '__all__'

	def __init__(self, items, *args, **kwargs):
		super(WorldEncounterLootModelForm, self).__init__(*args, **kwargs)
		self.fields['name'].queryset = items

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Row(
				Field('name', wrapper_class="col-md-6"),
				Field('quantity', wrapper_class="col-md-6"),
				Field('in_project', type="hidden"),
				Field('in_worldencounter', type="hidden"),
			)
		)
class CityDemographicsModelForm(ModelForm):
	class Meta:
		model = CityDemographics
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(CityDemographicsModelForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Row(
				Field('race', wrapper_class="col-md-6"),
				Field('percent', wrapper_class="col-md-6"),
				Field('in_project', type="hidden"),
				Field('in_city', type="hidden")
			)
		)
