import os

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from models import *
from nodes import keyboard, courseTabs
from garrays import *

class MainPage(webapp.RequestHandler):
    def get(self):
        qU = gUser(self)
        mode = 'colemak'; garray=[]
        garray = [
            'welcome start by typing this line here ',
            'you can log in by clicking users above ',
            'you can also change your keyboard layout ',
            'i recomend colemak but many prefer dvorak ',
            'stats are shown below and saved if you log in ',
            'there are lessons poems and even songs ',
            'this is the last line of the tutorial how did you do ']
        lesson = 'tutorial'

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            urltext = 'Logout '+str(qU.name)
        else:
            url = users.create_login_url(self.request.uri)
            urltext = 'Login'

        tabs = courseTabs(qU)
        board = keyboard("colemak")

        template_values = {
            "tabs": tabs,
            "garray": garray,
            "lesson": lesson,
            "board": board,
            "url": url,
            "urltext": urltext
            }
        path = os.path.join(os.path.dirname(__file__),'templates/type.html')
        self.response.out.write(template.render(path, template_values))

class GetLesson(webapp.RequestHandler):
    def get(self):
        name = self.request.get("name")
        lesson = Lesson.gql("WHERE name = :1", name).get()
        text = lesson.text; text2=''
        for i in range(len(text)):
            text2+=text[i]+'||'
        text2=text2[0:-2]
        self.response.out.write(text2+'|||'+name)

class GetLayout(webapp.RequestHandler):
    def get(self):
        name = str(self.request.get("name"))
        board = keyboard(name)
        board = [board[0]+'&nbsp;&nbsp;'+board[1],
                 board[2]+'&nbsp;&nbsp;'+board[3],
                 board[4]+'&nbsp;&nbsp;'+board[5]]
        self.response.out.write(board)

class AddGarrays(webapp.RequestHandler):
    def get(self):
        qCs = Course.all() #work around double add
        for course in lessonSet:
            qC = Course(name = course)
            qC.put()
            for lesson in lessonSet[course]:
                qL = Lesson(course = qC)
                qL.name = lesson["name"]
                qL.text = lesson["text"]
                qL.number = lesson["number"]
                qL.put()
        self.redirect('/')

class AddLesson(webapp.RequestHandler):
    def get(self):
        qCs = Course.all().fetch(1000)
        clist=[]
        for qC in qCs:
            clist.append(qC.name)
        template_values = {"clist": clist}
        path = os.path.join(os.path.dirname(__file__), 'templates/addlesson.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        qU = gUser(self)
        course = self.request.get("course")
        lname = self.request.get("name")
        if course == "new":
            qC = Course(name=lname)
            try: qC.user=qU
            except: pass
            qC.put()
        else:
            qC = Course.gql("WHERE name = :1", course).get()
            num = self.request.get("number")
            if num == '':
                qLs = Lesson.gql("WHERE course = :1", qC)
                try: num = max([qL.number for qL in qLs])
                except: num = 1

            text = self.request.get("text").replace('\r','\n').replace('\n\n','\n')
            lines = text.split("\n")
            lines = [line for line in lines if len(line)>=2]
            for line in lines:
                line = line.strip(' ')+' '
            qL = Lesson(course = qC,
                name = lname,
                text = lines,
                number = int(num))
            qL.put()
        self.redirect("/addlesson")
