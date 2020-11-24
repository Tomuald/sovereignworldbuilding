from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Row
from crispy_forms.bootstrap import InlineCheckboxes

from Dungeon.models import Dungeon, Roomset, Room, RoomLoot

class DungeonModelForm(ModelForm):
	class Meta:
		model = Dungeon
		fields = '__all__'

	def clean_title(self):
		data = self.cleaned_data['title']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.title == data:
			if self.dungeons.filter(title=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)

		return data

	def __init__(self, dungeons, *args, **kwargs):
		super(DungeonModelForm, self).__init__(*args, **kwargs)
		self.dungeons = dungeons
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('title'),
			Field('landscape'),
			Field('description', id="textarea"),
			Field('in_project', type="hidden"),
			Field('in_area', type="hidden"),
		)

class RoomsetModelForm(ModelForm):
	class Meta:
		model = Roomset
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.roomsets.filter(name=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, roomsets, *args, **kwargs):
		super(RoomsetModelForm, self).__init__(*args, **kwargs)
		self.roomsets = roomsets

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('name'),
			Field('description', id="textarea"),
			Field('in_project', type="hidden"),
			Field('in_dungeon', type="hidden"),
		)

class RoomModelForm(ModelForm):
	class Meta:
		model = Room
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.rooms.filter(name=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, room_exits, rooms, *args, **kwargs):
		super(RoomModelForm, self).__init__(*args, **kwargs)
		self.rooms = rooms
		self.fields['exits'].queryset = room_exits

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('name'),
			Field('room_number'),
			Field('description', id="textarea"),
			Field('flavor_text'),
			InlineCheckboxes('exits'),
			Field('in_project', type="hidden"),
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
				Field('in_project', type="hidden"),
				Field('in_room', type="hidden")
			)
		)
