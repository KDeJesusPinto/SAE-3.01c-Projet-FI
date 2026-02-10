import io
from datetime import datetime
from flask import Flask
from appSoutenance.importer_csv import importer_etudiants_stages, importer_entreprises
from appSoutenance.models import db, Etudiant, Entreprise


def test_importer_etudiants_stages_success(testapp: Flask):
    """Test de l'importation réussie d'étudiants depuis un CSV"""

    with testapp.app_context():
        contenu = (
            "mail_etu,nom_stagiaire,prenom_stagiaire,civilite_stagiaire\n"
            "jean.dupont@etu.univ-orleans.fr,Dupont,Jean,M.\n"
            "marie.curie@etu.univ-orleans.fr,Curie,Marie,Mme\n"
        )
        fichier = io.BytesIO(contenu.encode("utf-8"))

        succes, message = importer_etudiants_stages(fichier)

        assert succes is True
        assert "2 lignes traitées" in message

        etu = Etudiant.query.filter_by(
            email_etudiant="jean.dupont@etu.univ-orleans.fr"
        ).first()
        assert etu is not None
        assert etu.nom_etudiant == "Dupont"

        db.session.rollback()


def test_importer_etudiants_stages_invalid_format(testapp: Flask):
    """Test de l'importation avec un format de colonnes incorrect"""

    with testapp.app_context():
        contenu = "nom_stagiaire,prenom_stagiaire\nDoe,John\n"
        fichier = io.BytesIO(contenu.encode("utf-8"))

        succes, message = importer_etudiants_stages(fichier)

        assert succes is False
        assert "Format CSV invalide" in message
        db.session.rollback()


def test_importer_etudiants_stages_empty_email(testapp: Flask):
    """Test de l'importation avec un email manquant"""
    
    with testapp.app_context():
        contenu = "mail_etu,nom_stagiaire,prenom_stagiaire,civilite_stagiaire\n,N/C,Jean,M.\n"
        fichier = io.BytesIO(contenu.encode("utf-8"))
        succes, message = importer_etudiants_stages(fichier)
        assert succes is True
        assert "0 lignes traitées" in message
        db.session.rollback()


def test_importer_etudiants_stages_existing_student(testapp: Flask):
    """Test de l'importation d'un étudiant déjà existant"""

    with testapp.app_context():
        email = "test@test.fr"
        etu = Etudiant(
            nom_etudiant="Existant",
            prenom_etudiant="Test",
            email_etudiant=email,
            date_naissance=datetime(2000, 1, 1).date(),
            civilite_etudiant="M.",
        )
        db.session.add(etu)
        db.session.commit()

        contenu = f"mail_etu,nom_stagiaire,prenom_stagiaire,civilite_stagiaire\n{email},Existant,Test,M.\n"
        fichier = io.BytesIO(contenu.encode("utf-8"))
        succes, message = importer_etudiants_stages(fichier)

        assert succes is True
        assert "1 lignes traitées" in message
        assert Etudiant.query.filter_by(email_etudiant=email).count() == 1
        db.session.rollback()


def test_importer_etudiants_stages_exception(testapp: Flask):
    """Test de la gestion d'erreur lors de l'importation"""

    with testapp.app_context():
        succes, message = importer_etudiants_stages(None)
        assert succes is False
        assert message is not None
        db.session.rollback()


def test_importer_entreprises_success(testapp: Flask):
    """Test de l'importation réussie d'entreprises"""

    with testapp.app_context():
        contenu = (
            "service_adm_nom_service,service_adm_ville_service,service_adm_adr1_service,service_adm_cp_service\n"
            "TECH SOLUTIONS,ORLEANS,12 Rue de la Paix,45000\n"
        )
        fichier = io.BytesIO(contenu.encode("utf-8"))

        succes, message = importer_entreprises(fichier)

        assert succes is True
        assert "1 entreprises ajoutées" in message

        ent = Entreprise.query.filter_by(nom_entreprise="Tech Solutions").first()
        assert ent is not None
        assert ent.ville == "Orleans"

        db.session.rollback()


def test_importer_entreprises_doublon(testapp: Flask):
    """Vérifie que l'importation ne crée pas de doublons pour les entreprises"""

    with testapp.app_context():
        ent_existante = Entreprise(
            nom_entreprise="Deja La",
            ville="Orleans",
            adresse="Rue test",
            code_postal="45000",
            secteur="NC",
            typeE="NC",
        )
        db.session.add(ent_existante)
        db.session.commit()

        contenu = "service_adm_nom_service,service_adm_ville_service\nDEJA LA,ORLEANS\n"
        fichier = io.BytesIO(contenu.encode("utf-8"))

        succes, message = importer_entreprises(fichier)

        assert succes is True
        assert "0 entreprises ajoutées" in message
        db.session.rollback()


def test_importer_entreprises_empty_name(testapp: Flask):
    """Test de l'importation d'une entreprise sans nom"""

    with testapp.app_context():
        contenu = "service_adm_nom_service,service_adm_ville_service\n,Orleans\n"
        fichier = io.BytesIO(contenu.encode("utf-8"))
        succes, message = importer_entreprises(fichier)
        assert succes is True
        assert "0 entreprises ajoutées" in message
        db.session.rollback()


def test_importer_entreprises_exception(testapp: Flask):
    """Test de la gestion d'erreur critique lors de l'importation entreprises"""

    with testapp.app_context():
        succes, message = importer_entreprises(None)
        assert succes is False
        assert "Erreur critique" in message
        db.session.rollback()
