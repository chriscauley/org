from django.template.response import TemplateResponse
from .models import Gallery, GallerySection

def index(request,slug):
  gallery = Gallery.objects.get(slug=slug)
  values = {
    'gallery': gallery,
    }
  return TemplateResponse(request,'gallery/index.html',values)

def detail(request,gallery_slug,section_slug):
  section = GallerySection.objects.get(slug=section_slug,gallery__slug=gallery_slug)
  values = {
    'gallery': section.gallery,
    'section': section,
    }
  return TemplateResponse(request,'gallery/index.html',values)
