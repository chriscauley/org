from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import os

admin.autodiscover()

urlpatterns = patterns(
  'herefm',
  #(r'^login','ezgauth.login'),
  #(r'^logout','ezgauth.logout'),
  (r'^player','views.player'),
  (r'^admin/', include(admin.site.urls)),
  (r'^$','views.player'),
)

if settings.DEBUG:
  urlpatterns += patterns(
    '',
    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': os.path.join(settings.SPATH, 'media'),
         'show_indexes': True}),
    url(r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': os.path.join(settings.SPATH, 'static'),
         'show_indexes': True}),
    )
