from .app import db

class Entreprise (db.Model):
    id_entreprise = db.Column(db.Integer, primary_key = True)
    nom_entreprise = db.Column(db.String(200), nullable = False)
    secteur = db.Column(db.String(200), nullable = False)
    adresse = db.Column(db.String(300), nullable = False)
    typeE = db.Column(db.String(100), nullable = False)
    tel_entreprise = db.Column(db.String(20))
    email_entreprise = db.Column(db.String(200))

    def __init__(self, nom_entreprise, secteur, adresse, type, tel_entreprise, email_entreprise):
        self.nom_entreprise = nom_entreprise
        self.secteur = secteur
        self.adresse = adresse
        self.typeE = type
        self.tel_entreprise = tel_entreprise
        self.email_entreprise = email_entreprise
    
    def __repr__(self):
        return f"<Entreprise {self.nom_entreprise} de type {self.typeE} dans le secteur {self.secteur} situé à {self.adresse}. \nTel: {self.tel_entreprise} \nEmail: {self.email_entreprise}>"

class Demarche(db.Model):
    id_demarche = db.Column(db.Integer, primary_key = True)
    source = db.Column(db.String(300), nullable = False)
    typeD = db.Column(db.String(100), nullable = False)
    situation = db.Column(db.String(300), nullable = False)
    date_envoi = db.Column(db.Date, nullable = False)
    date_relance = db.Column(db.Date)
    resultat = db.Column(db.String(300))
    raison_refus = db.Column(db.String(300))
    cv = db.Column(db.String(200))
    lettre_motiv = db.Column(db.String(200))
    id_entreprise = db.Column(db.Integer, db.ForeignKey("entreprise.Id_entreprise"))
    entreprise = db.relationship("Entreprise", backref = db.backref("demarches", lazy = "dynamic"))

    def __init__(self, id_demarche, source, type, situation, date_envoi, date_relance, resultat, raison_refus, cv, lettre):
        self.id_demarche = id_demarche
        self.source = source
        self.typeD = type
        self.situation = situation
        self.date_envoi = date_envoi
        self.date_relance = date_relance
        self.resultat = resultat
        self.raison_refus = raison_refus
        self.cv = cv
        self.lettre_motiv = lettre

    def __repr__(self):
        return f"<Demarche {self.id_demarche} de type {self.typeD} envoyée le {self.date_envoi} pour l'entreprise {self.entreprise.nom_entreprise}. Situation actuelle: {self.situation}>"


class Stage(db.Model):
    id_stage = db.Column(db.Integer, primary_key = True)
    typeS = db.Column(db.String(100), nullable = False)
    duree = db.Column(db.Integer, nullable = False)
    date_debut = db.Column(db.Date, nullable = False)
    sujet = db.Column(db.String(300), nullable = False)
    description = db.Column(db.String(500))
    competence = db.Column(db.String(200))
    revenu = db.Column(db.Float)
    id_demarche = db.Column(db.Integer, db.ForeignKey("demarche.id_demarche"))
    demarche = db.relationship("Demarche", backref = db.backref("stages", lazy = "dynamic"))

    def __init__(self, type, duree, date_debut, sujet, description, competence, revenu):
        self.typeS = type
        self.duree = duree
        self.date_debut = date_debut
        self.sujet = sujet
        self.description = description
        self.competence = competence
        self.revenu = revenu

    def __repr__(self):
        return f"<Stage {self.sujet} de type {self.typeS} débutant le {self.date_debut} pour une durée de {self.duree} semaines>"
