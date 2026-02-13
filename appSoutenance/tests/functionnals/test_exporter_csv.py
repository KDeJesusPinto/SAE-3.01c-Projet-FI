import io
import csv
from datetime import datetime
from flask import Flask
from appSoutenance.exporter_csv import exporter_etudiants, exporter_entreprises, exporter_soutenances
from appSoutenance.models import db, Etudiant, Entreprise, Soutenance, Stage, Demarche, Appartenir, Promo, Enseignant, Composer, Jury

def test_exporter_etudiants_success(testapp: Flask):
    """Test de l'exportation réussie des étudiants"""

    with testapp.app_context():
        # Nettoyage de la base
        db.session.query(Appartenir).delete()
        db.session.query(Etudiant).delete()
        db.session.query(Promo).delete()
        db.session.commit()

        e = Etudiant(nom_etudiant="Dupont", prenom_etudiant="Jean", email_etudiant="jean.dupont@test.fr", 
                     date_naissance=datetime(2000, 1, 1).date(), civilite_etudiant="M.")
        db.session.add(e)
        db.session.flush()
        
        p = Promo(nom_promo="BUT2", annee_promo=2024, formation_promo="Informatique")
        db.session.add(p)
        
        app = Appartenir(id_etudiant=e.id_etudiant, nom_promo="BUT2", annee_promo=2024, regime_etudiant="Formation initiale")
        db.session.add(app)
        db.session.commit()

        output = exporter_etudiants()
        content = output.getvalue()
        reader = csv.reader(io.StringIO(content), delimiter=';')
        rows = list(reader)

        assert len(rows) == 2
        assert rows[0] == ['ID', 'Nom', 'Prénom', 'Email', 'Promo', 'Année', 'Régime']
        assert rows[1][1] == "Dupont"
        assert rows[1][4] == "BUT2"
        
        db.session.rollback()

def test_exporter_etudiants_empty(testapp: Flask):
    """Test de l'exportation quand il n'y a pas d'étudiants"""

    with testapp.app_context():
        # Nettoyage de la base
        db.session.query(Appartenir).delete()
        db.session.query(Etudiant).delete()
        db.session.commit()

        output = exporter_etudiants()
        content = output.getvalue()
        reader = csv.reader(io.StringIO(content), delimiter=';')
        rows = list(reader)
        assert len(rows) == 1
        db.session.rollback()

def test_exporter_entreprises_success(testapp: Flask):
    """Test de l'exportation réussie des entreprises"""

    with testapp.app_context():
        # Nettoyage de la base
        db.session.query(Entreprise).delete()
        db.session.commit()

        ent = Entreprise(nom_entreprise="TechCorp", secteur="Informatique", ville="Orléans", 
                         adresse="1 rue de la Paix", code_postal="45000", typeE="PME")
        db.session.add(ent)
        db.session.commit()

        output = exporter_entreprises()
        content = output.getvalue()
        reader = csv.reader(io.StringIO(content), delimiter=';')
        rows = list(reader)

        assert len(rows) == 2
        assert rows[0] == ['ID', 'Nom', 'Ville', 'Adresse', 'CP', 'Secteur', 'Type', 'Tel', 'Email']
        assert rows[1][1] == "TechCorp"
        assert rows[1][2] == "Orléans"
        
        db.session.rollback()

def test_exporter_soutenances_success(testapp: Flask):
    """Test de l'exportation réussie des soutenances"""

    with testapp.app_context():
        # Nettoyage de la base
        db.session.query(Composer).delete()
        db.session.query(Jury).delete()
        db.session.query(Soutenance).delete()
        db.session.query(Stage).delete()
        db.session.query(Demarche).delete()
        db.session.query(Appartenir).delete()
        db.session.query(Etudiant).delete()
        db.session.query(Promo).delete()
        db.session.query(Entreprise).delete()
        db.session.query(Enseignant).delete()
        db.session.commit()

        e = Etudiant(nom_etudiant="Martin", prenom_etudiant="Alice", email_etudiant="alice@test.fr", 
                     date_naissance=datetime(2000, 1, 1).date(), civilite_etudiant="Mme")
        db.session.add(e)
        db.session.flush()
        
        ent = Entreprise(nom_entreprise="Ent", secteur="S", ville="V", adresse="A", code_postal="00", typeE="T")
        db.session.add(ent)
        db.session.flush()
        
        d = Demarche(source="Test", typeD="Stage", situation="Acceptée", date_envoi=datetime.now().date(), 
                     id_entreprise=ent.id_entreprise, id_etudiant=e.id_etudiant)
        db.session.add(d)
        db.session.flush()
        
        st = Stage(typeS="Stage", date_debut=datetime.now().date(), date_fin=datetime.now().date(), 
                   titre_stage="Développement Web", theme_stage="Web", id_demarche=d.id_demarche)
        db.session.add(st)
        db.session.flush()
        
        sout = Soutenance(salle=101, dateS=datetime(2024, 6, 15).date(), h_debut="14:00", id_stage=st.id_stage)
        db.session.add(sout)
        db.session.flush()
        
        ens1 = Enseignant(nom="Durand", prenom="Paul", civilite="M.", email="paul@test.fr", 
                          login_enseignant="pdurand", pwd_enseignant="hash")
        ens2 = Enseignant(nom="Dupond", prenom="Pierre", civilite="M.", email="pierre@test.fr", 
                          login_enseignant="pdupond", pwd_enseignant="hash")
        db.session.add(ens1)
        db.session.add(ens2)
        db.session.flush()
        
        comp1 = Composer(id_enseignant=ens1.id_enseignant, id_soutenance=sout.id_soutenance)
        comp2 = Composer(id_enseignant=ens2.id_enseignant, id_soutenance=sout.id_soutenance)
        db.session.add(comp1)
        db.session.add(comp2)
        db.session.commit()

        output = exporter_soutenances()
        content = output.getvalue()
        reader = csv.reader(io.StringIO(content), delimiter=';')
        rows = list(reader)

        assert len(rows) == 2
        assert rows[0] == ['ID', 'Date', 'Heure', 'Salle', 'Etudiant', 'Titre Stage', 'Jury']
        assert rows[1][4] == "Martin Alice"
        assert rows[1][5] == "Développement Web"
        assert "Durand Paul" in rows[1][6]
        assert "Dupond Pierre" in rows[1][6]
        assert ", " in rows[1][6]
        
        db.session.rollback()

def test_exporter_soutenances_no_jury(testapp: Flask):
    """Test de l'exportation d'une soutenance sans jury"""

    with testapp.app_context():
        db.session.query(Composer).delete()
        db.session.query(Soutenance).delete()
        db.session.query(Stage).delete()
        db.session.commit()
        
        sout = Soutenance(salle=202, dateS=datetime(2024, 6, 20).date(), h_debut="10:00", id_stage=999)
        db.session.add(sout)
        db.session.commit()

        output = exporter_soutenances()
        rows = list(csv.reader(io.StringIO(output.getvalue()), delimiter=';'))
        
        assert rows[-1][4] == "NC"
        assert rows[-1][5] == "NC"
        assert rows[-1][6] == ""
        db.session.rollback()

def test_exporter_soutenances_partial_data(testapp: Flask):
    """Test de l'exportation avec un stage sans étudiant"""
    
    with testapp.app_context():
        # Nettoyage
        db.session.query(Composer).delete()
        db.session.query(Soutenance).delete()
        db.session.query(Stage).delete()
        db.session.query(Demarche).delete()
        db.session.query(Entreprise).delete()
        db.session.commit()

        ent = Entreprise(nom_entreprise="E", secteur="S", ville="V", adresse="A", code_postal="0", typeE="T")
        db.session.add(ent)
        db.session.flush()

        d = Demarche(source="T", typeD="S", situation="A", date_envoi=datetime.now().date(), 
                     id_entreprise=ent.id_entreprise, id_etudiant=999)
        db.session.add(d)
        db.session.flush()

        st = Stage(typeS="S", date_debut=datetime.now().date(), date_fin=datetime.now().date(), 
                   titre_stage="Stage Test", theme_stage="Web", id_demarche=d.id_demarche)
        db.session.add(st)
        db.session.flush()

        sout = Soutenance(salle=303, dateS=datetime(2024, 1, 1).date(), h_debut="09:00", id_stage=st.id_stage)
        db.session.add(sout)
        db.session.commit()

        output = exporter_soutenances()
        rows = list(csv.reader(io.StringIO(output.getvalue()), delimiter=';'))
        
        assert rows[-1][4] == "NC"
        assert rows[-1][5] == "Stage Test"
        db.session.rollback()
