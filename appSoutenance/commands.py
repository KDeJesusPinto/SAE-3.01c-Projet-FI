import csv
import click
import logging as lg
from datetime import datetime
from .app import app, db
from .models import *

@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    """Crée les tables et importe les données depuis un CSV."""
    
    
    db.drop_all()
    db.create_all()
    
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # On met des valeurs par défaut si certains champs sont vides
            #Etudiant
            nom_stagiaire = row['nom_stagiaire'] or "Nom inconnu"
            prenom_stagiaire = row['prenom_stagiaire'] or "Prénom inconnu"
            civilite_stagiaire = row['civilite_stagiaire'] or "NC"
            email = row['mail_perso'] or row['mail_etu'] or "email@inconnu.com"
            
            # Création de l'étudiant
            etu = Etudiant(
                nom_etudiant=nom_stagiaire,
                prenom_etudiant=prenom_stagiaire,
                civilite_etudiant=civilite_stagiaire,
                date_naissance=datetime(2000, 1, 1).date(),  # Valeur par défaut
                email_etudiant=email
            )
            db.session.add(etu)
            db.session.flush()  # flush pour récupérer l'ID

            #Promo
            nom_promo = row.get("lib_import") or "Promo inconnue"
            annee_promo = 2025  # valeur par défaut
            promo = Promo(
                nom_promo=nom_promo,
                annee_promo=annee_promo,
                formation_promo="Informatique"
            )
            db.session.add(promo)
            db.session.flush()
            
            # Association étudiant → promo
            appart = Appartenir(
                id_etudiant=etu.id_etudiant,
                nom_promo=promo.nom_promo,
                annee_promo=promo.annee_promo,
                regime_etudiant=row.get('intitule_regime_inscription') or "Initiale"
            )
            db.session.add(appart)

            #Entreprise
            nom_entreprise = row.get("service_adm_nom_service") or "Entreprise inconnue"
            entreprise = Entreprise.query.filter_by(nom_entreprise=nom_entreprise).first()
            if not entreprise:
                entreprise = Entreprise(
                    nom_entreprise=nom_entreprise,
                    secteur="NC",
                    ville=row.get("service_adm_ville_service") or "Ville inconnue",
                    adresse=row.get("service_adm_adr1_service") or "Adresse inconnue",
                    code_postal=row.get("service_adm_cp_service") or "00000",
                    typeE="NC",
                    tel_entreprise=None,
                    email_entreprise=None
                )
                db.session.add(entreprise)
                db.session.flush()

            #maitre de stage 
            nom_maitre = row.get("nom_employe_tut") or "Nom inconnu"
            prenom_maitre = row.get("prenom_employe_tut") or "Prénom inconnu"
            email_maitre = row.get("mail_employe_tut") or "email@inconnu.com"
            maitre = MaitreStage.query.filter_by(nom_maitre=nom_maitre, prenom_maitre=prenom_maitre).first()
            if not maitre:
                maitre = MaitreStage(
                    civilite_maitre=row.get("civilite_employe_tut") or "NC",
                    nom_maitre=nom_maitre,
                    prenom_maitre=prenom_maitre,
                    email_maitre=email_maitre,
                    id_entreprise=entreprise.id_entreprise,
                    tel_maitre=row.get("tel_employe_tut")
                )
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
            
            demarche = Demarche(
                source="CSV import",
                typeD="Stage",
                situation="En cours",
                date_envoi=dtdeb or datetime.today().date(),
                date_relance=None,
                resultat=None,
                raison_refus=None,
                cv=None,
                lettre_motiv=None,
                id_entreprise=entreprise.id_entreprise,
                id_etudiant=etu.id_etudiant
            )
            db.session.add(demarche)
            db.session.flush()   
            # Stage
            stage = Stage(
                typeS="Stage",
                date_debut=dtdeb or datetime.today().date(),
                date_fin=dtfin or datetime.today().date(),
                titre_stage=row.get("titre_stage") or "Stage inconnu",
                theme_stage=row.get("theme_stage") or "NC",
                id_demarche=demarche.id_demarche,
                id_maitre=maitre.id_maitre
            )
            db.session.add(stage)
        db.session.commit()
        lg.warning("Database initialized!!!!")
