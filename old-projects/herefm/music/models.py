from django.db import models
from django.conf import settings
from herefm.people.models import Band,Artist
from geo.models import Venue
import random,simplejson

ntbt = {'null':True, 'blank':True}

class Album(models.Model):
  name = models.CharField(max_length=50)
  band = models.ForeignKey(Band, null=True,blank=True)
  date = models.DateTimeField()
  kinds = [('album','Album'),('single','Single'),('ep','EP'),('live','Live')]
  kind = models.CharField(max_length=10,choices=kinds,default=kinds[0][0])
  path = models.CharField(max_length=127,null=True,blank=True)
  #location = models.ForeignKey(Venue,null=True,blank=True)
  def __unicode__(self):
    return "[%s] %s"%(self.date.year,self.name)
  class Meta:
    ordering = ('date',)

class RandomManager(models.Manager):
  def random(self,n,*args,**kwargs):
    qs = self.filter(*args,**kwargs)
    try:
      return [qs[i] for i in random.sample(range(qs.count()),n)]
    except ValueError:
      qs = list(qs)
      random.shuffle(qs)
      return qs

class Song(models.Model):
  name = models.CharField(max_length=50)
  album = models.ForeignKey(Album,null=True,blank=True)
  order = models.IntegerField(null=True,blank=True)
  band = models.ForeignKey(Band,null=True,blank=True)
  src = models.FileField(".ogg File",max_length=200,
               upload_to=settings.UPLOAD_DIR + '/songs/%Y-%m')
  dummy = models.BooleanField(default=False)

  objects = RandomManager()

  @property
  def json(self):
    return { "name": "%s -- %s"%(self.name,self.band),
         "oga": self.src.url,
         }
  @property
  def dumps(self):
    return simplejson.dumps(self.json)
  def __unicode__(self):
    return self.name
  #def serialize(self):

class GuestAppearance(models.Model):
  artist = models.ForeignKey(Artist)
  song = models.ForeignKey(Song)
  
class Show(models.Model):
  name = models.CharField(max_length=256)
  venue = models.ForeignKey(Venue)
  description = models.TextField(max_length=2048,**ntbt)
  image = models.ImageField(upload_to=settings.UPLOAD_DIR+'/shows',**ntbt)
  datetime = models.DateTimeField(**ntbt)
  locked = models.BooleanField(default=False)
  ticket_url = models.URLField(verify_exists=False,**ntbt)
  tba = models.BooleanField(default=False)
  objects = RandomManager()

  src = lambda self: self.image or self.venue.image

  get_headliners = lambda self: [a.band for a in self.appearance_set.filter(headlining=True)]
  get_openers = lambda self: [a.band for a in self.appearance_set.filter(headlining=False)]
  def get_bands(self):
    return [a.band for a in self.appearance_set.all()]
  def random_band(self):
    return random.choice(self.get_bands())
  def json(self):
    return {
      "name": self.name,
      "venue": self.venue,
      "img": self.src.url,
      "datetime": self.datetime.strftime("%m.d.Y"),
      "ticet_url": self.ticket_url,
      }
  dumps = lambda self: simplejson.dumps(self.json)
  __unicode__ = lambda self: "%s -- %s"%(self.venue,self.datetime)

class Appearance(models.Model):
  show = models.ForeignKey(Show)
  band = models.ForeignKey(Band)
  order = models.IntegerField(default=99)
  headlining = models.BooleanField(default=False)
  __unicode__ = lambda self: "%s @ %s"%(self.band,self.show)
  class Meta:
    ordering = ("order",)

class TicketPrice(models.Model):
  show = models.ForeignKey(Show)
  price = models.FloatField()
  description = models.CharField(max_length=32)
  __unicode__ = lambda self: "%s: $%.2f @ %s"%(self.description,self.price,self.show)
