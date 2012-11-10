domain = 'http://demo.lablackey.com'    #your domain here!
auth_url = 'http://ezgauth.appspot.com'   #your appspot instance here!
key = 'make a secret key!'

def e(s,key):
    key = key*(len(s)/len(key)+1)
    return ''.join([chr(ord(s[i])^ord(key[i])) for i in range(len(s))])

def check_login(f):
    def wrap(request,*args,**kwargs):
        if not request.user.is_authenticated():
            from django.contrib.auth.models import User
            from django.http import HttpResponseRedirect
            if 'token' in request.GET:
                import urllib2
                from simplejson import loads
                from django.contrib.auth import login
                sock = urllib2.urlopen('%s/token?token=%s'%(auth_url,request.GET['token']))
                email = e(sock.read(),key)
                sock.close()
                u = User.objects.filter(email=email)
                if u:
                    u = u[0]
                else:
                    u = User(email=email,username=email)
                    u.save()
                u.backend='django.contrib.auth.backends.ModelBackend'
                login(request,u)
            else:
                from django.http import HttpResponseRedirect
                return HttpResponseRedirect('%s/?url=%s'%(auth_url,domain+request.path))
        return f(request,*args,**kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap

@check_login
def login(request):
    if not 'next' in request.GET:
        next = '/'
    return HttpResponseRedirect(next)

def logout(request):
    from django.contrib.auth import logout
    from django.http import HttpResponseRedirect
    logout(request)
    #logout of google, redirect to '/'
    return HttpResponseRedirect(auth_url+'/logout?url=%s'%domain)
