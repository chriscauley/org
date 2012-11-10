from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

_urls = lambda *ns: [url(r'^%s/'%n, include('%s.urls'%n, namespace=n, app_name=n)) for n in ns]
# neat function for splatting apps where url==app_name==namespace

urlpatterns = patterns(
  '',
  (r'^grappelli/', include('grappelli.urls')),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^$', 'maria.views.home',name='home'),
  url(r'^about/$', 'maria.views.about',name='about'),
  url(r'^(art|curated)/$','gallery.views.index'),
  *_urls('gallery')
)

favicon = '%sfavicon.ico'%settings.STATIC_URL
if settings.DEBUG:
  favicon = '%smwm.ico'%settings.STATIC_URL
  urlpatterns += patterns(
    '',
    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT,
         'show_indexes': True}),
    )

urlpatterns += patterns(
  'django.views.generic.simple',
  (r'^favicon.ico$', 'redirect_to',{'url': favicon}),
)
