import urllib2

def deunicode(s):
    try:
        return s.decode("ascii") # no bad characters, yay!
    except UnicodeDecodeError:
        pass # lets hope we got them all
    chars = {r'\xe2\x80\x99':r"\'", # apostrophe
             r'\xe2\x80\x98':r"\'", # single inverted comma
             r'\xe2\x80\x9c':r'\"', # start-quote
             r'\xe2\x80\x9d':r'\"', # end-quote
             r'\xe2\x80\x93':r'-', # long-dash
             r'\xe2\x80\x94':r'-', # short-dash
             r'\xe2\x80\xa2':r'&middot;', # middle dot
             r'\xe2\x80\xa6':r'...', # elipses
             r'\xc2\xae': r'&reg;', # registered (R)
             r'\xe2\x84\xa2': r'&trade;', # TM
             r'\xc3\xa9': r'&eacute;', # accute accented e
             r'\xe2\x82\xac': r'&euro;', # Euro
             r'\xc3\xa0': r'agrave', # grave accented a
             r'\xc3\xb1': r'&ntilde;', #tilde accented n
             }
    s = repr(s)
    for k,v in chars.items():
        s = s.replace(k,v)
    s = eval(s)
    try:
        return s.encode("ascii")
    except UnicodeDecodeError:
        print "sort through the shit, extend chars, try again..."
    for i,line in enumerate(s.split('\n')):
        try:
            line.encode("ascii")
        except UnicodeDecodeError:
            print '\n',i,repr(line)
            print line
    exit() # note, this exits the program, unconditionally

def open_or_download(url,fname,force=False,decode=False):
    try:
        if force: raise IOError
        f = open(fname,'r')
        raw = f.read()
        f.close()
    except IOError:
        print 'downloading %s'%url
        request = urllib2.Request(url)
        request.add_header('User-Agent','Ramalamadingdong')
        raw = urllib2.build_opener().open(request).read()
        if decode:
            raw = deunicode(raw)
            raw = raw.replace('&nbsp;',' ')
        f = open(fname,'w')
        f.write(raw)
        f.close()
    return raw
