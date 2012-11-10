from django.conf import settings
import requests, urllib2, os, datetime, re
from pyquery import PyQuery as pq
from people.models import Band
from music.models import Show, Appearance
from geo.models import Venue

def curl(url,allow_error=True):
  try:
    resp = urllib2.urlopen(url)
    contents = resp.read()
  except urllib2.HTTPError, error:
    if allow_error:
      contents = error.read()
      return contents
  print "error at : %s"%url

def cached_download(url,fname,force=False,allow_error=True):
  fname = os.path.join(os.path.dirname(__file__),fname)
  try:
    f = open(fname,'r')
  except IOError:
    force = True
  if not force:
    f = open(fname,'r')
    content = f.read()
    f.close()
    return content
  content = curl(url,allow_error=allow_error)
  if content is not None:
    f = open(fname,'w')
    f.write(content)
    f.close()
    print fname + " saved!"
    return content

def cached_img(url,fname,force=False):
  r = requests.get(url)
  if r.status_code >= 400:
    print "error @ %s: \n    %s"%(url,r.status_code)
    return False
  try:
    f = open(fname,'r')
  except IOError:
    force = True
  if not force:
    f = open(fname,'r')
    content = f.read()
    f.close()
    return fname
  content = r.content
  f = open(fname,'w')
  f.write(content)
  f.close()
  print fname + " saved!"
  return fname

main_html = cached_download('http://www.fitzlivemusic.com/shows.php','cache/fitz_shows.html')
shows = pq(main_html)
dates = shows(".stubwire_eventbox_eventdate")
names = shows(".stubwire_eventbox_eventname")
for i in range(len(names)):
  if not names.eq(i).children("a"):
    continue
  href = names.eq(i).children("a").attr("href")
  date = dates.eq(i)
  m, d, y = date.find(".month").text(), date.find(".day").text(), 2012
  t = date.find(".showtime").text()
  defaults = {
    "venue": Venue.objects.get(name="Fitzgerald's"),
    "name": names.eq(i).text(),
    "datetime": datetime.datetime.strptime("%s %s %s %s"%(m,d,y,t),"%b %d %Y %I:%M%p")
    }
  show,new = Show.objects.get_or_create(ticket_url=href,defaults=defaults)
  if new: print "Show created: %s"%show
  text = cached_download(href,"cache/"+href.replace("/","")[-5:])
  img = re.findall(r'<img src=\"([^\"]+files/events/[^\"]+)\"',text)
  if len(img):
    path = os.path.join(settings.MEDIA_ROOT,'uploads/shows/show_%s.png'%show.id)
    img = cached_img(img[0].replace("small","original"),path)
    show.image = None
    if img:
      show.image = path.split("media/")[1]
    show.save()
  else:
    pass #print "No image for show: %s"%href
  text = text.replace("Local:","Headliner:").replace("&nbsp;","")
  text = text.split("Headliner:")
  if len(text) != 2: # usually a non-stubwire url
    #print "parse failed " + href
    continue
  text = text[1].split("</td>")[0]
  headliners,openers = (text.split("Opener:")+[""])[:2]
  _get_bands = lambda s: [t.strip() for t in re.findall("\t([^\t]+)<br",s)]
  order = 0
  for name in _get_bands(headliners):
    if len(name)>64: print name # some shows have all bands on one line
    b, new = Band.objects.get_or_create(name=name[:64])
    if new: print "Band created: " + name
    order += 1
    defaults = {"headlining":True, "order":order}
    a,new = Appearance.objects.get_or_create(band=b,show=show,defaults=defaults)
  for name in _get_bands(openers):
    if len(name)>64: print name # some shows have all bands on one line
    b, new = Band.objects.get_or_create(name=name[:64])
    if new: print "Band created: " + name
    order += 1
    defaults = {"headlining": False, "order":order}
    a,new = Appearance.objects.get_or_create(band=b,show=show,defaults=defaults)
