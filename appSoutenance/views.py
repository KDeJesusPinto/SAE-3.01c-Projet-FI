from .app import app
from flask import render_template, request, url_for , redirect
from appSoutenance.models import Etudiant

@app.route('/')
@app.route('/connexion/')
def index():
    return render_template("index.html", title="Soutenance - Connexion", accueil="index")

########################## POUR LES ÉTUDIANTS ##########################

@app.route('/etudiant/')
def accueil_etudiant():
    lst_demarches = {
        15:["Google", 2, 'refusé'],
        1:["Microsoft", 8, 'validé'],
        2:["Ubisoft", 9, 'en attente de validation'],
        11:["Apple", 10, 'convention signée'],
        12:["IUT'O", 256, 'validé'],
        9:["Cognosphère", 10, 'convention signée']
    }
    return render_template("etudiant/accueil_etu.html", accueil="accueil_etudiant", prenom="Leni", nom="Doe", title="Accueil", liste_dem=lst_demarches)

@app.route('/etudiant/demarches/')
def demarches():
    lst_demarches = {
        15:["Google", 2, 'refusé'],
        1:["Microsoft", 8, 'validé'],
        2:["Ubisoft", 9, 'en attente de validation'],
        11:["Apple", 10, 'convention signée'],
        12:["IUT'O", 256, 'validé'],
        9:["Cognosphère", 10, 'convention signée']
    }
    return render_template("etudiant/demarches.html", accueil="accueil_etudiant", title="Mes démarches", liste_dem=lst_demarches)

@app.route('/etudiant/stage/')
def info_stage():
    return render_template("etudiant/info_stage_valide.html", accueil="accueil_etudiant", title="Mon stage")

@app.route('/etudiant/demarches/new1/')
def nouvelle_demarche1():
    return render_template("etudiant/nouvelle_demarche1.html", accueil="accueil_etudiant", title="Nouvelle démarche")

@app.route('/etudiant/demarches/new2/')
def nouvelle_demarche2():
    return render_template("etudiant/nouvelle_demarche2.html", accueil="accueil_etudiant", title="Nouvelle démarche")

@app.route('/etudiant/demarches/new3/')
def nouvelle_demarche3():
    return render_template("etudiant/nouvelle_demarche3.html", accueil="accueil_etudiant", title="Nouvelle démarche")

@app.route('/etudiant/demarches/resume/')
def resume_demarche_etudiant():
    return render_template("etudiant/resume_demarche.html", accueil="accueil_etudiant", title="Résumé de la démarche")

########################## POUR LES ENSEIGNANTS ##########################

@app.route('/enseignant/')
def accueil_enseignant():
    return render_template("enseignant/accueil_enseignant.html", accueil="accueil_enseignant", title="Accueil")

@app.route('/enseignant/planning/')
def planning_enseignant():
    return render_template("enseignant/planning_enseignant.html", accueil="accueil_enseignant", title="Planning enseignant")

@app.route('/enseignant/liste+etu/')
def liste_etu_enseignant():
    lesEtudiants=Etudiant.query.all()
    return render_template("enseignant/lst_etudiants_enseignant.html", accueil="accueil_enseignant", title="Liste des étudiants",etudiants=lesEtudiants)

@app.route('/enseignant/liste+etu/etudiant/')
def detail_etudiant_ens():
    return render_template("admin/detail_etudiant_ens.html", accueil="accueil_enseignant", title="Detail de l'etudiant")

########################## POUR LES ADMINISTRATEURS ##########################

@app.route('/admin/')
def accueil_admin():
    return render_template("admin/accueil_admin.html", accueil="accueil_admin", title="Accueil")

@app.route('/admin/planning/')
def planning_admin():
    return render_template("admin/planning_admin.html", accueil="accueil_admin", title="Planning")

@app.route('/admin/enseignant/')
def detail_enseignant():
    return render_template("admin/detail_enseignant.html", accueil="accueil_admin", title="Detail de l'enseignant")

@app.route('/admin/etudiant/')
def detail_etudiant_admin():
    return render_template("admin/detail_etudiant_admin.html", accueil="accueil_admin", title="Detail de l'etudiant")

@app.route('/admin/liste+enseignants/')
def liste_ens_admin():
    return render_template("admin/lst_enseignants.html", accueil="accueil_admin", title="Liste enseignants")

@app.route('/admin/liste+etudiants/')
def liste_etu_admin():
    return render_template("admin/lst_etudiants_admin.html", accueil="accueil_admin", title="Liste etudiants")

if __name__== "__main__":
    app.run()