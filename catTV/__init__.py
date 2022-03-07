import os
from flask import Flask
from flask_bootstrap import Bootstrap
from catTV import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(config.Config)
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=80)

from catTV import routes, models
