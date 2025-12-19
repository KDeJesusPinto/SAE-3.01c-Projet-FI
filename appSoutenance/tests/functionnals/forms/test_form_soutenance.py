from flask import Flask
from appSoutenance.forms import FormSoutenance, db


def test_form_soutenance_valide(testapp: Flask):
    """Test du formulaire de soutenance avec des données valides"""

    with testapp.app_context():
        form = FormSoutenance(
            id_stage="1",
            h_debut="09:00",
            dateS="2025-06-15",
            salle="101",
            nom_enseignant="Jean Dubois",
        )
        assert form.validate() is True
        db.session.rollback()


def test_form_soutenance_sans_date(testapp: Flask):
    """Test du formulaire de soutenance sans la date (champ obligatoire)"""

    with testapp.app_context():
        form = FormSoutenance(id_stage="1", h_debut="10:00", dateS="", salle="102")
        assert form.validate() is False
        assert "dateS" in form.errors
        db.session.rollback()


def test_form_soutenance_structure_valide(testapp: Flask):
    """Vérifie que tous les champs attendus sont présents dans le formulaire"""

    with testapp.app_context():
        form = FormSoutenance()
        assert "id_soutenance" in form._fields
        assert "id_stage" in form._fields
        assert "h_debut" in form._fields
        assert "dateS" in form._fields
        assert "salle" in form._fields
        db.session.rollback()
