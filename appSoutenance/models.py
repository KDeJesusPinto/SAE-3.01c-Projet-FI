from .app import db


class Entreprise(db.Model):
    id_entreprise = db.Column(db.Integer, primary_key=True)
    nom_entreprise = db.Column(db.String(200), nullable=False)
    secteur = db.Column(db.String(200), nullable=False)
    ville = db.Column(db.String(100), nullable=False)
    adresse = db.Column(db.String(200), nullable=False)
    code_postal = db.Column(db.String(5), nullable=False)
    typeE = db.Column(db.String(100), nullable=False)
    tel_entreprise = db.Column(db.String(15))
    email_entreprise = db.Column(db.String(200))

    def __init__(self,
                 nom_entreprise,
                 secteur,
                 ville,
                 adresse,
                 code_postal,
                 typeE,
                 tel_entreprise=None,
                 email_entreprise=None):
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
    id_demarche = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(300), nullable=False)
    typeD = db.Column(db.String(100), nullable=False)
    situation = db.Column(db.String(300), nullable=False)
    date_envoi = db.Column(db.Date, nullable=False)
    date_relance = db.Column(db.Date)
    resultat = db.Column(db.String(300))
    raison_refus = db.Column(db.String(300))
    cv = db.Column(db.String(200))
    lettre_motiv = db.Column(db.String(200))

    # 1,1
    id_entreprise = db.Column(db.Integer,
                              db.ForeignKey("entreprise.id_entreprise"),
                              nullable=False)
    entreprise = db.relationship("Entreprise",
                                 backref=db.backref("demarches", lazy="joined"))

    # 1.1
    id_etudiant = db.Column(db.Integer,
                            db.ForeignKey("etudiant.id_etudiant"),
                            nullable=False)
    etudiant = db.relationship("Etudiant",
                               backref=db.backref("demarches", lazy="joined"))

    def __init__(self,
                 source,
                 typeD,
                 situation,
                 date_envoi,
                 id_entreprise,
                 id_etudiant,
                 date_relance=None,
                 resultat=None,
                 raison_refus=None,
                 cv=None,
                 lettre_motiv=None):
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
        self.id_etudiant = id_etudiant

    def __repr__(self):
        return f"<Demarche {self.id_demarche} de type {self.typeD} envoyée le {self.date_envoi} pour l'entreprise {self.entreprise.nom_entreprise}. Situation actuelle: {self.situation}>"


class Stage(db.Model):
    id_stage = db.Column(db.Integer, primary_key=True)
    typeS = db.Column(db.String(100), nullable=False)
    date_debut = db.Column(db.Date, nullable=False)
    date_fin = db.Column(db.Date, nullable=False)
    duree_stage = db.Column(db.Integer)
    unite_duree = db.Column(db.String(50))
    titre_stage = db.Column(db.String(100))
    theme_stage = db.Column(db.String(100))

    # 1,1
    id_demarche = db.Column(db.Integer,
                            db.ForeignKey("demarche.id_demarche"),
                            unique=True,
                            nullable=False)
    demarche = db.relationship("Demarche",
                               backref=db.backref("stage",
                                                  lazy="joined",
                                                  uselist=False))

    # 0,1
    id_maitre = db.Column(db.Integer,
                          db.ForeignKey("maitre_stage.id_maitre"),
                          unique=True,
                          nullable=True)
    maitre_stage = db.relationship("MaitreStage",
                                   backref=db.backref("stage",
                                                      lazy="select",
                                                      uselist=False))

    # 0,1
    # id_soutenance = db.Column(db.Integer, db.ForeignKey("soutenance.id_soutenance"), unique = True, nullable = True)
    # soutenance = db.relationship("Soutenance", backref = db.backref("stage", lazy = "select", uselist = False))

    def __init__(self,
                 typeS,
                 date_debut,
                 date_fin,
                 titre_stage,
                 theme_stage,
                 id_demarche,
                 id_maitre=None,
                 id_soutenance=None):
        self.typeS = typeS
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.titre_stage = titre_stage
        self.theme_stage = theme_stage
        self.id_demarche = id_demarche
        self.id_maitre = id_maitre
        self.id_soutenance = id_soutenance

    def __repr__(self):
        return f"<Stage {self.titre_stage} de type {self.typeS} débutant le {self.date_debut} et se terminant le {self.date_fin}>"


class MaitreStage(db.Model):
    id_maitre = db.Column(db.Integer, primary_key=True)
    civilite_maitre = db.Column(db.String(50), nullable=False)
    nom_maitre = db.Column(db.String(100), nullable=False)
    prenom_maitre = db.Column(db.String(100), nullable=False)
    tel_maitre = db.Column(db.String(15), nullable=True)
    email_maitre = db.Column(db.String(200), nullable=False)

    # 1,1
    id_entreprise = db.Column(db.Integer,
                              db.ForeignKey("entreprise.id_entreprise"),
                              nullable=False)
    entreprise = db.relationship("Entreprise",
                                 backref=db.backref("maitre_stage",
                                                    lazy="joined",
                                                    uselist=False))

    def __init__(self,
                 civilite_maitre,
                 nom_maitre,
                 prenom_maitre,
                 email_maitre,
                 id_entreprise,
                 tel_maitre=None):
        self.civilite_maitre = civilite_maitre
        self.nom_maitre = nom_maitre
        self.prenom_maitre = prenom_maitre
        self.tel_maitre = tel_maitre
        self.email_maitre = email_maitre
        self.id_entreprise = id_entreprise

    def __repr__(self):
        return f"<{self.civilite_maitre} {self.nom_maitre} {self.prenom_maitre} est le maitre de stage>"


class Soutenance(db.Model):
    id_soutenance = db.Column(db.Integer, primary_key=True)
    salle = db.Column(db.Integer, nullable=False)
    nom_bat = db.Column(db.String(50), nullable=False)
    dateS = db.Column(db.Date, nullable=False)
    h_debut = db.Column(db.String(5), nullable=False)
    h_fin = db.Column(db.String(5), nullable=False)

    # 1,1
    id_stage = db.Column(db.Integer,
                         db.ForeignKey("stage.id_stage"),
                         unique=True,
                         nullable=False)

    def __init__(self, salle, nom_bat, dateS, h_debut, h_fin, id_stage):
        self.salle = salle
        self.nom_bat = nom_bat
        self.dateS = dateS
        self.h_debut = h_debut
        self.h_fin = h_fin
        self.id_stage = id_stage

    def __repr__(self):
        return f"<La soutenance a lieu le {self.date} à {self.h_debut} au batîment {self.nom_bat} {self.salle}>"


class Etudiant(db.Model):
    id_etudiant = db.Column(db.Integer, primary_key=True)
    nom_etudiant = db.Column(db.String(100), nullable=False)
    prenom_etudiant = db.Column(db.String(100), nullable=False)
    civilite_etudiant = db.Column(db.String(10))
    date_naissance = db.Column(db.Date, nullable=False)
    telephone_etudiant = db.Column(db.String(15))
    email_etudiant = db.Column(db.String(200))

    # 0,N
    promos = db.relationship('Promo',
                             secondary='appartenir',
                             backref=db.backref('etudiants', lazy='dynamic'))

    def __init__(self,
                 nom_etudiant,
                 prenom_etudiant,
                 civilite_etudiant,
                 date_naissance,
                 telephone_etudiant=None,
                 email_etudiant=None):
        self.nom_etudiant = nom_etudiant
        self.prenom_etudiant = prenom_etudiant
        self.civilite_etudiant = civilite_etudiant
        self.date_naissance = date_naissance
        self.telephone_etudiant = telephone_etudiant
        self.email_etudiant = email_etudiant

    def __repr__(self):
        return f"<Etudiant {self.nom_etudiant} {self.prenom_etudiant}>"


class Promo(db.Model):
    nom_promo = db.Column(db.String(100), primary_key=True)
    annee_promo = db.Column(db.Integer, primary_key=True)
    formation_promo = db.Column(db.String(100), nullable=False)

    # 0,1
    id_enseignant = db.Column(db.Integer,
                              db.ForeignKey("enseignant.id_enseignant"),
                              nullable=True)
    enseignant = db.relationship("Enseignant",
                                 backref=db.backref("promos", lazy="select"))

    def __init__(self, nom_promo, annee_promo, formation_promo):
        self.nom_promo = nom_promo
        self.annee_promo = annee_promo
        self.formation_promo = formation_promo

    def __repr__(self):
        return f"<Promo: {self.nom_promo} {self.annee_promo} {self.formation_promo}>"


class Appartenir(db.Model):
    id_etudiant = db.Column(db.Integer,
                            db.ForeignKey("etudiant.id_etudiant"),
                            primary_key=True)

    etudiant = db.relationship("Etudiant",
                               backref=db.backref("appartenirs",
                                                  lazy="joined",
                                                  overlaps="promos,etudiants"),
                               overlaps="promos,etudiants")

    nom_promo = db.Column(db.String(100), primary_key=True)
    annee_promo = db.Column(db.Integer, primary_key=True)

    regime_etudiant = db.Column(db.String(100))

    __table_args__ = (db.ForeignKeyConstraint(
        ['nom_promo', 'annee_promo'],
        ['promo.nom_promo', 'promo.annee_promo']),)

    def __init__(self, id_etudiant, nom_promo, annee_promo, regime_etudiant):
        self.id_etudiant = id_etudiant
        self.nom_promo = nom_promo
        self.annee_promo = annee_promo
        self.regime_etudiant = regime_etudiant

    def __repr__(self):
        return f"<Etudiant : {self.id_etudiant} appartient a {self.nom_promo} en {self.annee_promo}>"


class Enseignant(db.Model):
    id_enseignant = db.Column(db.Integer, primary_key=True)
    nom_enseignant = db.Column(db.String(100))
    prenom_enseignant = db.Column(db.String(100))
    civilite_enseignant = db.Column(db.String(10))
    email_enseignant = db.Column(db.String(200))

    def __init__(self, nom, prenom, civilite, email):
        self.nom_enseignant = nom
        self.prenom_enseignant = prenom
        self.civilite_enseignant = civilite
        self.email_enseignant = email

    def __repr__(self):
        return f"<Enseignant : {self.id_enseignant} {self.civilite_enseignant} {self.nom_enseignant} {self.prenom_enseignant} {self.email_enseignant}>"


class Jury(db.Model):
    id_jury = db.Column(db.Integer, primary_key=True)
    date_jury = db.Column(db.Date)
    h_jury = db.Column(db.String(5))
    duree_jury = db.Column(db.Integer)  # durée en minutes

    # 0,1
    id_soutenance = db.Column(db.Integer,
                              db.ForeignKey("soutenance.id_soutenance"),
                              unique=True,
                              nullable=True)
    soutenance = db.relationship("Soutenance",
                                 backref=db.backref("jury",
                                                    lazy="select",
                                                    uselist=False))

    def __init__(self, date_jury, heure_jury, duree_jury, id_soutenance=None):
        self.date_jury = date_jury
        self.h_jury = heure_jury
        self.duree_jury = duree_jury
        self.id_soutenance = id_soutenance

    def __repr__(self):
        return f"<Le jury pour la soutenance {self.id_soutenance} le {self.date_jury} a {self.heure_jury} pendant {self.duree_jury} minutes>"


class Composer(db.Model):
    # 0,N
    id_enseignant = db.Column(db.Integer,
                              db.ForeignKey("enseignant.id_enseignant"),
                              primary_key=True)
    enseignant = db.relationship("Enseignant",
                                 backref=db.backref("compositions",
                                                    lazy="dynamic"))

    # 0,N
    id_soutenance = db.Column(db.Integer,
                              db.ForeignKey("soutenance.id_soutenance"),
                              primary_key=True)
    soutenance = db.relationship("Soutenance",
                                 backref=db.backref("compositions",
                                                    lazy="dynamic"))

    def __init__(self, id_enseignant, id_soutenance):
        self.id_enseignant = id_enseignant
        self.id_soutenance = id_soutenance


class Tutorer(db.Model):
    annee = db.Column(db.Integer)
    # 0,N
    id_enseignant = db.Column(db.Integer,
                              db.ForeignKey("enseignant.id_enseignant"),
                              primary_key=True)
    enseignant = db.relationship("Enseignant",
                                 backref=db.backref("tutorats", lazy="dynamic"))

    # 0,N
    id_etudiant = db.Column(db.Integer,
                            db.ForeignKey("etudiant.id_etudiant"),
                            primary_key=True)
    etudiant = db.relationship("Etudiant",
                               backref=db.backref("tutorats", lazy="dynamic"))

    def __init__(self, id_enseignant, id_etudiant, annee):
        self.id_enseignant = id_enseignant
        self.id_etudiant = id_etudiant
        self.annee = annee
