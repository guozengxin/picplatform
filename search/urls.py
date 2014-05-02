from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^blacklist/$', views.blacklist, name='blacklist'),
    url(r'^bl-search$', views.bl_search, name='bl-search'),
)
