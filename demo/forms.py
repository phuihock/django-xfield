#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import forms, fields
from django.utils.translation import ugettext as _
from xfield.fields import ExpandableField
from xfield.widgets import ExpandableWidget

class EchoForm0(forms.Form):
    input = ExpandableField(fields.CharField, min_values=0, max_length=100)

class EchoForm1(forms.Form):
    input = ExpandableField(fields.CharField, min_values=1, max_length=100)

class EchoForm2(forms.Form):
    input = ExpandableField(fields.CharField, min_values=3, max_length=100, initial=['First', '', 'Third'])  # you can provide initial values, but it must be a list

class EchoForm3(forms.Form):
    COLOR_CHOICES = (
        ('r', _('Red')),
        ('y', _('Yellow')),
        ('b', _('Blue')),
        ('g', _('Green')),
    )
    input = ExpandableField(fields.ChoiceField, min_values=1, choices=COLOR_CHOICES)

class EchoForm4(EchoForm0):
    def clean_input(self):
        error_messages = []
        has_error = False
        values = self.cleaned_data['input']  # because this is an expandable field, it returns a list
        for v in values:
            if v != 'Y' and v != 'y':
                error_messages.append('You can only answer "Y"')
                has_error = True
            else:
                error_messages.append('')
        if has_error:
            raise forms.ValidationError(error_messages)
        return values

class EchoForm5(forms.Form):
    input = ExpandableField(fields.IntegerField, min_values=1, initial=[1])  # you can provide initial, but it must a list
    def clean(self):
        error_messages = []
        has_error = False
        values = self.cleaned_data['input']  # because this is an expandable field, it returns a list
        
        for i, cv in enumerate(values):
            if i > 0:
                pv = values[i - 1]
                if pv and pv >= cv:
                    error_messages.append('This must be larger than %d' % pv)
                    has_error = True
                    continue
            error_messages.append('')
        if has_error:
            self._errors['input'] = self.error_class(error_messages)
            del self.cleaned_data['input']
        return self.cleaned_data

