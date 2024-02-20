from app import app
from flask import request
from flask import render_template, flash, redirect, url_for, jsonify


print("here I am")


# @app.route("/")
# @app.route("/index")
# def index():
#     return "Hello, World!_)_!!"


@app.route("/", methods=("GET", "POST"))
@app.route("/index")
def index():
    return render_template("index.html", title="Your Own TARDIS")
