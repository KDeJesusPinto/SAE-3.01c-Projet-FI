from .app import app
from flask import render_template, request, url_for , redirect

@app.route('/')
@app.route('/connexion/')
def index():
    return render_template("index.html", title="Soutenance - Connexion")

#Pour page enseignants
@app.route('/enseignant/')
def accueil_enseignant():
    return render_template("enseignant/accueil_enseignant.html", title="Accueil")

@app.route('/enseignant/planning/')
def planning_enseignant():
    return render_template("enseignant/planning_enseignant.html", title="Planning enseignant")

@app.route('/enseignant/liste+etu/')
def liste_etu_enseignant():
    return render_template("enseignant/lst_etudiants_enseignant.html", title="Liste des étudiants")

@app.route('/enseignant/liste+etu/etudiant/')
def detail_etudiant_ens():
    return render_template("admin/detail_etudiant__ens.html", title="Detail de l'etudiant")


#Pour page étudiants
@app.route('/etudiant/')
def accueil_etudiant():
    return render_template("etudiant/accueil_etu.html", title="Accueil")

@app.route('/etudiant/demarches/')
def demarches_etudiant():
    return render_template("etudiant/demarches.html", title="Mes démarches")

@app.route('/etudiant/stage/')
def info_stage():
    return render_template("etudiant/info_stage_valide.html", title="Mon stage")

@app.route('/etudiant/demarches/new/')
def nouvelle_demarches_etudiant():
    return render_template("etudiant/nouvelle_demarches.html", title="Nouvelle démarche")

@app.route('/etudiant/demarches/resume/')
def resume_demarches_etudiant():
    return render_template("etudiant/resume_demarche.html", title="Résumé de la démarche")


#Pour page administrateur
@app.route('/admin/')
def accueil_admin():
    return render_template("admin/accueil_admin.html", title="Accueil")

@app.route('/admin/planning/')
def planning_admin():
    return render_template("admin/planning_admin.html", title="Plannng")

@app.route('/admin/liste+enseignants/')
def liste_ens_admin():
    return render_template("admin/lst_enseignants_admin.html", title="Liste enseignants")

@app.route('/admin/liste+etudiants/')
def liste_etu_admin():
    return render_template("admin/lst_etudiants_admin.html", title="Liste etudiants")

@app.route('/admin/enseignant/')
def detail_enseignant():
    return render_template("admin/detail_enseignant.html", title="Detail de l'enseignant")

@app.route('/admin/etudiant/')
def detail_etudiant_admin():
    return render_template("admin/detail_etudiant_admin.html", title="Detail de l'etudiant")




if __name__== "__main__":
    app.run()