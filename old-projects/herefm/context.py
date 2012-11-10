from django.conf import settings
def process(request):
  return {
    "JP_URL": settings.STATIC_URL + "js/jPlayer/",
    "STATIC_URL": settings.STATIC_URL,
    }
