from django.db import models
from lablackey.photo.models import PhotoModel, Photo
from lablackey.db.models import SlugModel, OrderedModel
from sorl.thumbnail import ImageField

class Gallery(SlugModel,OrderedModel):
  src = ImageField(upload_to='uploads/photos/%Y-%m',max_length=300)
  class Meta:
    verbose_name_plural = "Galleries"

class GallerySection(SlugModel,OrderedModel):
  gallery = models.ForeignKey(Gallery)
  src = models.ForeignKey(Photo)
  hover = models.ForeignKey(Photo,related_name="+")
  left = models.IntegerField(default=0)
  top = models.IntegerField(default=0)
  class Meta:
    ordering = ("order",)

class GalleryItem(SlugModel,PhotoModel):
  section = models.ForeignKey(GallerySection)
