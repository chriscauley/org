from django.contrib import admin
from spider.models import Site

class SiteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Site,SiteAdmin)
