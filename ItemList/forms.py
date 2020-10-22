from django import forms
from django.forms import ModelForm

from django.core.exceptions import ValidationError

from tinymce.widgets import TinyMCE
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from ItemList.models import Itemlist, Item

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
