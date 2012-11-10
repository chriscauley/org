from django.contrib import admin
from django.contrib.admin import helpers
from django.contrib.admin.util import unquote
from django.core.exceptions import PermissionDenied, ValidationError
from django.db import transaction
from django.forms.formsets import all_valid
from django.forms.forms import NON_FIELD_ERRORS
from django.http import Http404
from django.utils.html import escape
from django.utils.decorators import method_decorator
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_protect

from photo.admin_mixins import (
    PhotoForeignKeyForm, RequiredPhotoForeignKeyForm)
from asset.models import DigitalAsset, SlideshowPhoto #, Slideshow, Slide


csrf_protect_m = method_decorator(csrf_protect)


def is_vimeo_html(value):
    return value.startswith('<iframe src="http://player.vimeo.com/video/')

class CarouselSlideshowInlineAdminForm(RequiredPhotoForeignKeyForm):
    is_image_required = True
    class Meta:
        model = DigitalAsset


class CarouselSlideshowInlineAdmin(admin.TabularInline):
    form = CarouselSlideshowInlineAdminForm
    model = SlideshowPhoto
    fk_name = 'asset'
    extra = 1


class DigitalAssetAdminForm(PhotoForeignKeyForm):

    class Meta:
        model = DigitalAsset

    """def clean_embedded_video_url(self):
        value = self.cleaned_data.get('embedded_video_url')
        value = value.strip()
        if value and not is_vimeo_url(value):
            raise ValidationError("This is not a valid vimeo embedded video.")
        return value"""


class DigitalAssetAdmin(admin.ModelAdmin):
    class Media:
        js = ['ckeditor/ckeditor.js']

    form = DigitalAssetAdminForm
    list_display = ('order', 'kicker')
    list_display_links = ['kicker']
    list_editable = ['order']
    search_fields = ('kicker', 'description')
    fields = (
        'order', 'kicker', 'description', 'video_url', 'url', 'image')
    inlines = [ CarouselSlideshowInlineAdmin, ]
"""
class SlideInlineAdminForm(RequiredPhotoForeignKeyForm):
    is_image_required = True
    class Meta:
        model = DigitalAsset

class SlideInlineAdmin(admin.TabularInline):
    form = SlideInlineAdminForm
    model = Slide
    fk_name = 'slideshow'
    extra = 1


class SlideshowAdmin(admin.ModelAdmin):

    list_display = ['identifier']
    fields = ['identifier']

    inlines = [
        SlideInlineAdmin,
        ]
"""
admin.site.register(DigitalAsset, DigitalAssetAdmin)
