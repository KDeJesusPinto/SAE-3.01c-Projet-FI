from flask import Flask
from appSoutenance.forms import ImportForm
from appSoutenance.models import db


def test_import_form_invalide(testapp: Flask):
    """Test de validation du formulaire d'importation (champs manquants)"""

    with testapp.app_context():
        form = ImportForm()
        assert form.validate() is False
        assert "type_import" in form.errors
        assert "ficCSV" in form.errors
        db.session.rollback()


def test_import_form_choices(testapp: Flask):
    """Vérifie les options disponibles dans le sélecteur d'import"""

    with testapp.app_context():
        form = ImportForm()
        choices = [c[0] for c in form.type_import.choices]
        assert "entreprises" in choices
        assert "etudiants_stages" in choices
        db.session.rollback()
