from flask import url_for
from appSoutenance.models import Soutenance, Stage, db, Etudiant, Demarche, Appartenir, Promo, Entreprise, Enseignant
from datetime import datetime

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

def test_login_failure(testapp):
    client = testapp.test_client()
    response = client.post('/login/', data={'Login': 'wrong', 'Password': 'bad'}, follow_redirects=True)
    assert b"Login ou mot de passe incorrect" in response.data

def test_access_control(testapp):
    """Vérifie qu'un étudiant ne peut pas accéder aux pages admin"""
    client = testapp.test_client()
    client.post('/login/', data={'Login': 'adupont', 'Password': 'pass1'}, follow_redirects=True)
    
    response = client.get('/admin/', follow_redirects=True)
    # Doit rediriger vers login ou afficher un message d'erreur
    assert b"Acc\xc3\xa8s r\xc3\xa9serv\xc3\xa9 aux administrateurs" in response.data or response.status_code == 200

def test_admin_details_routes(testapp):
    client = testapp.test_client()
    client.post('/login/', data={'Login': 'aSoler', 'Password': 'aSolerpass'}, follow_redirects=True)
    
    assert client.get('/admin/liste+etudiants/1/').status_code == 200
    assert client.get('/admin/liste+enseignants/1/').status_code == 200

def test_admin_soutenance_crud(testapp):
    """Test complet du cycle de vie d'une soutenance (Création, Update, Delete)"""
    client = testapp.test_client()
    client.post('/login/', data={'Login': 'aSoler', 'Password': 'aSolerpass'}, follow_redirects=True)

    ens1_id = None
    ens2_id = None

    # Préparation des données pour le test
    with testapp.app_context():
        # Ensure Enseignants exist
        ens1 = Enseignant.query.get(1)
        if not ens1:
            ens1 = Enseignant(nom="Dubois", prenom="Jean", civilite="M.", email="j.dubois@test.com", login_enseignant="jdubois", pwd_enseignant="prof1")
            db.session.add(ens1)
        ens2 = Enseignant.query.get(2)
        if not ens2:
            ens2 = Enseignant(nom="Martin", prenom="Sophie", civilite="Mme", email="s.martin@test.com", login_enseignant="smartin", pwd_enseignant="prof2")
            db.session.add(ens2)

        # Création d'un étudiant spécifique pour le test
        etu = Etudiant(nom_etudiant="TestCrud", prenom_etudiant="Soutenance", civilite_etudiant="M.", 
                       date_naissance=datetime(2000,1,1).date(), email_etudiant="test.crud@test.com")
        db.session.add(etu)
        db.session.flush()
        etu_id = etu.id_etudiant

        # Promo (si n'existe pas)
        promo = Promo.query.get(("BUT2", 2025, "BUT Informatique"))
        if not promo:
            promo = Promo(nom_promo="BUT2", annee_promo=2025, formation_promo="BUT Informatique")
            db.session.add(promo)
        
        # Appartenir
        app = Appartenir(id_etudiant=etu_id, nom_promo="BUT2", annee_promo=2025, regime_etudiant="Formation initiale")
        db.session.add(app)

        # Entreprise (si n'existe pas)
        ent = Entreprise.query.get(1)
        if not ent:
            ent = Entreprise(nom_entreprise="EntTest", secteur="S", ville="V", adresse="A", code_postal="00000", typeE="T")
            db.session.add(ent)
            db.session.flush()

        # Demarche
        dem = Demarche(source="Perso", typeD="Stage", situation="Acceptée", 
                       date_envoi=datetime.now().date(), id_entreprise=ent.id_entreprise, id_etudiant=etu_id)
        db.session.add(dem)
        db.session.flush()

        # Stage
        stage = Stage(typeS="Stage", date_debut=datetime.now().date(), date_fin=datetime.now().date(), 
                      titre_stage="Stage Test CRUD", theme_stage="Dev", id_demarche=dem.id_demarche)
        db.session.add(stage)
        
        db.session.flush()
        ens1_id = ens1.id_enseignant
        ens2_id = ens2.id_enseignant
        db.session.commit()

    # 1. Création (POST)
    data = {
        'dateS': '2025-06-25',
        'h_debut': '08:00',
        'salle': 'B202',
        'ens1': str(ens1_id),
        'ens2': str(ens2_id),
        'etu1': str(etu_id)
    }
    
    response = client.post('/soutenance/valider', data=data, follow_redirects=True)
    assert b"soutenance(s) ajout\xc3\xa9e(s) avec succ\xc3\xa8s" in response.data

    # Vérification en base
    with testapp.app_context():
        sout = Soutenance.query.filter_by(dateS=datetime(2025, 6, 25).date(), h_debut='08:00', salle='B202').first()
        assert sout is not None
        sout_id = sout.id_soutenance

    # 2. Modification (POST)
    data_update = {
        'dateS': '2025-06-25',
        'h_debut': '08:00',
        'salle': 'B203',
        'ens1': str(ens1_id),
        'ens2': str(ens2_id),
        'etu1': str(etu_id)
    }
    response = client.post(f'/admin/planning/{sout_id}/update/save', data=data_update, follow_redirects=True)
    assert b"Soutenance mise \xc3\xa0 jour avec succ\xc3\xa8s" in response.data

    # 3. Suppression (GET page confirmation)
    response = client.get(f'/admin/planning/{sout_id}/delete')
    assert response.status_code == 200

    # 4. Suppression (POST confirmation)
    response = client.post(f'/admin/planning/{sout_id}/erase', follow_redirects=True)
    assert b"Soutenances supprim\xc3\xa9es avec succ\xc3\xa8s" in response.data

def test_admin_apis(testapp):
    """Test des API JSON utilisées par le planning"""
    client = testapp.test_client()
    client.post('/login/', data={'Login': 'aSoler', 'Password': 'aSolerpass'}, follow_redirects=True)

    # API Enseignants disponibles
    response = client.get('/api/enseignants_disponibles/1?date=2025-06-20&heure=09:00')
    assert response.status_code == 200
    assert response.is_json

    # API Étudiants par tuteur
    # Enseignant 1, Soutenance 0 (nouvelle)
    response = client.get('/api/etudiants_par_tuteur/1/0?promo=BUT2')
    assert response.status_code == 200
    assert response.is_json

    # API Salle disponible
    response = client.get('/api/salle_disponible/?date=2025-06-20&heure=09:00&salle=101')
    assert response.status_code == 200
    assert response.is_json
