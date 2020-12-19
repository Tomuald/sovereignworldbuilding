from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from theLodge.models import SharedItemlist

class ExportItemlistForm(forms.ModelForm):
    class Meta:
        model = SharedItemlist
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExportItemlistForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Export', css_class="btn-success float-right"))

        self.helper.layout = Layout(
            Field('name', readonly=True),
            Field('game_system'),
            Field('description'),
            Field('shared_by', type="hidden"),
            Field('itemlist', type="hidden"),
        )

class ImportItemlistForm(forms.Form):
    # Queryset of Projects in User's library.
    to_project = forms.ModelChoiceField(queryset=None)

    def clean(self):
        data = self.cleaned_data['to_project']
        if data.itemlist_set.filter(name=self.il_name).exists():
            msg = "%s already exists in this project." % self.il_name
            self.add_error('to_project', msg)

        return data

    def __init__(self, projects, il_name, *args, **kwargs):
        super(ImportItemlistForm, self).__init__(*args, **kwargs)
        self.fields['to_project'].queryset = projects
        self.il_name = il_name

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Import', css_class="btn-success float-right"))

        self.helper.layout = Layout(
            Field('to_project'),
        )
