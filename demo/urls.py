#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('demo.views',
    url(r'^$', 'echo'),
    url(r'^echo$', 'echo', name="demo_echo"),
)
