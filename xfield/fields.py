#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms.util import ValidationError
from xfield.widgets import ExpandableWidget 
import logging

def ExpandableField(base_field, min_values=0, max_values=None, **kwargs):
    class _ExpandableField(base_field):
        def __init__(self, **kwargs):
            self.min_values = min_values
            self.max_values = max_values  # WARNING: max_values is not implemented

            if not 'widget' in kwargs:
                widget = ExpandableWidget(base_field.widget, min_values, max_values)
            else:
                widget = kwargs.pop('widget')
                # check the type of the widget. we can't do isinstance() or issubclass() without some magic because
                # expandable field is an instance of a dynamic class
                widget_type = type(widget)
                if widget_type.__name__ != '_ExpandableWidget':
                    raise AttributeError("'%s' is not an instance of ExpandableWidget" % widget_type.__name__)

                if callable(widget):
                    widget = widget()

            if 'initial' in kwargs:
                initial = kwargs['initial']
                if not hasattr(initial, '__iter__'):
                    raise AttributeError("ExpandableField accepts only iterable initial data.")

            super(_ExpandableField, self).__init__(widget=widget, **kwargs)

        def clean(self, values, initial=None):
            values = values is None and [u""] or list(values)
            has_error = False
            errors = ['' for i in range(len(values))]
            for i, v in enumerate(values):
                # if no value provided for this expandable field, check if user has satisfied the number of minimum
                # values
                if v:
                    try:
                        # If ExpandableField wraps around a FileField, the field's clean() method must be passed a second
                        # argument; @see django/forms/forms.py, line 282
                        if isinstance(base_field, forms.FileField):
                            values[i] = super(_ExpandableField, self).clean(v, initial)
                        else:
                            values[i] = super(_ExpandableField, self).clean(v)
                    except ValidationError, e:
                        errors[i] = e.messages[0]  # we are only interested in the first error message
                        has_error = True
                    except Exception, e:
                        logging.error(e)
                else:
                    if i >= self.min_values:  # min_values is 1-based, i is 0-based
                        # so we got the number of required values, continue
                        values[i] = v
                    else:
                        try:
                            errors[i] = self.default_error_messages['required']
                        except KeyError:
                            errors[i] = self.default_error_messages['invalid']
                        has_error = True

            if has_error:
                raise ValidationError(errors)
            else:
                return values
    return _ExpandableField(**kwargs)
