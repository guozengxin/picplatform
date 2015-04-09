from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^shopvr-forcequery$', views.shopvr_forcequery, name='shopvr-forcequery'),
    url(r'^run-shopvr-force$', views.run_shopvr_force, name='run-shopvr-force'),
    url(r'^$', views.index, name='index'),
    url(r'^cache$', views.cache, name='cache'),
    url(r'^cachepost$', views.cachepost, name='cachepost'),
    url(r'^query$', views.query, name='query'),
    url(r'^querypost$', views.querypost, name='querypost'),
)
