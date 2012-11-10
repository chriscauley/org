from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic.simple import direct_to_template
from context import header
import os

admin.autodiscover()

urlpatterns = patterns(
  '',
  (r'^$','views.map'),
  (r'^home$','views.home'),
  (r'^event.json$','views.eventJSON'),
  (r'^grappelli/', include('grappelli.urls')),
  (r'^ajax_select/', include('ajax_select.urls')),
  (r'^admin/', include(admin.site.urls)),
  (r'^map/$','views.map'),
)

if settings.DEBUG:
  urlpatterns += staticfiles_urlpatterns()
  urlpatterns += patterns(
    '',
    url(r'^media/(?P<path>.*)$',
      'django.views.static.serve',
      {'document_root': os.path.join(settings.SPATH, 'media'),
       'show_indexes': True}),
    )
"""    url(r'^static/(?P<path>.*)$',
      'django.views.static.serve',
      {'document_root': os.path.join(settings.SPATH, 'static'),
       'show_indexes': True}),"""
