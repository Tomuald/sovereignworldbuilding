from django import forms

from tinymce.widgets import TinyMCE
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from Project.models import Project


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
