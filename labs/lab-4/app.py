"""app.py: render and route to webpages"""
<<<<<<< HEAD
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, insert
=======
from flask import render_template
>>>>>>> main

from server import *

# create a webpage based off of the html in templates/index.html
<<<<<<< HEAD
# not required: if you want to play around with some html, feel free
# to edit templates/index.html
=======
>>>>>>> main
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)

