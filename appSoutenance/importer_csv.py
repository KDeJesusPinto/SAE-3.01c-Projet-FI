import csv
import logging as lg
from datetime import datetime
import io
from .models import db, Etudiant, Promo, Appartenir, Entreprise, MaitreStage, Demarche, Stage
from sqlalchemy.exc import IntegrityError


def importer_etudiants_stages(file_storage):
    """Importe les données Étudiants/Stages à partir d'un flux de fichier CSV."""
    ajout = 0
    try:
        stream = io.TextIOWrapper(file_storage.stream, encoding='utf-8')
        reader = csv.DictReader(stream)


        for row in reader:


            email = row.get('mail_perso') or row.get('mail_etu') or "email@anonyme.com"
            etu = Etudiant.query.filter_by(email_etudiant=email).first()
            if not etu:
                etu = Etudiant(
                    nom_etudiant=row.get('nom_stagiaire') or "anonyme",
                    prenom_etudiant=row.get('prenom_stagiaire') or "anonyme",
                    date_naissance=datetime(2000, 1, 1).date(),
                    email_etudiant=email)
                db.session.add(etu)
                db.session.flush()            
            ajout += 1


        db.session.commit()
        lg.warning(f"Importation Étudiants/Stages terminée : {ajout} lignes traitées.")
        return True, f"{ajout} lignes d'étudiants et stages importées avec succès."


    except IntegrityError:
        db.session.rollback()
        return False, "Erreur d'intégrité de la base de données (doublon ou clé manquante). Le fichier n'a pas été importé."
    except Exception as e:
        db.session.rollback()
        lg.error(f"Erreur lors de l'importation Étudiants/Stages: {e}")
        return False, f"Erreur critique lors de l'importation : {e}"


def importer_entreprises(file_storage):
    """Importe les entreprises à partir d'un flux de fichier CSV."""
    try:
        stream = io.TextIOWrapper(file_storage.stream, encoding='utf-8')
        reader = csv.DictReader(stream)
        ajout = 0
        db.session.commit()
        lg.warning(f"Importation Entreprises terminée : {ajout} entreprises ajoutées.")
        return True, f"{ajout} entreprises ajoutées avec succès."
    except Exception as e:
        db.session.rollback()
        lg.error(f"Erreur lors de l'importation Entreprises: {e}")
        return False, f"Erreur critique lors de l'importation : {e}"