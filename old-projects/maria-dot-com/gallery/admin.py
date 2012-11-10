from django.contrib import admin
from .models import Gallery, GallerySection, GalleryItem
from lablackey.db.admin import SlugModelAdmin,OrderedModelAdmin,OrderedModelInline,SlugModelInline

class GallerySectionInline(OrderedModelInline,SlugModelInline):
  model = GallerySection

class GalleryAdmin(SlugModelAdmin,OrderedModelAdmin):
  inlines = [GallerySectionInline]

class GalleryItemInline(OrderedModelInline,SlugModelInline):
  model = GalleryItem

class GallerySectionAdmin(OrderedModelAdmin,SlugModelAdmin):
  inlines = [GalleryItemInline]

class GalleryItemAdmin(OrderedModelAdmin,SlugModelAdmin):
  pass

admin.site.register(Gallery,GalleryAdmin)
admin.site.register(GallerySection,GallerySectionAdmin)
admin.site.register(GalleryItem,GalleryItemAdmin)
