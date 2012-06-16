import urllib2

def download(url,name):
    s = urllib2.urlopen(url)
    text = s.read()
    s.close()
    f = open(name,"w")
    f.write(text)
    f.close()

def open_file(name):
    f = open(name,"r")
    text = f.read()
    f.close()
    return text
