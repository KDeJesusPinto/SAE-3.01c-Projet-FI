from appSoutenance.models import Etudiant
from datetime import datetime

def test_routes_etudiant(testapp):
    client = testapp.test_client()
    # Connexion étudiant
    client.post('/login/', data={'Login': 'adupont', 'Password': 'pass1'}, follow_redirects=True)

    assert client.get('/etudiant/').status_code == 200
    assert client.get('/etudiant/soutenances/').status_code == 200
    assert client.get('/etudiant/soutenances/1/').status_code == 200