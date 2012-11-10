from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from views import MainPage, AddGarrays, AddScore, GetLesson, GetLayout, AddLesson

application = webapp.WSGIApplication([
    ("/", MainPage),
    ("/addgarrays", AddGarrays),
    ("/addscore", AddScore),
    ("/getlesson", GetLesson),
    ("/getlayout", GetLayout),
    ("/addlesson", AddLesson),
     ],debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
