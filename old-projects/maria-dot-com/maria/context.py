from django.conf import settings

def nav(request):
  """
  nav should be a list of dictionaries like { 'name':str, 'url':str }
  "/" should be added after the for loop since s.startswith("/"[1:]) is always true
  header returns a dict of nav dicts.
  """
  page_name = "home"
  nav = [
    {'name': 'art','url': '/art/', 'left': -3},
    {'name': 'curated','url': '/curated/', 'left': -3},
    {'name': 'about','url': '/about/', 'left': -8},
    {'name': 'blog','url': '/blog/', 'left': 3},
    {'name': 'contact','url': '/contact/', 'left': -7},
    {'name': 'shop','url': '/shop/', 'left': -6},
    ]
  for n in nav:
    n['hover'] = True
    if request.path.startswith(n['url']):
      n['current'] = True
      page_name = n['name']
  return {
    'header_links': { 'nav': nav },
    'page_name': page_name,
    'STATIC_URL': settings.STATIC_URL,
    'nav_wxh': "2000x57",
    }
