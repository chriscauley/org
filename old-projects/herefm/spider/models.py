from django.db import models
from geo.models import Venue
import urllib2, datetime, re
from pyquery import PyQuery as pq
#from lablackey.models import ntbt

ntbt = { "null": True,"blank": True }
strptime = datetime.datetime.strptime

def curl(url):
    sock = urllib2.urlopen(self.spiderurl)
    html = sock.read()
    sock.close()
    return html

class Site(models.Model):
    name = models.CharField(max_length=128)
    venue = models.ForeignKey(Venue)
    url = models.URLField(verify_exists=False)
    url_selector = models.CharField(max_length=128,**ntbt)
    default_start_time = models.FloatField(**ntbt)
    ticket_selector = models.CharField(max_length=128,**ntbt)
    spiderurl = models.URLField(verify_exists = False,**ntbt)
    date_selector = models.CharField(max_length=128,**ntbt)
    date_strptime = models.CharField(max_length=32,**ntbt)
    date_regexp = models.CharField(max_length=32,**ntbt)
    band_selector = models.CharField(max_length=128,**ntbt)
    band_splitters = models.CharField(max_length=128,help_text = "i.e. \",|w/\"",**ntbt)
    def spider(self):
        urls = [self.url]
        if self.url_selector:
            P = pq(curl(self.url))
            urls = [pq(a).attr("href") for a in P.find(self.url_selector)]
        for url in urls:
            self.eat_url(url)
    def eat_url(self,url):
        P = curl(url)
        dt = datetime.timedelta(self.default_start_time/24.)
        dates = [strptime(d.text.strip()[-10:],self.date_strptime)+dt for d in P.find(self.date_selector)]
        bands = [b.text.strip() for b in P.find(self.band_selector)]
        m = 'splittasplittasplitta'
        bands = [re.findall("([\w\' ]*?)(?=%s)"%(self.band_splitters+"|"+m),b+m) for b in bands]
        tickets = [pq(a).attr("href") for a in P.find(self.ticket_selector)]
        for d,bs,t in zip(dates,bands,tickets):
            s,new = Show.objects.get_or_create(venue=self.venue,datetime=d,ticket_url=t)
            if s.locked:
                continue
            if new:
                print s," created"
            for _b in bs:
                b = _b.strip().title()
                if not b:
                    continue
                if b.lower()=="tba":
                    s.tba = True
                    continue
                band,new = Band.objects.get_or_create(name=b)
                if new:
                    print band," created"
                s.bands.add(band)
                s.save()
    def eat_url(url):
        from music.models import Show
        from people.models import Band

    def __unicode__(self):
        return self.name
