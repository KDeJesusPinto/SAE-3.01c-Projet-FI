import csv
import logging as lg
from datetime import datetime
import io
from .models import db, Etudiant, Promo, Appartenir, Entreprise, MaitreStage, Demarche, Stage
from sqlalchemy.exc import IntegrityError


def importer_etudiants_stages(file_storage):
    """Importe les données Étudiants/Stages à partir d'un flux de fichier CSV"""

    ajout = 0
    try:
        content = file_storage.read().decode('utf-8')
        stream = io.StringIO(content)
        reader = csv.DictReader(stream)

        champs_attendus = ['mail_etu', 'nom_stagiaire', 'prenom_stagiaire', 'civilite_stagiaire']
        if not all(champ in reader.fieldnames for champ in champs_attendus):
            return False, f"Format CSV invalide. Colonnes attendues : {', '.join(champs_attendus)}"

        for row in reader:
            email = row.get('mail_perso') or row.get('mail_etu')
            if not email:
                continue
            etu = Etudiant.query.filter_by(email_etudiant=email).first()
            if not etu:
                etu = Etudiant(
                    nom_etudiant=row.get('nom_stagiaire') or "anonyme",
                    prenom_etudiant=row.get('prenom_stagiaire') or "anonyme",
                    date_naissance=datetime(2000, 1, 1).date(),
                    email_etudiant=email,
                    civilite_etudiant=row.get('civilite_stagiaire') or "M.")
                db.session.add(etu)
                db.session.flush()            
            ajout += 1


        db.session.commit()
        return True, f"{ajout} lignes traitées."
    
    except Exception as e:
        db.session.rollback()
        return False, str(e)


def importer_entreprises(file_storage):
    """Importe les entreprises à partir d'un flux de fichier CSV"""
    
    try:
        content = file_storage.read().decode('utf-8')
        stream = io.StringIO(content) 
        reader = csv.DictReader(stream)
        ajout = 0
        for row in reader:
            nom = (row.get('service_adm_nom_service') or "").strip().upper()
            ville = (row.get('service_adm_ville_service') or "").strip().upper()
            if not nom:
                continue
            
            # Eviter les doublons
            existante = Entreprise.query.filter(
                db.func.upper(db.func.trim(Entreprise.nom_entreprise)) == nom,
                db.func.upper(db.func.trim(Entreprise.ville)) == ville).first()
            
            if not existante:
                ent = Entreprise(
                    nom_entreprise=nom.title(),
                    adresse=row.get('service_adm_adr1_service') or "Adresse inconnue",
                    code_postal=row.get('service_adm_cp_service') or "00000",
                    ville=ville.title(),
                    secteur="NC",
                    typeE="NC"
                )
                db.session.add(ent)
                ajout += 1

        db.session.commit()
        return True, f"{ajout} entreprises ajoutées avec succès."
    except Exception as e:
        db.session.rollback()
        lg.error(f"Erreur lors de l'importation Entreprises: {e}")
        return False, f"Erreur critique lors de l'importation : {e}"
    
def suppression_sauts_a_la_ligne_csv(nom_fichier):
    with open(nom_fichier, "r") as file:
        entete = file.readline().split(",") # liste contenant les entêtes
        nb_virgules_par_ligne = len(entete) - 1
        cpt_virgules = 0
        resultat = ""

        fichier_original = file.read()
        #print(fichier_original)

        for carac in fichier_original:
            if carac == ",":
                cpt_virgules += 1

            elif carac == "\n":
                #print("haaaa")

                if cpt_virgules >= nb_virgules_par_ligne:
                    #print("réinitialisation à 0")
                    cpt_virgules = 0
                else:
                    continue

            resultat += carac
            #print(cpt_virgules, nb_virgules_par_ligne)

        #print(resultat)

        with open("appSoutenance/data/nouveau_fichier.csv", "w") as nouveau_fichier:
            nouveau_fichier.write(",".join(entete) + resultat)


if __name__ == "__main__":
    suppression_sauts_a_la_ligne_csv('appSoutenance/data/arexis_donnees.csv')