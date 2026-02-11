from flask import Flask
from appSoutenance.forms import ExportForm
from appSoutenance.models import db

def test_export_form_valide(testapp: Flask):
    """Test du formulaire d'export avec des données valides"""

    with testapp.app_context():
        form = ExportForm(type_export="etudiants")
        assert form.validate() is True
        db.session.rollback()

def test_export_form_invalide(testapp: Flask):
    """Test du formulaire d'export avec des données invalides"""

    with testapp.app_context():
        form = ExportForm()
        assert form.validate() is False
        assert "type_export" in form.errors
        db.session.rollback()

def test_export_form_choix(testapp: Flask):
    """Vérifie les options disponibles dans le sélecteur d'export"""

    with testapp.app_context():
        form = ExportForm()
        choix = [c[0] for c in form.type_export.choix]
        assert "etudiants" in choix
        assert "entreprises" in choix
        assert "soutenances" in choix
        db.session.rollback()