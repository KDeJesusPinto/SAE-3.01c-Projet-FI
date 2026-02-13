from flask import url_for

def test_routes_public(testapp):
    client = testapp.test_client()
    # Page d'accueil / Connexion
    assert client.get('/').status_code == 200
    assert client.get('/connexion/').status_code == 200
    assert client.get('/login/').status_code == 200

def test_routes_etudiant(testapp):
    client = testapp.test_client()
    # Connexion étudiant
    client.post('/login/', data={'Login': 'adupont', 'Password': 'pass1'}, follow_redirects=True)
    
    # Pages étudiant
    assert client.get('/etudiant/').status_code == 200
    # On suppose que l'étudiant 1 existe (chargé par loaddb)
    assert client.get('/etudiant/demarches/?num_personne=1').status_code == 200
    assert client.get('/etudiant/stage/?num_personne=1').status_code == 200
    assert client.get('/etudiant/demarches/new1/?num_personne=1').status_code == 200
    assert client.get('/etudiant/demarches/resume/?num_personne=1').status_code == 200

def test_routes_enseignant(testapp):
    client = testapp.test_client()
    # Connexion enseignant
    client.post('/login/', data={'Login': 'jdubois', 'Password': 'prof1'}, follow_redirects=True)
    
    # Pages enseignant
    assert client.get('/enseignant/').status_code == 200
    assert client.get('/enseignant/planning/').status_code == 200
    assert client.get('/enseignant/soutenances/').status_code == 200
    assert client.get('/enseignant/liste+etu/').status_code == 200

def test_routes_admin(testapp):
    client = testapp.test_client()
    # Connexion admin
    client.post('/login/', data={'Login': 'aSoler', 'Password': 'aSolerpass'}, follow_redirects=True)
    
    # Pages admin
    assert client.get('/admin/').status_code == 200
    assert client.get('/admin/planning/').status_code == 200
    assert client.get('/admin/planning/but2').status_code == 200
    assert client.get('/admin/planning/but3').status_code == 200
    assert client.get('/admin/liste+enseignants/').status_code == 200
    assert client.get('/admin/liste+etudiants/').status_code == 200
    assert client.get('/admin/liste+soutenances+candides/').status_code == 200
    assert client.get('/admin/planning/creation_soutenance/').status_code == 200
