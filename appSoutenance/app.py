from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db.init_app(app)