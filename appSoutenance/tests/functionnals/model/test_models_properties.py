from datetime import datetime
from appSoutenance.models import db, Soutenance, Enseignant, Composer, Stage, Demarche, Etudiant, Appartenir, Promo, Entreprise, Tutorer

def test_soutenance_properties_and_init(testapp):
    """Test des propriétés de Soutenance et des constructeurs manquants"""

    with testapp.app_context():
        # 1. Setup Enseignants
        ens1 = Enseignant(nom="Prof1", prenom="P1", civilite="M.", email="p1@test.com", login_enseignant="p1", pwd_enseignant="pass")
        ens2 = Enseignant(nom="Prof2", prenom="P2", civilite="M.", email="p2@test.com", login_enseignant="p2", pwd_enseignant="pass")
        db.session.add_all([ens1, ens2])
        
        # 2. Setup Etudiant & Promo
        etu = Etudiant(nom_etudiant="Etu", prenom_etudiant="P", civilite_etudiant="M.", date_naissance=datetime(2000,1,1).date(), email_etudiant="e@test.com")
        db.session.add(etu)
        db.session.flush()
        
        promo = Promo(nom_promo="BUT2-Test", annee_promo=2025, formation_promo="Info")
        db.session.add(promo)
        
        app = Appartenir(id_etudiant=etu.id_etudiant, nom_promo="BUT2-Test", annee_promo=2025, regime_etudiant="FI")
        db.session.add(app)
        
        # 3. Setup Stage
        ent = Entreprise(nom_entreprise="EntTest", secteur="S", ville="V", adresse="A", code_postal="00000", typeE="T")
        db.session.add(ent)
        db.session.flush()
        
        dem = Demarche(source="S", typeD="Stage", situation="A", date_envoi=datetime.now().date(), id_entreprise=ent.id_entreprise, id_etudiant=etu.id_etudiant)
        db.session.add(dem)
        db.session.flush()
        
        st = Stage(typeS="Stage", date_debut=datetime.now().date(), date_fin=datetime.now().date(), titre_stage="T", theme_stage="Th", id_demarche=dem.id_demarche)
        db.session.add(st)
        db.session.flush()
        
        # 4. Test Soutenance Init with h_fin
        sout = Soutenance(salle=101, dateS=datetime.now().date(), h_debut="10:00", id_stage=st.id_stage, h_fin="11:00", nom_bat="B")
        db.session.add(sout)
        db.session.commit()
        
        assert sout.h_fin == "11:00"
        
        # 5. Test jury_noms property
        assert sout.jury_noms == "Jury non assigné"
        
        c1 = Composer(id_enseignant=ens1.id_enseignant, id_soutenance=sout.id_soutenance)
        c2 = Composer(id_enseignant=ens2.id_enseignant, id_soutenance=sout.id_soutenance)
        db.session.add_all([c1, c2])
        db.session.commit()
        
        assert "Prof1 P1" in sout.jury_noms
        
        # 6. Test nom_promo property
        assert sout.nom_promo == "BUT2-Test"
        
        db.session.delete(app)
        db.session.commit()
        db.session.expire(etu)
        db.session.expire(sout)
        
        assert sout.nom_promo == "N/C"

        # 7. Test branche N/C finale
        sout_orphan = Soutenance(salle=102, dateS=datetime.now().date(), h_debut="14:00", id_stage=999999)
        assert sout_orphan.nom_promo == "N/C"

def test_tutorer_init(testapp):
    """Test de l'initialisation de Tutorer pour couvrir __init__"""
    with testapp.app_context():
        # Création d'un enseignant et d'un étudiant pour le test
        ens = Enseignant(nom="ProfT", prenom="T", civilite="M.", email="pt@test.com", login_enseignant="pt", pwd_enseignant="pass")
        db.session.add(ens)
        
        etu = Etudiant(nom_etudiant="EtuT", prenom_etudiant="T", civilite_etudiant="M.", date_naissance=datetime(2000,1,1).date(), email_etudiant="et@test.com")
        db.session.add(etu)
        db.session.commit()

        tut = Tutorer(id_enseignant=ens.id_enseignant, id_etudiant=etu.id_etudiant, annee=2025)
        db.session.add(tut)
        db.session.commit()

        assert tut.id_enseignant == ens.id_enseignant
        assert tut.id_etudiant == etu.id_etudiant
        assert tut.annee == 2025
