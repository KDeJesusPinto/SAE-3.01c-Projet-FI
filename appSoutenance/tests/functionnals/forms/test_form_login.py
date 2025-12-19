from flask import Flask
from appSoutenance.forms import LoginForm

def test_login_form_valid(testapp: Flask):
    """Test du formulaire de connexion avec des données valides"""

    with testapp.app_context():
        form = LoginForm(
            Login='jdubois',
            Password='prof1'
        )
        
        user = form.get_authenticated_enseignant()
        assert user is not None
        assert user.login_enseignant == 'jdubois'


def test_login_form_invalid_password(testapp: Flask):
    """Test du formulaire de connexion avec un mauvais mot de passe"""

    with testapp.app_context():
        form = LoginForm(
            Login='jdubois',
            Password='prof123'
        )
        
        user = form.get_authenticated_enseignant()
        assert user is None


def test_login_form_user_not_found(testapp: Flask):
    """Test du formulaire de connexion avec un utilisateur inexistant"""

    with testapp.app_context():
        form = LoginForm(
            Login='utilisateur_inexistant',
            Password='mdp'
        )
        
        user = form.get_authenticated_enseignant()
        assert user is None
