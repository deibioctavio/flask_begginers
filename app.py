#!python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home/index.html")

@app.route('/welcome')
def welcome():
    return "Welcome to welcome page from My First Flask App"

@app.route('/potato')
def potato():
    return "Welcome to potato page from My First Flask App"

@app.route('/another')
def another():
    return "Welcome to another page from My First Flask App"


@app.route('/req',  methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def reqs():
    if request.method == 'POST':
        return "You've request POST method"

    elif request.method == 'GET':
        return "You've request GET method"

    elif request.method == 'PUT':
        return "You've request PUT method"

    elif request.method == 'DELETE':
        return "You've request DELETE method"

    else:
        return "You've request another different method from [GET, POST, PUT, DELETE]"

app.run()
