import os, sys

SFILE = __file__
SPATH = os.path.normpath(os.path.join(os.path.dirname(SFILE), '..'))

ADMIN_MEDIA_PREFIX = '/static/grappelli/'
MEDIA_ROOT = os.path.join(SPATH, 'media')
STATIC_ROOT = os.path.join(SPATH, 'static')
MEDIA_URL = '/media/'
#STATIC_DOC_ROOT = os.path.join(SPATH,'static')
STATIC_URL = '/static/'
UPLOAD_DIR = 'uploads'
LOGIN_REDIRECT_URL = "/admin/"
LOGIN_URL = "/admin/login"

SITE_NAME = "Houston Counter Crawl"
GRAPPELLI_ADMIN_HEADLINE = 'HCC - Admin'
GRAPPELLI_ADMIN_TITLE = 'HCC Admin'

AJAX_LOOKUP_CHANNELS = {
  'place': ('lablackey.content.ajax_lookup', 'PlaceLookup'),
  'photo': ('lablackey.photo.ajax_lookup', 'PhotoLookup'),
  }

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MAPS_API_KEY = 'ABQIAAAAeppD1h9lB7H61ozR18SeZRS_YqHDtehKcRTrrAGjc25rDMjatxT8nvoX4-jJXcRPaT4I-RdMYv3fJA'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'crawl.db',
  }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  'compressor.finders.CompressorFinder',
  #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
  os.path.join(SPATH, 'templates'),
)

INSTALLED_APPS = (
  'grappelli',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.admin',
  'django.contrib.staticfiles',
  'sorl.thumbnail',
  'ajax_select',
  'south',
  #'devserver',

  # lablackey
  'lablackey.geo',
  'lablackey.photo',
  'lablackey.articles',
  'lablackey.content',
  'lablackey.event',
  'artist',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  "django.contrib.auth.context_processors.auth",
  "django.core.context_processors.request",
  "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.media",
  "django.core.context_processors.request",
  "django.contrib.messages.context_processors.messages",
  'context.process',
)

import re
import socket
# Remove characters that are invalid for python modules.
machine = re.sub('[^A-z0-9._]', '_', socket.gethostname())

try:
  istr = 'settings.local'
  tmp = __import__(istr)
  mod = sys.modules[istr]
except ImportError:
  print "No %r module found for this machine" % istr
else:
  for setting in dir(mod):
    if setting == setting.upper():
      setattr(sys.modules[__name__], setting, getattr(mod, setting))
