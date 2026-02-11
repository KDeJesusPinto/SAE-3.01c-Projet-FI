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