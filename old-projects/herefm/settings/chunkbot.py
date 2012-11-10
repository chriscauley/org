import os, sys

SFILE = __file__
SPATH = os.path.normpath(os.path.join(os.path.dirname(SFILE), '..'))

MEDIA_URL = 'http://media.herefm.com:8000/media/'
STATIC_ROOT_DOC = os.path.join(SPATH,'static')
STATIC_URL = 'http://static.herefm.com:8000/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL+'admin/'
