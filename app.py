from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = True
@app.route("/")
def welcome():
    return "Hello World"

from controller import *