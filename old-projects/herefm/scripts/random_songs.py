from django.conf import settings
from music.models import Song
from people.models import Band
from django.core.files import File
import random

for b in Band.objects.all():
  if not b.song_set.all():
    for i in range(2):
      s = random.choice(Song.objects.filter(band__isnull=True).filter(dummy=True))
      s = Song(
        name=s.name,
        src=str(s.src),
        band=b)
      s.save()
    print "2 songs created for %s"%b
