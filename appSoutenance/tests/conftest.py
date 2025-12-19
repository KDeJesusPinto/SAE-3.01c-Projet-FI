import pytest
from pathlib import Path
from sqlalchemy import text
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
        
        sql_file = Path("appSoutenance/data/insertion.sql")
        if sql_file.exists():
            with open(sql_file, "r", encoding="utf-8") as f:
                sql_script = f.read()
                for statement in sql_script.split(";"):
                    statement = statement.strip()
                    if statement:
                        db.session.execute(text(statement))
            db.session.commit()
            
        yield app
        db.session.remove()
        db.drop_all()
