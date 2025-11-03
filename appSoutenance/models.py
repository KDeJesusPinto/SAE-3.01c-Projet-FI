from .app import db

class Entreprise (db.Model):
    id_entreprise = db.Column(db.Integer, primary_key = True)
    nom_entreprise = db.Column(db.String(200), nullable = False)
    secteur = db.Column(db.String(200), nullable = False)
    adresse = db.Column(db.String(300), nullable = False)
    type = db.Column(db.String(100), nullable = False)
    tel_entreprise = db.Column(db.String(20), nullable = False)
    email_entreprise = db.Column(db.String(200), nullable = False)
    