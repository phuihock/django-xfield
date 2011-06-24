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
