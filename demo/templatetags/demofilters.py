#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template import Library
register = Library()

@register.filter
def getitem(_list, idx):
    if len(_list) > idx:
        return _list.__getitem__(idx)
    else:
        return ''

@register.filter
def range(length):
    return xrange(length)
