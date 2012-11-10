from django.contrib import admin
from geo.models import City, Venue

class VenueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Venue,VenueAdmin)
admin.site.register(City)
