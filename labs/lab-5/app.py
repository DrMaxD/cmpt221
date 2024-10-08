"""app.py: render and route to webpages"""
from flask import render_template

from db.server import app

# create a webpage based off of the html in templates/index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/important')
def important():
    return render_template('Important.html')

@app.route('/thoughts')
def thoughts():
    return render_template('Thoughts.html')

@app.route('/doge')
def doge():
    return render_template('Doge.html')

if __name__ == "__main__":
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)

