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
           print(f"--- Enseignant non trouvé pour le login : {self.Login.data} ---")
           return None
      
       m = sha256()
       m.update(self.Password.data.encode())
       passwd_hache_entree = m.hexdigest()


        # >>> DIAGNOSTIC CLÉ : Imprimez les deux valeurs pour comparaison <<<
       print("---------------------------------------------------------------------")
       print(f"Login réussi (DB)      : {enseignant.login_enseignant}")
       print(f"MDP Haché ENTRÉ        : {passwd_hache_entree}")
       print(f"MDP Haché STOCKÉ (DB)  : {enseignant.pwd_enseignant}")
       print("---------------------------------------------------------------------")
        # >>> FIN DU DIAGNOSTIC <<<

       if passwd_hache_entree != enseignant.pwd_enseignant:
            # L'utilisateur existe, mais le mot de passe ne correspond pas.
            return None
       return enseignant
    
    def get_authenticated_admin(self):
       admin = Admini.query.filter(Admini.login_admin == self.Login.data).first()

       if admin is None:
           return None
      
       m = sha256()
       m.update(self.Password.data.encode())


       passwd = m.hexdigest()
       if passwd != admin.pwd_admin:
           return None
       return admin

    
