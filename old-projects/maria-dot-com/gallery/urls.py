from django.conf.urls import patterns, include, url
from django.conf import settings
_urls = lambda *ns: [url(r'^%s/'%n, include('%s.urls'%n, namespace=n, app_name=n)) for n in ns]
s='([\w\d\-\_]+)'
urlpatterns = patterns(
  'gallery.views',
  url('^%s/$'%s,'index'),
  url('^%s/%s/$'%(s,s),'detail',name='detail'),
)
