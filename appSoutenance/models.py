from .app import db

class Entreprise (db.Model):
    Id_entreprise = db.Column(db.Integer, primary_key = True)
    Nom_entreprise = db.Column(db.String(200), nullable = False)
    Secteur = db.Column(db.String(200), nullable = False)
    Adresse = db.Column(db.String(300), nullable = False)
    Type = db.Column(db.String(100), nullable = False)
    Tel_entreprise = db.Column(db.String(20), nullable = False)
    Email_entreprise = db.Column(db.String(200), nullable = False)

    def __init__(self, nom_entreprise, secteur, adresse, type, tel_entreprise, email_entreprise):
        self.Nom_entreprise = nom_entreprise
        self.Secteur = secteur
        self.Adresse = adresse
        self.Type = type
        self.Tel_entreprise = tel_entreprise
        self.Email_entreprise = email_entreprise
    
    def __repr__(self):
        return f"<Entreprise {self.Nom_entreprise} de type {self.Type} dans le secteur {self.Secteur} situé à {self.Adresse}. \nTel: {self.Tel_entreprise} \nEmail: {self.Email_entreprise}>"