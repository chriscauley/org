from django.db import models
from django.contrib.auth.models import User
import random

class Band(models.Model):
    name = models.CharField(max_length=64)
    #hometown = models.
    def random_song(self):
        return random.choice(self.song_set.all())
    def __unicode__(self):
        return self.name
    
class Artist(models.Model):
    stagename = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    user = models.ForeignKey(User,null=True,blank=True)
    #instrument
    acts = models.ManyToManyField(Band)
