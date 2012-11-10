from django.shortcuts import render_to_response
from django.template import RequestContext
from music.models import Song, Show
import datetime

def player(request):
  today = datetime.date.today()
  shows = Show.objects.random(10,datetime__gte=today,appearance__band__song__isnull=False)
  songs = [s.random_band().random_song() for s in shows]
  values = {
    'shows': shows,
    'songs': songs
    }
  values = RequestContext(request,values)
  return render_to_response("player.html",values)

def playlistJSON(request):
  import random
  songs = Song.objects.random(10)
  return HttpResponse(json.dumps([s.json for s in songs]))
