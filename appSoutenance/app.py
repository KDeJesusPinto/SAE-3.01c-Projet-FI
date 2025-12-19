from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #éventuellement ajouter "app" entre les parenthèses 
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "index"
login_manager.login_message = ""