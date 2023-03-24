from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    x=3
    return "Hello, Flask!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name):
    return render_template("hello_there.html", username=name)