from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('home.html')

@app.route("/birds")
def birds():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=80)
