import os
os.environ["DJANGO_SETTINGS_MODULE"] = 'herefm.settings'
from django.conf import settings
import sys,re,datetime
from django.core.files import File
sys.path.append(settings.SPATH)

from music.models import *

args = sys.argv

band = args[1]
band,new = Band.objects.get_or_create(name="Green Day")

def import_album(path):
    year,name = re.findall(r"\[(\d*)\](.*)",path)[0]
    name=name.replace("_"," ").replace("/","").strip()
    a = Album.objects.get_or_create(name=name,date=datetime.date(int(year),1,1))[0]
    for fname in os.listdir(path):
        if fname.endswith('.ogg'):
            f = open(os.path.join(path,fname))
            name = ' '.join(re.split('[_\W]*',fname[:-4])).strip()
            order = int(name[:2])
            name = name[3:]
            try:
                Song.objects.get(name=name)
            except Song.DoesNotExist:
                s = Song(name=name,
                         order=order,
                         src = File(f))
                s.save()
                print s.id

for album in os.listdir(args[1]):
    import_album(os.path.join(args[1],album))
