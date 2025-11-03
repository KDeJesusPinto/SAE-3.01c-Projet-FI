from .app import db

class Entreprise (db.Model):
    Id_entreprise = db.Column(db.Integer, primary_key = True)
    Nom_entreprise = db.Column(db.String(200), nullable = False)
    Secteur = db.Column(db.String(200), nullable = False)
    Adresse = db.Column(db.String(300), nullable = False)
    Type = db.Column(db.String(100), nullable = False)
    Tel_entreprise = db.Column(db.String(20))
    Email_entreprise = db.Column(db.String(200))

    def __init__(self, nom_entreprise, secteur, adresse, type, tel_entreprise, email_entreprise):
        self.Nom_entreprise = nom_entreprise
        self.Secteur = secteur
        self.Adresse = adresse
        self.Type = type
        self.Tel_entreprise = tel_entreprise
        self.Email_entreprise = email_entreprise
    
    def __repr__(self):
        return f"<Entreprise {self.Nom_entreprise} de type {self.Type} dans le secteur {self.Secteur} situé à {self.Adresse}. \nTel: {self.Tel_entreprise} \nEmail: {self.Email_entreprise}>"
    
class Demarche(db.Model):
    Id_demarche = db.Column(db.Integer, primary_key = True)
    Source = db.Column(db.String(300), nullable = False)
    Type = db.Column(db.String(100), nullable = False)
    Situation = db.Column(db.String(300), nullable = False)
    Date_envoi = db.Column(db.Date, nullable = False)
    Date_relance = db.Column(db.Date)
    Resultat = db.Column(db.String(300))
    Raison_refus = db.Column(db.String(300))
    Cv = db.Column(db.String(200))
    Lettre_motiv = db.Column(db.String(200))
    entreprise_id = db.Column(db.Integer, db.ForeignKey("entreprise.Id_entreprise"))
    entreprise = db.relationship("Entreprise", backref = db.backref("demarches", lazy = "dynamic"))

    def __init__(self, id_demarche, source, type, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre):
        self.Id_demarche = id_demarche
        self.Source = source
        self.Type = type
        self.Situation = situation
        self.Date_envoi = date_envoi
        self.Date_relance = date_relance
        self.Resultat = resultat
        self.Raison_refus = raison_refus
        self.Cv = cv
        self.Lettre_motiv = lettre
    
    def __repr__(self):
        return f"<Demarche {self.Id_demarche} de type {self.Type} envoyée le {self.Date_envoi} pour l'entreprise {self.entreprise.Nom_entreprise}. Situation actuelle: {self.Situation}>"




# class Contact(db.Model):
# class Travailler(db.Model):
# class Stage(db.Model):
# class Obtenir(db.Model):