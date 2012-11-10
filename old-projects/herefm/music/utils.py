from herefm.music.models import Song, Album
from herefm.people.models import Band
import os, re

def from_folder(path):
    band_name = path.split('/')[-1].replace('_',' ')
    band = Band.objects.get_or_create(name=band_name)[0]
    walk = os.walk(path)
    pwd = os.getcwd()
    for w in walk:
        song_names = [s for w in w[1] if '.ogg' in s]
        if song_names:
            os.chdir(os.path.join(pwd,w[0]))
            album = w[0].split('/')[-1]
            year = re.findall(r'\[(\d{4})\] ?_?(.*?)',album)
            if year:
                year,album = year[0][0],year[0][1].replace('_',' ').strip()
            else:
                year = None
            album = Album.objects.get_or_create(year=year,
                                                name=album,
                                                band=band,
                                                path=os.getcwd())[0]
            for s in sorted(song_names):
                s = Song(name=s.replace('_',' ')[:-4],album=album)
                s.filename = s
                s.save()
                
                
                
