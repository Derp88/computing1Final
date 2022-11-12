# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template

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

application = default_app()

