from django import forms
from django.forms import ModelForm

from tinymce.widgets import TinyMCE
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from Pantheon.models import Pantheon, God

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
