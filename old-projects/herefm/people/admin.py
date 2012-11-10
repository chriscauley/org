from herefm.people.models import Band, Artist
from music.models import Song
from django.contrib import admin

class SongInline(admin.TabularInline):
  model = Song

class BandAdmin(admin.ModelAdmin):
  inlines = [SongInline]

admin.site.register(Band,BandAdmin)
admin.site.register(Artist)
