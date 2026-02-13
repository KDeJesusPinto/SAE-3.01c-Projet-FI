def test_routes_enseignant(testapp):
    client = testapp.test_client()
    # Connexion enseignant
    client.post('/login/', data={'Login': 'jdubois', 'Password': 'prof1'}, follow_redirects=True)
    
    # Pages enseignant
    assert client.get('/enseignant/').status_code == 200
    assert client.get('/enseignant/planning/').status_code == 200
    assert client.get('/enseignant/soutenances/').status_code == 200
    assert client.get('/enseignant/liste+etu/').status_code == 200
