import re

from django import forms
from django.utils.translation import gettext as _

from haystack.forms import ModelSearchForm


BOOLEAN_OPERATORS = (
    ('and', 'and'),
    ('or', 'or'),
    ('and_n', 'and not'),
    ('or_n', 'or not'),
)

FILTERS = (
    ('begins_with', _('Begins with')),
    ('ends_with', _('Ends with')),
    ('contains', _('Contains')),
    ('exactly_equals', _('Exactly equals')),
    ('regex', _('Regular expression')),
)

FILTERS_DICT = {
    'begins_with': '__istartswith',
    'ends_with': '__iendswith',
    'contains': '__icontains',
    'exactly_equals': '',
    'regex': '__iregex',
}

FILTERABLE_FIELDS = (
    ('headword', _('Headword')),
    ('citation_form', _('Citation Form')),
)

FILTERABLE_FIELDS_DICT = {
    'headword': 'headword',
    'citation_form': 'lexcitationform__value',
}


class LexiconSearchForm(ModelSearchForm):
    q = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mr-3'}))


class LexicalSearchFilterForm(forms.Form):
    query_string = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    operator = forms.ChoiceField(
        choices=BOOLEAN_OPERATORS,
        widget=forms.Select(attrs={'class': 'custom-select'})
    )
    filter = forms.ChoiceField(
        choices=FILTERS,
        widget=forms.Select(attrs={'class': 'custom-select'})
    )
    filter_on = forms.ChoiceField(
        choices=FILTERABLE_FIELDS,
        widget=forms.Select(attrs={'class': 'custom-select'})
    )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['filter'] == 'regex':
            qs = cleaned_data['query_string']
            try:
                re.compile(qs)
            except Exception:
                self.add_error('query_string', forms.ValidationError('Invalid regular expression.'))


LexicalSearchFilterFormset = forms.formset_factory(LexicalSearchFilterForm)
