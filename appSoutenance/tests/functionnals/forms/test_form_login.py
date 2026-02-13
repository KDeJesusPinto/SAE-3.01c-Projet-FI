from hashlib import sha256
from datetime import datetime
from flask import Flask
from appSoutenance.forms import LoginForm
from appSoutenance.models import db, Enseignant, Etudiant, Admini


def test_login_form_enseignant_valid(testapp: Flask):
    """Test du formulaire de connexion avec des données valides enseignant"""

    with testapp.app_context():
        form = LoginForm(Login="jdubois", Password="prof1")
        user = form.get_authenticated_enseignant()
        assert user is not None
        assert user.login_enseignant == "jdubois"


def test_login_form_etudiant_valid(testapp: Flask):
    """Test du formulaire de connexion avec des données valides étudiant"""

    with testapp.app_context():
        form = LoginForm(Login="adupont", Password="pass1")
        user = form.get_authenticated_etudiant()
        assert user is not None
        assert user.login_etudiant == "adupont"


def test_login_form_admin_valid(testapp: Flask):
    """Test du formulaire de connexion avec des données valides admin"""

    with testapp.app_context():
        form = LoginForm(Login="aSoler", Password="aSolerpass")
        user = form.get_authenticated_admin()
        assert user is not None
        assert user.login_admin == "aSoler"



def test_login_form_enseignant_invalid_password(testapp: Flask):
    """Test du formulaire de connexion avec un mauvais mot de passe"""

    with testapp.app_context():
        form = LoginForm(Login="jdubois", Password="prof123")
        assert form.get_authenticated_enseignant() is None

def test_login_form_etudiant_invalid_password(testapp: Flask):
    """Test de l'authentification étudiant avec un mauvais mot de passe"""

    with testapp.app_context():
        form = LoginForm(Login="adupont", Password="mdp")
        assert form.get_authenticated_etudiant() is None

def test_login_form_admin_invalid_password(testapp: Flask):
    """Test de l'authentification admin avec un mauvais mot de passe"""

    with testapp.app_context():
        form = LoginForm(Login="aSoler", Password="mdp")
        assert form.get_authenticated_admin() is None



def test_login_form_etudiant_sha256(testapp: Flask):
    """Test du fallback SHA256 pour étudiant"""

    with testapp.app_context():
        mdp_clair = "secret123"
        h = sha256()
        h.update(mdp_clair.encode())
        mdp_hashe = h.hexdigest()

        nouveau_etu = Etudiant(
            nom_etudiant="Test",
            prenom_etudiant="Sha",
            civilite_etudiant="M.",
            date_naissance=datetime(2000, 1, 1).date(),
            login_etudiant="shaetu",
            pwd_etudiant=mdp_hashe,
        )
        db.session.add(nouveau_etu)
        db.session.flush()

        form = LoginForm(Login="shaetu", Password=mdp_clair)
        user = form.get_authenticated_etudiant()
        assert user is not None
        db.session.rollback()

def test_login_form_admin_sha256(testapp: Flask):
    """Test du fallback SHA256 pour admin"""

    with testapp.app_context():
        mdp_clair = "secret123"
        h = sha256()
        h.update(mdp_clair.encode())
        mdp_hashe = h.hexdigest()

        nouvel_admin = Admini(
            id_admin="A999",
            nom_admin="Test",
            prenom_admin="Sha",
            login_admin="shaadmin",
            pwd_admin=mdp_hashe,
        )
        db.session.add(nouvel_admin)
        db.session.flush()

        form = LoginForm(Login="shaadmin", Password=mdp_clair)
        user = form.get_authenticated_admin()
        assert user is not None
        db.session.rollback()

def test_login_form_enseignant_sha256(testapp: Flask):
    """Test du fallback SHA256 pour enseignant"""

    with testapp.app_context():
        mdp_clair = "secret123"
        h = sha256()
        h.update(mdp_clair.encode())
        mdp_hashe = h.hexdigest()

        nouveau_prof = Enseignant(
            nom="Test",
            prenom="Sha",
            civilite="M.",
            email="sha@test.fr",
            login_enseignant="shasuser",
            pwd_enseignant=mdp_hashe,
        )
        db.session.add(nouveau_prof)
        db.session.flush()

        form = LoginForm(Login="shasuser", Password=mdp_clair)
        user = form.get_authenticated_enseignant()
        assert user is not None
        db.session.rollback()



def test_login_form_etudiant_not_found(testapp: Flask):
    """Test de l'authentification étudiant avec un utilisateur inexistant"""

    with testapp.app_context():
        form = LoginForm(Login="inconnu", Password="mdp")
        assert form.get_authenticated_etudiant() is None

def test_login_form_admin_not_found(testapp: Flask):
    """Test de l'authentification admin avec un utilisateur inexistant"""

    with testapp.app_context():
        form = LoginForm(Login="inconnu", Password="mdp")
        assert form.get_authenticated_admin() is None

def test_login_form_enseignant_not_found(testapp: Flask):
    """Test de l'authentification enseignant avec un utilisateur inexistant"""

    with testapp.app_context():
        form = LoginForm(Login="inconnu", Password="mdp")
        user = form.get_authenticated_enseignant()
        assert user is None
