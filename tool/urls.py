from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^urlbase64/$', views.urlbase64, name='urlbase64'),
    url(r'^base64-encode$', views.base64_encode, name='base64-encode'),
    url(r'^base64-decode$', views.base64_decode, name='base64-decode'),
)
