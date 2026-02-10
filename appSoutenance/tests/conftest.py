import pytest
from pathlib import Path
from sqlalchemy import text
import subprocess
from appSoutenance.app import app, db

@pytest.fixture
def testapp():
    """Fixture pour initialiser l'application et la base de données pour les tests"""
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
    })

    with app.app_context():
        db.session.remove()
        db.engine.dispose()

    with app.app_context():
        db.drop_all()
        db.create_all()
        
        runner = app.test_cli_runner()
        runner.invoke(args=['loaddb', 'appSoutenance/data/arexis_donnees.csv'])

        yield app
        db.session.rollback()
        db.session.remove()
        db.drop_all()
