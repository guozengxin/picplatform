from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^urlbase64/$', views.urlbase64, name='urlbase64'),
    url(r'^base64-encode$', views.base64_encode, name='base64-encode'),
    url(r'^base64-decode$', views.base64_decode, name='base64-decode'),
    url(r'^vr-forcequery$', views.vr_forcequery, name='vr-forcequery'),
    url(r'^run-force$', views.run_force, name='run-force'),
    url(r'^groupnews$', views.groupnews, name='groupnews'),
)
