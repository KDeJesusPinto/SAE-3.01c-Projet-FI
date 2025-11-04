from .app import db

class Entreprise (db.Model):
    id_entreprise = db.Column(db.Integer, primary_key = True)
    nom_entreprise = db.Column(db.String(200), nullable = False)
    secteur = db.Column(db.String(200), nullable = False)
    adresse = db.Column(db.String(300), nullable = False)
    Code_postal = db.Column(db.Integer(5), nullable = False)
    Ville = db.Column(db.String(100), nullable = False)
    typeE = db.Column(db.String(100), nullable = False)
    tel_entreprise = db.Column(db.String(20))
    email_entreprise = db.Column(db.String(200))

    def __init__(self, nom_entreprise, secteur, adresse, code_postal, ville, type, tel_entreprise, email_entreprise):
        self.nom_entreprise = nom_entreprise
        self.secteur = secteur
        self.adresse = adresse
        self.Code_postal = code_postal
        self.Ville = ville
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