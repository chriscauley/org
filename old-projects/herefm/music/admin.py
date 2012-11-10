from herefm.music.models import Song, Album, Show, TicketPrice, Appearance
from django.contrib import admin

class BaseModelAdmin(admin.ModelAdmin):
  exclude = ('author',)
  readonly_fields = ('entered','modified')
  def save_model(self,request,obj,form,change):
    if not obj.id:
      obj.author = request.user
    obj.save()

class AppearanceInline(admin.TabularInline):
  model = Appearance

class TicketPriceInline(admin.TabularInline):
  model = TicketPrice

class ShowAdmin(admin.ModelAdmin):
  field_sets = ((None,{'fields':('venue','review','datetime','tba','image')}),)
  list_display = ('__str__',"image")
  def _thumbnail(self,obj):
    return """<img src="%s" width="100" />"""%("/media/"+str(obj.src()))
  _thumbnail.allow_tags = True
  inlines = [AppearanceInline, TicketPriceInline]

class SongAdmin(admin.ModelAdmin):
  list_display = ["__str__","band"]
  list_editable = ['band']

admin.site.register(Album)
admin.site.register(Song,SongAdmin)
admin.site.register(Show,ShowAdmin)
admin.site.register(TicketPrice)

