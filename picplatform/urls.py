from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'picplatform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('index.urls', namespace='index')),
    url(r'^tool/', include('tool.urls', namespace='tool')),
    url(r'^search/', include('search.urls', namespace='search')),
    url(r'^show/', include('show.urls', namespace='show')),
    url(r'^shop/', include('shop.urls', namespace='shop')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
