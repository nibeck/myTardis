from app import app
from flask import request
from flask import render_template, flash, redirect, url_for, jsonify
from rpi_ws281x import Color
from app.models import TARDIS
from color_utils import hex_to_color

BLUE = Color(0, 0, 255)
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
PURPLE = Color(127, 0, 255)
YELLOW = Color(255, 255, 0)
GREEN = Color(50, 205, 50)
TEAL = Color(100, 128, 128)
NAVY = Color(0, 0, 128)
LIGHTRED = Color(5, 0, 0)
TARDISBLUE = Color(0, 59, 111)
GRAY = Color(66, 66, 66)
print("here I am")

# careet TARDOIS object for controlling
# myTARDIS = TARDIS("mike")
myTARDIS = TARDIS("mike", RED)
# myTARDIS.turnOff()

# @app.route("/")
# @app.route("/index")
# def index():
#     return "Hello, World!_)_!!"


@app.route("/", methods=("GET", "POST"))
@app.route("/index")
def index():
    return render_template("index.html", title="Your Own TARDIS")


@app.route("/test", methods=("GET", "POST"))
def test():
    return render_template("index-tst.html", title="Your Own TARDIS")


@app.route("/old", methods=("GET", "POST"))
def old():
    return render_template("index-old.html", title="Your Own TARDIS")


@app.route("/gpt", methods=("GET", "POST"))
def gpt():
    return render_template("index-gpt.html", title="Your Own TARDIS")


@app.route("/pulse", methods=("GET", "POST"))
def pulse():
    return render_template("index.html", title="Your Own TARDIS")


@app.route("/tardis/off", methods=("GET", "POST"))
def turnOff():
    print("In Turn Off")
    myTARDIS.turnOff()
    return "Successfully turned Off"


@app.route("/tardis/on", methods=("GET", "POST"))
def turnOn():
    print("In Turn On")
    # Grab color passed back from web client and turn TARDIS on with that Color
    newColor = hex_to_color(request.form["newColor"])
    myTARDIS.setWindowColors(newColor)
    print(request.form["newColor"])
    myTARDIS.turnOn()
    return "Successfully turned On"


@app.route("/tardis/color", methods=("GET", "POST"))
def tardisColor():
    print("In TARDIS Color")
    newColor = hex_to_color(request.form["newColor"])
    myTARDIS.setWindowColors(newColor)
    print(request.form["newColor"])
    return "Successfully changes Color"
