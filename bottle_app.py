# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template, post

#Menu
@route('/')
def menu():
    return template("menu.html")

#Page where user records match
@route('/recordMatch')
def recordMatch():
    return template("recordMatchForm.html")

#Page that confirms user input and saves data
@post('/storeData')
def storeData():
    return template("storeData.html")

#Page that shows links to all possible ways to view match data
@route('/viewData')
def viewDataMenu():
    return template("viewData/menu.html")

#Page to get team number for the display
@route('/viewData/individualMatch')
def viewDataIndividualMatch():
    return template("viewData/individualMatch.html")

#Page where the match number is selected
@post('/viewData/individualMatchChoose')
def viewDataIndividualMatchChoose():
    return template("viewData/individualMatchChoose.html")

#Page to display indivdual match data of one team
@post('/viewData/individualMatchReceived')
def viewDataIndividualMatchReceived():
    return template("viewData/individualMatchReceived.html")

#Page to select match number, to show stats of all teams in match
@route('/viewData/match')
def viewDataMatch():
    return template("viewData/match.html")
#Gets the match data
@post('/viewData/matchReceived')
def viewDataMatchReceived():
    return template("viewData/matchReceived.html")

#Page to select team number, to show avg stats of team
@route('/viewData/teamAverage')
def viewDataTeamAverage():
    return template("viewData/teamAverage.html")
#Gets avg data
@post('/viewData/teamAverageReceived')
def viewDataTeamAverageReceived():
    return template("/viewData/teamAverageReceived.html")

application = default_app()

