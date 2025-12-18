from collections import defaultdict
from .app import app
from flask import render_template, request, url_for, redirect, flash
from appSoutenance.models import Etudiant, Demarche, Promo, Appartenir, Stage, Soutenance, Enseignant, Composer, Tutorer
from sqlalchemy import desc, distinct
from .models import db



@app.route('/')
@app.route('/connexion/')
def index():
    return render_template("index.html",
                           title="Soutenance - Connexion",
                           accueil="index")


########################## POUR LES ÉTUDIANTS ##########################

def sort_id(demarche):
    return demarche.id_demarche

@app.route('/etudiant/')
def accueil_etudiant():
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.get(num_personne)
    lst_demarches = sorted(list(etudiant.demarches), key=sort_id)[:2]
    return render_template("etudiant/accueil_etu.html", accueil="accueil_etudiant", personne=etudiant, title="Accueil", liste_dem=lst_demarches)

@app.route('/etudiant/demarches/')
def demarches():
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.get(num_personne)
    #lst_demarches = sorted(list(etudiant.demarches), key=sort_id)
    lst_demarches = {
        15: ["Google", 2, 'refusé'],
        1: ["Microsoft", 8, 'validé'],
        2: ["Ubisoft", 9, 'en attente de validation'],
        11: ["Apple", 10, 'convention signée'],
        12: ["IUT'O", 256, 'validé'],
        9: ["Cognosphère", 10, 'convention signée']
    }
    return render_template("etudiant/demarches.html", accueil="accueil_etudiant", personne=etudiant, title="Mes démarches", liste_dem=lst_demarches)

@app.route('/etudiant/stage/')
def info_stage():
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/info_stage_valide.html", accueil="accueil_etudiant", personne=etudiant, title="Mon stage")

@app.route('/etudiant/demarches/new1/')
def nouvelle_demarche1():
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/nouvelle_demarche1.html", accueil="accueil_etudiant", personne=etudiant, title="Nouvelle démarche")

@app.route('/etudiant/demarches/new2/')
def nouvelle_demarche2():
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/nouvelle_demarche2.html", accueil="accueil_etudiant", personne=etudiant, title="Nouvelle démarche")

@app.route('/etudiant/demarches/new3/')
def nouvelle_demarche3():
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/nouvelle_demarche3.html", accueil="accueil_etudiant", personne=etudiant, title="Nouvelle démarche")

@app.route('/etudiant/demarches/resume/')
def resume_demarche_etudiant():
    num_personne = request.args.get('num_personne')
    etudiant = Etudiant.query.filter(Etudiant.id_etudiant==num_personne).one()
    return render_template("etudiant/resume_demarche.html", accueil="accueil_etudiant", personne=etudiant, title="Résumé de la démarche")

########################## POUR LES ENSEIGNANTS ##########################


@app.route('/enseignant/')
def accueil_enseignant():
    num_personne = request.args.get('num_personne')


    queryListeTutore=Etudiant.query.join(Tutorer,Etudiant.id_etudiant==Tutorer.id_etudiant).filter(Tutorer.id_enseignant==num_personne)
    query_soutenance_prevue=Soutenance.query.join(Composer,Composer.id_soutenance==Soutenance.id_soutenance).filter(Composer.id_enseignant==num_personne).order_by(Soutenance.dateS,Soutenance.h_debut)

    res_tutore = []
    res_soutenance=[]

    for etudiant in queryListeTutore:
        derniere_demarche = Demarche.query.filter_by(id_etudiant=etudiant.id_etudiant).order_by(desc(Demarche.date_envoi)).first()
        soutenance_prevue_tutore=Soutenance.query.join(Stage,Stage.id_stage==Soutenance.id_stage).join(Demarche,Demarche.id_demarche==Stage.id_demarche).join(Etudiant,Etudiant.id_etudiant==Demarche.id_etudiant).filter(Etudiant.id_etudiant==etudiant.id_etudiant).first()
        res_tutore.append({'etudiant':etudiant,'etat':derniere_demarche.situation if derniere_demarche else "Aucune",'soutenance_tutore':soutenance_prevue_tutore})
        
    for soutenance in query_soutenance_prevue:
        res_soutenance.append({'soutenance':soutenance})
    res_date=query_soutenance_prevue.distinct(Soutenance.dateS)
    enseignant = Enseignant.query.filter(Enseignant.id_enseignant==num_personne).one()
    nb_soutenance_place=query_soutenance_prevue.count()
    nb_soutenance_place_tutore=queryListeTutore.count()

    return render_template("enseignant/accueil_enseignant.html", accueil="accueil_enseignant", personne=enseignant, title="Accueil",liste_tutore=res_tutore,liste_souteance=res_soutenance,date_soute=res_date,nb_sout_place=nb_soutenance_place)

@app.route('/enseignant/planning/')
def planning_enseignant():
    num_personne = request.args.get('num_personne')
    enseignant = Enseignant.query.filter(Enseignant.id_enseignant==num_personne).one()
    return render_template("enseignant/planning_enseignant.html", accueil="accueil_enseignant", personne=enseignant, title="Planning enseignant")

@app.route('/enseignant/liste+etu/')
def liste_etu_enseignant():
    num_personne = request.args.get('num_personne')
    enseignant = Enseignant.query.filter(Enseignant.id_enseignant==num_personne).one()
    lesEtudiants = Etudiant.query.all()
    res = []

    for etudiant in lesEtudiants:
        appartenance = Appartenir.query.filter_by(
            id_etudiant=etudiant.id_etudiant).first()
        promo = Promo.query.filter_by(nom_promo=appartenance.nom_promo,
                                      annee_promo=appartenance.annee_promo
                                     ).first() if appartenance else None

        nb_demarches = Demarche.query.filter_by(
            id_etudiant=etudiant.id_etudiant).count()

        derniere_demarche = Demarche.query.filter_by(id_etudiant=etudiant.id_etudiant)\
            .order_by(desc(Demarche.date_envoi)).first()

        res.append({
            'etudiant':
                etudiant,
            'formation':
                promo.formation_promo if promo else "None",
            'annee':
                promo.annee_promo if promo else "None",
            'promo':
                promo.nom_promo if promo else "None",
            'nb_demarches':
                nb_demarches,
            'situation':
                derniere_demarche.situation if derniere_demarche else "Aucune"
        })
    return render_template("enseignant/lst_etudiants_enseignant.html", accueil="accueil_enseignant", personne=enseignant, title="Liste des étudiants",resultats=res)

@app.route('/enseignant/liste+etu/etudiant/')
def detail_etudiant_ens():
    num_personne = request.args.get('num_personne')
    enseignant = Enseignant.query.filter(Enseignant.id_enseignant==num_personne).one()
    return render_template("admin/detail_etudiant_ens.html", accueil="accueil_enseignant", personne=enseignant, title="Detail de l'etudiant")

@app.route('/enseignant/soutenances/')
def liste_soutenance_ens():

    num_personne = request.args.get('num_personne')
    enseignant = Enseignant.query.filter(Enseignant.id_enseignant==num_personne).one()
    soutenanceInscrit=Soutenance.query.join(Composer,Composer.id_soutenance==Soutenance.id_soutenance).filter(Composer.id_enseignant==num_personne).order_by(Soutenance.dateS,Soutenance.h_debut)
    soutenances=Soutenance.query.join(Composer,Composer.id_soutenance==Soutenance.id_soutenance).join(Enseignant,Composer.id_enseignant==Enseignant.id_enseignant).all()
    res_soutenance=[]
    for soutenance in soutenances:
        etudiant=Etudiant.query.join(Demarche,Etudiant.id_etudiant==Demarche.id_etudiant).join(Stage,Demarche.id_demarche==Stage.id_demarche).join(Soutenance,Soutenance.id_stage==Stage.id_stage).filter(Soutenance.id_soutenance==soutenance)
        res_soutenance.append({'soutenance':soutenance,'etudiant':etudiant})

    return render_template("enseignant/soutenance_enseignant.html",accueil="accueil_enseignant",personne=enseignant,liste_soutenances=res_soutenance)

########################## POUR LES ADMINISTRATEURS ##########################


@app.route('/admin/')
def accueil_admin():
    nb_etudiants = Etudiant.query.count()
    nb_stages_trouves = Stage.query.count()
    nb_etudiants_alternants = Appartenir.query.filter_by(
        regime_etudiant='Alternance').count()
    nb_soutenances_alternants = 0
    nb_soutenances_posees = Soutenance.query.count()
    nb_soutenances_attente_candide = 0
    return render_template(
        "admin/accueil_admin.html",
        accueil="accueil_admin",
        title="Accueil",
        nb_stages_trouves=nb_stages_trouves,
        nb_etudiants=nb_etudiants,
        nb_etudiants_alternants=nb_etudiants_alternants,
        nb_soutenances_alternants=nb_soutenances_alternants,
        nb_soutenances_posees=nb_soutenances_posees,
        nb_soutenances_attente_candide=nb_soutenances_attente_candide)


@app.route('/admin/planning/')
def planning_admin():
    return render_template("admin/planning_admin.html",
                           accueil="accueil_admin",
                           title="Planning")


@app.route('/admin/liste+enseignants/<int:id>/')
def detail_enseignant(id):
    enseignant = Enseignant.query.get(id)
    return render_template("admin/detail_enseignant.html",
                           accueil="accueil_admin",
                           title="Detail de l'enseignant",
                           enseignant=enseignant)


@app.route('/admin/liste+etudiants/<int:id>/')
def detail_etudiant_admin(id):
    etudiant = Etudiant.query.get(id)
    return render_template("admin/detail_etudiant_admin.html",
                           accueil="accueil_admin",
                           title="Detail de l'etudiant",
                           etudiant=etudiant)


@app.route('/admin/liste+enseignants/')
def liste_ens_admin():
    lesEnseignants = Enseignant.query.all()
    res = []

    for enseignant in lesEnseignants:
        nb_tutore = Tutorer.query.filter_by(
            id_enseignant=enseignant.id_enseignant).count()
        nb_soutenances = Composer.query.filter_by(
            id_enseignant=enseignant.id_enseignant).count()

        res.append({
            "enseignant": enseignant,
            "nb_tutores": nb_tutore,
            "nb_soutenances": nb_soutenances,
        })

    return render_template("admin/lst_enseignants.html",
                           accueil="accueil_admin",
                           title="Liste enseignants",
                           resultats=res)


@app.route('/admin/liste+etudiants/')
def liste_etu_admin():
    lesEtudiants = Etudiant.query.all()

    tri = request.args.get("trier", "Nom")

    res = []

    for etudiant in lesEtudiants:
        appartenance = Appartenir.query.filter_by(
            id_etudiant=etudiant.id_etudiant).first()
        promo = Promo.query.filter_by(nom_promo=appartenance.nom_promo,
                                      annee_promo=appartenance.annee_promo
                                     ).first() if appartenance else None

        nb_demarches = Demarche.query.filter_by(
            id_etudiant=etudiant.id_etudiant).count()

        derniere_demarche = Demarche.query.filter_by(id_etudiant=etudiant.id_etudiant)\
                                  .order_by(desc(Demarche.date_envoi)).first()

        res.append({
            'etudiant':
                etudiant,
            'formation':
                promo.formation_promo,
            'annee':
                promo.annee_promo,
            'promo':
                promo.nom_promo,
            'nb_demarches':
                nb_demarches,
            'situation':
                derniere_demarche.situation if derniere_demarche else "Aucune"
        })

    if tri == "Nom":
        res = sorted(res, key=lambda x: x["etudiant"].nom_etudiant)
    elif tri == "Annee":
        res = sorted(res, key=lambda x: (x["annee"] is None, x["annee"]))
    elif tri == "NbDemarches":
        res = sorted(res, key=lambda x: x["nb_demarches"], reverse=True)

    return render_template("admin/lst_etudiants_admin.html",
                           accueil="accueil_admin",
                           title="Liste etudiants",
                           resultats=res)


if __name__ == "__main__":
    app.run()
