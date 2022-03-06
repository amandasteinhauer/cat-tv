from flask import render_template
from catTV import app

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('home.html')

@app.route("/birds")
def birds():
    return render_template('home.html')

