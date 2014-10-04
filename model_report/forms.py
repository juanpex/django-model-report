# coding=utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _


class ConfigForm(forms.Form):

    DEFAULT_CHART_TYPES = (
        ('area', _('Area')),
        ('line', _('Line')),
        ('column', _('Columns')),
        ('pie', _('Pie')),
    )
    CHART_SERIE_OPERATOR = (
        ('', '---------'),
        ('sum', _('Sum')),
        ('len', _('Count')),
        ('avg', _('Average')),
        ('min', _('Min')),
        ('max', _('Max')),
    )

    chart_mode = forms.ChoiceField(label=_('Chart type'), choices=(), required=False)
    serie_field = forms.ChoiceField(label=_('Serie field'), choices=(), required=False)
    serie_op = forms.ChoiceField(label=_('Serie operator'), choices=CHART_SERIE_OPERATOR, required=False)

    def __init__(self, *args, **kwargs):
        super(ConfigForm, self).__init__(*args, **kwargs)
        choices = [('', '')]
        for k, v in self.DEFAULT_CHART_TYPES:
            if k in self.chart_types:
                choices.append([k, v])
        self.fields['chart_mode'].choices = list(choices)
        choices = [('', '')]
        for i, (index, mfield, field, caption) in enumerate(self.serie_fields):
            choices += (
                (index, caption),
            )
        self.fields['serie_field'].choices = list(choices)

    def get_config_data(self):
        data = getattr(self, 'cleaned_data', {})
        if not data:
            return {}
        if not data['serie_field'] or not data['chart_mode'] or not data['serie_op']:
            return {}
        data['serie_field'] = int(data['serie_field'])
        return data


class GroupByForm(forms.Form):

    groupby = forms.ChoiceField(label=_('Group by field:'), required=False)
    onlytotals = forms.BooleanField(label=_('Show only totals'), required=False)

    def _post_clean(self):
        pass

    def __init__(self, **kwargs):
        super(GroupByForm, self).__init__(**kwargs)
        choices = [(None, '')]
        for i, (mfield, field, caption) in enumerate(self.groupby_fields):
            choices.append((field, caption))
        self.fields['groupby'].choices = choices
        data = kwargs.get('data', {})
        if data:
            self.fields['groupby'].initial = data.get('groupby', '')

    def get_cleaned_data(self):
        cleaned_data = getattr(self, 'cleaned_data', {})
        if 'groupby' in cleaned_data:
            if unicode(cleaned_data['groupby']) == u'None':
                cleaned_data['groupby'] = None
        return cleaned_data