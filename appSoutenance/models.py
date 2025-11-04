from .app import db

class Entreprise(db.Model):
    id_entreprise = db.Column(db.Integer, primary_key = True)
    nom_entreprise = db.Column(db.String(200), nullable = False)
    secteur = db.Column(db.String(200), nullable = False)
    adresse = db.Column(db.String(300), nullable = False)
    code_postal = db.Column(db.String(5), nullable = False)
    ville = db.Column(db.String(100), nullable = False)
    typeE = db.Column(db.String(100), nullable = False)
    tel_entreprise = db.Column(db.String(15))
    email_entreprise = db.Column(db.String(200))

    def __init__(self, nom_entreprise, secteur, adresse, code_postal, ville, typeE, tel_entreprise = None, email_entreprise = None):
        self.nom_entreprise = nom_entreprise
        self.secteur = secteur
        self.adresse = adresse
        self.code_postal = code_postal
        self.ville = ville
        self.typeE = typeE
        self.tel_entreprise = tel_entreprise
        self.email_entreprise = email_entreprise
    
    def __repr__(self):
        return f"<Entreprise {self.nom_entreprise} de type {self.typeE} dans le secteur {self.secteur} situé à {self.ville} {self.code_postal} {self.adresse}. \nTel: {self.tel_entreprise} \nEmail: {self.email_entreprise}>"


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

    # 1,1
    id_entreprise = db.Column(db.Integer, db.ForeignKey("entreprise.id_entreprise"), nullable = False)
    entreprise = db.relationship("Entreprise", backref = db.backref("demarches", lazy = "dynamic"))

    def __init__(self, source, typeD, situation, date_envoi, id_entreprise, date_relance = None, resultat = None, raison_refus = None, cv = None, lettre_motiv = None):
        self.source = source
        self.typeD = typeD
        self.situation = situation
        self.date_envoi = date_envoi
        self.id_entreprise = id_entreprise
        self.date_relance = date_relance
        self.resultat = resultat
        self.raison_refus = raison_refus
        self.cv = cv
        self.lettre_motiv = lettre_motiv

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

    # 1,1
    id_demarche = db.Column(db.Integer, db.ForeignKey("demarche.id_demarche"), unique = True, nullable = False)
    demarche = db.relationship("Demarche", backref=db.backref("stage", lazy = "joined", uselist = False))

    # 0,1
    id_maitre = db.Column(db.Integer, db.ForeignKey("maitre_stage.id_maitre"), unique=True, nullable = True)
    maitre_stage = db.relationship("MaitreStage", backref=db.backref("stage", lazy = "joined", uselist = False))

    # 0,1
    id_soutenance = db.Column(db.Integer, db.ForeignKey("soutenance.id_soutenance"), unique = True, nullable = True)
    soutenance = db.relationship("Soutenance", backref=db.backref("stage_rel", lazy = "select", uselist = False))

    def __init__(self, typeS, duree, date_debut, sujet, id_demarche, description = None, competence = None, revenu = None):
        self.typeS = typeS
        self.duree = duree
        self.date_debut = date_debut
        self.sujet = sujet
        self.id_demarche = id_demarche
        self.description = description
        self.competence = competence
        self.revenu = revenu

    def __repr__(self):
        return f"<Stage {self.sujet} de type {self.typeS} débutant le {self.date_debut} pour une durée de {self.duree} semaines>"


class MaitreStage(db.Model):
    id_maitre = db.Column(db.Integer, primary_key = True)
    civilite_maitre = db.Column(db.String(50), nullable = False)
    nom_maitre = db.Column(db.String(100), nullable = False)
    prenom_maitre = db.Column(db.String(100), nullable = False)
    tel_maitre = db.Column(db.String(15), nullable = True)
    email_maitre = db.Column(db.String(200), nullable = False)

    # 1,1
    id_entreprise = db.Column(db.Integer, db.ForeignKey("entreprise.id_entreprise"), nullable = False)
    entreprise = db.relationship("Entreprise", backref = db.backref("maitre_stage", lazy = "joined", uselist = False))

    def __init__(self, civilite_maitre, nom_maitre, prenom_maitre, email_maitre, id_entreprise, tel_maitre = None):
        self.civilite_maitre = civilite_maitre
        self.nom_maitre = nom_maitre
        self.prenom_maitre = prenom_maitre
        self.tel_maitre = tel_maitre
        self.email_maitre = email_maitre
        self.id_entreprise = id_entreprise

    def __repr__(self):
        return f"<{self.civilite_maitre} {self.nom_maitre} {self.prenom_maitre} est le maitre de stage>"


class Soutenance(db.Model):
    id_soutenance = db.Column(db.Integer, primary_key = True)
    salle = db.Column(db.Integer, nullable = False)
    nom_bat = db.Column(db.String(50), nullable = False)
    date = db.Column(db.Date, nullable = False)
    h_debut = db.Column(db.String(5), nullable = False)
    h_fin = db.Column(db.String(5), nullable = False)

    # 1,1
    id_stage = db.Column(db.Integer, db.ForeignKey("stage.id_stage"), unique = True, nullable = False)

    def __init__(self, salle, nom_bat, date, h_debut, h_fin, id_stage):
        self.salle = salle
        self.nom_bat = nom_bat
        self.date = date
        self.h_debut = h_debut
        self.h_fin = h_fin
        self.id_stage = id_stage

    def __repr__(self):
        return f"<La soutenance a lieu le {self.date} à {self.h_debut} au batîment {self.nom_bat} {self.salle}>"

    
class Etudiant(db.Model):
    Id_etudiant=db.Columm(db.Integer,primary_key=True)
    Nom_etudiant=db.Column(db.String(20),nullable=False)
    Prenom_etudiant=db.Column(db.String(20),nullable=False)
    Date_naissance=db.Column(db.String(20),nullable=False)
    Telephone_etudiant=db.Column(db.String(10),nullable=False)
    Email_etudiant=db.Column(db.String(100),nullable=False)

    def _init_(self,Id_etudiant,Nom_etudiant,Prenom_etudiant,Date_naissance,Telephone_etudiant,Email_etudiant):
        self.Id_etudiant=Id_etudiant
        self.Nom_etudiant=Nom_etudiant
        self.Prenom_etudiant=Prenom_etudiant
        self.Date_naissance=Date_naissance
        self.Telephone_etudiant=Telephone_etudiant
        self.Email_etudiant=Email_etudiant
    
    def _repr_(self):
        return f"Etudiant :{self.Nom_etudiant} {self.Prenom_etudiant} nait le {self.Date_naissance} contact: {self.Email_etudiant} {self.Telephone_etudiant}"
    
class Promo(db.Model):
    Nom_Promo=db.Column(db.String(20),primary_key=True)
    Annee_Promo=db.Column(db.String(20),primary_key=True)
    Formation_Promo=db.Column(db.String(20),nullable=False)

    def _init_(self,Id_Promo,Nom_Promo,Annee_Promo,Formation_Promo):
            self.Nom_Promo=Nom_Promo
            self.Annee_Promo=Annee_Promo
            self.Formation_Promo=Formation_Promo

    def _repr_(self):
        return f"Promo : {self.Nom_Promo} {self.Annee_Promo} {self.Formation_Promo}"

class Appartenir(db.Model):
    Id_etudiant=db.Columm(db.Integer,db.ForeignKey("etudiant.Id_etudiant"),primary_key=True)
    etudiant=db.relationship("Etudiant",backref=db.backref(""),lazy="dynamic")
    Nom_Promo=db.Column(db.String(20),primary_key=True)
    Annee_Promo=db.Column(db.String(20),primary_key=True)

    def _init_(self,Id_etudiant,Nom_Promo,Annee_Promo):
        self.Id_etudiant=Id_etudiant
        self.Nom_Promo=Nom_Promo
        self.Annee_Promo=Annee_Promo
    
    def _repr_(self):
        return f"etudiant : {self.Id_etudiant} appatient a {self.Nom_Promo} en {self.Annee_Promo}"

