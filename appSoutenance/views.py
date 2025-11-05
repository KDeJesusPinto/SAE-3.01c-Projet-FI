from .app import app
from flask import render_template, request, url_for , redirect

@app.route('/')
@app.route('/connexion/')
def index():
    return render_template("index.html", title="Soutenance - Connexion", accueil="index")

########################## POUR LES ÉTUDIANTS ##########################

@app.route('/etudiant/')
def accueil_etudiant():
    return render_template("etudiant/accueil_etu.html", accueil="accueil_etudiant", prenom="Leni", nom="Doe", title="Accueil")

@app.route('/etudiant/demarches/')
def demarches():
    return render_template("etudiant/demarches.html", accueil="accueil_etudiant")

########################## POUR LES ENSEIGNANTS ##########################

@app.route('/enseignant/')
def accueil_enseignant():
    return render_template("enseignant/accueil_enseignant.html", title="Accueil")

@app.route('/enseignant/liste+etu/')
def liste_etu_enseignant():
    return render_template("enseignant/lst_etudiants_enseignant.html", title="Liste des étudiants")

########################## POUR LES ADMINISTRATEURS ##########################

@app.route('/admin/')
def accueil_admin():
    return render_template("admin/accueil_admin.html", accueil="accueil_admin", title="Accueil")




if __name__== "__main__":
    app.run()