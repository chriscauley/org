from lablackey.event.models import Schedule
from django.conf import settings
header = ['blog','map'] #'calendar','about','contact','rss']

def process(request):
  nav = {
    'header': header,
    'current': request.path.split('/')[1] or 'map',
    }

  return {
    'nav': nav,
    'schedules': Schedule.objects.all(),
    'STATIC_URL': settings.STATIC_URL,
    }
