from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^shopvr-forcequery$', views.shopvr_forcequery, name='shopvr-forcequery'),
    url(r'^run-shopvr-force$', views.run_shopvr_force, name='run-shopvr-force'),
)
