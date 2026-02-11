from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, IntegerField, SelectField, SubmitField, FormField, PasswordField, DateField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed
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
   
class FormSoutenance(FlaskForm):
    id_soutenance = HiddenField("ID:")
    id_stage = HiddenField("ID du stage ")
    h_debut = StringField("Heure de début: ")
    dateS = DateField("Date de la soutenance: ", validators=[DataRequired()])
    salle = StringField ("Salle de la soutenance: ")
    nom_enseignant =  StringField("Liste prof")


class ImportForm(FlaskForm):
    type_import = SelectField(
        "Type de données à importer :",
        choices=[
            ('etudiants_stages', 'Étudiants et Stages'),
            ('entreprises', 'Entreprises')
        ],
        validators=[DataRequired(message="Veuillez sélectionner le type d'import.")]
    )
    ficCSV = FileField("Sélectionner un fichier CSV",
                       validators = [FileRequired("Sélectionnez un fichier CSV"),
                                     FileAllowed(['csv'], "Format CSV uniquement")]
                        )
    submit = SubmitField("Importer le fichier CSV")

class ExportForm(FlaskForm):
    type_export = SelectField(
        "Type de données à exporter :",
        choices=[
            ('etudiants', 'Étudiants'),
            ('entreprises', 'Entreprises'),
            ('soutenances', 'Soutenances')
        ],
        validators=[DataRequired(message="Veuillez sélectionner le type d'export.")]
    )
    submit = SubmitField("Exporter en CSV")
