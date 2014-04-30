from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^blacklist/$', views.blacklist, name='blacklist'),
)
