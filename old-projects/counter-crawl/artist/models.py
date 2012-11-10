from django.db import models
from lablackey.geo.models import Location
from lablackey.event.models import Event

class Artist(models.Model):
  name = models.CharField(max_length=64)
  __unicode__ = lambda self: self.name

medium_choices = [
  ('music','music'),
  ('visual art','visual art'),
  ('performance','performance'),
  ]

class Performance(models.Model):
  event = models.ForeignKey(Event,null=True,blank=True)
  location = models.ForeignKey(Location,null=True,blank=True)
  medium = models.CharField(max_length=64,choices=medium_choices)
  artist = models.ForeignKey(Artist)
  order = models.IntegerField(default=9999)
  __unicode__ = lambda self: "%s (%s)"%(self.artist,self.event)
  def save(self,*args,**kwargs):
    if self.event and not self.location:
      self.location = self.event.location
    return super(Performance,self).save(*args,**kwargs)
  class Meta:
    ordering = ("order",)
