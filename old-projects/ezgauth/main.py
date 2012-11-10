from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from django.utils.simplejson import dumps as json
from google.appengine.ext import db

key = 'make a secret key!'

class Token(db.Model):
    user = db.UserProperty()
    token = db.StringProperty()

class Login(webapp.RequestHandler):
    def get(self):
        import string,random
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
            return
        seed = string.letters+string.digits
        t = Token()
        t.user = users.get_current_user()
        t.token = ''.join([seed[int(random.random()*len(seed))] for i in range(30)])
        t.put()
        url = self.request.get('url')
        if "?" in url:
            url += "&"
        else:
            url += "?"
        self.redirect(url+"token="+t.token)

class Logout(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect(self.request.get('url'))
        else:
            url = self.request.get('url')
            if "?" in url:
                url += "&"
            else:
                url += "?"
            self.redirect(users.create_logout_url(url+'status=loggedout'))

class CheckToken(webapp.RequestHandler):
    def get(self):
        def e(s,key):
            key = key*(len(s)/len(key)+1)
            return ''.join([chr(ord(s[i])^ord(key[i])) for i in range(len(s))])
        qs = "SELECT * FROM Token WHERE token = '%s'"%self.request.get('token')
        t = db.GqlQuery(qs).get()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(e(t.user.email(),key))
        t.delete()

application = webapp.WSGIApplication(
    [(r'/token',CheckToken),
     (r'/logout',Logout),
     (r'/', Login)],
    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
