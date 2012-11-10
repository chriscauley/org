from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import USStateField
import urllib2, datetime, re
#from lablackey.models import ntbt

ntbt = { "null": True,"blank": True }

class GeoModel(models.Model):
    lat = models.FloatField(**ntbt)
    lon = models.FloatField(**ntbt)
    class Meta:
        abstract = True

class City(GeoModel):
    name = models.CharField(max_length=128)
    state = USStateField()
    def __unicode__(self):
        return "%s, %s"%(self.name,self.state)
    class Meta:
        verbose_name_plural = "Cities"

class LocationModel(GeoModel):
    address = models.CharField(max_length=64,**ntbt)
    address2 = models.CharField(max_length=64,**ntbt)
    city = models.ForeignKey(City)
    zip_code = models.IntegerField()
    class Meta:
        abstract = True

strptime = datetime.datetime.strptime

class Venue(LocationModel):
    name = models.CharField(max_length=128)
    # phone = USPhoneNumberField(**ntbt)
    contact = models.ForeignKey(User,**ntbt)
    default_start_time = models.FloatField(**ntbt)
    image = models.ImageField(upload_to=settings.UPLOAD_DIR+'/show',**ntbt)
    def __unicode__(self):
        return "%s - %s"%(self.name,self.city)
