from flask import Flask
import operations
from flask import request
# Put your app in here.

app = Flask(__name__)


@app.route("/add")
def addition_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operations.add(a, b))


@app.route('/sub')
def subtract_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operations.sub(a, b))


@app.route('/mult')
def multiply_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operations.mult(a, b))


@app.route('/div')
def division_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operations.div(a, b))

