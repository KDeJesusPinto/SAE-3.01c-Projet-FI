from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, IntegerField, SubmitField, FormField, PasswordField
from wtforms.validators import DataRequired, NumberRange
from hashlib import sha256
from appSoutenance.models import Etudiant, Enseignant, Admini
   
class LoginForm(FlaskForm):
    Login = StringField("Identifiant", validators=[DataRequired()])
    Password = PasswordField("Mot de passe", validators=[DataRequired()])
    next = HiddenField()

    def get_authenticated_etudiant(self):
       etudiant = Etudiant.query.filter(Etudiant.login_etudiant == self.Login.data).first()
       if etudiant is None:
           return None
      
       if etudiant.pwd_etudiant == self.Password.data:
           return etudiant

       m = sha256()
       m.update(self.Password.data.encode())
       if m.hexdigest() == etudiant.pwd_etudiant:
           return etudiant
           
       return None
    
    def get_authenticated_enseignant(self):
       enseignant = Enseignant.query.filter(Enseignant.login_enseignant == self.Login.data).first()
       if enseignant is None:
           return None
      
       if enseignant.pwd_enseignant == self.Password.data:
           return enseignant

       m = sha256()
       m.update(self.Password.data.encode())
       if m.hexdigest() == enseignant.pwd_enseignant:
           return enseignant

       return None
    
    def get_authenticated_admin(self):
       admin = Admini.query.filter(Admini.login_admin == self.Login.data).first()
       if admin is None:
           return None
      
       if admin.pwd_admin == self.Password.data:
           return admin

       m = sha256()
       m.update(self.Password.data.encode())
       if m.hexdigest() == admin.pwd_admin:
           return admin

       return None

    
