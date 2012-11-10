from django.db import models
from content.models import Page
from photo.models import Photo
import re,urlparse

def validate_video_url(url):
    from django.forms import ValidationError
    if url:
        up = urlparse.urlparse(url)
        if 'youtube.com' in up.hostname:
            params = urlparse.parse_qs(up.query)
            return params['v'][0]
        elif 'vimeo.com' in up.hostname:
            return re.search(r'(\d*)$', url).groups()[0]
        else:
            raise ValidationError("URL must link to a YouTube or Vimeo video.")
        return url
    return None

_url_help = 'Local urls must start with "/", external urls must start with "http://".'

class DigitalAsset(models.Model):
    class Meta:
        ordering = ['order']
        verbose_name = 'Carousel Frame'
        verbose_name_plural = 'Carousel'

    page = models.ForeignKey(Page,default=1)
    order = models.PositiveIntegerField()
    kicker = models.CharField(max_length =256)
    description = models.TextField()
    video_url = models.URLField("Video URL",null=True,blank=True,
                                validators=[validate_video_url],verify_exists=False)
    url = models.CharField(max_length=200,null=True,blank=True,help_text=_url_help)
    image = models.ForeignKey(Photo, blank =True, null =True)
    logo = models.ForeignKey(Photo, blank =True, null =True,related_name="+")
    slideshow_photos = models.ManyToManyField(Photo,through ='asset.SlideshowPhoto',
                                              related_name ='slideshow_asset')
    @property
    def key(self):
      up = urlparse.urlparse(self.video_url)
      if 'youtube.com' in up.hostname:
        params = urlparse.parse_qs(up.query)
        return params['v'][0]

      elif 'vimeo.com' in up.hostname:
          return re.search(r'(\d*)$', self.video_url).groups()[0]

    def embed_video(self,width=900,height=495,play=False):
        autoplay = ''
        if play:
            autoplay = '&autoplay=1'
        if not self.video_url:
            return ''
        if 'vimeo.com' in self.video_url:
            s = '<iframe src="http://player.vimeo.com/video/%(key)s?title=0&amp;byline=0&amp;portrait=0%(autoplay)s" width="%(width)s" height="%(height)s" frameborder="0"></iframe>'
        if 'youtube.com' in self.video_url:
            s = '<iframe width="%(width)s" height="%(height)s" src="http://www.youtube.com/embed/%(key)s?controls=0&wmode=opaque%(autoplay)s" frameborder="0" allowfullscreen></iframe>'
        return s%{'key':self.key,'width':width,'height':height,'autoplay':autoplay}
    def play_video(self,**kwargs):
        return self.embed_video(play=True,**kwargs)
    @property
    def content_html(self):
        if self.image is not None:
            return self.image.carousel_img
        return self.embed_video

class SlideshowPhoto(models.Model):
    class Meta:
        ordering = ['order']
    order = models.PositiveIntegerField()
    asset = models.ForeignKey(DigitalAsset)
    image = models.ForeignKey(Photo)
