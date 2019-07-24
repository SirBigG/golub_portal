from django.conf.urls import url

from . import views

app_name = 'events'

urlpatterns = [
    url(r'^$', views.EventList.as_view(), name='event-list'),
    url(r'^create/$', views.EventFormView.as_view(), name='event-form'),
    url(r'^(?P<slug>[\w-]+).html$', views.EventDetail.as_view(), name='event-detail'),
]
