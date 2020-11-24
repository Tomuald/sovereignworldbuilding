from django import forms
from django.forms import ModelForm

from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from ItemList.models import Itemlist, Item
from Project.models import Project

class ItemlistModelForm(ModelForm):
	class Meta:
		model = Itemlist
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.itemlists.filter(name=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data


	def __init__(self, itemlists, *args, **kwargs):
		super(ItemlistModelForm, self).__init__(*args, **kwargs)
		self.itemlists = itemlists

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('name'),
			Field('description', id="textarea"),
			Field('in_project', type="hidden"),
		)

class ItemModelForm(ModelForm):
	class Meta:
		model = Item
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.items.filter(name=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, items, *args, **kwargs):
		super(ItemModelForm, self).__init__(*args, **kwargs)
		self.items = items

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('name'),
			Field('item_type'),
			Field('item_cost'),
			Field('description', id="textarea"),
			Field('in_project', type="hidden"),
			Field('in_itemlist', type="hidden"),
		)
