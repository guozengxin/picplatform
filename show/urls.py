from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^task-monitor/$', views.task_monitor, name='task-monitor'),
    url(r'^get-result$', views.get_result, name='get-result'),
)
