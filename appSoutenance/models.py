from .app import db

class Entreprise (db.Model):
    Id_entreprise = db.Column(db.Integer, primary_key = True)
    Nom_entreprise = db.Column(db.String(200), nullable = False)
    Secteur = db.Column(db.String(200), nullable = False)
    Adresse = db.Column(db.String(300), nullable = False)
    Code_postal = db.Column(db.Integer(5), nullable = False)
    Ville = db.Column(db.String(100), nullable = False)
    Type = db.Column(db.String(100), nullable = False)
    Tel_entreprise = db.Column(db.String(20), nullable = False)
    Email_entreprise = db.Column(db.String(200), nullable = False)

    def __init__(self, nom_entreprise, secteur, adresse, code_postal, ville, type, tel_entreprise, email_entreprise):
        self.Nom_entreprise = nom_entreprise
        self.Secteur = secteur
        self.Adresse = adresse
        self.Code_postal = code_postal
        self.Ville = ville
        self.Type = type
        self.Tel_entreprise = tel_entreprise
        self.Email_entreprise = email_entreprise
    
    def __repr__(self):
        return f"<Entreprise {self.Nom_entreprise} de type {self.Type} dans le secteur {self.Secteur} situé à {self.Adresse}. \nTel: {self.Tel_entreprise} \nEmail: {self.Email_entreprise}>"
    

class MaitreStage (db.Model):
    Id_maitre = db.Column(db.Integer, primary_key = True)
    Civilite_maitre = db.Column(db.String(50), nullable = False)
    Nom_maitre = db.Column(db.String(100), nullable = False)
    Prenom_maitre = db.Column(db.String(100), nullable = False)
    Tel_maitre = db.Column(db.Integer(10), nullable = True)
    Email_maitre = db.Column(db.String(200), nullable = False)

    entreprise_id = db.Column(db.Integer, db.ForeignKey ("entreprise.Id_entreprise"))
    entreprise = db.relationship("Entreprise", backref = db.backref("maitre", lazy = "dynamic"))

    def __init__(self, id_maitre, civilite_maitre, nom_maitre, prenom_maitre, tel_maitre, email_maitre):
        self.Id_maitre = id_maitre
        self.Civilite_maitre = civilite_maitre
        self.Nom_maitre = nom_maitre
        self.Prenom_maitre = prenom_maitre
        self.Tel_maitre = tel_maitre
        self.Email_maitre = email_maitre

    def __repr__(self):
        return f"<{self.Civilite_maitre} {self.Nom_maitre} {self.Prenom_maitre} est le maitre de stage>"
    


class Soutenance (db.Model) :
    Id_soutenance = db.Column(db.Integer, primary_key = True)
    Salle = db.Column(db.Integer(5), nullable = False)
    Nom_bat = db.Column(db.String(50), nullable = False)
    Date = db.Column(db.Date(10), nullable = False)
    H_debut = db.Column(db.String(5), nullable = False)
    H_fin  = db.Column(db.String(5), nullable = False)

    stage_id = db.Column(db.Integer, db.ForeignKey ("stage.Id_stage"))
    stage = db.relationship("Stage", backref = db.backref("soutenance", lazy = "dynamic"))

    def __init__(self, id_soutenance, salle, nom_bat, date, h_debut,h_fin) :
        self.Id_soutenance = id_soutenance
        self.Salle = salle
        self.Nom_bat = nom_bat
        self.Date = date
        self.H_debut = h_debut
        self.H_fin = h_fin

    def __repr__(self):
        return f"<La soutenance a lieu le {self.Date} à {self.H_debut} au batîment {self.Nom_bat} {self.Salle}>"