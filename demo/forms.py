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
    input = ExpandableField(fields.CharField, min_values=3, max_length=100)

class EchoForm3(forms.Form):
    COLOR_CHOICES = (
        ('r', _('Red')),
        ('y', _('Yellow')),
        ('b', _('Blue')),
    )
    input = ExpandableField(fields.ChoiceField, choices=COLOR_CHOICES)

class EchoForm4(EchoForm0):
    def clean_input(self):
        error_messages = []
        has_error = False
        values = self.cleaned_data['input']  # this is a list
        for v in values:
            if v != 'Y' and v != 'y':
                error_messages.append('You can only answer "Y"')
                has_error = True
            else:
                error_messages.append('')
        if has_error:
            raise forms.ValidationError(error_messages)
        return values
