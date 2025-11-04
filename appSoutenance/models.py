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

