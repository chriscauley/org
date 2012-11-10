from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.views.generic import TemplateView
from django.conf import settings
from collections import defaultdict

from lablackey.event.models import Schedule, Event
from lablackey.articles.models import Article

import os,datetime,urllib2,simplejson

def home(request):
  values = { 'feed_items': Article.objects.all(),
             'current': 'home',}
  values = RequestContext(request,values)
  return TemplateResponse(request,"home.html",values)

def eventJSON(request):
  event = Event.objects.filter(id=request.GET['pk']).select_related('performance')[0]
  performances = defaultdict(list)
  for p in event.performance_set.all():
    performances[p.medium].append(p)
  performances = sorted(performances.items())
  values = {
    'event': event,
    'performances': performances,
    }
  return TemplateResponse(request,"_event.html",values)

def map(request):
  return TemplateResponse(request,"map.html",{})
