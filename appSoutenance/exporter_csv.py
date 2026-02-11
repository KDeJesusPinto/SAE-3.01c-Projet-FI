import csv
import io
from .models import Etudiant, Entreprise, Soutenance, Stage, Appartenir, Enseignant, Composer

def exporter_etudiants():
    """Exporte les données des étudiants"""
    output = io.StringIO()
    writer = csv.writer(output, delimiter=';')
    writer.writerow(['ID', 'Nom', 'Prénom', 'Email', 'Promo', 'Année', 'Régime'])
    
    etudiants = Etudiant.query.all()
    for e in etudiants:
        app = Appartenir.query.filter_by(id_etudiant=e.id_etudiant).first()
        promo = app.nom_promo if app else ""
        annee = app.annee_promo if app else ""
        regime = app.regime_etudiant if app else ""
        writer.writerow([e.id_etudiant, e.nom_etudiant, e.prenom_etudiant, e.email_etudiant, promo, annee, regime])
    
    output.seek(0)
    return output

def exporter_entreprises():
    """Exporte les données des entreprises"""
    output = io.StringIO()
    writer = csv.writer(output, delimiter=';')
    writer.writerow(['ID', 'Nom', 'Ville', 'Adresse', 'CP', 'Secteur', 'Type', 'Tel', 'Email'])
    
    entreprises = Entreprise.query.all()
    for ent in entreprises:
        writer.writerow([
            ent.id_entreprise, ent.nom_entreprise, ent.ville, ent.adresse, 
            ent.code_postal, ent.secteur, ent.typeE, ent.tel_entreprise, ent.email_entreprise
        ])
    
    output.seek(0)
    return output

def exporter_soutenances():
    """Exporte les données des soutenances"""
    output = io.StringIO()
    writer = csv.writer(output, delimiter=';')
    writer.writerow(['ID', 'Date', 'Heure', 'Salle', 'Etudiant', 'Titre Stage', 'Jury'])
    
    soutenances = Soutenance.query.all()
    for s in soutenances:
        stage = Stage.query.get(s.id_stage)
        etudiant_str = "NC"
        titre_stage = "NC"
        if stage:
            titre_stage = stage.titre_stage
            if stage.demarche and stage.demarche.etudiant:
                etudiant_str = f"{stage.demarche.etudiant.nom_etudiant} {stage.demarche.etudiant.prenom_etudiant}"
        
        enseignants = Enseignant.query.join(Composer).filter(Composer.id_soutenance == s.id_soutenance).all()
        jury_str = ", ".join([f"{ens.nom_enseignant} {ens.prenom_enseignant}" for ens in enseignants])
        
        writer.writerow([
            s.id_soutenance, 
            s.dateS, 
            s.h_debut, 
            s.salle, 
            etudiant_str, 
            titre_stage, 
            jury_str
        ])
    
    output.seek(0)
    return output