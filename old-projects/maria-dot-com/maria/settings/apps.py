THUMBNAIL_FORMAT = "PNG"
THUMBNAIL_DEBUG = True
INSTALLED_APPS = (
  'main', #abstract classes only
  'grappelli',
  'devserver',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'south',
  'sorl.thumbnail',
  'lablackey.photo',
  'lablackey.content',
  'lablackey.db',
  'gallery',
  'crop_override',
)
