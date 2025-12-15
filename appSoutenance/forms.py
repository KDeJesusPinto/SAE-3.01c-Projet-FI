from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, IntegerField, SubmitField, FormField, PasswordField
from wtforms.validators import DataRequired, NumberRange
from hashlib import sha256
from appSoutenance.models import Etudiant, Enseignant, Admini
   
class LoginForm(FlaskForm):
    Login = StringField("Identifiant")
    Password = PasswordField("Mot de passe")
    next = HiddenField()

    def get_authenticated_etudiant(self):
       etudiant = Etudiant.query.filter(Etudiant.login_etudiant == self.Login.data).first()

       if etudiant is None:
           return None
      
       m = sha256()
       m.update(self.Password.data.encode())


       passwd = m.hexdigest()
       if passwd != etudiant.pwd_etudiant:
           return None
       return etudiant
    
    def get_authenticated_enseignant(self):
       enseignant = Enseignant.query.filter(Enseignant.login_enseignant == self.Login.data).first()

       if enseignant is None:
           return None
      
       m = sha256()
       m.update(self.Password.data.encode())


       passwd = m.hexdigest()
       if passwd != enseignant.pwd_etudiant:
           return None
       return enseignant
    
    def get_authenticated_admin(self):
       admin = Admini.query.filter(Admini.login_admin == self.Login.data).first()

       if admin is None:
           return None
      
       m = sha256()
       m.update(self.Password.data.encode())


       passwd = m.hexdigest()
       if passwd != admin.pwd_etudiant:
           return None
       return admin

    
