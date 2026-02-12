#test_model.py
from datetime import date
from appSoutenance.models import *


def test_entreprise_repr(testapp):
    with testapp.app_context():
        entreprise = Entreprise.query.get(1)
        expected = f"<Entreprise {entreprise.nom_entreprise} de type {entreprise.typeE} dans le secteur {entreprise.secteur} situé à {entreprise.ville} {entreprise.code_postal} {entreprise.adresse}. \nTel: {entreprise.tel_entreprise} \nEmail: {entreprise.email_entreprise}>"
        assert repr(entreprise) == expected


def test_demarche_repr(testapp):
    with testapp.app_context():
        demarche = Demarche.query.get(1)
        expected = f"<Demarche {demarche.id_demarche} de type {demarche.typeD} envoyée le {demarche.date_envoi} pour l'entreprise {demarche.entreprise.nom_entreprise}. Situation actuelle: {demarche.situation}>"
        assert repr(demarche) == expected

def test_stage_repr(testapp):
    with testapp.app_context():
        stage = Stage.query.get(1)
        expected = f"<Stage {stage.titre_stage} de type {stage.typeS} débutant le {stage.date_debut} et se terminant le {stage.date_fin}>"
        assert repr(stage) == expected

def test_maitre_stage_repr(testapp):
    with testapp.app_context():
        maitre_stage = MaitreStage.query.get(1)
        expected = f"<{maitre_stage.civilite_maitre} {maitre_stage.nom_maitre} {maitre_stage.prenom_maitre} est le maitre de stage>"
        assert repr(maitre_stage) == expected

def test_soutenance_repr(testapp):
    with testapp.app_context():
        soutenance = Soutenance.query.get(1)
        expected = f"<La soutenance a lieu le {soutenance.dateS} à {soutenance.h_debut} au batîment {soutenance.nom_bat} {soutenance.salle}>"
        assert repr(soutenance) == expected

def test_etudiant_repr(testapp):
    with testapp.app_context():
        etudiant = Etudiant.query.get(1)
        expected = f"<Etudiant {etudiant.nom_etudiant} {etudiant.prenom_etudiant}>"
        assert repr(etudiant) == expected

def test_promo_repr(testapp):
    with testapp.app_context():
        promo = db.session.get(Promo, ('BUT2', 2025, 'BUT Informatique'))

        assert promo is not None, "La promo n'a pas été trouvée dans la base de test"
        expected = f"<Promo: {promo.nom_promo} {promo.annee_promo} {promo.formation_promo}>"
        assert repr(promo) == expected

def test_appartenir_repr(testapp):
    with testapp.app_context():
        appartenir = db.session.get(Appartenir, (1, "BUT Informatique", 2025))
        if appartenir:
            expected = f"<Etudiant : {appartenir.id_etudiant} appartient a {appartenir.nom_promo} en {appartenir.annee_promo}>"
            assert repr(appartenir) == expected

def test_enseignant_repr(testapp):
    with testapp.app_context():
        enseignant = Enseignant.query.get(1)
        expected = f"<Enseignant : {enseignant.id_enseignant} {enseignant.civilite_enseignant} {enseignant.nom_enseignant} {enseignant.prenom_enseignant} {enseignant.email_enseignant}>"
        assert repr(enseignant) == expected

def test_jury_repr(testapp):
    with testapp.app_context():
        jury = Jury.query.get(1)
        expected = f"<Le jury pour la soutenance {jury.id_soutenance} le {jury.date_jury} a {jury.h_jury} pendant {jury.duree} minutes>"
        assert repr(jury) == expected

def test_admini_repr(testapp):
    with testapp.app_context():
        admini = db.session.get(Admini, "A001")
        expected = f"<Admininistration : {admini.id_admin} {admini.nom_admin} {admini.prenom_admin} {admini.login_admin}>"
        assert repr(admini) == expected