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
@route('/viewMatchMenu')
def viewmatchMenu():
    return template("viewMatchMenu.html")

#Page to get match number and team number for the display
@route('/viewMatchDataIndividual')
def viewMatchDataIndividual():
    return template("viewMatchDataIndividual.html")

#Page to display indivdual match data of one team
@post('viewMatchDataIndividualReceived')
def viewMatchDataIndividualReceived():
    return template("viewMatchDataIndividualReceived.html")

application = default_app()

