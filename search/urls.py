from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^blacklist/$', views.blacklist, name='blacklist'),
    url(r'^bl-search$', views.bl_search, name='bl-search'),
    url(r'^docid2url/$', views.docid2url, name='docid2url'),
    url(r'^docid-trans$', views.docid_trans, name='docid-trans'),
    url(r'^umis-force/$', views.umis_force, name='umis-force'),
    url(r'^send2query$', views.send2query, name='send2query'),
)
