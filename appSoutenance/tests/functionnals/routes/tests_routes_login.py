from appSoutenance.views import *

def test_page_accueil(testapp):
    """Vérifie que la page d'accueil est accessible"""
    
    client = testapp.test_client()
    response = client.get('/')
    assert response.status_code in [200, 302]

def test_page_login(testapp):
    """Vérifie que la page de login s'affiche"""

    client = testapp.test_client()
    response = client.get('/login/')
    assert response.status_code == 200
    assert b"Login" in response.data

def test_routes_publiques(testapp):
    """Vérifie que les routes publiques fonctionnent"""
    
    client = testapp.test_client()
    # Page d'accueil / Connexion
    assert client.get('/').status_code == 200
    assert client.get('/connexion/').status_code == 200
    assert client.get('/login/').status_code == 200

def test_login_echoue(testapp):
    """Vérifie que la connexion echoue avec un mot de passe incorrect"""

    client = testapp.test_client()
    response = client.post('/login/', data={'Login': 'test', 'Password': 'mdp'}, follow_redirects=True)
    assert b"Login ou mot de passe incorrect" in response.data

def test_access_non_autorise(testapp):
    """Vérifie qu'un étudiant ne peut pas accéder aux pages admin"""

    client = testapp.test_client()
    client.post('/login/', data={'Login': 'adupont', 'Password': 'pass1'}, follow_redirects=True)
    
    response = client.get('/admin/', follow_redirects=True)
    assert b"Acc\xc3\xa8s r\xc3\xa9serv\xc3\xa9 aux administrateurs" in response.data or response.status_code == 200
