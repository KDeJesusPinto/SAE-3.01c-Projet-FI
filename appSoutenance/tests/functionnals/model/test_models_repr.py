#test_model.py
from datetime import date
from appSoutenance.models import *

def test_load_user(testapp):
    """Test de la fonction load_user"""

    with testapp.app_context():
        user_etu = load_user("ETU_1")
        assert user_etu is not None 
        assert isinstance(user_etu, Etudiant)
        assert user_etu.get_id() == "ETU_1"

        user_ens = load_user("ENS_1")
        assert user_ens is not None
        assert isinstance(user_ens, Enseignant)
        assert user_ens.get_id() == "ENS_1"

        user_adm = load_user("ADM_A001")
        assert user_adm is not None
        assert isinstance(user_adm, Admini)
        assert user_adm.get_id() == "ADM_A001"

        assert load_user("INVALIDE_123") is None
        assert load_user("123") is None

    

def test_entreprise_repr(testapp):
    """Test de la représentation de l'objet Entreprise"""

    with testapp.app_context():
        entreprise = Entreprise.query.get(1)
        expected = f"<Entreprise {entreprise.nom_entreprise} de type {entreprise.typeE} dans le secteur {entreprise.secteur} situé à {entreprise.ville} {entreprise.code_postal} {entreprise.adresse}. \nTel: {entreprise.tel_entreprise} \nEmail: {entreprise.email_entreprise}>"
        assert repr(entreprise) == expected


def test_demarche_repr(testapp):
    """Test de la représentation de l'objet Démarche"""

    with testapp.app_context():
        demarche = Demarche.query.get(1)
        expected = f"<Demarche {demarche.id_demarche} de type {demarche.typeD} envoyée le {demarche.date_envoi} pour l'entreprise {demarche.entreprise.nom_entreprise}. Situation actuelle: {demarche.situation}>"
        assert repr(demarche) == expected

def test_stage_repr(testapp):
    """Test de la représentation de l'objet Stage"""

    with testapp.app_context():
        stage = Stage.query.get(1)
        expected = f"<Stage {stage.titre_stage} de type {stage.typeS} débutant le {stage.date_debut} et se terminant le {stage.date_fin}>"
        assert repr(stage) == expected

def test_maitre_stage_repr(testapp):
    """Test de la représentation de l'objet MaitreStage"""

    with testapp.app_context():
        maitre_stage = MaitreStage.query.get(1)
        expected = f"<{maitre_stage.civilite_maitre} {maitre_stage.nom_maitre} {maitre_stage.prenom_maitre} est le maitre de stage>"
        assert repr(maitre_stage) == expected

def test_soutenance_repr(testapp):
    """Test de la représentation de l'objet Soutenance"""

    with testapp.app_context():
        soutenance = Soutenance.query.get(1)
        expected = f"<La soutenance a lieu le {soutenance.dateS} à {soutenance.h_debut} au batiment {soutenance.nom_bat} {soutenance.salle}>"
        assert repr(soutenance) == expected

def test_etudiant_repr(testapp):
    """Test de la représentation de l'objet Etudiant"""

    with testapp.app_context():
        etudiant = Etudiant.query.get(1)
        expected = f"<Etudiant {etudiant.nom_etudiant} {etudiant.prenom_etudiant}>"
        assert repr(etudiant) == expected

def test_promo_repr(testapp):
    """Test de la représentation de l'objet Promo"""

    with testapp.app_context():
        promo = db.session.get(Promo, ('BUT2', 2025, 'BUT Informatique'))

        assert promo is not None, "La promo n'a pas été trouvée dans la base de test"
        expected = f"<Promo: {promo.nom_promo} {promo.annee_promo} {promo.formation_promo}>"
        assert repr(promo) == expected

def test_appartenir_repr(testapp):
    """Test de la représentation de l'objet Appartenir"""

    with testapp.app_context():
        appartenir = db.session.get(Appartenir, (1, "BUT2", 2025))
        if appartenir:
            expected = f"<Etudiant : {appartenir.id_etudiant} appartient a {appartenir.nom_promo} en {appartenir.annee_promo}>"
            assert repr(appartenir) == expected

def test_enseignant_repr(testapp):
    """Test de la représentation de l'objet Enseignant"""

    with testapp.app_context():
        enseignant = Enseignant.query.get(1)
        expected = f"<Enseignant : {enseignant.id_enseignant} {enseignant.civilite_enseignant} {enseignant.nom_enseignant} {enseignant.prenom_enseignant} {enseignant.email_enseignant}>"
        assert repr(enseignant) == expected

def test_jury_repr(testapp):
    """Test de la représentation de l'objet Jury"""

    with testapp.app_context():
        jury = Jury.query.get(1)
        expected = f"<Le jury pour la soutenance {jury.id_soutenance} le {jury.date_jury} a {jury.h_jury} pendant {jury.duree} minutes>"
        assert repr(jury) == expected

def test_admini_repr(testapp):
    """Test de la représentation de l'objet Admini"""

    with testapp.app_context():
        admini = db.session.get(Admini, "A001")
        expected = f"<Admininistration : {admini.id_admin} {admini.nom_admin} {admini.prenom_admin} {admini.login_admin}>"
        assert repr(admini) == expected


def test_user_get_id(testapp):
    """Vérifie que get_id() retourne le préfixe correct pour chaque type"""

    with testapp.app_context():
        etu = db.session.get(Etudiant, 1)
        assert etu.get_id() == f"ETU_{etu.id_etudiant}"

        ens = db.session.get(Enseignant, 1)
        assert ens.get_id() == f"ENS_{ens.id_enseignant}"

        adm = db.session.get(Admini, "A001")
        assert adm.get_id() == f"ADM_{adm.id_admin}"


def test_entreprise_demarches_relationship(testapp):
    """Vérifie la relation Entreprise <--> Démarche"""

    with testapp.app_context():
        ent = db.session.get(Entreprise, 1)
        assert hasattr(ent, 'demarches')
        if ent.demarches:
            assert ent.demarches[0].id_entreprise == ent.id_entreprise

def test_etudiant_promo_relationship(testapp):
    """Vérifie la relation Étudiant <--> Promo via Appartenir"""
    
    with testapp.app_context():
        etu = db.session.get(Etudiant, 1)
        assert hasattr(etu, 'appartenirs')
        assert hasattr(etu, 'promos')