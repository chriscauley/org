from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.api import users
import datetime

def gUser(wApp):
    user = users.get_current_user()
    qU = User.gql("WHERE name = :1", user).get()
    try: qU.name
    except:
        User(name = user).put()
        qU = User.gql("WHERE name = :1", user).get()
    stats = UserStats(user=qU)
    stats.lastplay = datetime.datetime.now().date()
    return qU

#class AddUser(webapp.RequestHandler):
#    User(name=self.request.get("user")).put()

class User(db.Model):
    name = db.UserProperty()

class UserStats(db.Model):
    user = db.ReferenceProperty(User, collection_name="stats")
    lastplay = db.DateProperty()
    plays = db.IntegerProperty()
    lessons_added = db.IntegerProperty()

class Course(db.Model):
    name = db.StringProperty()
    user = db.UserProperty()

class Lesson(db.Model):
    course = db.ReferenceProperty(Course, collection_name = 'lessons')
    name = db.StringProperty()
    text = db.ListProperty(str)
    number = db.IntegerProperty()
    user = db.UserProperty()

class Score(db.Model):
    user = db.ReferenceProperty(User, collection_name = 'user')
    lesson = db.ReferenceProperty(Lesson, collection_name = 'lesson')
    speed = db.ListProperty(int)
    accuracy = db.ListProperty(int)

    def _stats_sh(self):
        if self.speed == []:
            return 0
        else:
            return max(self.speed)

    def _stats_ah(self):
        if self.accuracy == []:
            return 0
        else:
            return max(self.accuracy)

    def _stats_sa(self):
        if self.speed == []:
            return 0
        else:
            return sum(self.speed)/len(self.speed)

    def _stats_aa(self):
        if self.accuracy == []:
            return 0
        else:
            return sum(self.accuracy)/len(self.accuracy)

    sHigh = property(_stats_sh)
    aHigh = property(_stats_ah)
    sAve = property(_stats_sa)
    aAve = property(_stats_aa)

"""    def smax(iList):
        if iList == []:
            return 0
        else:
            return max(iList)

    def smean(iList):
        if iList == []:
            return 0
        else:
            return mean(iList)"""

class AddScore(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if user:
            pass
        else:
            user="Anon"
        qU = User.gql("WHERE name = :1", user).get()

        lesson = self.request.get("lesson")
        qL = Lesson.gql("WHERE name = :1", lesson).get()
        qS = Score.gql("WHERE lesson = :1 AND user = :2", qL, qU).get()
        if str(qS)=="None":
            qS = Score()
            qS.lesson = qL
            qS.speed = []
            qS.accuracy = []
            qS.user = qU
        spd = int(float(self.request.get("spd")))
        acc = int(float(self.request.get("acc")))
        response = ['Score recorded']
        if spd>qS._stats_sh():
            response.append('<br />Speed is personal best!')
        if acc>qS._stats_ah():
            response.append('<br />Accuracy is personal best!')
        qS.speed.append(spd)
        qS.accuracy.append(acc)
        qS.put()
        self.response.out.write(response)
