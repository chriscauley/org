import os, sys

SFILE = __file__
SPATH = os.path.normpath(os.path.join(os.path.dirname(SFILE), '..'))
p = '/usr/lib/python2.6/dist-packages/'
if not p in sys.path:
  sys.path.append(p)

TEMPLATE_DIRS = (os.path.join(SPATH,'templates'),)
MEDIA_ROOT = os.path.join(SPATH,'media')
UPLOAD_DIR = 'uploads'

MEDIA_URL = '/media/'
STATIC_ROOT_DOC = os.path.join(SPATH,'static')
STATIC_URL = '/static/'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (('Chris Cauley','chris@lablackey.com'),)
MANAGERS = ADMINS

DATABASES = {
  'default': {
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    'NAME': 'herefm',
    'USER': 'postgres',
    'PASSWORD': 'postgres',
    'HOST': '',
    'PORT': '',
  }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

GOOGLE_API_KEY = "herefm.com"
GOOGLE_API_SECRET = "8fou19ohD2QLWy3+ORXt08uR"
SECRET_KEY = '@qk!66f22_9_#5u#z+qvh6(6t)4ebg*mv(b=2ul#=j9-)(zdwp'

TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  "django.contrib.auth.context_processors.auth",
  "django.core.context_processors.request",
  "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.media",
  "django.core.context_processors.request",
  "django.contrib.messages.context_processors.messages",
  "context.process",
)

MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'herefm.urls'

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.staticfiles',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.admin',
  'herefm.people',
  'south',
  'geo',
  'herefm.music',
  'sorl.thumbnail',
  'tagging',
  'voting',
  #'spider',
)

# App specific settings
#### django-tagging
FORCE_LOWERCASE_TAGS = True
MAX_TAG_LENGTH = 50 # same as default

import re
import socket
# Remove characters that are invalid for python modules.
machine = re.sub('[^A-z0-9._]', '_', socket.gethostname())

try:
  istr = 'settings.' + machine
  tmp = __import__(istr)
  mod = sys.modules[istr]
except ImportError:
  print "No %r module found for this machine" % istr
else:
  for setting in dir(mod):
    if setting == setting.upper():
      setattr(sys.modules[__name__], setting, getattr(mod, setting))
