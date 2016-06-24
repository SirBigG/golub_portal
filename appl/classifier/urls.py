from __future__ import unicode_literals

from django.conf.urls import url

from appl.classifier.views import LocationAutocomplete, LocationListView


urlpatterns = [
    url(r'^location-autocomplete/$', LocationAutocomplete.as_view(),
        name='location-autocomplete'),
    url(r'api/locations/$', LocationListView.as_view(), name='location-list'),
]
