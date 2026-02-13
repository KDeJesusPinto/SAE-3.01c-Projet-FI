from datetime import date
from appSoutenance.models import *

def test_new_entreprise_creation(testapp):
    """Vérifie la création manuelle d'une entreprise"""
    
    with testapp.app_context():
        new_ent = Entreprise(
            nom_entreprise="Test Corp",
            secteur="Informatique",
            ville="Orléans",
            adresse="1 rue du test",
            code_postal="45000",
            typeE="PME"
        )
        db.session.add(new_ent)
        db.session.commit()
        assert new_ent.id_entreprise is not None
        assert new_ent.nom_entreprise == "Test Corp"

def test_new_maitre_stage_creation(testapp):
    """Vérifie la création manuelle d'un maître de stage"""

    with testapp.app_context():
        new_maitre = MaitreStage(
            civilite_maitre="M.",
            nom_maitre="Dupont",
            prenom_maitre="Jean",
            email_maitre="jean.dupont@test.com",
            id_entreprise=1
        )
        db.session.add(new_maitre)
        db.session.commit()
        assert new_maitre.id_maitre is not None

def test_new_promo_creation(testapp):
    """Vérifie la création manuelle d'une promo"""
    
    with testapp.app_context():
        new_promo = Promo("BUT Test", 2030, "Informatique")
        db.session.add(new_promo)
        db.session.commit()
        assert new_promo.nom_promo == "BUT Test"

def test_new_tutorer_creation(testapp):
    """Vérifie la création d'une relation de tutorat"""

    with testapp.app_context():
        etu = Etudiant(
            nom_etudiant="TestTutorat",
            prenom_etudiant="Jean",
            civilite_etudiant="M.",
            date_naissance=date(2000, 1, 1),
            email_etudiant="jean.testtutorat@example.com"
        )
        db.session.add(etu)
        db.session.flush()

        tut = Tutorer(id_enseignant=1, id_etudiant=etu.id_etudiant, annee=2025)
        db.session.add(tut)
        db.session.commit()
        assert tut.id_enseignant == 1

def test_new_enseignant_creation(testapp):
    """Vérifie la création manuelle d'un enseignant"""

    with testapp.app_context():
        ens = Enseignant("Nom", "Prenom", "M.", "email@test.com", "login", "pwd")
        db.session.add(ens)
        db.session.commit()
        assert ens.id_enseignant is not None

def test_new_assembler_creation(testapp):
    """Vérifie la création d'une relation Assembler (Jury-Admin)"""

    with testapp.app_context():
        # Admin A001 et Jury 1 existent via loaddb
        assembler = Assembler(id_jury=1, id_admin="A001")
        db.session.add(assembler)
        db.session.commit()
        assert assembler.id_jury == 1