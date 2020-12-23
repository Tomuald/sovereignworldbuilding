from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from theLodge.models import SharedItemlist
from theLodge.models import SharedUniverse

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
    itemlist_name = forms.CharField()

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
        self.fields['itemlist_name'].initial = self.il_name

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Import', css_class="btn-success float-right"))

        self.helper.layout = Layout(
            Field('itemlist_name', readonly=True),
            Field('to_project'),
        )
class ExportUniverseForm(forms.ModelForm):
    class Meta:
        model = SharedUniverse
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExportUniverseForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Export', css_class="btn-success float-right"))

        self.helper.layout = Layout(
            Field('name', readonly=True),
            Field('game_system'),
            Field('description'),
            Field('shared_by', type="hidden"),
            Field('universe', type="hidden"),
        )

class ImportUniverseForm(forms.Form):
    to_project = forms.ModelChoiceField(queryset=None)
    universe_name = forms.CharField()

    def clean(self):
        data = self.cleaned_data['to_project']
        if data.universe_set.filter(name=self.universe_name).exists():
            msg = "%s already exists in this project." % self.universe_name
            self.add_error('to_project', msg)
        if data.universe_set.count() == 1:
            msg = "A project can only contain 1 universe."
            self.add_error('to_project', msg)

    def __init__(self, projects, universe_name, *args, **kwargs):
        super(ImportUniverseForm, self).__init__(*args, **kwargs)
        self.fields['to_project'].queryset = projects
        self.universe_name = universe_name
        self.fields['universe_name'].initial = self.universe_name

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Import', css_class="btn-success float-right"))

        self.helper.layout = Layout(
            Field('universe_name', readonly=True),
            Field('to_project'),
        )
