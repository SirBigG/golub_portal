from __future__ import unicode_literals

from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from api.v1.classifiers.views import LocationListView, CategoryListView


urlpatterns = format_suffix_patterns([
    url(r'locations/$', LocationListView.as_view(), name='location-list'),
    url(r'categories/$', CategoryListView.as_view(), name='category-list'),
])