from appSoutenance.views import *

def test_home_page(testapp):
    """Vérifie que la page d'accueil est accessible"""
    client = testapp.test_client()
    response = client.get('/')
    assert response.status_code in [200, 302]

def test_login_page_loads(testapp):
    """Vérifie que la page de login s'affiche"""
    client = testapp.test_client()
    response = client.get('/login/')
    assert response.status_code == 200
    assert b"Login" in response.data