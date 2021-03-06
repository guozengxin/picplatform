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
    url(r'^searchhub$', views.searchhub, name='searchhub'),
    url(r'^searchhubpost$', views.searchhubpost, name='searchhubpost'),
    url(r'^sqo$', views.sqo, name='sqo'),
    url(r'^sqopost$', views.sqopost, name='sqopost'),
    url(r'^productinfo$', views.productinfo, name='productinfo'),
    url(r'^productinfopost$', views.productinfopost, name='productinfopost'),
)
