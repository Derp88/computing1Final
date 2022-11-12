# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template

@route('/')
def menu():
    return template("pageMenu.html")

application = default_app()

