from django.contrib import admin
from .models import Artist, Performance
from lablackey.event.models import Event
from lablackey.event.admin import EventAdmin

class ArtistAdmin(admin.ModelAdmin):
  pass

class PerformanceAdmin(admin.ModelAdmin):
  pass

admin.site.register(Artist,ArtistAdmin)
admin.site.register(Performance,PerformanceAdmin)

class PerformanceInline(admin.TabularInline):
  model = Performance
  fields = ('artist','medium','order')

class EventAdmin(EventAdmin):
  inlines = [PerformanceInline]

admin.site.unregister(Event)
admin.site.register(Event,EventAdmin)
