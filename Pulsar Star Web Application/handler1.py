#even in the handler, must also import flask and import request
from flask import request

def helloworld():
    return 'Hello world!'

#@app.route('/greet/', defaults={'name':'nobody'})
#@app.route('/greet/<name>')
def greet(name):
    return 'Good morning, '+name

#@app.route('/add/<int:x>/<int:y>')
def add(x,y):
    return 'Total is ' + str(x+y)

#@app.route('/sayhello', methods=['GET','POST'])
def say_hello():
    name = request.args.get('name') or request.form.get('name')
    return "Hello " + name