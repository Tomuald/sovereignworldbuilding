from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from Pantheon.models import Pantheon, God

class PantheonModelForm(ModelForm):
	class Meta:
		model = Pantheon
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.pantheons.filter(name=data).exists():
				msg = "%s is already in this project" % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, pantheons, *args, **kwargs):
		super(PantheonModelForm, self).__init__(*args, **kwargs)
		self.pantheons = pantheons

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('name'),
			Field('background', id="textarea"),
			Field('in_project', type="hidden"),
			Field('in_universe', type="hidden"),
		)

class GodModelForm(ModelForm):
	class Meta:
		model = God
		fields = '__all__'

	def clean_name(self):
		data = self.cleaned_data['name']
		if '/' in data:
			msg = "'/' is not a valid character."
			raise forms.ValidationError(msg)
		if not self.instance.name == data:
			if self.gods.filter(name=data).exists():
				msg = "%s already exists in this project." % data
				raise forms.ValidationError(msg)
		return data

	def __init__(self, gods, *args, **kwargs):
		super(GodModelForm, self).__init__(*args, **kwargs)
		self.gods = gods

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Create', css_class="btn-success float-right"))

		self.helper.layout = Layout(
			Field('name'),
			Field('alternative_names'),
			Field('alignment'),
			Field('background', id="textarea"),
			Field('in_project', type="hidden"),
			Field('in_pantheon', type="hidden"),
		)
