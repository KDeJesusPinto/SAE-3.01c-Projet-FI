from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, IntegerField, SubmitField, FormField, PasswordField
from wtforms.validators import DataRequired, NumberRange
from hashlib import sha256
from appSoutenance.models import Etudiant, Enseignant, Admini
   
class LoginForm(FlaskForm):
    Login = StringField("Identifiant")
    Password = PasswordField("Mot de passe")
    next = HiddenField()

    def get_authenticated_user(self):
        user = Etudiant.query.filter_by(login_per=self.Login.data).first()

        if user is None:
            return None

        m = sha256()
        m.update(self.Password.data.encode())

        if m.hexdigest() == user.mdp:
            return user
        return None

    
