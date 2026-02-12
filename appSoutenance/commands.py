import csv
import subprocess
import click
import logging as lg
from sqlalchemy import text
from datetime import datetime
from pathlib import Path
from .app import app, db
from .models import *


@app.cli.command()
def resetdb():
    """Réinitialise la base de données à son état initial"""
    db.drop_all()
    db.create_all()

    sql_file = Path("appSoutenance/data/donnee.sql")
    if sql_file.exists():
        with open(sql_file, "r", encoding="utf-8") as f:
            sql_script = f.read()
            for statement in sql_script.split(";"):
                statement = statement.strip()
                if statement:
                    db.session.execute(text(statement))
                    db.session.commit()
        db.session.commit()
        lg.warning("Base de données réinitialisée avec succès !")
    else:
        lg.warning("Tables créées mais aucun fichier donnee.sql trouvé pour les données initiales")


@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    """Crée les tables et importe les données depuis un CSV."""

    db.drop_all()
    db.create_all()

    # Exécution du script d'insertion
    sql_file = Path("appSoutenance/data/donnee.sql")
    if sql_file.exists():
        with open(sql_file, "r", encoding="utf-8") as f:
            sql_script = f.read()
            for statement in sql_script.split(";"):
                statement = statement.strip()
                if statement:
                    db.session.execute(text(statement))
                    db.session.commit()
        db.session.commit()
        lg.warning("Fichier donnee.sql exécuté avec succès!")
    else:
        lg.warning("Aucun fichier donnee.sql trouvé.")

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            #Etudiant
            nom_stagiaire = row['nom_stagiaire'] or "anonyme"
            prenom_stagiaire = row['prenom_stagiaire'] or "anonyme"
            civilite_stagiaire = row['civilite_stagiaire'] or "NC"
            email = row['mail_perso'] or row['mail_etu'] or "email@anonyme.com"

            # Création de l'étudiant
            etu = Etudiant.query.filter_by(email_etudiant=email).first()
            if not etu:
                etu = Etudiant(
                    nom_etudiant=nom_stagiaire,
                    prenom_etudiant=prenom_stagiaire,
                    civilite_etudiant=civilite_stagiaire,
                    date_naissance=datetime(2000, 1, 1).date(),
                    email_etudiant=email,
                    login_etudiant=email.split('@')[0],
                    pwd_etudiant=nom_stagiaire.lower())
                db.session.add(etu)
                db.session.flush()

            #Promo
            nom_promo = row.get("lib_import") or "Promo inconnue"
            annee_promo = 2025
            promo = Promo.query.filter_by(nom_promo=nom_promo, annee_promo=annee_promo).first()
            if not promo:
                promo = Promo(nom_promo=nom_promo,
                              annee_promo=annee_promo,
                              formation_promo="Informatique")
                db.session.add(promo)
                db.session.flush()

            # Association étudiant --> promo
            appart = Appartenir.query.filter_by(
                id_etudiant=etu.id_etudiant,
                nom_promo=promo.nom_promo,
                annee_promo=promo.annee_promo
            ).first()
            if not appart:
                appart = Appartenir(
                    id_etudiant=etu.id_etudiant,
                    nom_promo=promo.nom_promo,
                    annee_promo=promo.annee_promo,
                    regime_etudiant=row.get('intitule_regime_inscription') or "Initiale")
                db.session.add(appart)

            # Entreprise
            nom_ent = row.get(
                "service_adm_nom_service") or "Entreprise inconnue"
            ville_ent = (row.get("service_adm_ville_service") or
                         "Ville inconnue").upper()
            entreprise = Entreprise.query.filter_by(nom_entreprise=nom_ent,
                                                    ville=ville_ent).first()
            if not entreprise:
                entreprise = Entreprise(
                    nom_entreprise=nom_ent,
                    secteur="NC",
                    ville=row.get("service_adm_ville_service") or
                    "Ville inconnue",
                    adresse=row.get("service_adm_adr1_service") or
                    "Adresse inconnue",
                    code_postal=row.get("service_adm_cp_service") or "00000",
                    typeE="NC",
                    tel_entreprise=None,
                    email_entreprise=None)
                db.session.add(entreprise)
                db.session.flush()

            # Maitre de stage
            nom_maitre = row.get("nom_employe_tut") or "Nom inconnu"
            prenom_maitre = row.get("prenom_employe_tut") or "Prénom inconnu"
            email_maitre = row.get("mail_employe_tut") or "email@inconnu.com"
            maitre = MaitreStage.query.filter_by(
                nom_maitre=nom_maitre, prenom_maitre=prenom_maitre).first()
            if not maitre:
                maitre = MaitreStage(
                    civilite_maitre=row.get("civilite_employe_tut") or "NC",
                    nom_maitre=nom_maitre,
                    prenom_maitre=prenom_maitre,
                    email_maitre=email_maitre,
                    id_entreprise=entreprise.id_entreprise,
                    tel_maitre=row.get("tel_employe_tut"))
                db.session.add(maitre)
                db.session.flush()

            # Demarche
            try:
                dtdeb = datetime.strptime(row['dtdeb_stage'], "%d/%m/%Y").date()
            except (ValueError, TypeError):
                dtdeb = None
            try:
                dtfin = datetime.strptime(row['dtfin_stage'], "%d/%m/%Y").date()
            except (ValueError, TypeError):
                dtfin = None

            demarche = Demarche.query.filter_by(
                id_etudiant=etu.id_etudiant,
                id_entreprise=entreprise.id_entreprise,
                typeD="Stage"
            ).first()

            if not demarche:
                demarche = Demarche(source="CSV import",
                                    typeD="Stage",
                                    situation="En cours",
                                    date_envoi=dtdeb or datetime.today().date(),
                                    id_entreprise=entreprise.id_entreprise,
                                    id_etudiant=etu.id_etudiant)
                db.session.add(demarche)
                db.session.flush()

            # Stage
            if not Stage.query.filter_by(id_demarche=demarche.id_demarche).first():
                stage = Stage(typeS="Stage",
                              date_debut=dtdeb or datetime.today().date(),
                              date_fin=dtfin or datetime.today().date(),
                              titre_stage=row.get("titre_stage") or "Stage inconnu",
                              theme_stage=row.get("theme_stage") or "NC",
                              id_demarche=demarche.id_demarche,
                              id_maitre=maitre.id_maitre)
                db.session.add(stage)
                db.session.flush()
        db.session.commit()
        lg.warning("Database initialized!!!!")

    # Import CSV entreprises dans le dossier
    data_dir = Path("appSoutenance/data/entreprises")
    for fichier in data_dir.glob("*.csv"):
        importer_entreprises(fichier)

    lg.warning("Import des entreprises du dossier terminé !")


def importer_entreprises(fichier):
    with open(fichier, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        ajout = 0
        for row in reader:
            nom = (row.get('service_adm_nom_service') or "").strip().upper()
            ville = (row.get('service_adm_ville_service') or "").strip().upper()
            adresse = " ".join(
                filter(None, [
                    row.get('service_adm_adr1_service'),
                    row.get('service_adm_adr2_service')
                ])).strip()
            if not nom:
                continue
            existante = Entreprise.query.filter(
                db.func.upper(db.func.trim(Entreprise.nom_entreprise)) == nom,
                db.func.upper(db.func.trim(Entreprise.ville)) == ville).first()
            if existante:
                continue
            ent = Entreprise(
                nom_entreprise=nom.title(),
                adresse=adresse,
                code_postal=row.get('service_adm_cp_service') or "",
                ville=ville.title(),
                secteur="NC",
                typeE="NC",
            )
            db.session.add(ent)
            ajout += 1
        db.session.commit()
        lg.warning(f"{fichier.name} : {ajout} entreprises ajoutées.")

@app.cli.command()
@click.pass_context
def test(ctx):
    """Lance les tests unitaires avec coverage et reload automatique."""
    import sys

    # 1. Réinitialisation initiale
    ctx.invoke(loaddb, filename='appSoutenance/data/arexis_donnees.csv')

    try:
        # 2. Exécution des tests via subprocess pour un coverage précis
        res = subprocess.run([
            "coverage", "run", "-m", "pytest", 
            "--cov=appSoutenance", "--cov-report=term-missing", "appSoutenance/tests"
        ])
        # 3. Affichage du rapport de couverture
        subprocess.run(["coverage", "report", "-m"])
        return_code = res.returncode
    finally:
        # 4. Nettoyage des sessions et réinitialisation finale pour retrouver la base de dev propre
        db.session.remove()
        db.engine.dispose()
        ctx.invoke(loaddb, filename='appSoutenance/data/arexis_donnees.csv')

    sys.exit(return_code)
