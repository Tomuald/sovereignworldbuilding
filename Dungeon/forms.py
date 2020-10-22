from django import forms
from django.forms import ModelForm

from tinymce.widgets import TinyMCE
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import InlineCheckboxes

from Dungeon.models import Dungeon, Roomset, Room, RoomLoot

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
	
	def __init__(self, rooms, *args, **kwargs):
		super(RoomModelForm, self).__init__(*args, **kwargs)
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
