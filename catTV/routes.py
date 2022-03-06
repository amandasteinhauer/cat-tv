from flask import render_template
from catTV import app

@app.route("/")
@app.route('/index')
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/birds")
def birds():
    return render_template('videos.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

