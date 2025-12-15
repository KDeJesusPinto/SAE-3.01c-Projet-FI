from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #éventuellement ajouter "app" entre les parenthèses 
db.init_app(app)