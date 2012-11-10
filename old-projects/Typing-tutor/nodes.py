import os

from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from models import *

def courseTabs(qU):
    qCs = Course.all().fetch(1000)
    tabs = [];
    for qC in qCs:
        tab = {};
        tab["name"]= qC.name
        tab["namenospace"] = qC.name.replace(' ','')
        smallList = ''
        qLs = Lesson.gql("WHERE course=:1 ORDER BY number", qC)
        smallList+="\n    <div id='tabs-"+qC.name.replace(' ','')+"'><table class=\"lessons\">"
        smallList+="\n        <tr>"
        smallList+="\n            <td>Name:</td>"
        smallList+="\n            <td>Top Speed:</td>"
        smallList+="\n            <td>Mean Speed:</td>"
        smallList+="\n            <td>Top Acc:</td>"
        smallList+="\n            <td>Mean Acc:</td>"
        smallList+="\n        </tr>"
        for qL in qLs:
            qLn = qL.name
            qS = Score.gql("WHERE user = :1 AND lesson = :2", qU, qL).get()
            if str(qS)=='None':
                qS=Score() 
            oc="onclick=\"changeLesson('"+qLn+"')\""
            smallList+="\n        <tr>"
            smallList+="\n            <td><a href='#' "+oc+">"+qLn+"</a></td>"
            smallList+="\n            <td>"+str(qS.sHigh)+" cpm</td>"
            smallList+="\n            <td>"+str(qS.sAve)+" cpm</td>"
            smallList+="\n            <td>"+str(qS.aHigh)+" %</td>"
            smallList+="\n            <td>"+str(qS.aAve)+" %</td>"
            smallList+="\n        </tr>"
        smallList+="\n    </table></div>\n"
        tab["cont"] = smallList
        tabs.append(tab)
    return tabs

def keyboard(mode):
    from garrays import keys, codes
    board=[]
    keys = keys[mode]
    for ks in keys:
        nb='    '
        for k in ks:
            nb = nb + """<span id='code"""+codes[k.lower()]+"""'>"""+k+"""</span><!--
    -->"""
        board.append(nb)
    return board
